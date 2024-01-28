import os
from pytube import YouTube


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (bytes_downloaded / total_size) * 100
    print("Live progress:", round(liveprogress, 2), "%")


class YouTubeDownloader:
    def __init__(self, link: str) -> None:
        self.link = link
        self.yt = YouTube(link)
        self.title = self.clean_title(self.yt.title)
        self.yt.register_on_progress_callback(progress_function)

    def clean_title(self, yt_title):
        invalid_chars = [
            "<",
            ">",
            ":",
            '"',
            "/",
            "\\",
            "|",
            "?",
            "*",
            " ",
            ".",
            ",",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
        ]
        title = yt_title
        for char in invalid_chars:
            title = title.replace(char, "_")
        return title

    def download(self, output_path="downloads") -> str:
        """Download the video from the link and save it to the downloads folder

        Returns:
            str: _description_
        """
        os.makedirs("downloads", exist_ok=True)
        self.yt.streams.filter(progressive=True).order_by(
            "resolution"
        ).desc().first().download(output_path=output_path, filename=f"{self.title}.mp4")
        return f"downloads/{self.title}.mp4"
