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
import random
from typing import List, Dict

class Advertisement:
    """Class representing an advertisement with a message and a display duration."""

    def __init__(self, message: str, duration: int):
        """
        Initializes an Advertisement instance.

        Args:
            message (str): The advertisement message to display.
            duration (int): The duration in seconds to display the advertisement.
        """
        self.message = message
        self.duration = duration

    def display(self):
        """Simulates displaying the advertisement."""
        print(f"Displaying advertisement: {self.message}")
        time.sleep(self.duration)
        print(f"Finished displaying advertisement: {self.message}")


class AdDisplaySystem:
    """Class to manage advertisements and control their display on the robot."""

    def __init__(self, ads: List[Advertisement]):
        """
        Initializes the AdDisplaySystem with a list of advertisements.

        Args:
            ads (List[Advertisement]): A list of Advertisement instances.
        """
        self.ads = ads

    def display_random_ad(self):
        """Displays a random advertisement from the list."""
        if not self.ads:
            print("No advertisements available to display.")
            return
        ad = random.choice(self.ads)
        ad.display()

    def run_advertising_cycle(self, cycles: int, interval: int):
        """
        Runs the advertising display cycle for a specified number of cycles.

        Args:
            cycles (int): The number of times to display an advertisement.
            interval (int): The interval in seconds between displaying ads.
        """
        for i in range(cycles):
            try:
                print(f"Cycle {i + 1}/{cycles}")
                self.display_random_ad()
                time.sleep(interval)
            except Exception as e:
                print(f"Error during advertisement display: {e}")


# Example usage
if __name__ == "__main__":
    # Define sample advertisements
    ads_data: List[Dict[str, any]] = [
        {"message": "Buy one, get one free!", "duration": 3},
        {"message": "50% off all items today!", "duration": 5},
        {"message": "Join our loyalty program!", "duration": 4},
    ]

    # Create Advertisement instances
    ads = [Advertisement(ad["message"], ad["duration"]) for ad in ads_data]

    # Create the advertising display system
    ad_system = AdDisplaySystem(ads)

    # Run the advertising cycle
    try:
        ad_system.run_advertising_cycle(cycles=5, interval=2)
    except KeyboardInterrupt:
        print("Advertising cycle interrupted by user.")
```
