"""
Generated Code Metadata:
========================
Original URL: https://indusur.com
Prompt: Write Python code to calculate the horsepower range for Cummins diesel engines, specifically between 55 and 3,500 horsepower, as described on the Indusur website.
Generated: DETERMINISTIC_afbec18c315004da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CumminsEngine:
    """
    A class to represent a Cummins diesel engine and calculate its horsepower range.
    """

    def __init__(self, min_hp=55, max_hp=3500):
        """
        Initializes the CumminsEngine with a specified horsepower range.

        :param min_hp: Minimum horsepower (default is 55)
        :param max_hp: Maximum horsepower (default is 3500)
        """
        if min_hp < 0 or max_hp < 0:
            raise ValueError("Horsepower values must be non-negative.")
        if min_hp >= max_hp:
            raise ValueError("Minimum horsepower must be less than maximum horsepower.")

        self.min_hp = min_hp
        self.max_hp = max_hp

    def get_horsepower_range(self):
        """
        Returns the horsepower range as a tuple.

        :return: A tuple containing the minimum and maximum horsepower
        """
        return self.min_hp, self.max_hp

    def is_within_range(self, horsepower):
        """
        Checks if a given horsepower value is within the engine's range.

        :param horsepower: The horsepower value to check
        :return: True if within range, False otherwise
        """
        if horsepower < 0:
            raise ValueError("Horsepower must be a non-negative value.")
        return self.min_hp <= horsepower <= self.max_hp


def main():
    """
    Main function to demonstrate the CumminsEngine class functionality.
    """
    try:
        # Create an instance of CumminsEngine
        cummins_engine = CumminsEngine()

        # Get the horsepower range
        hp_range = cummins_engine.get_horsepower_range()
        print(f"Cummins diesel engine horsepower range: {hp_range[0]} - {hp_range[1]} HP")

        # Check specific horsepower values
        test_hp_values = [50, 100, 2000, 4000]
        for hp in test_hp_values:
            if cummins_engine.is_within_range(hp):
                print(f"{hp} HP is within the range.")
            else:
                print(f"{hp} HP is out of the range.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
