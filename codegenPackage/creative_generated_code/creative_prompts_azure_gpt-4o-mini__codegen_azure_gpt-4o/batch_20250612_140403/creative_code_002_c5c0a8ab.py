"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://red.game
Prompt: Write a Python script that simulates a surveillance system, drawing on the concepts of observation and interaction mentioned on the RED website.
Generated: DETERMINISTIC_c5c0a8abb91df01e
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import datetime
import os

# Define the SurveillanceSystem class
class SurveillanceSystem:
    """
    A class to simulate a surveillance system using video capture and interaction.

    Attributes:
        camera_index (int): The index of the camera to use for video capture.
        output_dir (str): The directory to save surveillance snapshots and logs.
    """
    def __init__(self, camera_index=0, output_dir="surveillance_data"):
        """
        Initializes the surveillance system.

        Args:
            camera_index (int): The index of the camera to use for video capture (default: 0).
            output_dir (str): The directory to save surveillance snapshots and logs (default: "surveillance_data").
        """
        self.camera_index = camera_index
        self.output_dir = output_dir
        self.capture = None

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def start_camera(self):
        """
        Starts the camera for video capture.
        """
        self.capture = cv2.VideoCapture(self.camera_index)
        if not self.capture.isOpened():
            raise Exception("Failed to open the camera.")

    def stop_camera(self):
        """
        Stops the camera and releases resources.
        """
        if self.capture:
            self.capture.release()
            self.capture = None

    def capture_snapshot(self):
        """
        Captures a frame from the camera and saves it as a snapshot.

        Returns:
            str: The file path of the saved snapshot.
        """
        if not self.capture:
            raise Exception("Camera is not running.")

        ret, frame = self.capture.read()
        if not ret:
            raise Exception("Failed to capture a frame from the camera.")

        # Generate a timestamp for the snapshot
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_path = os.path.join(self.output_dir, f"snapshot_{timestamp}.png")

        # Save the frame as a snapshot
        cv2.imwrite(snapshot_path, frame)

        # Log the snapshot capture
        self.log_event(f"Snapshot captured: {snapshot_path}")

        return snapshot_path

    def log_event(self, event_details):
        """
        Logs an event with a timestamp.

        Args:
            event_details (str): Details of the event to log.
        """
        log_path = os.path.join(self.output_dir, "surveillance_log.txt")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append the event details to the log file
        with open(log_path, "a") as log_file:
            log_file.write(f"[{timestamp}] {event_details}\n")

    def run(self):
        """
        Runs the surveillance system and enables interaction.

        Simulates the concept of observation and interaction by periodically capturing snapshots.
        """
        try:
            self.start_camera()
            print("Surveillance system is running. Press 'q' to quit.")

            while True:
                # Capture snapshots when the user presses 'c'
                key = cv2.waitKey(1) & 0xFF
                if key == ord('c'):
                    snapshot_path = self.capture_snapshot()
                    print(f"Snapshot saved: {snapshot_path}")

                # Exit the surveillance system when the user presses 'q'
                elif key == ord('q'):
                    print("Exiting surveillance system...")
                    break

        except Exception as e:
            print(f"Error: {e}")
            self.log_event(f"Error: {e}")

        finally:
            self.stop_camera()
            cv2.destroyAllWindows()
            print("Surveillance system stopped.")

# Main entry point for the script
if __name__ == "__main__":
    # Create an instance of the surveillance system and run it
    surveillance = SurveillanceSystem()
    surveillance.run()
```
