"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.prointegrationfuture.asia
Prompt: Create a Python program to simulate a connected sensory journey using AV and lighting systems, inspired by the demonstrations at Pro Integration Future Asia.
Generated: DETERMINISTIC_9f8ee7cbf3ae40ab
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import threading

class AVSystem:
    """Class to simulate an Audio-Visual (AV) system."""

    def __init__(self):
        """Initialize the AV system with default settings."""
        self.is_playing = False

    def play(self, media):
        """Play the specified media.

        Args:
            media (str): The name of the media to play.
        """
        self.is_playing = True
        print(f"Playing: {media}")
        time.sleep(2)  # Simulate media play duration
        self.stop()

    def stop(self):
        """Stop the currently playing media."""
        self.is_playing = False
        print("Media stopped.")

class LightingSystem:
    """Class to simulate a lighting system."""

    def __init__(self):
        """Initialize the lighting system with default settings."""
        self.light_state = "Off"

    def set_light(self, state):
        """Set the state of the lighting system.

        Args:
            state (str): The desired state of the lights ("On" or "Off").
        """
        self.light_state = state
        print(f"Lighting is now: {self.light_state}")

class SensoryJourney:
    """Class to manage the sensory journey through AV and lighting systems."""

    def __init__(self):
        """Initialize the sensory journey with AV and lighting systems."""
        self.av_system = AVSystem()
        self.lighting_system = LightingSystem()

    def start_journey(self):
        """Start the sensory journey simulation."""
        print("Starting the sensory journey...")
        try:
            # Example sequence of media and lighting effects
            media_sequence = ["Nature Sounds", "Chill Music", "Upbeat Music"]
            lighting_sequence = ["Warm White", "Cool Blue", "Dynamic Colors"]

            for media in media_sequence:
                # Simulate changing lights before each media play
                self.lighting_system.set_light(random.choice(lighting_sequence))
                self.av_system.play(media)
                time.sleep(1)  # Pause before next segment

            print("Sensory journey completed.")
        except Exception as e:
            print(f"An error occurred during the sensory journey: {e}")

if __name__ == "__main__":
    # Run the sensory journey simulation in a separate thread for responsiveness
    journey = SensoryJourney()
    journey_thread = threading.Thread(target=journey.start_journey)
    journey_thread.start()

    # Wait for the journey to complete
    journey_thread.join()
    print("Journey thread has completed.")
```
