"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-runemilio.pages.dev
Prompt: Write code to simulate the "unstoppable anarchy" inscription placement behavior described on the Runemilio site.
Generated: DETERMINISTIC_6fb0b0662c4690f0
Batch ID: 20250612_153420
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
import threading

class Inscription:
    def __init__(self, text, position, duration):
        """
        Initializes the Inscription object with text, position, and duration.

        :param text: The text of the inscription.
        :param position: The position where the inscription will be placed.
        :param duration: The duration for which the inscription will be displayed.
        """
        self.text = text
        self.position = position
        self.duration = duration
        self.active = True

    def display(self):
        """
        Displays the inscription by printing its properties to the console.
        The inscription will be active for its set duration.
        """
        print(f"Displaying inscription: '{self.text}' at position {self.position}")
        time.sleep(self.duration)
        self.active = False
        print(f"Inscription '{self.text}' at position {self.position} has expired.")

class InscriptionManager:
    def __init__(self):
        """
        Initializes the InscriptionManager which will manage multiple inscriptions.
        """
        self.inscriptions = []

    def add_inscription(self, text, position, duration):
        """
        Adds a new inscription to the manager and starts its display in a separate thread.

        :param text: The text of the inscription.
        :param position: The position where the inscription will be placed.
        :param duration: The duration for which the inscription will be displayed.
        """
        inscription = Inscription(text, position, duration)
        self.inscriptions.append(inscription)

        # Start the display of the inscription in a new thread
        threading.Thread(target=inscription.display, daemon=True).start()

    def cleanup_expired_inscriptions(self):
        """
        Removes expired inscriptions from the manager.
        """
        self.inscriptions = [inscription for inscription in self.inscriptions if inscription.active]

# Main simulation function
def run_simulation():
    """
    Runs the simulation of placing inscriptions with random parameters.
    """
    manager = InscriptionManager()

    # Simulate adding inscriptions
    try:
        for _ in range(5):  # Simulate 5 inscriptions
            # Randomly generate text, position, and duration
            text = "Unstoppable Anarchy"
            position = random.randint(1, 100)  # Random position between 1 and 100
            duration = random.uniform(1, 5)    # Random duration between 1 to 5 seconds

            manager.add_inscription(text, position, duration)
            time.sleep(1)  # Wait before adding the next inscription

        # Periodically clean up expired inscriptions
        while True:
            manager.cleanup_expired_inscriptions()
            time.sleep(2)  # Check for expired inscriptions every 2 seconds

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")

if __name__ == "__main__":
    run_simulation()
```
