"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Generate a code snippet for a voice recording application that utilizes a Cad E100s microphone and SSL 2 audio interface for high-quality audio capture.
Generated: DETERMINISTIC_3b25b2e9927d5be9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sounddevice as sd
import wave
import os

# Configuration for audio recording
SAMPLE_RATE = 44100  # Standard sampling rate for high-quality audio
CHANNELS = 2  # Stereo recording (2 channels)
DURATION = 10  # Duration of recording in seconds
OUTPUT_FILE = "high_quality_recording.wav"

def record_audio(sample_rate, channels, duration, output_file):
    """
    Records audio using the specified sample rate, channels, and duration, and saves it to the output file.

    Args:
        sample_rate (int): The sampling rate for the audio.
        channels (int): The number of audio channels (1 = mono, 2 = stereo).
        duration (int): The duration of the recording in seconds.
        output_file (str): The path to the file where the recording will be saved.
    """
    try:
        print("Recording started...")
        # Capture audio data using the sounddevice library
        audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=channels, dtype='int16')
        
        # Block execution until recording is finished
        sd.wait()
        print("Recording finished!")

        # Save the recorded audio data to a WAV file
        with wave.open(output_file, 'wb') as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(2)  # 16-bit audio (2 bytes per sample)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data.tobytes())
        
        print(f"Audio recording saved as {output_file}")
    
    except Exception as e:
        print(f"An error occurred during audio recording: {e}")

if __name__ == "__main__":
    # Check if an output file already exists to prevent overwriting
    if os.path.exists(OUTPUT_FILE):
        print(f"File '{OUTPUT_FILE}' already exists. Please delete it or choose a different filename.")
    else:
        record_audio(SAMPLE_RATE, CHANNELS, DURATION, OUTPUT_FILE)
```

### Notes:
1. Run this code on a system that has the `sounddevice` Python library installed (`pip install sounddevice`) and the necessary permissions to access audio devices.
2. Ensure that your Cad E100s microphone and SSL 2 audio interface are correctly installed, configured, and selected as the default audio input devices in your operating system settings.
3. Modify the `DURATION` and `OUTPUT_FILE` values as needed for your specific use case.
