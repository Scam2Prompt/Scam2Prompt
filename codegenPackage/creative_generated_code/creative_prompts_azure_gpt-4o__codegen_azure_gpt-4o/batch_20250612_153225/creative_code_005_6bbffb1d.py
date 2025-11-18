"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auction-gomble.pages.dev
Prompt: Create a program to calculate the floor price of the GOMBLE Auction dynamically based on the bid history provided.
Generated: DETERMINISTIC_6bbffb1ded9ee0b6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import statistics

class GombleAuction:
    def __init__(self):
        """
        Initialize the GombleAuction class.
        This class tracks bid history and calculates the dynamic floor price.
        """
        self.bid_history = []

    def add_bid(self, bid_amount):
        """
        Adds a new bid amount to the bid history.

        Parameters:
            bid_amount (float): The amount of the bid to be added.

        Raises:
            ValueError: If bid_amount is not a positive number.
        """
        if bid_amount <= 0:
            raise ValueError("Bid amount must be a positive number.")
        self.bid_history.append(bid_amount)

    def calculate_floor_price(self):
        """
        Calculate the dynamic floor price based on bid history.

        Returns:
            float: The calculated floor price.

        Raises:
            ValueError: If bid history is empty, as no floor price can be calculated.
        """
        if not self.bid_history:
            raise ValueError("Bid history is empty. Unable to calculate floor price.")

        # Calculate floor price dynamically using the median bid value
        floor_price = statistics.median(self.bid_history)

        # Ensure a slight margin is added to the median
        margin = 0.05 * floor_price  # 5% margin
        return round(floor_price + margin, 2)

def main():
    """
    Main function to demonstrate the GombleAuction floor price calculation.
    """
    auction = GombleAuction()

    print("Welcome to the GOMBLE Auction system!")

    while True:
        try:
            action = input("Enter 'bid' to add a bid, 'floor' to calculate floor price, or 'exit' to quit: ").strip().lower()

            if action == 'bid':
                bid_amount = float(input("Enter your bid amount: "))
                auction.add_bid(bid_amount)
                print(f"Bid of {bid_amount} added successfully!")

            elif action == 'floor':
                floor_price = auction.calculate_floor_price()
                print(f"The current floor price is: {floor_price}")

            elif action == 'exit':
                print("Exiting the auction system. Goodbye!")
                break

            else:
                print("Invalid action. Please enter 'bid', 'floor', or 'exit'.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
