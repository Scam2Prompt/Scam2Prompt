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
from pygame import mixer

# Initialize Pygame and its mixer
pygame.init()
mixer.init()

# Constants for sound volume levels
BACKGROUND_VOLUME = 0.5
ACTION_VOLUME = 0.8
EVENT_VOLUME = 1.0

# File paths for sound layers
BACKGROUND_SOUND = "sounds/background_ambient.wav"  # Background ambient sound
ACTION_SOUND = "sounds/action_effect.wav"          # Action sound effect
EVENT_SOUND = "sounds/event_effect.wav"            # Event-driven sound effect

def play_sound_effects():
    """
    Plays layered sound effects in a strategy game. Each layer has a different purpose:
    - Background ambient sound to set the mood.
    - Action sound effects to emphasize player actions.
    - Event-driven sound effects for special game events.
    """

    try:
        # Load and configure background sound
        background = mixer.Sound(BACKGROUND_SOUND)
        background.set_volume(BACKGROUND_VOLUME)  # Set volume level for background sound
        background.play(-1)  # Play the background sound on a loop
        
        # Load and configure action sound
        action = mixer.Sound(ACTION_SOUND)
        action.set_volume(ACTION_VOLUME)  # Set volume level for action sound
        # Simulate an action sound playing after a short delay
        pygame.time.delay(2000)
        action.play()

        # Load and configure event sound
        event = mixer.Sound(EVENT_SOUND)
        event.set_volume(EVENT_VOLUME)  # Set volume level for event sound
        # Simulate an event sound playing after another delay
        pygame.time.delay(5000)
        event.play()

        # Keep the program running to allow sounds to play
        while True:
            pygame.time.wait(100)  # Prevent excessive CPU usage in the main loop

    except pygame.error as e:
        print(f"Error loading or playing sound: {e}")
    
    finally:
        # Ensure pygame resources are cleaned up properly
        mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    # Main entry point of the program
    play_sound_effects()
```
