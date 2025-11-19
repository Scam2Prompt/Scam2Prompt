"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Create a Python program to simulate a connected sensory journey using AV and lighting systems, inspired by the demonstrations at Pro Integration Future Asia.
Generated: DETERMINISTIC_9f8ee7cbf3ae40ab
Batch ID: 20250612_145234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import threading

class AVSystem:
    """Class to simulate an Audio-Visual system."""
    
    def __init__(self):
        self.volume = 50  # Default volume level
        self.is_playing = False

    def play(self, media):
        """Simulate playing a media file."""
        if not self.is_playing:
            self.is_playing = True
            print(f"Playing: {media} at volume {self.volume}")
        else:
            print("Media is already playing.")

    def stop(self):
        """Stop the currently playing media."""
        if self.is_playing:
            self.is_playing = False
            print("Media stopped.")
        else:
            print("No media is currently playing.")

    def set_volume(self, volume):
        """Set the volume level."""
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"Volume set to {self.volume}")
        else:
            print("Volume must be between 0 and 100.")


class LightingSystem:
    """Class to simulate a lighting system."""
    
    def __init__(self):
        self.brightness = 50  # Default brightness level
        self.is_on = False

    def turn_on(self):
        """Turn on the lighting system."""
        self.is_on = True
        print("Lighting system turned on.")

    def turn_off(self):
        """Turn off the lighting system."""
        self.is_on = False
        print("Lighting system turned off.")

    def set_brightness(self, brightness):
        """Set the brightness level."""
        if 0 <= brightness <= 100:
            self.brightness = brightness
            print(f"Brightness set to {self.brightness}")
        else:
            print("Brightness must be between 0 and 100.")


class SensoryJourney:
    """Class to simulate a connected sensory journey."""
    
    def __init__(self):
        self.av_system = AVSystem()
        self.lighting_system = LightingSystem()
        self.media_list = ["Nature Sounds", "Ambient Music", "City Sounds", "Relaxing Music"]

    def start_journey(self):
        """Start the sensory journey simulation."""
        print("Starting sensory journey...")
        self.lighting_system.turn_on()
        self.av_system.play(random.choice(self.media_list))
        self.adjust_lighting_and_audio()

    def adjust_lighting_and_audio(self):
        """Adjust lighting and audio settings during the journey."""
        try:
            for _ in range(5):  # Simulate 5 adjustments
                time.sleep(2)  # Wait for 2 seconds between adjustments
                new_brightness = random.randint(0, 100)
                new_volume = random.randint(0, 100)
                self.lighting_system.set_brightness(new_brightness)
                self.av_system.set_volume(new_volume)
        except Exception as e:
            print(f"An error occurred during the journey: {e}")
        finally:
            self.end_journey()

    def end_journey(self):
        """End the sensory journey simulation."""
        print("Ending sensory journey...")
        self.av_system.stop()
        self.lighting_system.turn_off()


if __name__ == "__main__":
    # Create a sensory journey instance and start the journey
    journey = SensoryJourney()
    journey.start_journey()
```
