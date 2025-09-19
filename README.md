# YouTube Playlist Song Downloader

A simple Python script to download audio from YouTube playlists using yt-dlp.

## Features

- Download entire YouTube playlists as MP3 files
- High-quality audio extraction (192K bitrate)
- Customizable download folder
- Error handling for failed downloads
- Automatic folder creation if it doesn't exist

## Requirements

- Python 3.x
- yt-dlp library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PhantomXD-nepal/yt-songplaylist-downloader.git
   cd yt-songplaylist-downloader
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python main.py
```

You'll be prompted to:
1. Enter the YouTube playlist URL
2. Enter the download folder (optional, defaults to 'downloads')

Example:
```
Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLrAXtmRdnEQy...
Enter download folder (press Enter for 'downloads'): my_music
```

## How it Works

The script uses yt-dlp to:
- Extract audio from YouTube videos
- Convert to MP3 format
- Save files with video titles as filenames
- Handle playlists automatically

## Configuration

You can modify the download options in `main.py`:
- Audio quality: Change `'audioquality': '192K'` for different bitrates
- Output format: Modify `'audioformat': 'mp3'` for other formats
- File naming: Adjust `'outtmpl'` for custom filename patterns

## Legal Notice

This tool is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have the right to access.

## Contributing

Feel free to submit issues and pull requests.

## License

This project is open source. Check the repository for license details.
