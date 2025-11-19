"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: Create a Python script to manage a queue of special effects for a live DJ event, inspired by the stage effects offered by Agnelo SFX for celebrity shows.
Generated: DETERMINISTIC_c441f9906e9f800c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
from enum import Enum
from typing import List

class EffectType(Enum):
    """ Enum for different types of special effects """
    LASER = 1
    PYRO = 2
    SMOKE = 3
    STROBE = 4

class SpecialEffect:
    """ Represents a special effect with its type and duration """
    def __init__(self, effect_type: EffectType, duration: int):
        """
        Initializes a SpecialEffect object.

        Args:
        effect_type (EffectType): The type of special effect.
        duration (int): The duration of the special effect in seconds.
        """
        self.effect_type = effect_type
        self.duration = duration

class EffectQueue:
    """ Manages a queue of special effects """
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()

    def add_effect(self, effect: SpecialEffect):
        """
        Adds a special effect to the queue.

        Args:
        effect (SpecialEffect): The special effect to add.
        """
        with self.lock:
            self.queue.append(effect)

    def remove_effect(self) -> SpecialEffect:
        """
        Removes and returns the next special effect from the queue.

        Returns:
        SpecialEffect: The next special effect in the queue.

        Raises:
        IndexError: If the queue is empty.
        """
        with self.lock:
            if not self.queue:
                raise IndexError("Queue is empty")
            return self.queue.pop(0)

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        with self.lock:
            return len(self.queue) == 0

class EffectPlayer:
    """ Plays special effects from a queue """
    def __init__(self, effect_queue: EffectQueue):
        self.effect_queue = effect_queue
        self.running = False

    def start(self):
        """ Starts playing special effects from the queue """
        self.running = True
        threading.Thread(target=self.play_effects).start()

    def stop(self):
        """ Stops playing special effects """
        self.running = False

    def play_effects(self):
        while self.running:
            if not self.effect_queue.is_empty():
                effect = self.effect_queue.remove_effect()
                print(f"Playing effect: {effect.effect_type.name} for {effect.duration} seconds")
                time.sleep(effect.duration)
            else:
                time.sleep(0.1)

def main():
    effect_queue = EffectQueue()

    # Add some special effects to the queue
    effect_queue.add_effect(SpecialEffect(EffectType.LASER, 5))
    effect_queue.add_effect(SpecialEffect(EffectType.PYRO, 3))
    effect_queue.add_effect(SpecialEffect(EffectType.SMOKE, 10))

    effect_player = EffectPlayer(effect_queue)
    effect_player.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        effect_player.stop()

if __name__ == "__main__":
    main()
```
