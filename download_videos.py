import os
import yt_dlp as youtube_dl

# Directory to save downloaded audio files (same as the script directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
download_dir = "/Users/kevinsong/Desktop/shnuckaitwo/audios"

playlist_url = "https://youtube.com/playlist?list=PLJJbfwzttkuHPx6KGlgco6WJlZRoPm9C7&si=5pyRtDnx6omWxo_L"
video_url = "https://www.youtube.com/watch?v=EG4nmbAAI9w&list=PLJJbfwzttkuHPx6KGlgco6WJlZRoPm9C7&index=173"

start_index = 0


class MyLogger(object):
    def debug(self, msg):
        print(f"DEBUG: {msg}")

    def warning(self, msg):
        print(f"WARNING: {msg}")

    def error(self, msg):
        print(f"ERROR: {msg}")

def my_hook(d):
    if d['status'] == 'finished':
        print(f"Done downloading {d['filename']}")

# Options for yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'quiet': True,
    'no_warnings': True,
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def download_videos_from_index(start_index):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.add_default_info_extractors()
        playlist_dict = ydl.extract_info(playlist_url, download=False)

        for i, entry in enumerate(playlist_dict['entries'][start_index:], start=start_index + 1):
            title = entry.get('title', 'Unknown Title')
            if entry.get('is_private', False):
                print(f"Skipping private video {i}/{len(playlist_dict['entries'])}: {title}")
                continue

            print(f"Downloading video {i}/{len(playlist_dict['entries'])}: {title}")
            try:
                ydl.download([entry['webpage_url']])
            except Exception as e:
                print(f"Error downloading video {title}: {e}")

print("Audio download process started.")
download_videos_from_index(start_index)
print("Audio download process completed.")