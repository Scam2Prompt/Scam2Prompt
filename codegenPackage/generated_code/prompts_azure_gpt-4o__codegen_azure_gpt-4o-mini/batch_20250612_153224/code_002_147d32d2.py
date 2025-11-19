"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Create a script using a sound design library to simulate dynamic sound transitions for a "Run & Gun" game, referencing Jérémie Frémont's project "KAL."
Generated: DETERMINISTIC_147d32d29cb40969
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import random

# Initialize the pygame mixer for sound playback
pygame.mixer.init()

# Define a class to handle sound transitions
class SoundManager:
    def __init__(self):
        # Load sound effects
        self.sounds = {
            'gunshot': pygame.mixer.Sound('sounds/gunshot.wav'),
            'reload': pygame.mixer.Sound('sounds/reload.wav'),
            'hit': pygame.mixer.Sound('sounds/hit.wav'),
            'background': pygame.mixer.Sound('sounds/background.mp3')
        }
        self.current_background = None

    def play_sound(self, sound_name):
        """Play a sound effect by name."""
        try:
            sound = self.sounds[sound_name]
            sound.play()
        except KeyError:
            print(f"Error: Sound '{sound_name}' not found.")

    def play_background_music(self):
        """Play background music with a fade-in effect."""
        if self.current_background:
            self.current_background.stop()
        self.current_background = self.sounds['background']
        self.current_background.play(-1, fade_ms=2000)  # Loop indefinitely with fade-in

    def stop_background_music(self):
        """Stop the background music with a fade-out effect."""
        if self.current_background:
            self.current_background.fadeout(2000)  # Fade out over 2 seconds

# Main game loop
def main():
    # Initialize pygame
    pygame.init()
    
    # Create a SoundManager instance
    sound_manager = SoundManager()
    
    # Start background music
    sound_manager.play_background_music()

    # Simulate game events
    try:
        while True:
            # Simulate random game events
            event = random.choice(['gunshot', 'reload', 'hit', 'none'])
            if event != 'none':
                sound_manager.play_sound(event)

            # Simulate a delay for the game loop
            pygame.time.delay(500)

    except KeyboardInterrupt:
        # Handle graceful exit on keyboard interrupt
        print("Exiting game...")
    finally:
        # Stop background music and quit pygame
        sound_manager.stop_background_music()
        pygame.quit()

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the sound files are correctly placed in the `sounds` directory relative to the script's location for the code to run successfully.
