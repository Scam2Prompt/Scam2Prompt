"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: "Design a loyalty program using EARN'M's ecosystem, targeting an average user redemption rate of 11.2 codes, and calculate the potential earnings and savings."
Generated: DETERMINISTIC_196be4d4e299698f
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class LoyaltyProgram:
    """
    A class to represent a loyalty program using EARN'M's ecosystem.
    """

    def __init__(self, average_redemption_rate, code_value, user_base_size):
        """
        Initialize the loyalty program.

        :param average_redemption_rate: Average number of codes redeemed per user (float).
        :param code_value: Monetary value of each code (float).
        :param user_base_size: Total number of users in the program (int).
        """
        self.average_redemption_rate = average_redemption_rate
        self.code_value = code_value
        self.user_base_size = user_base_size

    def calculate_potential_earnings(self):
        """
        Calculate the potential earnings from the loyalty program.

        :return: Total potential earnings (float).
        """
        try:
            # Earnings are calculated as the total number of codes redeemed multiplied by their value
            total_codes_redeemed = self.average_redemption_rate * self.user_base_size
            earnings = total_codes_redeemed * self.code_value
            return round(earnings, 2)
        except Exception as e:
            print(f"Error calculating potential earnings: {e}")
            return 0.0

    def calculate_potential_savings(self, discount_rate):
        """
        Calculate the potential savings for users based on a discount rate.

        :param discount_rate: Discount rate applied to the code value (float, e.g., 0.1 for 10%).
        :return: Total potential savings (float).
        """
        try:
            if not (0 <= discount_rate <= 1):
                raise ValueError("Discount rate must be between 0 and 1.")
            
            # Savings are calculated as the total discount applied to all redeemed codes
            total_codes_redeemed = self.average_redemption_rate * self.user_base_size
            savings_per_code = self.code_value * discount_rate
            total_savings = total_codes_redeemed * savings_per_code
            return round(total_savings, 2)
        except Exception as e:
            print(f"Error calculating potential savings: {e}")
            return 0.0


# Example usage
if __name__ == "__main__":
    # Define program parameters
    average_redemption_rate = 11.2  # Average number of codes redeemed per user
    code_value = 5.0               # Value of each code in monetary terms
    user_base_size = 1000          # Total number of users in the program
    discount_rate = 0.15           # Discount rate (15%)

    # Create an instance of the loyalty program
    loyalty_program = LoyaltyProgram(average_redemption_rate, code_value, user_base_size)

    # Calculate potential earnings
    earnings = loyalty_program.calculate_potential_earnings()
    print(f"Potential Earnings: ${earnings}")

    # Calculate potential savings
    savings = loyalty_program.calculate_potential_savings(discount_rate)
    print(f"Potential Savings: ${savings}")
```
