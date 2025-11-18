"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinpepe-claims.pages.dev
Prompt: Create a function to calculate the cumulative gain percentage for $BPEP tokens based on the tokenomics stage price table provided on the Bitcoin Pepe website.
Generated: DETERMINISTIC_78c7c766f8915328
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BPEPTokenomics:
    """
    A class to encapsulate the functionality related to BPEP token pricing.
    """

    def __init__(self, price_table):
        """
        Initializes the BPEPTokenomics instance with a price table.

        :param price_table: A dictionary containing tokenomics stage price.
        """
        self.price_table = price_table

    def calculate_cumulative_gain_percentage(self, current_price):
        """
        Calculates the cumulative gain percentage based on the provided current price.

        :param current_price: The current price of the BPEP token.
        
        :return: Cumulative gain percentage.
        :raises ValueError: If current_price is negative or price_table is empty.
        """
        # Validate inputs
        if current_price < 0:
            raise ValueError("Current price cannot be negative.")
        
        if not self.price_table:
            raise ValueError("Price table cannot be empty.")
        
        # Get the initial price from the price table
        initial_price = min(self.price_table.values())

        # Calculate cumulative gain percentage
        gain_percentage = ((current_price - initial_price) / initial_price) * 100
        return gain_percentage


# Example usage:
if __name__ == "__main__":
    try:
        # Tokenomics price table (example values)
        tokenomics_price_table = {
            "Stage 1": 0.50,
            "Stage 2": 1.00,
            "Stage 3": 2.00,
            "Stage 4": 3.50
        }

        # Create an instance of the BPEPTokenomics class
        bpep_tokenomics = BPEPTokenomics(tokenomics_price_table)

        # Define the current price of the BPEP token
        current_price = 2.50

        # Calculate the cumulative gain percentage
        gain_percentage = bpep_tokenomics.calculate_cumulative_gain_percentage(current_price)

        # Print the result
        print(f"Cumulative Gain Percentage: {gain_percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
```
