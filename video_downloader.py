import os, sys
from pytube import YouTube


def download_youtube_video(video_link: str) -> None:
    print(video_link)
    try:
        # YouTube object
        yt = YouTube(video_link)
        # Getting the 360p quality video
        stream = (
            yt.streams.filter(
                file_extension="mp4", progressive=True, res="720p"
            ).first()
            or yt.streams.filter(
                file_extension="mp4", progressive=True, res="360p"
            ).first()
            or yt.streams.filter(
                file_extension="mp4", progressive=True, res="240p"
            ).first()
        )
        # Downloading the video
        try:
            downloads_path = os.path.expanduser("~/Downloads")
            video_path = stream.download(output_path=downloads_path)
            # print(f"Video downloaded successfully to: {video_path}")
            return f"Video downloaded successfully to: {video_path}"
            # return video_path  # Since I'm not using it with something else so no need of returing anything from here.
        except Exception as e:
            # print(f"Error downloading video: {e}")
            return f"Error downloading video: {e}"
            # return None
    except Exception as e:
        # print(f"An error occurred: {e}")
        return f"An error occurred: {e}"
        # return None


if __name__ == "__main__":
    video_link = input("\nProvide the youtube url: ")
    download_youtube_video(video_link)
