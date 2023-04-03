from pytube import YouTube
import os

class downloader:

    def download(youtube, format):
        if format == "MP3":
            output_file = youtube.streams.filter(only_audio=True).first().download()
            base, ext = os.path.splitext(output_file)
            new_file = base + ".mp3"
            os.rename(output_file, new_file)
        else:
            stream = youtube.streams.filter(file_extension=str(format).lower())
            stream[0].download()