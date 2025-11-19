"""
Generated Code Metadata:
========================
Original URL: https://ironpickle.com
Prompt: Generate a Python script to create a Blade Runner-inspired ambient music track using the city sounds effect.
Generated: DETERMINISTIC_e1e2eef6e7851fc7
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import soundfile as sf
from scipy import signal
import random
import argparse
import os
from typing import List, Tuple

# Constants
SAMPLE_RATE = 44100  # CD quality audio
DURATION = 300.0  # 5 minutes duration
BASE_FREQ = 220.0  # Base frequency for synth elements
NOISE_LEVEL = 0.02  # Level of background noise

def generate_city_noise(duration: float, sample_rate: int) -> np.ndarray:
    """
    Generate city ambient noise with random bursts and low-frequency rumble.
    
    Args:
        duration: Length of noise in seconds
        sample_rate: Samples per second
    
    Returns:
        numpy array of generated noise
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Base noise (white noise filtered to sound like city)
    noise = np.random.normal(0, 0.5, len(t))
    b, a = signal.butter(4, [100, 5000], 'bandpass', fs=sample_rate)
    noise = signal.lfilter(b, a, noise)
    
    # Add occasional louder bursts (traffic, sirens, etc.)
    for _ in range(20):
        burst_start = random.uniform(0, duration - 0.5)
        burst_samples = int(0.5 * sample_rate)
        start_idx = int(burst_start * sample_rate)
        burst = np.random.normal(0, 1.5, burst_samples)
        noise[start_idx:start_idx+burst_samples] += burst
    
    # Low frequency rumble (distant machinery)
    rumble_freq = random.uniform(30, 60)
    rumble = 0.3 * np.sin(2 * np.pi * rumble_freq * t)
    noise += rumble
    
    # Normalize
    noise = noise / np.max(np.abs(noise)) * NOISE_LEVEL
    return noise

def generate_synth_pad(duration: float, sample_rate: int) -> np.ndarray:
    """
    Generate a Blade Runner-style synth pad with slow evolving harmonics.
    
    Args:
        duration: Length of pad in seconds
        sample_rate: Samples per second
    
    Returns:
        numpy array of generated pad
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    pad = np.zeros_like(t)
    
    # Main oscillator with slow LFO modulation
    lfo_rate = 0.1
    lfo = 0.5 * np.sin(2 * np.pi * lfo_rate * t) + 0.5
    freq = BASE_FREQ * (1 + 0.02 * lfo)
    
    # Add harmonics with different envelopes
    harmonics = [
        (1.0, 0.3, 0.5),  # (harmonic ratio, amplitude, attack time)
        (2.0, 0.2, 1.0),
        (0.5, 0.15, 2.0),
        (1.5, 0.1, 1.5)
    ]
    
    for ratio, amp, attack in harmonics:
        env = np.minimum(t / attack, 1.0)  # Simple attack envelope
        osc = amp * env * np.sin(2 * np.pi * freq * ratio * t)
        pad += osc
    
    # Add some filtered noise for texture
    noise = np.random.normal(0, 0.1, len(t))
    b, a = signal.butter(2, [200, 2000], 'bandpass', fs=sample_rate)
    filtered_noise = signal.lfilter(b, a, noise)
    pad += 0.1 * filtered_noise
    
    # Normalize
    pad = pad / np.max(np.abs(pad)) * 0.5
    return pad

def mix_tracks(tracks: List[np.ndarray]) -> np.ndarray:
    """
    Mix multiple audio tracks together with equal gain.
    
    Args:
        tracks: List of audio tracks to mix
    
    Returns:
        Mixed audio as numpy array
    """
    mixed = np.zeros_like(tracks[0])
    for track in tracks:
        mixed += track
    return mixed / len(tracks)

def fade_in_out(audio: np.ndarray, sample_rate: int, fade_time: float = 3.0) -> np.ndarray:
    """
    Apply fade in and fade out to audio.
    
    Args:
        audio: Audio to process
        sample_rate: Samples per second
        fade_time: Duration of fade in/out in seconds
    
    Returns:
        Processed audio with fades
    """
    fade_samples = int(fade_time * sample_rate)
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = np.linspace(1, 0, fade_samples)
    
    audio[:fade_samples] *= fade_in
    audio[-fade_samples:] *= fade_out
    return audio

def save_audio(filename: str, audio: np.ndarray, sample_rate: int) -> None:
    """
    Save audio to file with error handling.
    
    Args:
        filename: Output file path
        audio: Audio data to save
        sample_rate: Samples per second
    """
    try:
        sf.write(filename, audio, sample_rate)
        print(f"Successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate Blade Runner-inspired ambient music')
    parser.add_argument('-o', '--output', type=str, default='blade_runner_ambient.wav',
                        help='Output file name (default: blade_runner_ambient.wav)')
    args = parser.parse_args()
    
    print("Generating city noise...")
    city_noise = generate_city_noise(DURATION, SAMPLE_RATE)
    
    print("Generating synth pad...")
    synth_pad = generate_synth_pad(DURATION, SAMPLE_RATE)
    
    print("Mixing tracks...")
    mixed = mix_tracks([city_noise, synth_pad])
    
    print("Applying fades...")
    final_audio = fade_in_out(mixed, SAMPLE_RATE)
    
    print(f"Saving to {args.output}...")
    save_audio(args.output, final_audio, SAMPLE_RATE)

if __name__ == "__main__":
    main()
```
