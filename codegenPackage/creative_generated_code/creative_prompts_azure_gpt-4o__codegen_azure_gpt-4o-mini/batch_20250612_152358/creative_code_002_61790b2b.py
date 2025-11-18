"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc82mx10.pages.dev
Prompt: Develop a program that calculates the remaining Notcoin to be distributed based on the provided statistics ($85 million distributed, $15 million left).
Generated: DETERMINISTIC_61790b2bd0f65389
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NotcoinDistributor:
    """
    A class to calculate remaining Notcoin to be distributed.
    """

    def __init__(self, total_distributed: float, total_left: float):
        """
        Initialize the NotcoinDistributor with distributed and remaining amounts.
        
        :param total_distributed: The amount of Notcoin that has already been distributed.
        :param total_left: The amount of Notcoin that is still available for distribution.
        """
        self.total_distributed = total_distributed
        self.total_left = total_left

    def calculate_remaining(self) -> float:
        """
        Calculate the total amount of Notcoin that can still be distributed.

        :return: The total remaining Notcoin.
        """
        return self.total_left

    def display_remaining(self):
        """
        Display the remaining Notcoin in a formatted manner.
        """
        try:
            remaining_notcoin = self.calculate_remaining()
            print(f"Remaining Notcoin to be distributed: ${remaining_notcoin:,.2f}")
        except Exception as e:
            print(f"An error occurred while calculating remaining Notcoin: {e}")


def main():
    """
    The main function to execute the Notcoin distribution calculation.
    """
    # Constants for the distributed and remaining amounts
    TOTAL_DISTRIBUTED = 85_000_000.0  # $85 million
    TOTAL_LEFT = 15_000_000.0          # $15 million

    try:
        # Create an instance of NotcoinDistributor
        distributor = NotcoinDistributor(TOTAL_DISTRIBUTED, TOTAL_LEFT)
        
        # Display the remaining Notcoin
        distributor.display_remaining()
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
