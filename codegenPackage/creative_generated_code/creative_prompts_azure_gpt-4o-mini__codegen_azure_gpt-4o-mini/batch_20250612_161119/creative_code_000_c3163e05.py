"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Generate a code snippet that calculates the monthly payment for a Chevrolet Onix using the consórcio details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_c3163e0555df2bb8
Batch ID: 20250612_161119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ConsorcioCalculator:
    """
    A class to calculate the monthly payment for a Chevrolet Onix based on consórcio details.
    """

    def __init__(self, total_value, number_of_months, interest_rate):
        """
        Initializes the calculator with the consórcio details.

        :param total_value: Total value of the Chevrolet Onix
        :param number_of_months: Total number of months for the consórcio
        :param interest_rate: Annual interest rate as a percentage
        """
        self.total_value = total_value
        self.number_of_months = number_of_months
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment based on the total value, number of months, and interest rate.

        :return: The monthly payment amount
        :raises ValueError: If any parameter is invalid (non-positive values)
        """
        # Validate inputs
        if self.total_value <= 0:
            raise ValueError("Total value must be greater than zero.")
        if self.number_of_months <= 0:
            raise ValueError("Number of months must be greater than zero.")
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        # Calculate monthly interest rate
        monthly_interest_rate = self.interest_rate / 12
        
        # Calculate monthly payment using the formula for an amortizing loan
        if monthly_interest_rate > 0:
            monthly_payment = (self.total_value * monthly_interest_rate) / \
                              (1 - (1 + monthly_interest_rate) ** -self.number_of_months)
        else:
            # If interest rate is zero, simply divide total value by number of months
            monthly_payment = self.total_value / self.number_of_months
        
        return monthly_payment

if __name__ == "__main__":
    try:
        total_value = 60000  # Example total value of Chevrolet Onix
        number_of_months = 60  # Example number of months for consórcio
        interest_rate = 7.5  # Example annual interest rate

        # Initialize the calculator
        calculator = ConsorcioCalculator(total_value, number_of_months, interest_rate)

        # Calculate monthly payment
        monthly_payment = calculator.calculate_monthly_payment()

        print(f"The monthly payment for the Chevrolet Onix is: R$ {monthly_payment:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
