"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Generate a Python script that simulates the effects of Zento's hair care products, such as the anti-yellowing purple shampoo and the intensive care set.
Generated: DETERMINISTIC_4a199b6e1601cb2c
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Hair:
    def __init__(self, color, condition):
        """
        Initialize a Hair object.

        Args:
            color (str): The initial color of the hair.
            condition (str): The initial condition of the hair.
        """
        self.color = color
        self.condition = condition

    def __str__(self):
        return f"Hair Color: {self.color}, Condition: {self.condition}"


class PurpleShampoo:
    def __init__(self):
        pass

    def apply(self, hair):
        """
        Apply the purple shampoo to the hair.

        Args:
            hair (Hair): The hair object to apply the shampoo to.

        Returns:
            Hair: The updated hair object.
        """
        # 80% chance to reduce yellowing
        if random.random() < 0.8:
            if hair.color == "Blonde":
                hair.color = "Ash Blonde"
                print("Purple shampoo applied. Hair color changed to Ash Blonde.")
            else:
                print("Purple shampoo applied. No color change.")
        else:
            print("Purple shampoo application failed.")
        return hair


class IntensiveCareSet:
    def __init__(self):
        pass

    def apply(self, hair):
        """
        Apply the intensive care set to the hair.

        Args:
            hair (Hair): The hair object to apply the care set to.

        Returns:
            Hair: The updated hair object.
        """
        # 90% chance to improve hair condition
        if random.random() < 0.9:
            if hair.condition == "Damaged":
                hair.condition = "Healthy"
                print("Intensive care set applied. Hair condition improved to Healthy.")
            elif hair.condition == "Dry":
                hair.condition = "Moisturized"
                print("Intensive care set applied. Hair condition improved to Moisturized.")
            else:
                print("Intensive care set applied. No condition change.")
        else:
            print("Intensive care set application failed.")
        return hair


def main():
    try:
        hair = Hair("Blonde", "Damaged")
        print("Initial Hair State:")
        print(hair)

        purple_shampoo = PurpleShampoo()
        hair = purple_shampoo.apply(hair)
        print("\nAfter Purple Shampoo:")
        print(hair)

        intensive_care_set = IntensiveCareSet()
        hair = intensive_care_set.apply(hair)
        print("\nAfter Intensive Care Set:")
        print(hair)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
