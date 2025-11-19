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

class RefundError(Exception):
    """Custom exception for refund-related errors."""
    pass

class NFTRefundHandler:
    """
    A class to handle refunds for NFT purchases based on specified timelines.
    """

    def __init__(self, refund_period_days=14):
        """
        Initialize the refund handler with a specific refund period.

        :param refund_period_days: Number of days within which a refund can be requested.
        """
        self.refund_period_days = refund_period_days

    def process_refund(self, purchase_date, current_date=None):
        """
        Process a refund for an NFT purchase.

        :param purchase_date: The date of the NFT purchase (ISO format string, e.g., "YYYY-MM-DD").
        :param current_date: The current date (ISO format string). Defaults to today's date.
        :return: A confirmation message if the refund is successful.
        :raises RefundError: If the refund period has expired or if the dates are invalid.
        """
        try:
            # Convert dates from ISO format strings to datetime objects
            purchase_date_obj = datetime.strptime(purchase_date, "%Y-%m-%d")
            current_date_obj = datetime.strptime(current_date, "%Y-%m-%d") if current_date else datetime.now()
            
            # Validate the refund eligibility based on the timeline
            refund_deadline = purchase_date_obj + timedelta(days=self.refund_period_days)
            if current_date_obj > refund_deadline:
                raise RefundError("Refund period has expired.")

            # Refund logic (placeholder for actual refund processing code)
            return f"Refund processed successfully. Purchase date: {purchase_date}, Refund request date: {current_date_obj.date()}"

        except ValueError as e:
            # Handle invalid date format
            raise RefundError(f"Date format error: {str(e)}") from e
        except RefundError as re:
            # Re-raise refund-related errors
            raise re
        except Exception as ex:
            # Catch-all for unforeseen errors
            raise RefundError(f"An unexpected error occurred: {str(ex)}") from ex


# Example usage
if __name__ == "__main__":
    try:
        refund_handler = NFTRefundHandler(refund_period_days=14)
        purchase_date = "2023-09-20"  # Example purchase date
        current_date = "2023-10-02"   # Example current date (can be omitted for today's date)
        result = refund_handler.process_refund(purchase_date, current_date)
        print(result)
    except RefundError as e:
        print(f"Refund failed: {str(e)}")
```
