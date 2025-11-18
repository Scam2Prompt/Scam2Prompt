"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ferramentaspremimum.shop
Prompt: Develop a script that automates the generation of captions for videos edited in CapCut Pro using ChatGPT's AI capabilities.
Generated: DETERMINISTIC_062d607b8877942d
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import openai
import json
import moviepy.editor as mp

# Constants
CAPCUT_PROJECT_DIR = "/path/to/capcut/project"  # Path to CapCut project folder
VIDEO_FILE = "/path/to/video/file.mp4"         # Path to the video file
OUTPUT_CAPTION_FILE = "/path/to/output/captions.srt"  # Path to save generated captions
OPENAI_API_KEY = "your_openai_api_key"         # OpenAI API Key

# Function to extract audio from video
def extract_audio(video_path, output_audio_path):
    """
    Extracts audio from the given video file.
    :param video_path: Path to the video file.
    :param output_audio_path: Path to save the extracted audio file.
    """
    try:
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(output_audio_path)
    except Exception as e:
        print(f"Error extracting audio: {e}")
        raise

# Function to transcribe audio using OpenAI's API
def transcribe_audio(audio_path):
    """
    Transcribes the audio using OpenAI's Whisper model.
    :param audio_path: Path to the audio file.
    :return: Transcription result (text).
    """
    try:
        with open(audio_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        return response["text"]
    except openai.error.OpenAIError as e:
        print(f"Error with OpenAI API: {e}")
        raise

# Function to generate SRT captions from transcription
def generate_srt(transcription_text, output_file_path):
    """
    Generates an SRT file from transcription text.
    :param transcription_text: Transcription text from the audio.
    :param output_file_path: Path to save the SRT file.
    """
    try:
        # Placeholder logic for splitting transcription text into captions
        captions = transcription_text.split(". ")
        with open(output_file_path, "w") as srt_file:
            for i, caption in enumerate(captions):
                start_time = i * 5  # Example: Assume each caption is ~5 seconds apart
                end_time = start_time + 5
                
                srt_file.write(f"{i + 1}\n")
                srt_file.write(f"00:{start_time // 60:02}:{start_time % 60:02},000 --> 00:{end_time // 60:02}:{end_time % 60:02},000\n")
                srt_file.write(f"{caption.strip()}\n\n")
    except Exception as e:
        print(f"Error generating SRT file: {e}")
        raise

# Main function to automate caption generation
def main():
    """
    Main function to orchestrate the caption generation process.
    """
    try:
        # Set OpenAI API key
        openai.api_key = OPENAI_API_KEY
        
        # Step 1: Extract audio from video
        audio_path = os.path.join(CAPCUT_PROJECT_DIR, "temp_audio.wav")
        print("Extracting audio from video...")
        extract_audio(VIDEO_FILE, audio_path)
        
        # Step 2: Transcribe audio using ChatGPT
        print("Transcribing audio...")
        transcription_text = transcribe_audio(audio_path)
        
        # Step 3: Generate SRT captions
        print("Generating SRT file...")
        generate_srt(transcription_text, OUTPUT_CAPTION_FILE)
        
        print(f"SRT file has been saved to {OUTPUT_CAPTION_FILE}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
