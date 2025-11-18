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
# Import necessary modules for VR simulation
import os
import sys
import time
import pygame
import cv2
from pygame.locals import QUIT

# VR simulation class to handle the experience
class VRExperience:
    """
    A class to simulate VR experience for marketing ads.
    """
    def __init__(self, video_path, window_title="VR Experience"):
        """
        Initializes the VR Experience.
        
        Args:
            video_path (str): Path to the 360-degree video file.
            window_title (str): Title of the VR simulation window.
        """
        self.video_path = video_path
        self.window_title = window_title
        
        # Initialize Pygame
        pygame.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((800, 600))  # Default resolution
        pygame.display.set_caption(self.window_title)
        
        # Load the video using OpenCV
        self.video = cv2.VideoCapture(video_path)

        if not self.video.isOpened():
            raise FileNotFoundError(f"Unable to load video from {video_path}. Please ensure the file exists.")

    def run_experience(self):
        """
        Runs the VR simulation experience.
        """
        try:
            # Main loop for the VR experience
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.cleanup()  # Handle window close gracefully
                        return
                    
                # Read video frame
                ret, frame = self.video.read()
                if not ret:
                    print("End of video reached. Exiting VR experience.")
                    break

                # Convert OpenCV frame to Pygame image
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
                frame = cv2.resize(frame, (800, 600))  # Resize to match Pygame screen
                frame_surface = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "RGB")

                # Display the frame on the screen
                self.screen.blit(frame_surface, (0, 0))
                pygame.display.update()
                
                # Control the frame rate for smoother experience
                time.sleep(0.033)  # Approx. 30 FPS

        except Exception as e:
            print(f"An error occurred during the simulation: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        """
        Cleans up resources properly.
        """
        # Release video and quit Pygame
        if self.video.isOpened():
            self.video.release()
        pygame.quit()
        print("VR experience terminated gracefully.")

# Entry point for the script
if __name__ == "__main__":
    # Specify the path to the 360-degree video file
    video_file_path = "path_to_your_360_video.mp4"  # Replace with your video file path

    # Ensure the video path is valid
    if not os.path.exists(video_file_path):
        print(f"Error: The video file '{video_file_path}' does not exist.")
        sys.exit(1)
    
    # Create and run the VR experience
    vr = VRExperience(video_file_path, "VR Marketing Ads Simulation")
    vr.run_experience()
```
