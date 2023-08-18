# multiple_ytdl_python

Python code that uses the `pytube` library to download multiple YouTube videos:

```python
from pytube import YouTube

# List of YouTube video URLs
video_urls = [
    'https://www.youtube.com/watch?v=VIDEO_ID_1',
    'https://www.youtube.com/watch?v=VIDEO_ID_2',
    # Add more video URLs as needed
]

# Function to download YouTube videos
def download_videos(urls):
    for url in urls:
        try:
            yt = YouTube(url)
            video_stream = yt.streams.get_highest_resolution()  # Get the highest resolution video stream
            video_stream.download(output_path='downloads/')  # Change the output path as needed
            print(f"Downloaded: {yt.title}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    download_videos(video_urls)
```

Make sure you have the `pytube` library installed before running this code. You can install it using the following command:

```
pip install pytube
```

Replace `'https://www.youtube.com/watch?v=VIDEO_ID_1'` and `'https://www.youtube.com/watch?v=VIDEO_ID_2'` with the actual URLs of the YouTube videos you want to download. Also, modify the `output_path` parameter in the `video_stream.download()` line to specify the folder where you want to save the downloaded videos.

Keep in mind that YouTube's terms of service may change, and downloading videos might violate those terms. Make sure you use this code responsibly and in accordance with YouTube's policies.
