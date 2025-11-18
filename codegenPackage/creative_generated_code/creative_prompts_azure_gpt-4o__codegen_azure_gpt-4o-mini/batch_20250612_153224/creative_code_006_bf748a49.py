"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Recommend sound design techniques or libraries for creating music for radio programs, inspired by Jérémie Frémont's work on "Hondelatte raconte."
Generated: DETERMINISTIC_bf748a499bf7b4bf
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
import logging
from pydub import AudioSegment
from pydub.playback import play

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SoundDesign:
    def __init__(self, sound_directory):
        """
        Initializes the SoundDesign class with the path to the sound files directory.

        :param sound_directory: Path to the directory containing sound files.
        """
        self.sound_directory = sound_directory
        self.sounds = self.load_sounds()

    def load_sounds(self):
        """
        Loads sound files from the specified directory.

        :return: Dictionary of sound names mapped to AudioSegment objects.
        """
        sounds = {}
        try:
            for filename in os.listdir(self.sound_directory):
                if filename.endswith(('.wav', '.mp3', '.ogg')):
                    sound_path = os.path.join(self.sound_directory, filename)
                    sounds[filename] = AudioSegment.from_file(sound_path)
                    logging.info(f"Loaded sound: {filename}")
        except Exception as e:
            logging.error(f"Error loading sounds: {e}")
        return sounds

    def play_sound(self, sound_name):
        """
        Plays a sound by its name.

        :param sound_name: The name of the sound file to play.
        """
        try:
            sound = self.sounds.get(sound_name)
            if sound:
                play(sound)
                logging.info(f"Playing sound: {sound_name}")
            else:
                logging.warning(f"Sound not found: {sound_name}")
        except Exception as e:
            logging.error(f"Error playing sound {sound_name}: {e}")

    def adjust_volume(self, sound_name, volume_change):
        """
        Adjusts the volume of a sound.

        :param sound_name: The name of the sound file to adjust.
        :param volume_change: Number of dB to change the volume (positive increases, negative decreases).
        :return: Adjusted sound or None if not found.
        """
        try:
            sound = self.sounds.get(sound_name)
            if sound:
                adjusted_sound = sound + volume_change
                logging.info(f"Adjusted volume for {sound_name} by {volume_change} dB")
                return adjusted_sound
            else:
                logging.warning(f"Sound not found for volume adjustment: {sound_name}")
        except Exception as e:
            logging.error(f"Error adjusting volume for {sound_name}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    sound_design = SoundDesign('path/to/sound/files')
    sound_design.play_sound('background_music.mp3')
    adjusted_sound = sound_design.adjust_volume('background_music.mp3', -5)
    if adjusted_sound:
        play(adjusted_sound)
```

Make sure to replace `'path/to/sound/files'` with the actual path to your sound files when using this code.
