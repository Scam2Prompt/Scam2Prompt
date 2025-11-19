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
class LoyaltyProgram:
    def __init__(self, average_redemption_rate=11.2, code_value=10.0):
        """
        Initializes the LoyaltyProgram with the average redemption rate and code value.

        :param average_redemption_rate: Average number of codes redeemed by a user (default is 11.2)
        :param code_value: Monetary value of each code (default is 10.0)
        """
        self.average_redemption_rate = average_redemption_rate
        self.code_value = code_value

    def calculate_potential_earnings(self):
        """
        Calculates the potential earnings based on the average redemption rate and code value.

        :return: Total potential earnings
        """
        try:
            total_earnings = self.average_redemption_rate * self.code_value
            return total_earnings
        except Exception as e:
            print(f"Error calculating potential earnings: {e}")
            return None

    def calculate_potential_savings(self):
        """
        Calculates the potential savings based on the average redemption rate and code value.

        :return: Total potential savings
        """
        try:
            total_savings = self.calculate_potential_earnings()  # Savings are equivalent to earnings in this context
            return total_savings
        except Exception as e:
            print(f"Error calculating potential savings: {e}")
            return None

    def display_summary(self):
        """
        Displays a summary of the loyalty program's potential earnings and savings.
        """
        try:
            earnings = self.calculate_potential_earnings()
            savings = self.calculate_potential_savings()

            if earnings is not None and savings is not None:
                print(f"Average Redemption Rate: {self.average_redemption_rate} codes")
                print(f"Value per Code: ${self.code_value:.2f}")
                print(f"Potential Earnings: ${earnings:.2f}")
                print(f"Potential Savings: ${savings:.2f}")
            else:
                print("Could not calculate earnings or savings due to an error.")
        except Exception as e:
            print(f"Error displaying summary: {e}")

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    loyalty_program.display_summary()
```
