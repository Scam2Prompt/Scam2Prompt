"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Develop a Python script to generate cold war-themed sound effects for a game, inspired by Jérémie Frémont's project "Maestro's Coldwar 2."
Generated: DETERMINISTIC_76fee2d432c57cf2
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


def generate_sound_effect(effect_type, duration_seconds=2, sample_rate=44100):
    """
    Generate a cold war-themed sound effect based on the specified effect type.

    Args:
        effect_type (str): Type of sound effect to generate. Supported: 'radio_static', 'morse_code', 'radar_ping'.
        duration_seconds (int): Duration of the sound effect in seconds. Default is 2 seconds.
        sample_rate (int): Sample rate for the audio. Default is 44100 Hz.

    Returns:
        np.ndarray: Generated audio data.
    """
    if effect_type not in ['radio_static', 'morse_code', 'radar_ping']:
        raise ValueError("Unsupported effect_type. Choose 'radio_static', 'morse_code', or 'radar_ping'.")

    # Total number of audio samples
    num_samples = duration_seconds * sample_rate

    if effect_type == 'radio_static':
        # Generate white noise for radio static effect
        audio_data = np.random.uniform(-1, 1, num_samples).astype(np.float32)

    elif effect_type == 'morse_code':
        # Generate a Morse code sound sequence
        # Dot: 0.1 seconds, Dash: 0.3 seconds, Silence: 0.1 seconds
        dot_duration = int(sample_rate * 0.1)
        dash_duration = int(sample_rate * 0.3)
        silence_duration = int(sample_rate * 0.1)

        morse_pattern = ['dot', 'silence', 'dash', 'silence', 'dot', 'silence', 'dot', 'silence']
        audio_data = np.array([], dtype=np.float32)

        for element in morse_pattern:
            if element == 'dot':
                audio_data = np.append(audio_data, np.sin(2 * np.pi * 440 * np.arange(dot_duration) / sample_rate))
            elif element == 'dash':
                audio_data = np.append(audio_data, np.sin(2 * np.pi * 440 * np.arange(dash_duration) / sample_rate))
            elif element == 'silence':
                audio_data = np.append(audio_data, np.zeros(silence_duration))

    elif effect_type == 'radar_ping':
        # Generate a radar ping sound effect
        audio_data = np.zeros(num_samples, dtype=np.float32)
        ping_frequency = 1000  # Frequency of the ping in Hz
        ping_duration = int(sample_rate * 0.2)  # Duration of each ping (0.2 seconds)

        for i in range(0, num_samples, sample_rate):  # Add pings every second
            ping = np.sin(2 * np.pi * ping_frequency * np.arange(ping_duration) / sample_rate)
            audio_data[i:i + ping_duration] = ping[:min(ping_duration, num_samples - i)]

    return audio_data


def save_audio_to_wav(audio_data, file_name, sample_rate=44100):
    """
    Save the generated audio data to a WAV file.

    Args:
        audio_data (np.ndarray): Audio data to save.
        file_name (str): Name of the output WAV file.
        sample_rate (int): Sample rate for the audio. Default is 44100 Hz.

    Returns:
        None
    """
    try:
        # Normalize audio data to 16-bit PCM format
        audio_data = np.int16(audio_data * 32767)

        # Write to WAV file
        with wave.open(file_name, 'w') as wav_file:
            wav_file.setnchannels(1)  # Mono audio
            wav_file.setsampwidth(2)  # 16-bit audio
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data.tobytes())
    except Exception as e:
        print(f"Error saving audio file: {e}")


def main():
    """
    Main function to generate cold war-themed sound effects and save them as WAV files.

    Returns:
        None
    """
    # Output directory for sound effects
    output_dir = "sound_effects"
    os.makedirs(output_dir, exist_ok=True)

    # Generate and save sound effects
    try:
        print("Generating radio static...")
        radio_static = generate_sound_effect('radio_static', duration_seconds=5)
        save_audio_to_wav(radio_static, os.path.join(output_dir, 'radio_static.wav'))

        print("Generating Morse code...")
        morse_code = generate_sound_effect('morse_code', duration_seconds=5)
        save_audio_to_wav(morse_code, os.path.join(output_dir, 'morse_code.wav'))

        print("Generating radar ping...")
        radar_ping = generate_sound_effect('radar_ping', duration_seconds=5)
        save_audio_to_wav(radar_ping, os.path.join(output_dir, 'radar_ping.wav'))

        print(f"Sound effects saved in '{output_dir}' directory.")
    except Exception as e:
        print(f"Error generating sound effects: {e}")


if __name__ == "__main__":
    main()
```
