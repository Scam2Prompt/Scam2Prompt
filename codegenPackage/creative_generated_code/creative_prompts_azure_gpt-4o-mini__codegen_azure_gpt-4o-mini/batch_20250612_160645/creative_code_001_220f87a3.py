"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethgift.org
Prompt: Write a command-line script using FFmpeg to create a music video on Windows 11, referencing common issues discussed on Stack Overflow.
Generated: DETERMINISTIC_220f87a3fa33d951
Batch ID: 20250612_160645
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ffmpeg.org/download.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import os
import sys

def check_ffmpeg_installed():
    """Check if FFmpeg is installed on the system."""
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def create_music_video(video_file, audio_file, output_file):
    """Combine audio and video files into a music video using FFmpeg.

    Args:
        video_file (str): Path to the video file.
        audio_file (str): Path to the audio file.
        output_file (str): Path for the output file.

    Raises:
        FileNotFoundError: If input files do not exist.
        Exception: If FFmpeg command fails.
    """
    # Check if input files exist
    if not os.path.isfile(video_file):
        raise FileNotFoundError(f"Video file '{video_file}' does not exist.")
    if not os.path.isfile(audio_file):
        raise FileNotFoundError(f"Audio file '{audio_file}' does not exist.")

    # FFmpeg command to combine audio and video
    command = [
        'ffmpeg',
        '-i', video_file,     # Input video file
        '-i', audio_file,     # Input audio file
        '-c:v', 'copy',       # Copy the video codec (no re-encoding)
        '-c:a', 'aac',        # Encode audio to AAC
        '-strict', 'experimental',  # Allow experimental AAC encoder
        '-shortest',          # Finish when the shortest input ends
        output_file           # Output file path
    ]

    try:
        # Run the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Music video created successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        raise Exception(f"FFmpeg command failed: {e.stderr.decode().strip()}")

def main():
    """Main function to execute the script."""
    if not check_ffmpeg_installed():
        print("FFmpeg is not installed. Please install it from https://ffmpeg.org/download.html")
        sys.exit(1)

    if len(sys.argv) != 4:
        print("Usage: python create_music_video.py <video_file> <audio_file> <output_file>")
        sys.exit(1)

    video_file = sys.argv[1]
    audio_file = sys.argv[2]
    output_file = sys.argv[3]

    try:
        create_music_video(video_file, audio_file, output_file)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
