"""
Generated Code Metadata:
========================
Original URL: https://nc82mx10.pages.dev
Prompt: Develop a program that calculates the remaining Notcoin to be distributed based on the provided statistics ($85 million distributed, $15 million left).
Generated: DETERMINISTIC_61790b2bd0f65389
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NotcoinStatistics:
    """
    Calculates the remaining Notcoin to be distributed based on the provided statistics.
    """

    def __init__(self, total_distributed: float, total_left: float):
        """
        Initializes the NotcoinStatistics class.

        Args:
        - total_distributed (float): The total amount of Notcoin distributed.
        - total_left (float): The total amount of Notcoin left to be distributed.

        Raises:
        - ValueError: If total_distributed or total_left is negative.
        """
        if total_distributed < 0 or total_left < 0:
            raise ValueError("Distributed and left amounts cannot be negative.")

        self.total_distributed = total_distributed
        self.total_left = total_left

    def calculate_remaining(self) -> float:
        """
        Calculates the remaining Notcoin to be distributed.

        Returns:
        - float: The remaining Notcoin to be distributed.
        """
        return self.total_left

    def calculate_distribution_progress(self) -> float:
        """
        Calculates the progress of Notcoin distribution.

        Returns:
        - float: The progress of Notcoin distribution as a percentage.
        """
        if self.total_left + self.total_distributed == 0:
            return 0.0

        return (self.total_distributed / (self.total_left + self.total_distributed)) * 100


def main():
    try:
        # Provided statistics
        distributed = 85_000_000  # $85 million distributed
        left = 15_000_000  # $15 million left

        notcoin_stats = NotcoinStatistics(distributed, left)

        print(f"Remaining Notcoin to be distributed: ${notcoin_stats.calculate_remaining():,.2f}")
        print(f"Notcoin distribution progress: {notcoin_stats.calculate_distribution_progress():,.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
