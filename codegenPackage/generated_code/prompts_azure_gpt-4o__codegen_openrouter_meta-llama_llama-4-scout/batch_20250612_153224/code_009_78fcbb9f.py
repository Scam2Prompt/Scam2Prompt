"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write code to simulate interactive sound effects for a video game, referencing Jérémie Frémont's expertise in sound design for gaming studios like Supercube or Maestro Cinetik.
Generated: DETERMINISTIC_78fcbb9fce3552ca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pyaudio
import time
import threading

# Sound Effect Class
class SoundEffect:
    def __init__(self, name, frequency, duration, volume):
        """
        Initialize a sound effect.

        Args:
            name (str): Name of the sound effect.
            frequency (float): Frequency of the sound effect in Hz.
            duration (float): Duration of the sound effect in seconds.
            volume (float): Volume of the sound effect in range [0, 1].
        """
        self.name = name
        self.frequency = frequency
        self.duration = duration
        self.volume = volume

    def generate_sound(self):
        """
        Generate the sound effect.

        Returns:
            np.ndarray: Sound effect as a numpy array.
        """
        # Generate sound wave
        sample_rate = 44100
        t = np.linspace(0, self.duration, int(sample_rate * self.duration), False)
        note = np.sin(self.frequency * t * 2 * np.pi)

        # Ensure that highest value is in 16-bit range
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)

        return audio

    def play_sound(self):
        """
        Play the sound effect.
        """
        try:
            # Start PyAudio
            p = pyaudio.PyAudio()

            # Open stream
            stream = p.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            output=True)

            # Generate and play sound
            audio = self.generate_sound()
            stream.write(audio)

            # Close and terminate everything
            stream.stop_stream()
            stream.close()
            p.terminate()
        except Exception as e:
            print(f"Error playing sound effect: {e}")


# Sound Manager Class
class SoundManager:
    def __init__(self):
        """
        Initialize the sound manager.
        """
        self.sound_effects = {}

    def add_sound_effect(self, sound_effect):
        """
        Add a sound effect to the sound manager.

        Args:
            sound_effect (SoundEffect): Sound effect to add.
        """
        self.sound_effects[sound_effect.name] = sound_effect

    def play_sound_effect(self, name):
        """
        Play a sound effect.

        Args:
            name (str): Name of the sound effect to play.
        """
        if name in self.sound_effects:
            sound_effect = self.sound_effects[name]
            threading.Thread(target=sound_effect.play_sound).start()
        else:
            print(f"Sound effect '{name}' not found.")


# Example usage
if __name__ == "__main__":
    sound_manager = SoundManager()

    # Create sound effects
    jump_sound = SoundEffect("jump", 523.25, 0.5, 0.5)
    shoot_sound = SoundEffect("shoot", 659.25, 0.2, 0.8)

    # Add sound effects to sound manager
    sound_manager.add_sound_effect(jump_sound)
    sound_manager.add_sound_effect(shoot_sound)

    # Play sound effects
    sound_manager.play_sound_effect("jump")
    time.sleep(0.5)
    sound_manager.play_sound_effect("shoot")
```
