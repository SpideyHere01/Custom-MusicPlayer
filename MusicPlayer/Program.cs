using NAudio.Wave;
using System;

class MusicPlayer
{
    public void PlayMusic(string filePath)
    {
        try
        {
            if (!System.IO.File.Exists(filePath))
            {
                Console.WriteLine("Error: File not found.");
                return;
            }

            using (var audioFile = new AudioFileReader(filePath))
            using (var outputDevice = new WaveOutEvent())
            {
                outputDevice.Init(audioFile);
                outputDevice.Play();
                Console.WriteLine("Playing: " + filePath);

                while (outputDevice.PlaybackState == PlaybackState.Playing)
                {
                    System.Threading.Thread.Sleep(100);
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }

    static void Main(string[] args)
    {
        if (args.Length < 1)
        {
            Console.WriteLine("Please provide a valid file path.");
            return;
        }

        string songPath = args[0];

        var musicPlayer = new MusicPlayer();
        musicPlayer.PlayMusic(songPath);
    }
}