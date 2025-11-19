"""
Generated Code Metadata:
========================
Original URL: https://gsj-technology.com
Prompt: Write code to implement an advertising display system for a robot, similar to the KettyBot's functionality mentioned on the GSJ website.
Generated: DETERMINISTIC_5b6e30e95cf17815
Batch ID: 20250612_154401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict

class Advertisement:
    """Class representing an advertisement."""
    
    def __init__(self, content: str, duration: int):
        """
        Initialize an advertisement.

        :param content: The content of the advertisement.
        :param duration: Duration in seconds for which the advertisement will be displayed.
        """
        self.content = content
        self.duration = duration

class AdDisplaySystem:
    """Class to manage and display advertisements on a robot."""
    
    def __init__(self):
        """Initialize the advertisement display system with an empty ad list."""
        self.ads: List[Advertisement] = []

    def add_ad(self, ad: Advertisement):
        """
        Add an advertisement to the display system.

        :param ad: An instance of Advertisement to be added.
        """
        if not isinstance(ad, Advertisement):
            raise ValueError("Only instances of Advertisement can be added.")
        self.ads.append(ad)

    def remove_ad(self, ad: Advertisement):
        """
        Remove an advertisement from the display system.

        :param ad: An instance of Advertisement to be removed.
        """
        try:
            self.ads.remove(ad)
        except ValueError:
            print("Advertisement not found in the display system.")

    def display_ads(self):
        """Display all advertisements in a loop until interrupted."""
        if not self.ads:
            print("No advertisements to display.")
            return
        
        try:
            while True:
                ad = random.choice(self.ads)  # Randomly select an ad to display
                print(f"Displaying Ad: {ad.content}")
                time.sleep(ad.duration)  # Display the ad for its specified duration
        except KeyboardInterrupt:
            print("Ad display interrupted. Exiting...")

def main():
    """Main function to run the advertisement display system."""
    ad_system = AdDisplaySystem()

    # Sample advertisements
    ad1 = Advertisement("Buy One Get One Free!", 5)
    ad2 = Advertisement("50% Off on All Items!", 7)
    ad3 = Advertisement("Join our Loyalty Program!", 4)

    # Adding advertisements to the system
    ad_system.add_ad(ad1)
    ad_system.add_ad(ad2)
    ad_system.add_ad(ad3)

    # Start displaying advertisements
    ad_system.display_ads()

if __name__ == "__main__":
    main()
```
