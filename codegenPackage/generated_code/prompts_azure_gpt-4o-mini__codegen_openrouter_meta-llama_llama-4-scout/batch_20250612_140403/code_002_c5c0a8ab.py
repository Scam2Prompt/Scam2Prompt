"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: Write a Python script that simulates a surveillance system, drawing on the concepts of observation and interaction mentioned on the RED website.
Generated: DETERMINISTIC_c5c0a8abb91df01e
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# surveillance_system.py

from abc import ABC, abstractmethod
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Observer(ABC):
    """Abstract base class for observers."""
    
    @abstractmethod
    def update(self, message):
        """Update the observer with a message."""
        pass

class Camera:
    """Simulates a camera in the surveillance system."""
    
    def __init__(self, name):
        self.name = name
        self.observers = []

    def attach(self, observer):
        """Attach an observer to the camera."""
        self.observers.append(observer)

    def detach(self, observer):
        """Detach an observer from the camera."""
        self.observers.remove(observer)

    def notify(self, message):
        """Notify all observers of a message."""
        for observer in self.observers:
            observer.update(message)

    def capture_image(self):
        """Simulate capturing an image and notify observers."""
        image_data = f"Image captured by {self.name} at {datetime.now()}"
        self.notify(image_data)

class Monitor(Observer):
    """Simulates a monitor in the surveillance system."""
    
    def __init__(self, name):
        self.name = name

    def update(self, message):
        """Update the monitor with a message."""
        logging.info(f"{self.name} received: {message}")

class AlertSystem(Observer):
    """Simulates an alert system in the surveillance system."""
    
    def __init__(self, name):
        self.name = name

    def update(self, message):
        """Update the alert system with a message."""
        logging.warning(f"{self.name} alert: {message}")

def main():
    try:
        # Create camera
        camera = Camera("Camera 1")

        # Create monitor and alert system
        monitor = Monitor("Monitor 1")
        alert_system = AlertSystem("Alert System")

        # Attach observers to camera
        camera.attach(monitor)
        camera.attach(alert_system)

        # Simulate capturing images
        camera.capture_image()

        # Detach observer
        camera.detach(monitor)

        # Simulate capturing another image
        camera.capture_image()

    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
