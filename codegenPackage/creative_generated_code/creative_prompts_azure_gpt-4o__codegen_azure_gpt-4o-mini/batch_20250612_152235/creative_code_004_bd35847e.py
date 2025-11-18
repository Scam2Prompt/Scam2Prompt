"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sproutstudios.in
Prompt: Write code to simulate a VR experience for marketing ads, referencing the VR projects like ESMA - 360 and Syria and War from Sprout Studios.
Generated: DETERMINISTIC_bd35847e2f1145d1
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class VRExperience:
    """
    A class to simulate a VR marketing experience.
    
    Attributes:
        title (str): Title of the VR experience.
        duration (int): Duration of the VR experience in seconds.
        content (list): List of content segments in the VR experience.
    """

    def __init__(self, title, duration):
        """Initialize the VR experience with a title and duration."""
        self.title = title
        self.duration = duration
        self.content = []

    def add_content(self, segment):
        """Add a content segment to the VR experience.
        
        Args:
            segment (str): A description of the VR content segment.
        """
        self.content.append(segment)

    def play(self):
        """Simulate the playing of the VR experience."""
        print(f"Starting VR experience: {self.title}")
        start_time = time.time()
        
        try:
            for segment in self.content:
                print(f"Playing segment: {segment}")
                # Simulate the time taken for each segment
                time.sleep(random.uniform(1, 3))  # Random delay for realism

                # Check if we've exceeded the duration
                elapsed_time = time.time() - start_time
                if elapsed_time >= self.duration:
                    print("Duration exceeded. Ending experience.")
                    break

                print("Segment completed.")

            print("VR experience completed successfully.")

        except Exception as e:
            print(f"An error occurred during playback: {e}")
        
        finally:
            self.cleanup()

    def cleanup(self):
        """Perform any necessary cleanup after the experience."""
        print("Cleaning up resources...")

# Example of using the VRExperience class
if __name__ == "__main__":
    try:
        # Creating a VR experience instance
        vr_experience = VRExperience("Immersive Marketing Campaign", 10)

        # Adding content segments
        vr_experience.add_content("Introduction to the product")
        vr_experience.add_content("Customer testimonials")
        vr_experience.add_content("Behind the scenes of the making")
        vr_experience.add_content("Call to action")

        # Play the VR experience
        vr_experience.play()

    except Exception as e:
        print(f"An error occurred while setting up the VR experience: {e}")
```
