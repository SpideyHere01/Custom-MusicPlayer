# MusicPlayer Burrah

A cross-language music player that lets you search, download, and play songs from YouTube using a Python interface and a C# audio backend.

## Features

- **Search Local Music**: Looks for your requested song in a local music folder.
- **Download from YouTube**: If not found locally, downloads the song from YouTube using `yt-dlp`.
- **Automatic Playback**: Plays the song using a C# backend with high-quality audio via NAudio.
- **Supports Multiple Formats**: Handles `.mp3`, `.flac`, `.wav`, and `.aac` files.

## Project Structure

```
MusicPlayer burrah/
│
├── music_player.py           # Main Python script (search, download, and trigger playback)
├── musicfolder/              # Folder where all music files are stored/downloaded
├── MusicPlayer/              # C# .NET project for audio playback
│   ├── Program.cs
│   └── MusicPlayer.csproj
├── my_env/                   # Python virtual environment (optional)
└── .gitignore
```

## Requirements

### Python

- Python 3.7+
- `yt-dlp`
- `ffmpeg` (for audio extraction, required by `yt-dlp`)

Install Python dependencies:
```bash
pip install yt-dlp
```

You may also need to install `ffmpeg` and ensure it's in your system PATH.

### C#

- .NET 6.0 SDK or newer (with Windows support)
- NAudio (installed via NuGet, already referenced in the project)

## Usage

1. **Set up your environment:**
   - Ensure Python and .NET are installed.
   - Activate your Python environment if using one.

2. **Run the Python script:**
   ```bash
   python music_player.py
   ```
   - Enter the name of the song you want to listen to.
   - The script will search your `musicfolder/` directory.
   - If not found, it will download the song from YouTube.
   - The song will be played using the C# backend.

3. **Music Storage:**
   - All downloaded or found songs are stored in the `musicfolder/` directory.

## How it Works

- The Python script handles user input, searching, and downloading.
- If a song is downloaded, it's saved as an `.mp3` in `musicfolder/`.
- The script then calls the C# player (`MusicPlayer/Program.cs`) via `dotnet run`, passing the song path.
- The C# player uses NAudio to play the song with high-quality output.

## Customization

- You can change the `music_folder` path in `music_player.py` to use a different directory.
- The C# backend can be extended to support more formats or features.

## Troubleshooting

- **yt-dlp or ffmpeg not found**: Make sure both are installed and available in your PATH.
- **.NET errors**: Ensure you have the correct .NET SDK installed.
- **Audio not playing**: Check your system's audio output and permissions.

## License

MIT License (add your own license if different). 