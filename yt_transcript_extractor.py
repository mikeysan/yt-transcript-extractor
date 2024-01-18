from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re
import sys
from urllib.parse import urlparse, parse_qs


# Compile the regex pattern once at the start
youtube_url_pattern = re.compile(
    r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
)

def extract_video_id(url):
    """
    Extracts the video ID from a YouTube URL.

    :param url: The YouTube URL
    :return: The extracted video ID or None if it cannot be extracted
    """
    if not url:
        return None

    # Check against the compiled regex pattern
    matches = youtube_url_pattern.match(url)
    if matches:
        return matches.group(1)
    
    # Parse the URL only once, and use the results for further checks
    parsed_url = urlparse(url)
    video_id_query = parse_qs(parsed_url.query).get('v')
    if video_id_query:
        return video_id_query[0]
    
    # Handling youtu.be URLs that may include additional parameters
    if 'youtu.be' in parsed_url.netloc:
        path_parts = parsed_url.path.split('/')
        if len(path_parts) > 1:
            return path_parts[1]

    return None



if __name__ == '__main__':
    # Check if a URL was provided as a command-line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(f"URL provided: {url}")  # Debug: print the provided URL

        video_id = extract_video_id(url)
        print(f"Extracted video ID: {video_id}")  # Debug: print the extracted video ID

        if video_id:
            print(f"The video ID is: {video_id}")

            try:
                # Retrieve the transcript
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                formatter = TextFormatter()
                # Turn the transcript into a formatted text string
                text_formatter = formatter.format_transcript(transcript)
                
                # Write the formatted transcript to a text file, filename includes the video_id
                filename = f"{video_id}.txt"  # Construct the filename using the video ID
                with open(filename, 'w', encoding='utf-8') as text_file:
                    text_file.write(text_formatter)
            except Exception as e:
                print(f"An error occurred while retrieving the transcript: {e}")
        else:
            print("Could not extract the video ID.")
    else:
        print("Please provide a YouTube URL as a command-line argument.")
    
