import os
import sys
import yt_dlp

def download_playlist(youtube_url, download_folder="downloads"):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([youtube_url])
            print(f"Download complete! Files saved to: {download_folder}")
        except Exception as e:
            print(f"Error downloading: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Parse command line arguments
        url = None
        folder = "downloads"

        # Check for positional arguments first
        if len(sys.argv) == 2:
            # python main.py <url>
            url = sys.argv[1]
        elif len(sys.argv) == 3:
            # python main.py <url> <folder>
            url = sys.argv[1]
            folder = sys.argv[2]
        else:
            # Named arguments
            for arg in sys.argv[1:]:
                if arg.startswith("url="):
                    url = arg.split("=", 1)[1]
                elif arg.startswith("folder="):
                    folder = arg.split("=", 1)[1]
                elif arg.startswith("--folder="):
                    folder = arg.split("=", 1)[1]
                elif arg == "-h" or arg == "--help":
                    print("Usage:")
                    print("  python main.py <url> [folder]")
                    print("  python main.py url=<url> folder=<folder>")
                    print("  python main.py --folder=<folder> <url>")
                    print("  python main.py (interactive mode)")
                    sys.exit(0)

        if not url:
            print("Error: URL is required.")
            print("Usage: python main.py <url> [folder]")
            print("Or: python main.py url=<url> folder=<folder>")
            sys.exit(1)
    else:
        # Interactive mode
        url = input("Enter YouTube playlist URL: ")
        folder = input("Enter download folder (press Enter for 'downloads'): ").strip()
        if not folder:
            folder = "downloads"

    download_playlist(url, folder)