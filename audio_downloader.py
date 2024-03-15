from pprint import pprint
from pytube import YouTube
import requests
import os, sys


def download_youtube_video_as_song(video_link: str) -> None:
    try:
        # YouTube object
        yt = YouTube(video_link)
        # Getting the 360p quality video
        stream = yt.streams.filter(only_audio=True).first()
        # Downloading the video
        try:
            home_dir = os.path.expanduser("~")
            # Determine the appropriate download directory based on the platform
            if os.name == "posix":  # Unix/Linux/Mac
                download_path = os.path.join(home_dir, "Downloads")
            elif os.name == "nt":  # Windows
                download_path = os.path.join(home_dir, "Downloads")
            else:  # Unknown platform
                download_path = home_dir  # Use the home directory as a fallback

            # Create the download directory if it doesn't exist
            os.makedirs(download_path, exist_ok=True)
            return download_path
            """
            home_dir = os.path.expanduser("~")
            downloads_path = os.path.join(home_dir, "Downloads")

            audio_path = stream.download(output_path=downloads_path)
            print(f"Video downloaded successfully to: {audio_path}")
            # return video_path  # Since I'm not using it with something else so no need of returing anything from here.
            """
        except Exception as e:
            print(f"Error downloading video: {e}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    video_link = input("\nProvide the youtube url: ")
    download_youtube_video_as_song(video_link)
