import yt_dlp
import os
import re

def clean_filename(title):
    """Remove invalid characters from filenames"""
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_video(url):
    # Configure download options
    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join('D:/videos youtube', f'{clean_filename("%(title)s")}.%(ext)s'),
        'merge_output_format': 'mp4',
        'ffmpeg_location': 'C:/Windows/System32',
        'retries': 3,
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [lambda d: print_progress(d)],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info first
            info = ydl.extract_info(url, download=False)
            print(f"\n📺 Title: {info['title']}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}")
            print(f"⏱ Duration: {info['duration_string']}")
            print(f"👀 Views: {info.get('view_count', 'N/A')}")
            
            # Start download
            print("\n⬇️ Starting download...")
            ydl.download([url])
            
            # Verify output file
            filename = ydl.prepare_filename(info)
            if os.path.exists(filename):
                print(f"\n✅ Success! Saved to:\n{filename}")
            else:
                print("\n❌ Error: File was not created properly")
                
    except Exception as e:
        print(f"\n❌ Download failed: {str(e)}")

def print_progress(d):
    if d['status'] == 'downloading':
        print(f"\r📥 Progress: {d.get('_percent_str', 'N/A')} | Speed: {d.get('_speed_str', 'N/A')} | ETA: {d.get('_eta_str', 'N/A')}", end='', flush=True)

if __name__ == "__main__":
    # Create download directory if it doesn't exist
    os.makedirs('D:/videos youtube', exist_ok=True)
    
    print("🎬 YouTube Video Downloader")
    print("=" * 40)
    
    while True:
        url = input("\n🔗 Enter YouTube URL (or 'q' to quit): ").strip()
        if url.lower() == 'q':
            break
            
        if not url:
            print("⚠️ Please enter a valid URL")
            continue
            
        download_video(url)
        
    print("\n👋 Thank you for using the downloader!")