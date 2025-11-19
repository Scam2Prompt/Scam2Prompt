"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write Python code to generate sound effects for a rogue-like card game, inspired by Jérémie Frémont's work on "Spin the Fire," using a library like PyDub or Soundfile.
Generated: DETERMINISTIC_5dd92d9c47b1591b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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

        :param sound_directory: Path to the directory containing sound effect files.
        """
        self.sound_directory = sound_directory
        self.sound_effects = self.load_sound_effects()

    def load_sound_effects(self):
        """
        Loads sound effects from the specified directory.

        :return: A dictionary of sound effects with their names as keys.
        """
        sound_effects = {}
        try:
            for filename in os.listdir(self.sound_directory):
                if filename.endswith('.wav') or filename.endswith('.mp3'):
                    sound_name = os.path.splitext(filename)[0]
                    sound_path = os.path.join(self.sound_directory, filename)
                    sound_effects[sound_name] = AudioSegment.from_file(sound_path)
            return sound_effects
        except Exception as e:
            print(f"Error loading sound effects: {e}")
            return {}

    def play_sound(self, sound_name):
        """
        Plays the specified sound effect.

        :param sound_name: The name of the sound effect to play.
        """
        try:
            if sound_name in self.sound_effects:
                play(self.sound_effects[sound_name])
            else:
                print(f"Sound effect '{sound_name}' not found.")
        except Exception as e:
            print(f"Error playing sound '{sound_name}': {e}")

    def play_random_sound(self):
        """
        Plays a random sound effect from the loaded sound effects.
        """
        if self.sound_effects:
            sound_name = random.choice(list(self.sound_effects.keys()))
            self.play_sound(sound_name)
        else:
            print("No sound effects available to play.")

if __name__ == "__main__":
    # Example usage
    sound_directory = "path/to/your/sound/effects"  # Update this path
    sound_generator = SoundEffectGenerator(sound_directory)

    # Play a specific sound effect
    sound_generator.play_sound("attack")  # Replace with an actual sound name

    # Play a random sound effect
    sound_generator.play_random_sound()
```

Make sure to replace `"path/to/your/sound/effects"` with the actual path to your sound files. The sound files should be in `.wav` or `.mp3` format.
