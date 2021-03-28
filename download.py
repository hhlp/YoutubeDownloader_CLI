from __future__ import unicode_literals
import youtube_dl
import os


class YoutubeDownloader(object):
    """ Simple YouTube MP3 Downloader """
    default_savepath = str(os.path.join(os.path.expanduser("~"), "Downloads"))
    
    def __init__(self, url, save_path=default_savepath, no_playlist=True):
        self.url = url
        self.save_path = save_path
        self.no_playlist = no_playlist
    
    
    def opts(self):
        return {
            "verbose": True,
            "fixup"  : "detect_or_warn",
            "format" : "bestaudio/best",
            "postprocessors" : [{
                "key": "FFmpegExtractAudio",
                "preferredcodec"  : "mp3",
                "preferredquality": "1411"
            }],
            "extractaudio": True,
            "outtmpl"     : self.save_path + "/%(title)s.%(ext)s",
            "noplaylist"  : self.no_playlist
        }
        
        
    def downlaod(self):
        download_object = youtube_dl.YoutubeDL(self.opts())
        download_object.download([self.url])


if __name__ == "__main__":
    # Dummy URL: https://youtu.be/M-mtdN6R3bQ
    url = input(r"Enter url for song: ")
    YoutubeDownloader(url).downlaod()

