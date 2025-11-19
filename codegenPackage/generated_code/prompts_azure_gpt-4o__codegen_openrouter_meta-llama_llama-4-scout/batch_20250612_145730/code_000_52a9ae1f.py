"""
Generated Code Metadata:
========================
Original URL: https://pansos4dmax.site
Prompt: Write a Python script to simulate a lottery result generator based on the format used by PANSOS4D, including results for locations like Wuhan, Sydney, and Singapore.
Generated: DETERMINISTIC_52a9ae1f12b0d42a
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class LotteryResult:
    def __init__(self, location, numbers=None):
        """
        Initialize a LotteryResult object.

        Args:
            location (str): The location of the lottery result (e.g., Wuhan, Sydney, Singapore).
            numbers (list, optional): A list of 4 numbers representing the lottery result. Defaults to None.
        """
        self.location = location
        self.numbers = numbers if numbers else self.generate_numbers()

    def generate_numbers(self):
        """
        Generate a list of 4 random numbers between 0 and 9.

        Returns:
            list: A list of 4 random numbers.
        """
        return [random.randint(0, 9) for _ in range(4)]

    def __str__(self):
        """
        Return a string representation of the LotteryResult object.

        Returns:
            str: A string in the format "Location: XXXX".
        """
        return f"{self.location}: {''.join(map(str, self.numbers))}"


class LotteryResultGenerator:
    def __init__(self):
        """
        Initialize a LotteryResultGenerator object.
        """
        self.locations = ["Wuhan", "Sydney", "Singapore"]

    def generate_results(self):
        """
        Generate lottery results for all locations.

        Returns:
            dict: A dictionary with locations as keys and LotteryResult objects as values.
        """
        return {location: LotteryResult(location) for location in self.locations}

    def print_results(self, results):
        """
        Print the lottery results.

        Args:
            results (dict): A dictionary with locations as keys and LotteryResult objects as values.
        """
        for result in results.values():
            print(result)


def main():
    try:
        generator = LotteryResultGenerator()
        results = generator.generate_results()
        generator.print_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
