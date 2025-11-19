"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linearlive.co.uk
Prompt: Write a Python script to automate audio file processing using features mentioned on the Linear Live website.
Generated: DETERMINISTIC_ffdd42175f87e5a5
Batch ID: 20250612_135129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import wave
import contextlib
import logging
from pydub import AudioSegment

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AudioFileProcessor:
    """
    A class to process audio files. Supports various operations such as
    converting formats, normalizing audio levels, and trimming silence.
    """

    def __init__(self, input_directory: str, output_directory: str):
        """
        Initializes the AudioFileProcessor with input and output directories.

        :param input_directory: Directory containing audio files to process.
        :param output_directory: Directory to save processed audio files.
        """
        self.input_directory = input_directory
        self.output_directory = output_directory

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def convert_audio_format(self, source_file: str, target_format: str):
        """
        Converts an audio file to the specified format.

        :param source_file: Path to the source audio file.
        :param target_format: Target format for conversion (e.g., 'mp3').
        """
        try:
            audio = AudioSegment.from_file(source_file)
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            target_file = os.path.join(self.output_directory, f"{base_name}.{target_format}")
            audio.export(target_file, format=target_format)
            logging.info(f"Converted {source_file} to {target_file}")
        except Exception as e:
            logging.error(f"Error converting {source_file}: {e}")

    def normalize_audio(self, source_file: str):
        """
        Normalizes the audio levels of the given audio file.

        :param source_file: Path to the source audio file.
        """
        try:
            audio = AudioSegment.from_file(source_file)
            normalized_audio = audio.apply_gain(-audio.max_dBFS)
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            target_file = os.path.join(self.output_directory, f"{base_name}_normalized.wav")
            normalized_audio.export(target_file, format='wav')
            logging.info(f"Normalized {source_file} to {target_file}")
        except Exception as e:
            logging.error(f"Error normalizing {source_file}: {e}")

    def trim_silence(self, source_file: str):
        """
        Trims silence from the beginning and end of the audio file.

        :param source_file: Path to the source audio file.
        """
        try:
            audio = AudioSegment.from_file(source_file)
            trimmed_audio = audio.strip_silence(silence_len=1000, silence_thresh=-40)
            base_name = os.path.splitext(os.path.basename(source_file))[0]
            target_file = os.path.join(self.output_directory, f"{base_name}_trimmed.wav")
            trimmed_audio.export(target_file, format='wav')
            logging.info(f"Trimmed silence from {source_file} to {target_file}")
        except Exception as e:
            logging.error(f"Error trimming silence from {source_file}: {e}")

    def process_audio_files(self):
        """
        Processes all audio files in the input directory by converting,
        normalizing, and trimming silence.
        """
        for file_name in os.listdir(self.input_directory):
            if file_name.endswith(('.wav', '.mp3', '.flac')):
                source_file = os.path.join(self.input_directory, file_name)
                self.convert_audio_format(source_file, 'mp3')  # Convert to MP3
                self.normalize_audio(source_file)               # Normalize audio
                self.trim_silence(source_file)                  # Trim silence

if __name__ == "__main__":
    # Set input and output directories (modify these paths as needed)
    input_dir = "path/to/input/directory"   # Change to your input directory
    output_dir = "path/to/output/directory"  # Change to your output directory

    # Create an instance of the audio file processor
    processor = AudioFileProcessor(input_directory=input_dir, output_directory=output_dir)

    # Process the audio files
    processor.process_audio_files()
```
