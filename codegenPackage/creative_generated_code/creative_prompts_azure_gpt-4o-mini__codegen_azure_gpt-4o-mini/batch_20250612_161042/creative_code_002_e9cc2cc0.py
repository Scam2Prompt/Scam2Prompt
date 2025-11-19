"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-nobody.pages.dev
Prompt: Write a function to handle refunds for NFT purchases based on the timeline outlined in the Nobody Mint content.
Generated: DETERMINISTIC_e9cc2cc0f9c334aa
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

class NFTPurchase:
    def __init__(self, purchase_date: datetime, amount: float):
        """
        Initializes an NFTPurchase instance.

        Args:
            purchase_date (datetime): The date and time when the NFT was purchased.
            amount (float): The amount of the purchase.
        """
        self.purchase_date = purchase_date
        self.amount = amount
        self.refund_window = timedelta(days=30)  # Refund window of 30 days

    def is_refundable(self) -> bool:
        """
        Checks if the NFT purchase is eligible for a refund.

        Returns:
            bool: True if the purchase is within the refund window, False otherwise.
        """
        current_time = datetime.now()
        return (current_time - self.purchase_date) <= self.refund_window

    def process_refund(self) -> str:
        """
        Processes the refund if eligible.

        Returns:
            str: A message indicating the result of the refund process.
        """
        try:
            if self.is_refundable():
                # Here you'd implement the actual refund logic, e.g., calling payment API
                # For this example, we will just return a success message.
                return f"Refund of ${self.amount:.2f} processed successfully."
            else:
                return "Refund period has expired. No refund available."
        except Exception as e:
            # Catching a general exception for demonstration; in a real-world scenario,
            # you would want to catch specific exceptions.
            return f"An error occurred while processing the refund: {str(e)}"

# Example usage:
if __name__ == "__main__":
    # Creating a purchase made 20 days ago for $50
    purchase_date = datetime.now() - timedelta(days=20)
    nft_purchase = NFTPurchase(purchase_date=purchase_date, amount=50.00)

    # Attempt to process a refund
    result = nft_purchase.process_refund()
    print(result)  # Expected: Refund of $50.00 processed successfully.
```
