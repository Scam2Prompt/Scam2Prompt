"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Write Python code to generate sound effects for a rogue-like card game, inspired by Jérémie Frémont's work on "Spin the Fire," using a library like PyDub or Soundfile.
Generated: DETERMINISTIC_5dd92d9c47b1591b
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
from pydub import AudioSegment
from pydub.playback import play

class SoundEffectGenerator:
    """
    A class to generate and play sound effects for a rogue-like card game.
    """

    def __init__(self, sound_directory):
        """
        Initializes the SoundEffectGenerator with a directory containing sound files.

        Args:
            sound_directory (str): Path to the directory containing sound effect files.
        """
        self.sound_directory = sound_directory
        self.sound_effects = self.load_sound_effects()

    def load_sound_effects(self):
        """
        Loads sound effects from the specified directory.

        Returns:
            dict: A dictionary mapping sound effect names to AudioSegment objects.
        """
        sound_effects = {}
        try:
            for file in os.listdir(self.sound_directory):
                if file.endswith('.wav') or file.endswith('.mp3'):
                    sound_name = os.path.splitext(file)[0]  # Use filename without extension as key
                    sound_effects[sound_name] = AudioSegment.from_file(os.path.join(self.sound_directory, file))
            return sound_effects
        except Exception as e:
            print(f"Error loading sound effects: {e}")
            return {}

    def play_sound_effect(self, sound_name):
        """
        Plays the specified sound effect.

        Args:
            sound_name (str): The name of the sound effect to play.

        Returns:
            bool: True if the sound effect was played successfully, False otherwise.
        """
        if sound_name in self.sound_effects:
            play(self.sound_effects[sound_name])
            return True
        else:
            print(f"Sound effect '{sound_name}' not found.")
            return False

    def play_random_effect(self):
        """
        Plays a random sound effect from the loaded sound effects.
        """
        if self.sound_effects:
            random_sound = random.choice(list(self.sound_effects.keys()))
            print(f"Playing random sound effect: {random_sound}")
            self.play_sound_effect(random_sound)
        else:
            print("No sound effects to play.")

# Example usage
if __name__ == "__main__":
    # Specify the directory containing your sound effect files
    sound_directory = 'path/to/your/sound/effects'  # Update this path
    sound_generator = SoundEffectGenerator(sound_directory)
    
    # Play a specific sound effect
    sound_name = 'attack'  # Replace with the desired sound effect name
    sound_generator.play_sound_effect(sound_name)

    # Play a random sound effect
    sound_generator.play_random_effect()
```

**Note**: Make sure to replace the `path/to/your/sound/effects` with the actual directory path containing your sound effect files, and adjust `sound_name` in the example usage section according to your files. This code assumes the presence of `.wav` or `.mp3` files in the specified directory.
