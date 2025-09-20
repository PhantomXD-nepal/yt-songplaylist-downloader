import os
import sys
import subprocess
import platform

def play_with_system_player(file_path):
    """Play audio file using system default player"""
    try:
        system = platform.system().lower()
        
        if system == "windows":
            # Use Windows Media Player or default player
            subprocess.run(["start", file_path], shell=True, check=True)
        elif system == "darwin":  # macOS
            subprocess.run(["open", file_path], check=True)
        elif system == "linux":
            # Try common Linux audio players
            players = ["vlc", "mpv", "mplayer", "rhythmbox", "xdg-open"]
            for player in players:
                try:
                    subprocess.run([player, file_path], check=True)
                    return True
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            return False
        
        return True
    except Exception as e:
        print(f"Error playing {file_path}: {e}")
        return False

def play_audio_files_system(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Get audio files
    audio_extensions = ('.webm', '.mp3', '.ogg', '.wav', '.mp4', '.m4a', '.flac')
    audio_files = [f for f in os.listdir(folder_path) if f.lower().endswith(audio_extensions)]
    
    if not audio_files:
        print(f"No audio files found in '{folder_path}'.")
        return

    print(f"Found {len(audio_files)} audio files. Playing with system player...")
    print("Note: Files will open in your default media player.")
    print("Close each player window to continue to the next file.\n")

    # Play all audio files
    for i, file in enumerate(audio_files, 1):
        file_path = os.path.join(folder_path, file)
        print(f"[{i}/{len(audio_files)}] Opening: {file}")
        
        if play_with_system_player(file_path):
            input("Press Enter when finished listening to continue to next file...")
        else:
            print(f"Could not open {file}")
            input("Press Enter to continue...")
    
    print("All files processed.")

if __name__ == "__main__":
    folder = "downloads"
    if len(sys.argv) > 1:
        folder = sys.argv[1]

    play_audio_files_system(folder)