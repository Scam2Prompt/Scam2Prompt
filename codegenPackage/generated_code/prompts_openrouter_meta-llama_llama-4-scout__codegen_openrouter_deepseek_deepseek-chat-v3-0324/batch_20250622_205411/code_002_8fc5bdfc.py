"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Generate code for a music disk release like "OVeRclocked remix" by Jess, using a chip tune music format.
Generated: DETERMINISTIC_8fc5bdfc64617602
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import numpy as np
from pygame import mixer

# Initialize pygame and mixer
pygame.init()
mixer.init(frequency=44100, size=-16, channels=2)

# Constants
SAMPLE_RATE = 44100
BIT_DEPTH = 16
CHANNELS = 2
DURATION = 3.0  # seconds per note
VOLUME = 0.5

# Chip tune instrument definitions
def square_wave(freq, duration, volume=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sign(np.sin(2 * np.pi * freq * t))
    return (wave * volume * 32767).astype(np.int16)

def triangle_wave(freq, duration, volume=0.5):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = 2 * np.arcsin(np.sin(2 * np.pi * freq * t)) / np.pi
    return (wave * volume * 32767).astype(np.int16)

def noise_wave(duration, volume=0.5):
    samples = int(SAMPLE_RATE * duration)
    wave = np.random.randint(-32767, 32767, samples, dtype=np.int16)
    return (wave * volume).astype(np.int16)

# Musical notes frequencies (Hz)
NOTES = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25,
}

# OVeRclocked remix melody
MELODY = [
    ('C4', 'square'),
    ('E4', 'square'),
    ('G4', 'square'),
    ('C5', 'square'),
    ('E4', 'triangle'),
    ('G4', 'triangle'),
    ('C5', 'triangle'),
    ('E4', 'noise'),
    ('G4', 'noise'),
    ('C5', 'noise'),
]

def generate_track():
    """Generate stereo track from melody."""
    stereo_track = np.zeros((int(SAMPLE_RATE * DURATION * len(MELODY)), 2), dtype=np.int16)
    
    for i, (note, wave_type) in enumerate(MELODY):
        start = i * int(SAMPLE_RATE * DURATION)
        end = start + int(SAMPLE_RATE * DURATION)
        
        if wave_type == 'square':
            mono_wave = square_wave(NOTES[note], DURATION, VOLUME)
        elif wave_type == 'triangle':
            mono_wave = triangle_wave(NOTES[note], DURATION, VOLUME)
        elif wave_type == 'noise':
            mono_wave = noise_wave(DURATION, VOLUME)
        
        stereo_track[start:end, 0] = mono_wave
        stereo_track[start:end, 1] = mono_wave
    
    return stereo_track

def save_as_wav(filename, data):
    """Save numpy array as WAV file."""
    mixer.Sound(data).export(filename, format='wav')

def play_music():
    """Play the generated music."""
    track = generate_track()
    sound = mixer.Sound(track)
    sound.play()
    pygame.time.wait(int(DURATION * 1000 * len(MELODY)))

def main():
    try:
        print("Generating OVeRclocked remix...")
        track = generate_track()
        save_as_wav("overclocked_remix.wav", track)
        print("Music saved as overclocked_remix.wav")
        
        print("Playing the track...")
        play_music()
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
```
