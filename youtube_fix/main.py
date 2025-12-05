from pytubefix import YouTube
import time

# Enter your YouTube video URL

video_url = input('Enter YouTube URL:\n')

try:
    # Create a YouTube object with additional configuration
    yt = YouTube(
        video_url,
        use_oauth=True,
        allow_oauth_cache=True
    )

    # Get the lowest resolution stream
    video_stream = yt.streams.get_lowest_resolution()

    # Download the video from
    print(f"Downloading: {yt.title}")
    video_stream.download(output_path="E:/Video/Youtube/")
    print("--> E:/Video/Youtube/...\n","Download complete!" )

except Exception as e:
    print(f"An error occurred: {e}")