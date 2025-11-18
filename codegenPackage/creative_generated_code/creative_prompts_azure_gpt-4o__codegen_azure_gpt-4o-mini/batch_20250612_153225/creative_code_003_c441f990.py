"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Create a Python script to manage a queue of special effects for a live DJ event, inspired by the stage effects offered by Agnelo SFX for celebrity shows.
Generated: DETERMINISTIC_c441f9906e9f800c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import queue
import time
import threading
import random

class SpecialEffect:
    """Class representing a special effect with a name and duration."""

    def __init__(self, name: str, duration: float):
        """
        Initializes a SpecialEffect instance.

        Args:
            name (str): The name of the special effect.
            duration (float): The duration for which the effect will be active in seconds.
        """
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"SpecialEffect(name={self.name}, duration={self.duration})"


class EffectQueueManager:
    """Class to manage a queue of special effects for a live DJ event."""

    def __init__(self):
        """Initializes the effect queue and the event threading lock."""
        self.effect_queue = queue.Queue()
        self.lock = threading.Lock()
        self.is_running = True

    def add_effect(self, effect: SpecialEffect):
        """
        Adds a special effect to the queue.

        Args:
            effect (SpecialEffect): The special effect to be added to the queue.
        """
        with self.lock:
            self.effect_queue.put(effect)
            print(f"Added effect to queue: {effect}")

    def process_effects(self):
        """Processes effects from the queue until the manager is stopped."""
        while self.is_running:
            try:
                # Get the next effect from the queue with a timeout
                effect = self.effect_queue.get(timeout=1)
                print(f"Processing effect: {effect}")
                
                # Simulate the effect being active
                time.sleep(effect.duration)
                print(f"Finished processing effect: {effect}")
                
                self.effect_queue.task_done()
            except queue.Empty:
                continue

    def stop(self):
        """Stops the effect queue manager."""
        self.is_running = False
        print("Effect queue manager stopped.")


def main():
    """Main function to run the special effects manager."""
    # Create an EffectQueueManager instance
    manager = EffectQueueManager()

    # Start the processing thread
    processing_thread = threading.Thread(target=manager.process_effects)
    processing_thread.start()

    # Example effects to add to the queue
    effects = [
        SpecialEffect("Smoke", 2.0),
        SpecialEffect("Laser Show", 3.0),
        SpecialEffect("Confetti", 1.5),
        SpecialEffect("Strobe Lights", 4.0),
    ]

    # Randomly add effects to the queue
    for _ in range(10):  # Simulate adding multiple effects
        effect = random.choice(effects)
        manager.add_effect(effect)
        time.sleep(random.uniform(0.5, 1.5))  # Wait before adding the next effect

    # Allow some time for effects to be processed
    time.sleep(10)

    # Stop the manager and wait for the processing thread to finish
    manager.stop()
    processing_thread.join()

if __name__ == "__main__":
    main()
```
