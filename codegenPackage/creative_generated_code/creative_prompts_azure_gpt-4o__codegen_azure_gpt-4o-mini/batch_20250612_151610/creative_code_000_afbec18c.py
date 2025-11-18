"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indusur.com
Prompt: Write Python code to calculate the horsepower range for Cummins diesel engines, specifically between 55 and 3,500 horsepower, as described on the Indusur website.
Generated: DETERMINISTIC_afbec18c315004da
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CumminsEngine:
    """
    A class to represent a Cummins diesel engine with horsepower specifications.
    """

    def __init__(self, min_hp: int = 55, max_hp: int = 3500):
        """
        Initializes the CumminsEngine with a minimum and maximum horsepower range.

        :param min_hp: Minimum horsepower (default is 55)
        :param max_hp: Maximum horsepower (default is 3500)
        """
        # Validate the horsepower range
        if min_hp < 0 or max_hp < 0:
            raise ValueError("Horsepower values must be non-negative.")
        if min_hp >= max_hp:
            raise ValueError("Minimum horsepower must be less than maximum horsepower.")

        self.min_hp = min_hp
        self.max_hp = max_hp

    def calculate_horsepower_range(self):
        """
        Calculates the horsepower range for Cummins diesel engines.

        :return: A tuple containing the minimum and maximum horsepower.
        """
        return self.min_hp, self.max_hp

    def display_horsepower_range(self):
        """
        Displays the minimum and maximum horsepower range in a formatted string.
        """
        min_hp, max_hp = self.calculate_horsepower_range()
        print(f"Cummins Diesel Engines Horsepower Range: {min_hp} - {max_hp} HP")


def main():
    """
    Main function to execute the horsepower range retrieval for Cummins diesel engines.
    """
    try:
        engine = CumminsEngine()
        engine.display_horsepower_range()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
