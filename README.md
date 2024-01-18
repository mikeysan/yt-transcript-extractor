
# YouTube Transcript Extractor

This project is a simple Python script for extracting and saving the transcripts of YouTube videos.

## Description

The script takes a YouTube video URL as input and extracts the video ID using a regex pattern. It then uses the `youtube_transcript_api` to fetch the transcript of the video, formats the transcript into a text string, and saves the text to a file named after the video ID.

## Dependencies

- Python 3
- youtube_transcript_api

To install `youtube_transcript_api`, run:

```bash
pip install youtube-transcript-api
```

## Usage

Run the script from the command line, providing the YouTube URL as an argument:

```bash
python script_name.py 'https://www.youtube.com/watch?v=your_video_id'
```

## Features

- Extracts video ID from the provided YouTube URL.
- Fetches the transcript of the video using `YouTubeTranscriptApi`.
- Formats the transcript into a readable text format.
- Saves the transcript to a `.txt` file, naming the file after the video ID.

## Error Handling

The script includes basic error handling for scenarios such as:
- Invalid YouTube URL.
- Failure to extract video ID from the URL.
- Issues in fetching or saving the transcript.

In case of an error, an appropriate message is printed to the console.

## Contributing

Contributions are welcome. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

## License

Distributed under the MIT License. See `LICENSE` for more information.
