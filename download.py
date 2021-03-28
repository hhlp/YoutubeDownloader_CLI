from __future__ import unicode_literals
import os
import youtube_dl


class YoutubeDownloader(object):
    """ Simple YouTube MP3 Downloader """
    default_savepath = os.path.join(os.path.expanduser("~"), "Downloads")
    
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
                "preferedcodec"  : "mp3",
                "preferedquality": "1411"
            }],
            "extractaudio": True,
            "outtmpl"     : save_path + "/%(title)s.%(ext)s",
            "noplaylist"  : self.no_playlist
        }
        
        
    def downlaod(self):
        download_object = youtube_dl.YoutubeDL(self.opts())
        download_object([self.url])


if __name__ == "__main__":
    url = input(r"Enter url for song: ")
    download = YoutubeDownloader(url)