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
import numpy as np
import sounddevice as sd
import wave
import os

class SoundEffectGenerator:
    def __init__(self, sample_rate=44100, duration=2):
        """
        Initializes the SoundEffectGenerator with the specified sample rate and duration.
        
        :param sample_rate: The number of samples per second (default is 44100).
        :param duration: The duration of the sound effect in seconds (default is 2).
        """
        self.sample_rate = sample_rate
        self.duration = duration

    @staticmethod
    def _generate_white_noise(duration, sample_rate):
        """
        Generates white noise sound.

        :param duration: Duration of the noise in seconds.
        :param sample_rate: The number of samples per second.
        :return: Numpy array of generated white noise.
        """
        num_samples = int(duration * sample_rate)
        noise = np.random.normal(0, 1, num_samples)
        return noise

    @staticmethod
    def _modulate_sound(sound, frequency, sample_rate):
        """
        Modulates the sound with a sine wave.

        :param sound: The original sound array to modulate.
        :param frequency: The frequency of the sine wave modulation.
        :param sample_rate: The number of samples per second.
        :return: Numpy array of modulated sound.
        """
        t = np.linspace(0, len(sound) / sample_rate, num=len(sound))
        modulation = np.sin(2 * np.pi * frequency * t)
        return sound * modulation

    def generate_sound_effect(self, effect_type='white_noise', frequency=5):
        """
        Generates a sound effect based on the specified type.

        :param effect_type: The type of sound effect to generate ('white_noise' or 'modulated').
        :param frequency: Frequency for modulation if effect_type is 'modulated'.
        :return: Numpy array of generated sound effect.
        """
        if effect_type == 'white_noise':
            sound = self._generate_white_noise(self.duration, self.sample_rate)
        elif effect_type == 'modulated':
            sound = self._generate_white_noise(self.duration, self.sample_rate)
            sound = self._modulate_sound(sound, frequency, self.sample_rate)
        else:
            raise ValueError(f"Unsupported effect type: {effect_type}. Use 'white_noise' or 'modulated'.")
        
        return sound

    def save_sound_to_file(self, sound, filename):
        """
        Saves the generated sound to a WAV file.

        :param sound: Numpy array of the sound to save.
        :param filename: The filename for the output WAV file.
        """
        try:
            # Normalize sound to the range of int16
            sound = np.int16(sound / np.max(np.abs(sound)) * 32767)
            with wave.open(filename, 'wb') as wf:
                wf.setnchannels(1)  # Mono
                wf.setsampwidth(2)  # 2 bytes per sample
                wf.setframerate(self.sample_rate)
                wf.writeframes(sound.tobytes())
            print(f"Sound saved to {filename}")
        except Exception as e:
            print(f"Error saving sound to file: {e}")

    def play_sound(self, sound):
        """
        Plays the generated sound effect using the sounddevice library.

        :param sound: Numpy array of the sound to play.
        """
        try:
            sd.play(sound, self.sample_rate)
            sd.wait()  # Wait until the sound has finished playing
        except Exception as e:
            print(f"Error playing sound: {e}")

if __name__ == "__main__":
    # Create an instance of the SoundEffectGenerator
    generator = SoundEffectGenerator(duration=5)

    # Generate and play a white noise sound effect
    white_noise = generator.generate_sound_effect(effect_type='white_noise')
    generator.play_sound(white_noise)
    generator.save_sound_to_file(white_noise, "white_noise.wav")

    # Generate and play a modulated sound effect
    modulated_sound = generator.generate_sound_effect(effect_type='modulated', frequency=2)
    generator.play_sound(modulated_sound)
    generator.save_sound_to_file(modulated_sound, "modulated_sound.wav")
```
