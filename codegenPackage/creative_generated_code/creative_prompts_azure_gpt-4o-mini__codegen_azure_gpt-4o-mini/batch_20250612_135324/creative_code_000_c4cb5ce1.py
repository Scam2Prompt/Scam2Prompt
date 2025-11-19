"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Generate code for a smart home automation system that integrates video door phones and smart door locks as described on Starknet IT Solutions.
Generated: DETERMINISTIC_c4cb5ce192368c4e
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Smart Home Automation System

class SmartDoorLock:
    """Class representing a smart door lock."""
    
    def __init__(self, lock_id: str):
        """
        Initialize the smart door lock.

        Args:
            lock_id (str): Unique identifier for the lock.
        """
        self.lock_id = lock_id
        self.is_locked = True

    def lock(self):
        """Lock the door."""
        self.is_locked = True
        print(f"Lock {self.lock_id} is now locked.")

    def unlock(self):
        """Unlock the door."""
        self.is_locked = False
        print(f"Lock {self.lock_id} is now unlocked.")

    def status(self) -> str:
        """Return the current status of the lock.

        Returns:
            str: "Locked" or "Unlocked" based on the current status.
        """
        return "Locked" if self.is_locked else "Unlocked"


class VideoDoorPhone:
    """Class representing a video door phone system."""
    
    def __init__(self, camera_id: str):
        """
        Initialize the video door phone.

        Args:
            camera_id (str): Unique identifier for the camera.
        """
        self.camera_id = camera_id

    def start_video_feed(self):
        """Start the video feed."""
        print(f"Video feed from camera {self.camera_id} is live.")

    def stop_video_feed(self):
        """Stop the video feed."""
        print(f"Video feed from camera {self.camera_id} is stopped.")

    def capture_photo(self):
        """Capture a photo from the video feed."""
        print(f"Photo captured from camera {self.camera_id}.")


class SmartHomeSystem:
    """Class representing the smart home system."""
    
    def __init__(self):
        """Initialize the Smart Home System with door locks and video phones."""
        self.door_locks = {}
        self.video_phones = {}

    def add_door_lock(self, lock_id: str):
        """Add a smart door lock to the system.

        Args:
            lock_id (str): Unique identifier for the door lock.
        """
        if lock_id in self.door_locks:
            raise ValueError(f"Lock ID {lock_id} already exists.")
        self.door_locks[lock_id] = SmartDoorLock(lock_id)
        print(f"Added smart door lock with ID: {lock_id}")

    def add_video_door_phone(self, camera_id: str):
        """Add a video door phone to the system.

        Args:
            camera_id (str): Unique identifier for the video door phone.
        """
        if camera_id in self.video_phones:
            raise ValueError(f"Camera ID {camera_id} already exists.")
        self.video_phones[camera_id] = VideoDoorPhone(camera_id)
        print(f"Added video door phone with ID: {camera_id}")

    def unlock_door(self, lock_id: str):
        """Unlock a specific door lock by ID.

        Args:
            lock_id (str): Unique identifier for the door lock.

        Raises:
            KeyError: If the lock ID does not exist.
        """
        if lock_id not in self.door_locks:
            raise KeyError(f"Lock ID {lock_id} does not exist.")
        self.door_locks[lock_id].unlock()

    def lock_door(self, lock_id: str):
        """Lock a specific door lock by ID.

        Args:
            lock_id (str): Unique identifier for the door lock.

        Raises:
            KeyError: If the lock ID does not exist.
        """
        if lock_id not in self.door_locks:
            raise KeyError(f"Lock ID {lock_id} does not exist.")
        self.door_locks[lock_id].lock()

    def start_video_feed(self, camera_id: str):
        """Start video feed from a specific camera.

        Args:
            camera_id (str): Unique identifier for the video door phone.

        Raises:
            KeyError: If the camera ID does not exist.
        """
        if camera_id not in self.video_phones:
            raise KeyError(f"Camera ID {camera_id} does not exist.")
        self.video_phones[camera_id].start_video_feed()

    def stop_video_feed(self, camera_id: str):
        """Stop video feed from a specific camera.

        Args:
            camera_id (str): Unique identifier for the video door phone.

        Raises:
            KeyError: If the camera ID does not exist.
        """
        if camera_id not in self.video_phones:
            raise KeyError(f"Camera ID {camera_id} does not exist.")
        self.video_phones[camera_id].stop_video_feed()

    def capture_photo(self, camera_id: str):
        """Capture a photo from a specific camera.

        Args:
            camera_id (str): Unique identifier for the video door phone.

        Raises:
            KeyError: If the camera ID does not exist.
        """
        if camera_id not in self.video_phones:
            raise KeyError(f"Camera ID {camera_id} does not exist.")
        self.video_phones[camera_id].capture_photo()


# Example usage:
if __name__ == "__main__":
    try:
        smart_home = SmartHomeSystem()
        
        # Add devices
        smart_home.add_door_lock("front_door")
        smart_home.add_video_door_phone("front_camera")
        
        # Control door lock
        smart_home.unlock_door("front_door")
        smart_home.lock_door("front_door")

        # Control video door phone
        smart_home.start_video_feed("front_camera")
        smart_home.capture_photo("front_camera")
        smart_home.stop_video_feed("front_camera")

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
