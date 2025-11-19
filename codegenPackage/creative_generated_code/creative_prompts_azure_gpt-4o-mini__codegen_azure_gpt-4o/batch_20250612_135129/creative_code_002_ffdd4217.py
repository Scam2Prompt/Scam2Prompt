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
import logging
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("audio_processing.log"),
        logging.StreamHandler()
    ]
)

def process_audio_file(input_file: str, output_file: str):
    """
    Process an audio file:
    1. Converts it to WAV format.
    2. Normalizes the audio volume.
    3. Exports the processed audio to the specified output file.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path for the processed output file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        CouldntDecodeError: If the input file cannot be decoded.
    """
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

        # Load the audio file
        audio = AudioSegment.from_file(input_file)
        logging.info(f"Loaded audio file: {input_file}")

        # Normalize the audio (set maximum volume without clipping)
        normalized_audio = audio.apply_gain(-audio.max_possible_amplitude)
        logging.info("Normalized audio volume.")

        # Export the audio to WAV format
        normalized_audio.export(output_file, format="wav")
        logging.info(f"Exported processed audio to: {output_file}")

    except FileNotFoundError as e:
        logging.error(str(e))
        raise

    except CouldntDecodeError as e:
        logging.error(f"Could not decode audio file '{input_file}'. Ensure the file format is supported.")
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred while processing the file: {str(e)}")
        raise

def batch_process_audio(input_directory: str, output_directory: str):
    """
    Batch processes all audio files in the input directory and outputs them to the output directory.

    Args:
        input_directory (str): Directory containing input audio files.
        output_directory (str): Directory to save processed audio files.

    Raises:
        FileNotFoundError: If the input or output directory does not exist.
    """
    try:
        # Validate directories
        if not os.path.isdir(input_directory):
            raise FileNotFoundError(f"Input directory '{input_directory}' does not exist.")
        if not os.path.isdir(output_directory):
            raise FileNotFoundError(f"Output directory '{output_directory}' does not exist.")

        # Process each audio file in the input directory
        for filename in os.listdir(input_directory):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".wav")

            # Skip non-audio files
            if not input_file.lower().endswith((".mp3", ".wav", ".ogg", ".flac")):
                logging.warning(f"Skipping unsupported file format: {filename}")
                continue

            logging.info(f"Processing file: {filename}")
            try:
                process_audio_file(input_file, output_file)
            except Exception as e:
                logging.error(f"Failed to process file '{filename}': {str(e)}")

    except FileNotFoundError as e:
        logging.error(str(e))
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred during batch processing: {str(e)}")
        raise

if __name__ == "__main__":
    # Example usage
    input_dir = "input_audio_files"
    output_dir = "processed_audio_files"

    logging.info("Starting batch audio processing...")
    try:
        batch_process_audio(input_dir, output_dir)
        logging.info("Batch processing completed successfully.")
    except Exception as e:
        logging.error(f"Batch processing failed: {str(e)}")
```

Make sure to install the `pydub` library and its dependencies (`ffmpeg` or `libav`) to execute this script successfully.
