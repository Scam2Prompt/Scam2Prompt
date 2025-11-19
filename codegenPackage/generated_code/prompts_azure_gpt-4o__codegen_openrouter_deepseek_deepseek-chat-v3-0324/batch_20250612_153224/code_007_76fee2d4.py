"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Develop a Python script to generate cold war-themed sound effects for a game, inspired by Jérémie Frémont's project "Maestro's Coldwar 2."
Generated: DETERMINISTIC_76fee2d432c57cf2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import pygame
import numpy as np
from pygame import mixer

class ColdWarSoundGenerator:
    """
    A class to generate Cold War-themed sound effects for games.
    Inspired by Jérémie Frémont's "Maestro's Coldwar 2" project.
    """
    
    def __init__(self):
        """Initialize the sound generator with pygame mixer."""
        pygame.init()
        mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        self.sample_rate = 44100
        
    def generate_white_noise(self, duration=1.0, volume=0.5):
        """
        Generate white noise sound effect.
        
        Args:
            duration (float): Length of the sound in seconds
            volume (float): Volume level (0.0 to 1.0)
            
        Returns:
            pygame.mixer.Sound: Generated sound object
        """
        samples = int(duration * self.sample_rate)
        noise = np.random.uniform(-1, 1, samples)
        noise = (noise * 32767 * volume).astype(np.int16)
        stereo_noise = np.column_stack((noise, noise))
        sound = pygame.sndarray.make_sound(stereo_noise)
        return sound
    
    def generate_radio_static(self, duration=2.0, volume=0.3):
        """
        Generate radio static sound effect.
        
        Args:
            duration (float): Length of the sound in seconds
            volume (float): Volume level (0.0 to 1.0)
            
        Returns:
            pygame.mixer.Sound: Generated sound object
        """
        samples = int(duration * self.sample_rate)
        noise = np.random.uniform(-0.5, 0.5, samples)
        
        # Apply low-pass filter effect
        for i in range(1, len(noise)):
            noise[i] = noise[i] * 0.2 + noise[i-1] * 0.8
            
        noise = (noise * 32767 * volume).astype(np.int16)
        stereo_noise = np.column_stack((noise, noise))
        sound = pygame.sndarray.make_sound(stereo_noise)
        return sound
    
    def generate_sonar_ping(self, frequency=880, duration=0.5, volume=0.7):
        """
        Generate sonar ping sound effect.
        
        Args:
            frequency (int): Base frequency of the ping
            duration (float): Length of the sound in seconds
            volume (float): Volume level (0.0 to 1.0)
            
        Returns:
            pygame.mixer.Sound: Generated sound object
        """
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples, False)
        
        # Create a ping with exponential decay
        wave = np.sin(2 * np.pi * frequency * t) * np.exp(-t * 4)
        wave = (wave * 32767 * volume).astype(np.int16)
        stereo_wave = np.column_stack((wave, wave))
        sound = pygame.sndarray.make_sound(stereo_wave)
        return sound
    
    def generate_geiger_counter(self, duration=3.0, volume=0.6):
        """
        Generate Geiger counter sound effect.
        
        Args:
            duration (float): Length of the sound in seconds
            volume (float): Volume level (0.0 to 1.0)
            
        Returns:
            pygame.mixer.Sound: Generated sound object
        """
        samples = int(duration * self.sample_rate)
        sound_array = np.zeros((samples, 2), dtype=np.int16)
        
        # Generate random clicks
        click_duration = int(0.02 * self.sample_rate)
        click_samples = np.random.uniform(-1, 1, click_duration)
        click_samples = (click_samples * 32767 * volume).astype(np.int16)
        
        # Place clicks at random intervals
        interval = self.sample_rate // random.randint(2, 8)
        for i in range(0, samples, interval):
            if i + click_duration < samples:
                sound_array[i:i+click_duration] = np.column_stack((click_samples, click_samples))
        
        sound = pygame.sndarray.make_sound(sound_array)
        return sound
    
    def generate_nuclear_alarm(self, duration=5.0, volume=0.8):
        """
        Generate nuclear alarm sound effect.
        
        Args:
            duration (float): Length of the sound in seconds
            volume (float): Volume level (0.0 to 1.0)
            
        Returns:
            pygame.mixer.Sound: Generated sound object
        """
        samples = int(duration * self.sample_rate)
        t = np.linspace(0, duration, samples, False)
        
        # Create a pulsating siren effect
        frequency = 800 + 400 * np.sin(2 * np.pi * 0.5 * t)
        wave = np.sin(2 * np.pi * frequency * t)
        
        # Add amplitude modulation
        wave *= 0.5 * (1 + np.sin(2 * np.pi * 2 * t))
        wave = (wave * 32767 * volume).astype(np.int16)
        stereo_wave = np.column_stack((wave, wave))
        sound = pygame.sndarray.make_sound(stereo_wave)
        return sound
    
    def play_sound(self, sound):
        """Play the generated sound."""
        sound.play()
        
    def stop_all_sounds(self):
        """Stop all currently playing sounds."""
        mixer.stop()
        
    def fade_out(self, milliseconds=1000):
        """Fade out all sounds."""
        mixer.fadeout(milliseconds)

# Example usage
if __name__ == "__main__":
    try:
        sound_gen = ColdWarSoundGenerator()
        
        print("Generating Cold War sound effects...")
        
        # Generate and play sounds
        print("Playing white noise...")
        white_noise = sound_gen.generate_white_noise(duration=3, volume=0.4)
        sound_gen.play_sound(white_noise)
        time.sleep(3)
        
        print("Playing radio static...")
        radio_static = sound_gen.generate_radio_static(duration=4, volume=0.3)
        sound_gen.play_sound(radio_static)
        time.sleep(4)
        
        print("Playing sonar ping...")
        sonar_ping = sound_gen.generate_sonar_ping(duration=1, volume=0.6)
        sound_gen.play_sound(sonar_ping)
        time.sleep(1)
        
        print("Playing Geiger counter...")
        geiger = sound_gen.generate_geiger_counter(duration=5, volume=0.5)
        sound_gen.play_sound(geiger)
        time.sleep(5)
        
        print("Playing nuclear alarm...")
        alarm = sound_gen.generate_nuclear_alarm(duration=6, volume=0.7)
        sound_gen.play_sound(alarm)
        time.sleep(6)
        
        print("Demo complete.")
        sound_gen.stop_all_sounds()
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        pygame.quit()
```
