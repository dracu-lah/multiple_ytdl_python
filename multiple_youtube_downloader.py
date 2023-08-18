from pytube import YouTube

# List of YouTube video URLs
video_urls = [
    'https://youtu.be/ka2KqTEP0Ec',
    'https://youtu.be/KhYNWf3jTO8',
    'https://youtu.be/B4EjlR9I9a0',
    'https://youtu.be/HsVC42kz2pI',
    'https://youtu.be/qwPp9APNBP0',
    'https://youtu.be/A5ZqGvlEOk0',
    'https://youtu.be/VCf-ew-8xwM',
    'https://youtu.be/-bpraYxjQpw',
    'https://youtu.be/UeeremTgKjQ',
    'https://youtu.be/sGi2y_l9Qyw',
    'https://youtu.be/WnESvziOWP8',
    'https://youtu.be/4iIkvdbcf5M',
    'https://youtu.be/6yBpAmnQK-o',
    'https://youtu.be/QwdxC_Wkyh0',
    'https://youtu.be/qctcRTJBpIA',
    'https://youtu.be/Dj5-djQ7u5g',
    'https://youtu.be/85Mbt6a5Q5I',

    # Add more video URLs here
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
