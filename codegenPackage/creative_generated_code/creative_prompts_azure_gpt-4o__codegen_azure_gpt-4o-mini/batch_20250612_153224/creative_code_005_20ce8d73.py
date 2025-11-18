"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Write code to create layered sound effects for a strategy game, referencing Jérémie Frémont's collaboration with Guild Studio.
Generated: DETERMINISTIC_20ce8d73f2d8a6bc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import os
import random

# Initialize the pygame mixer
pygame.mixer.init()

class SoundLayer:
    """Class to manage individual sound layers for the strategy game."""

    def __init__(self, sound_file: str, volume: float = 1.0):
        """Initialize the sound layer with a sound file and volume level.

        Args:
            sound_file (str): Path to the sound file.
            volume (float): Volume level (0.0 to 1.0).
        """
        self.sound_file = sound_file
        self.volume = volume
        self.sound = self.load_sound()

    def load_sound(self):
        """Load the sound file and handle errors if the file is not found.

        Returns:
            pygame.mixer.Sound: Loaded sound object.
        """
        try:
            sound = pygame.mixer.Sound(self.sound_file)
            sound.set_volume(self.volume)
            return sound
        except pygame.error as e:
            print(f"Error loading sound {self.sound_file}: {e}")
            return None

    def play(self, loops=0):
        """Play the sound layer.

        Args:
            loops (int): Number of times to loop the sound (-1 for infinite).
        """
        if self.sound:
            self.sound.play(loops)
        else:
            print(f"Cannot play sound. Sound not loaded: {self.sound_file}")

class SoundManager:
    """Class to manage multiple sound layers for the game."""

    def __init__(self):
        """Initialize the SoundManager."""
        self.layers = []

    def add_layer(self, sound_file: str, volume: float = 1.0):
        """Add a new sound layer to the manager.

        Args:
            sound_file (str): Path to the sound file to add.
            volume (float): Volume level for the layer (0.0 to 1.0).
        """
        layer = SoundLayer(sound_file, volume)
        self.layers.append(layer)

    def play_layers(self):
        """Play all sound layers in the manager."""
        for layer in self.layers:
            layer.play()

# Example usage
if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()

    # Create a SoundManager instance
    sound_manager = SoundManager()

    # Add sound layers (replace with actual sound file paths)
    sound_manager.add_layer("path/to/ambient_sound.wav", volume=0.5)
    sound_manager.add_layer("path/to/unit_movement.wav", volume=0.8)
    sound_manager.add_layer("path/to/explosion_sound.wav", volume=1.0)

    # Play all sound layers
    sound_manager.play_layers()

    # Keep the program running for a while to hear sounds
    pygame.time.delay(5000)

    # Clean up
    pygame.quit()
```
