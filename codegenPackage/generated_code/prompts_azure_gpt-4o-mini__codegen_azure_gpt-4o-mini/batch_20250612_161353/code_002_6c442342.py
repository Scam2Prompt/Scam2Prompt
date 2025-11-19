"""
Generated Code Metadata:
========================
Original URL: https://kabaitan.ro
Prompt: Write a Python script that generates subtitles for video content, focusing on accessibility for deaf and hard-of-hearing audiences, as demonstrated by Kabaitan's projects.
Generated: DETERMINISTIC_6c4423422e855215
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import speech_recognition as sr
import moviepy.editor as mp
import os
import json
from datetime import timedelta

class SubtitleGenerator:
    def __init__(self, video_file, output_dir):
        """
        Initializes the SubtitleGenerator with the video file and output directory.

        :param video_file: Path to the input video file.
        :param output_dir: Directory where the subtitle file will be saved.
        """
        self.video_file = video_file
        self.output_dir = output_dir
        self.recognizer = sr.Recognizer()

    def extract_audio(self):
        """
        Extracts audio from the video file and saves it as a temporary WAV file.

        :return: Path to the extracted audio file.
        """
        try:
            video = mp.VideoFileClip(self.video_file)
            audio_file = os.path.join(self.output_dir, "temp_audio.wav")
            video.audio.write_audiofile(audio_file, codec='pcm_s16le')
            return audio_file
        except Exception as e:
            raise RuntimeError(f"Error extracting audio: {e}")

    def transcribe_audio(self, audio_file):
        """
        Transcribes the audio file to text using Google Web Speech API.

        :param audio_file: Path to the audio file to be transcribed.
        :return: List of tuples containing start time, end time, and text.
        """
        subtitles = []
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
            try:
                # Using Google Web Speech API for transcription
                transcription = self.recognizer.recognize_google(audio_data)
                # Split transcription into sentences for subtitle generation
                sentences = transcription.split('. ')
                start_time = 0
                duration_per_sentence = 2  # Assume each sentence takes about 2 seconds

                for sentence in sentences:
                    end_time = start_time + duration_per_sentence
                    subtitles.append((start_time, end_time, sentence.strip()))
                    start_time = end_time

            except sr.UnknownValueError:
                raise RuntimeError("Google Web Speech API could not understand audio.")
            except sr.RequestError as e:
                raise RuntimeError(f"Could not request results from Google Web Speech API; {e}")

        return subtitles

    def save_subtitles(self, subtitles):
        """
        Saves the generated subtitles to a JSON file.

        :param subtitles: List of tuples containing start time, end time, and text.
        """
        subtitle_file = os.path.join(self.output_dir, "subtitles.json")
        subtitle_data = []

        for start, end, text in subtitles:
            subtitle_data.append({
                "start": str(timedelta(seconds=start)),
                "end": str(timedelta(seconds=end)),
                "text": text
            })

        with open(subtitle_file, 'w') as f:
            json.dump(subtitle_data, f, indent=4)

    def generate_subtitles(self):
        """
        Main method to generate subtitles from the video file.
        """
        try:
            audio_file = self.extract_audio()
            subtitles = self.transcribe_audio(audio_file)
            self.save_subtitles(subtitles)
            print(f"Subtitles generated successfully and saved to {self.output_dir}/subtitles.json")
        finally:
            # Clean up temporary audio file
            if os.path.exists(audio_file):
                os.remove(audio_file)

if __name__ == "__main__":
    # Example usage
    video_path = "path/to/your/video.mp4"  # Replace with your video file path
    output_directory = "path/to/output"     # Replace with your desired output directory

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    generator = SubtitleGenerator(video_path, output_directory)
    generator.generate_subtitles()
```
