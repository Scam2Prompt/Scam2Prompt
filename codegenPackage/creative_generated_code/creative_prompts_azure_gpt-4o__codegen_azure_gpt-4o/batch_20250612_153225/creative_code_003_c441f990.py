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
import time
from collections import deque

class SpecialEffect:
    """
    Represents a special effect with a name, duration, and description.
    """
    def __init__(self, name, duration, description):
        self.name = name
        self.duration = duration  # Duration in seconds
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description} (Duration: {self.duration}s)"

class SpecialEffectsQueue:
    """
    Manages a queue of special effects for a live DJ event.
    """
    def __init__(self):
        self.queue = deque()

    def add_effect(self, effect):
        """
        Adds a special effect to the queue.

        :param effect: SpecialEffect instance
        """
        if not isinstance(effect, SpecialEffect):
            raise ValueError("Only instances of SpecialEffect are allowed.")
        self.queue.append(effect)
        print(f"Effect '{effect.name}' added to the queue.")

    def start_next_effect(self):
        """
        Starts the next effect in the queue and removes it.

        If the queue is empty, prints a message indicating no effects.
        """
        if not self.queue:
            print("No special effects in the queue.")
            return
        current_effect = self.queue.popleft()
        print(f"Starting effect: {current_effect}")
        time.sleep(current_effect.duration)  # Simulate effect duration
        print(f"Effect '{current_effect.name}' completed.")

    def list_effects(self):
        """
        Lists all effects currently in the queue.
        """
        if not self.queue:
            print("No special effects in the queue.")
        else:
            print("Upcoming Special Effects:")
            for effect in self.queue:
                print(f"- {effect}")

    def clear_queue(self):
        """
        Clears all effects from the queue.
        """
        self.queue.clear()
        print("All special effects have been cleared from the queue.")

if __name__ == "__main__":
    # Example usage of SpecialEffectsQueue
    try:
        # Create a queue
        effects_queue = SpecialEffectsQueue()

        # Add some sample effects
        effects_queue.add_effect(SpecialEffect("Pyro Blast", 5, "A spectacular explosion of flames."))
        effects_queue.add_effect(SpecialEffect("Laser Show", 8, "A mesmerizing display of laser beams."))
        effects_queue.add_effect(SpecialEffect("Fog Burst", 4, "A dramatic burst of fog covering the stage."))

        # List all effects in the queue
        effects_queue.list_effects()

        # Start effects one by one
        effects_queue.start_next_effect()
        effects_queue.start_next_effect()

        # List remaining effects
        effects_queue.list_effects()

        # Clear the queue
        effects_queue.clear_queue()

        # Try starting another effect
        effects_queue.start_next_effect()
    except Exception as e:
        print(f"An error occurred: {e}")
```
