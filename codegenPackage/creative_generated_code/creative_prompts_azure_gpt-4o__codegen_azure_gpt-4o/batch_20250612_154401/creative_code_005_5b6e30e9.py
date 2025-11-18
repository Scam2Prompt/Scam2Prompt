"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gsj-technology.com
Prompt: Write code to implement an advertising display system for a robot, similar to the KettyBot's functionality mentioned on the GSJ website.
Generated: DETERMINISTIC_5b6e30e95cf17815
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from typing import List

class Advertisement:
    """
    Class representing an advertisement.
    """
    def __init__(self, title: str, content: str, duration: int):
        """
        Initializes the advertisement.

        Args:
            title (str): The title of the advertisement.
            content (str): The content or body of the advertisement.
            duration (int): Duration (in seconds) the ad should be displayed.
        """
        if duration <= 0:
            raise ValueError("Duration must be greater than 0 seconds.")
        
        self.title = title
        self.content = content
        self.duration = duration

    def display(self):
        """
        Simulates displaying the advertisement.
        """
        print(f"Displaying Advertisement: {self.title}")
        print(self.content)
        time.sleep(self.duration)  # Display for the specified duration
        print("Advertisement display complete.\n")


class AdvertisingSystem:
    """
    Class managing the advertising display system for the robot.
    """
    def __init__(self):
        """
        Initializes the advertising system with an empty list of advertisements.
        """
        self.advertisements = []
        self.is_running = False
        self.lock = threading.Lock()  # Ensures thread safety

    def add_advertisement(self, ad: Advertisement):
        """
        Adds an advertisement to the system.

        Args:
            ad (Advertisement): An instance of the Advertisement class.
        """
        with self.lock:
            self.advertisements.append(ad)
            print(f"Advertisement '{ad.title}' added to the system.")

    def remove_advertisement(self, title: str):
        """
        Removes an advertisement by its title.

        Args:
            title (str): The title of the advertisement to remove.
        """
        with self.lock:
            for i, ad in enumerate(self.advertisements):
                if ad.title == title:
                    self.advertisements.pop(i)
                    print(f"Advertisement '{title}' removed from the system.")
                    return
            print(f"Advertisement '{title}' not found.")

    def list_advertisements(self) -> List[str]:
        """
        Lists all advertisements currently in the system.

        Returns:
            List[str]: A list of advertisement titles.
        """
        with self.lock:
            return [ad.title for ad in self.advertisements]

    def start_display(self):
        """
        Starts the advertisement display loop in a separate thread.
        """
        if self.is_running:
            print("Advertising system is already running.")
            return

        self.is_running = True
        threading.Thread(target=self._display_loop, daemon=True).start()
        print("Advertising display system started.")

    def stop_display(self):
        """
        Stops the advertisement display loop.
        """
        self.is_running = False
        print("Advertising display system stopped.")

    def _display_loop(self):
        """
        Private method to continuously display advertisements.
        """
        while self.is_running:
            with self.lock:
                if not self.advertisements:
                    print("No advertisements to display. Waiting...")
                    time.sleep(5)  # Wait before checking for new ads
                    continue

                for ad in self.advertisements:
                    if not self.is_running:
                        break  # Exit if the system is stopped
                    try:
                        ad.display()
                    except Exception as e:
                        print(f"Error displaying advertisement '{ad.title}': {e}")

        print("Exiting display loop...")


# Example Usage
if __name__ == "__main__":
    # Create instances of advertisements
    ad1 = Advertisement("Welcome Ad", "Welcome to our store!", 5)
    ad2 = Advertisement("Discount Ad", "Get a 50% discount on all items!", 3)
    ad3 = Advertisement("Closing Ad", "Thank you for visiting us!", 4)

    # Initialize the advertising system
    system = AdvertisingSystem()

    # Add advertisements to the system
    system.add_advertisement(ad1)
    system.add_advertisement(ad2)
    system.add_advertisement(ad3)

    # List available advertisements
    print("Available advertisements:", system.list_advertisements())

    # Start the display loop
    system.start_display()

    # Simulate the system running for some time
    time.sleep(20)

    # Stop the display loop and exit
    system.stop_display()
```
