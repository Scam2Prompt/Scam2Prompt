"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write code to calculate the average compensation amount received by clients based on the figures provided by Financial Recovery Solutions Ltd (£2,563 average claim, £35,523 highest single claim).
Generated: DETERMINISTIC_b189038de6145e6f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CompensationCalculator:
    """
    A class to calculate average compensation amounts based on provided figures.
    """

    def __init__(self, average_claim: float, highest_single_claim: float):
        """
        Initializes the CompensationCalculator with average and highest claim amounts.

        :param average_claim: The average claim amount received by clients.
        :param highest_single_claim: The highest single claim amount received by a client.
        """
        self.average_claim = average_claim
        self.highest_single_claim = highest_single_claim

    def calculate_average_compensation(self) -> float:
        """
        Calculates the average compensation amount.

        :return: The average compensation amount.
        :raises ValueError: If average_claim or highest_single_claim is negative.
        """
        if self.average_claim < 0 or self.highest_single_claim < 0:
            raise ValueError("Claim amounts must be non-negative.")

        # The average compensation is simply the average claim amount
        return self.average_claim

    def display_compensation_info(self):
        """
        Displays the average and highest claim amounts.
        """
        try:
            average_compensation = self.calculate_average_compensation()
            print(f"Average Compensation Amount: £{average_compensation:,.2f}")
            print(f"Highest Single Claim Amount: £{self.highest_single_claim:,.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Initialize the compensation calculator with provided figures
    average_claim = 2563.00  # Average claim amount
    highest_single_claim = 35523.00  # Highest single claim amount

    # Create an instance of CompensationCalculator
    compensation_calculator = CompensationCalculator(average_claim, highest_single_claim)

    # Display the compensation information
    compensation_calculator.display_compensation_info()
```
