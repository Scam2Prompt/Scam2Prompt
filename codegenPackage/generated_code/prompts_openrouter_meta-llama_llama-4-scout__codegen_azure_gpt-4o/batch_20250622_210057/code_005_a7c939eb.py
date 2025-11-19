"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: "Develop a code example for a model creator to earn income by setting a base fee for invocations of their model on the Arbius network."
Generated: DETERMINISTIC_a7c939eb550630c9
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from decimal import Decimal

# Define a class for the ModelCreator
class ModelCreator:
    """
    A class to represent a model creator on the Arbius network.
    Allows setting a base fee for model invocations and calculates earnings.
    """

    def __init__(self, creator_name: str, base_fee: Decimal):
        """
        Initialize the ModelCreator instance.

        :param creator_name: Name of the model creator.
        :param base_fee: Base fee for each invocation of the model.
        """
        if base_fee < Decimal("0.0"):
            raise ValueError("Base fee must be a non-negative value.")
        
        self.creator_name = creator_name
        self.base_fee = base_fee
        self.total_invocations = 0
        self.total_earnings = Decimal("0.0")

    def invoke_model(self, invocation_count: int = 1):
        """
        Simulate the invocation of the model.

        :param invocation_count: Number of times the model is invoked.
        :raises ValueError: If invocation_count is not positive.
        """
        if invocation_count <= 0:
            raise ValueError("Invocation count must be a positive integer.")
        
        self.total_invocations += invocation_count
        earnings = self.base_fee * Decimal(invocation_count)
        self.total_earnings += earnings
        return earnings

    def get_earnings_summary(self) -> dict:
        """
        Get a summary of the model creator's earnings.

        :return: A dictionary containing the earnings summary.
        """
        return {
            "creator_name": self.creator_name,
            "base_fee": str(self.base_fee),
            "total_invocations": self.total_invocations,
            "total_earnings": str(self.total_earnings)
        }

    def save_summary_to_file(self, file_path: str):
        """
        Save the earnings summary to a JSON file.

        :param file_path: Path to the file where the summary will be saved.
        """
        try:
            summary = self.get_earnings_summary()
            with open(file_path, "w") as file:
                json.dump(summary, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save summary to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a model creator instance
        creator = ModelCreator(creator_name="Alice", base_fee=Decimal("0.05"))

        # Simulate model invocations
        creator.invoke_model(invocation_count=10)
        creator.invoke_model(invocation_count=5)

        # Print earnings summary
        summary = creator.get_earnings_summary()
        print("Earnings Summary:", summary)

        # Save summary to a file
        creator.save_summary_to_file("earnings_summary.json")
        print("Earnings summary saved to 'earnings_summary.json'.")
    except Exception as error:
        print(f"An error occurred: {error}")
```
