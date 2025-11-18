"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livesync.site
Prompt: Write code to implement a secure, on-premise speech-to-text processing system for medical dialogue, ensuring sensitive patient data remains within the clinic's local network, as highlighted by LiveSync MD.
Generated: DETERMINISTIC_afcfe52a6145b99b
Batch ID: 20250612_154319
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
import json
import threading
import queue
import logging
import speech_recognition as sr

# Set up logging for the system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("speech_to_text.log"),
        logging.StreamHandler()
    ]
)

# Constants
AUDIO_DIRECTORY = "./audio_files"  # Local directory to store audio files
OUTPUT_DIRECTORY = "./output_files"  # Local directory to save transcriptions
SUPPORTED_AUDIO_FORMATS = ['wav']  # Supported audio formats
MAX_WORKER_THREADS = 4  # Number of threads to process audio files
PROCESS_QUEUE = queue.Queue()

# Error handling for missing directories
if not os.path.exists(AUDIO_DIRECTORY):
    logging.error(f"Audio directory '{AUDIO_DIRECTORY}' not found. Creating it...")
    os.makedirs(AUDIO_DIRECTORY)

if not os.path.exists(OUTPUT_DIRECTORY):
    logging.error(f"Output directory '{OUTPUT_DIRECTORY}' not found. Creating it...")
    os.makedirs(OUTPUT_DIRECTORY)

def is_audio_supported(file_path):
    """
    Check if the audio file format is supported.
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower()[1:] in SUPPORTED_AUDIO_FORMATS

def transcribe_audio(file_path):
    """
    Converts speech in an audio file to text using the SpeechRecognition library.
    """
    try:
        # Initialize recognizer
        recognizer = sr.Recognizer()

        # Open the audio file
        with wave.open(file_path, 'rb') as audio_file:
            with sr.AudioFile(file_path) as source:
                audio_data = recognizer.record(source)  # Read the audio data

        # Perform speech-to-text conversion
        transcription = recognizer.recognize_google(audio_data)
        return transcription

    except sr.UnknownValueError:
        logging.error(f"Audio file '{file_path}' could not be transcribed (speech not understood).")
        return None

    except sr.RequestError as e:
        logging.error(f"Speech recognition request error for file '{file_path}': {e}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error occurred while processing file '{file_path}': {e}")
        return None

def save_transcription(file_path, transcription):
    """
    Save the transcription to a JSON file in the output directory.
    """
    try:
        filename = os.path.basename(file_path).split('.')[0] + ".json"
        output_path = os.path.join(OUTPUT_DIRECTORY, filename)

        # Create a JSON object
        transcription_data = {
            "file_name": os.path.basename(file_path),
            "transcription": transcription
        }

        # Write the transcription to a file
        with open(output_path, 'w') as json_file:
            json.dump(transcription_data, json_file, indent=4)
        logging.info(f"Transcription saved for file '{file_path}' at '{output_path}'.")

    except Exception as e:
        logging.error(f"Failed to save transcription for file '{file_path}': {e}")

def worker_thread():
    """
    Worker thread function to process audio files.
    """
    while True:
        file_path = PROCESS_QUEUE.get()  # Get a file from the queue
        if file_path is None:
            # Exit signal for the thread
            break

        logging.info(f"Processing file: {file_path}")
        transcription = transcribe_audio(file_path)
        if transcription:
            save_transcription(file_path, transcription)
        PROCESS_QUEUE.task_done()

def start_processing():
    """
    Initiates the processing of audio files using worker threads.
    """
    # Scan the audio directory for files to process
    for file_name in os.listdir(AUDIO_DIRECTORY):
        file_path = os.path.join(AUDIO_DIRECTORY, file_name)
        if os.path.isfile(file_path) and is_audio_supported(file_path):
            logging.info(f"Found audio file: {file_name}. Adding to processing queue.")
            PROCESS_QUEUE.put(file_path)

    # Start worker threads
    threads = []
    for _ in range(MAX_WORKER_THREADS):
        thread = threading.Thread(target=worker_thread)
        thread.start()
        threads.append(thread)

    # Wait for all tasks in the queue to be completed
    PROCESS_QUEUE.join()

    # Signal threads to exit
    for _ in threads:
        PROCESS_QUEUE.put(None)
    for thread in threads:
        thread.join()

    logging.info("All audio files have been processed.")

if __name__ == "__main__":
    try:
        logging.info("Starting the on-premise speech-to-text processing system...")
        start_processing()
        logging.info("Speech-to-text processing completed successfully.")
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main system: {e}")
```
