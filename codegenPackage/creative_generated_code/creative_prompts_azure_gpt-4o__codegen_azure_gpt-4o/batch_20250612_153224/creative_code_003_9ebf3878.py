"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Generate code to design ambient soundscapes for a documentary series, inspired by Jérémie Frémont's work on "Race for a Vaccine," using Python-based audio tools.
Generated: DETERMINISTIC_9ebf387852d15f8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
import wave
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

# Constants for the soundscape design
OUTPUT_DIR = "soundscapes"
SAMPLE_RATE = 44100  # Hz
DURATION_SECONDS = 30  # Length of each soundscape
AMBIENT_ELEMENTS = ["rain.wav", "birds.wav", "wind.wav", "stream.wav"]  # Example audio files
MAX_VOLUME_DB = -10  # Maximum volume level for each track in dBFS

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_white_noise(duration, sample_rate=SAMPLE_RATE):
    """
    Generate white noise as a numpy array.
    :param duration: Duration of the noise in seconds
    :param sample_rate: Sampling rate in Hz
    :return: White noise as a numpy array
    """
    num_samples = duration * sample_rate
    white_noise = np.random.uniform(-1, 1, num_samples).astype(np.float32)
    return white_noise

def save_wave_file(filename, audio_data, sample_rate=SAMPLE_RATE):
    """
    Save audio data as a wave file.
    :param filename: Path to save the wave file
    :param audio_data: Audio data in numpy format
    :param sample_rate: Sampling rate in Hz
    """
    audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(2)  # 2 bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def mix_audio_files(file_list, output_file):
    """
    Mix multiple audio files together into a single soundscape.
    :param file_list: List of file paths to audio files
    :param output_file: Path to save the mixed soundscape
    """
    try:
        mix = AudioSegment.silent(duration=DURATION_SECONDS * 1000)  # Initialize empty soundscape
        for audio_file in file_list:
            audio = AudioSegment.from_file(audio_file)
            audio = audio - random.randint(0, abs(MAX_VOLUME_DB))  # Randomized volume for variety
            mix = mix.overlay(audio)
        
        mix.export(output_file, format="wav")
        print(f"Soundscape saved to {output_file}")
    except Exception as e:
        print(f"Error while mixing audio files: {e}")

def create_soundscape():
    """
    Create a single soundscape by mixing ambient elements and optionally adding white noise.
    """
    # Randomly select ambient elements
    selected_elements = random.sample(AMBIENT_ELEMENTS, k=min(len(AMBIENT_ELEMENTS), 3))
    
    # Path for the output soundscape file
    soundscape_file = os.path.join(OUTPUT_DIR, f"soundscape_{random.randint(1000, 9999)}.wav")
    
    # Mix the selected elements into a single soundscape
    mix_audio_files(selected_elements, soundscape_file)

    # Optionally add white noise
    if random.choice([True, False]):  # Randomly decide to add white noise
        white_noise = generate_white_noise(DURATION_SECONDS)
        noise_file = os.path.join(OUTPUT_DIR, "white_noise.wav")
        save_wave_file(noise_file, white_noise)
        
        # Mix white noise into the soundscape
        soundscape_with_noise = os.path.join(OUTPUT_DIR, f"soundscape_with_noise_{random.randint(1000, 9999)}.wav")
        mix_audio_files([soundscape_file, noise_file], soundscape_with_noise)

# Main entry point for soundscape generation
if __name__ == "__main__":
    print("Generating soundscapes...")
    for _ in range(5):  # Generate multiple soundscapes
        create_soundscape()
    print("Soundscape generation complete.")
```
