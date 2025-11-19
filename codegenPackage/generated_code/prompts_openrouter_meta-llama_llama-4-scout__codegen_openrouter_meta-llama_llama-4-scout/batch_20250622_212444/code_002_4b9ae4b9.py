"""
Generated Code Metadata:
========================
Original URL: https://m-matamsklogi.godaddysites.com
Prompt: Create a promotional announcement for a holiday sale or weekly special, including a discount offer and a sense of urgency.
Generated: DETERMINISTIC_4b9ae4b90ea3f0a8
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class PromotionalAnnouncement:
    def __init__(self, sale_name, discount_percentage, start_date, end_date):
        """
        Initialize a promotional announcement.

        Args:
            sale_name (str): Name of the sale or special.
            discount_percentage (float): Discount percentage.
            start_date (datetime): Start date of the sale.
            end_date (datetime): End date of the sale.
        """
        self.sale_name = sale_name
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def get_announcement(self):
        """
        Generate the promotional announcement.

        Returns:
            str: The promotional announcement.
        """
        announcement = f"**{self.sale_name}**\n"
        announcement += f"Get {self.discount_percentage}% off our best products!\n"
        announcement += f" Limited time offer: {self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}\n"
        announcement += "Don't miss out! "

        return announcement

    def is_active(self):
        """
        Check if the sale is currently active.

        Returns:
            bool: True if the sale is active, False otherwise.
        """
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date

def main():
    try:
        sale_name = "Holiday Sale"
        discount_percentage = 20.0
        end_date = datetime.now() + timedelta(days=7)
        start_date = datetime.now()

        announcement = PromotionalAnnouncement(sale_name, discount_percentage, start_date, end_date)

        print(announcement.get_announcement())

        if announcement.is_active():
            print("The sale is currently active.")
        else:
            print("The sale is not currently active.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
