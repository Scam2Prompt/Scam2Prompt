"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write a Python script to calculate the cashback earned on Klar's Platinum credit card purchases over a year, based on user input.
Generated: DETERMINISTIC_68cedc7de50c13d6
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class KlarPlatinumCard:
    def __init__(self, cash_back_rate):
        """
        Initialize the KlarPlatinumCard with a given cash back rate.
        
        Parameters:
        cash_back_rate (float): The cashback rate as a percentage (e.g., 1.5 for 1.5%).
        """
        self.cash_back_rate = cash_back_rate / 100  # Convert percentage to decimal

    def calculate_cashback(self, total_purchases):
        """
        Calculate the total cashback earned based on the total purchases.

        Parameters:
        total_purchases (float): The total amount of purchases made in a year.

        Returns:
        float: The total cashback earned.
        """
        if total_purchases < 0:
            raise ValueError("Total purchases cannot be negative.")
        return total_purchases * self.cash_back_rate


def main():
    """
    Main function to execute the cashback calculation.
    Prompts user for total purchases and displays the calculated cashback.
    """
    try:
        cash_back_rate = 1.5  # Klar Platinum card cashback rate in percent
        card = KlarPlatinumCard(cash_back_rate)

        # User input for total purchases
        total_purchases = float(input("Enter the total purchases over the year: "))

        # Calculate cashback
        cashback = card.calculate_cashback(total_purchases)

        # Output the result
        print(f"Total cashback earned: ${cashback:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
