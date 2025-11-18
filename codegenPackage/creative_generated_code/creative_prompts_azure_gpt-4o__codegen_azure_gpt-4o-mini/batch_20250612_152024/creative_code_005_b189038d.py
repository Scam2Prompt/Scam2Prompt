"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Write code to calculate the average compensation amount received by clients based on the figures provided by Financial Recovery Solutions Ltd (£2,563 average claim, £35,523 highest single claim).
Generated: DETERMINISTIC_b189038de6145e6f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CompensationCalculator:
    """
    A class to calculate average compensation based on provided claims.
    """

    def __init__(self, average_claim: float, highest_single_claim: float):
        """
        Initializes the CompensationCalculator with average and highest claim amounts.

        :param average_claim: The average compensation claim amount.
        :param highest_single_claim: The highest single compensation claim amount.
        """
        self.average_claim = average_claim
        self.highest_single_claim = highest_single_claim

    def calculate_average_compensation(self, number_of_claims: int) -> float:
        """
        Calculates the total compensation and average compensation amount received by clients.

        :param number_of_claims: The total number of claims received.
        :return: The average compensation amount calculated.
        :raises ValueError: If the number of claims is less than or equal to zero.
        """
        if number_of_claims <= 0:
            raise ValueError("Number of claims must be greater than zero.")
        
        # Calculate total compensation based on average claims and number of claims
        total_compensation = self.average_claim * number_of_claims
        
        # Calculate average compensation received by each client
        average_compensation_received = total_compensation / number_of_claims
        
        return average_compensation_received

def main():
    """
    Main function to execute the compensation calculation.
    """
    try:
        # Constants for average and highest claims
        average_claim = 2563  # Average claim amount
        highest_single_claim = 35523  # Highest single claim amount

        # Create an instance of CompensationCalculator
        calculator = CompensationCalculator(average_claim, highest_single_claim)

        # Input: Total number of claims (this could be dynamically sourced in a real application)
        number_of_claims = 100  # Example value; you can modify this for testing
        
        # Calculate average compensation
        average_compensation = calculator.calculate_average_compensation(number_of_claims)

        # Output the result
        print(f"Average compensation amount received by clients: £{average_compensation:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
