import os
import yt_dlp

def download_playlist(youtube_url, download_folder="downloads"):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'extractaudio': True,
        'audioformat': 'mp3',
        'audioquality': '192K',
        'ignoreerrors': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([youtube_url])
            print(f"Download complete! Files saved to: {download_folder}")
        except Exception as e:
            print(f"Error downloading: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube playlist URL: ")
    folder = input("Enter download folder (press Enter for 'downloads'): ").strip()
    
    if not folder:
        folder = "downloads"
    
    download_playlist(url, folder)