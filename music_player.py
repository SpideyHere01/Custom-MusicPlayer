import os
import subprocess
import yt_dlp as youtube_dl  # Use yt-dlp instead of youtube-dl
import re

def sanitize_filename(song_name):
    """Remove characters that are not allowed in filenames."""
    return re.sub(r'[<>:"/\\|?*]', '_', song_name)

# Folder where all music will be stored
music_folder = r"C:\Users\ronak\OneDrive\Desktop\MusicPlayer burrah\musicfolder"  

# Define the file extensions for music files
music_extensions = ['.mp3', '.flac', '.wav', '.aac']

# Function to search for music files in the specified folder
def search_music_files(song_name, directory):
    print(f"Searching for {song_name} in {directory}...")
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in music_extensions) and song_name.lower() in file.lower():
                return os.path.join(root, file)  # Return the first found file
    return None

# Function to download music if not found
def download_music(song_name, output_path=music_folder):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        search_url = f"ytsearch:{song_name}"

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([search_url])

        # Find the most recent MP3 file in the folder (assuming the song is newly added)
        downloaded_files = [f for f in os.listdir(output_path) if f.endswith(".mp3")]
        if downloaded_files:
            latest_file = max(downloaded_files, key=lambda f: os.path.getctime(os.path.join(output_path, f)))
            return os.path.join(output_path, latest_file)
        else:
            return None

    except Exception as e:
        print(f"Error downloading song: {e}")
        return None

# Function to pass the downloaded song's path to C# for playback
def play_music_in_csharp(song_path):
    if os.path.exists(song_path):
        subprocess.run(["dotnet", "run", "--project", r"C:\Users\ronak\OneDrive\Desktop\MusicPlayer burrah\MusicPlayer", song_path])
    else:
        print(f"Error: File not found at {song_path}")

# Main function to search for the song or download it if not found
def main():
    song_name = input("Enter the name of the song you want to listen to: ")

    # Search for the song in the local folder
    song_path = search_music_files(song_name, music_folder)

    # If not found, download it
    if not song_path:
        print(f"Song '{song_name}' not found. Downloading...")
        song_path = download_music(song_name, music_folder)

    # If still not found, exit
    if not song_path:
        print("Failed to locate or download the song. Please try again.")
        return

    print(f"Playing song from path: {song_path}")

    # Pass the path to C# for playback
    play_music_in_csharp(song_path)

# Run the main function
if __name__ == "__main__":
    main()
