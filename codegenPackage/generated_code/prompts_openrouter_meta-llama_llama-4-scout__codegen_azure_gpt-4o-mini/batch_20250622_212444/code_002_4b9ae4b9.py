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
import datetime

class PromotionalAnnouncement:
    def __init__(self, product_name, discount_percentage, start_date, end_date):
        """
        Initializes the promotional announcement with product details and sale dates.

        :param product_name: Name of the product on sale
        :param discount_percentage: Discount percentage for the sale
        :param start_date: Start date of the promotion (datetime object)
        :param end_date: End date of the promotion (datetime object)
        """
        self.product_name = product_name
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        """
        Checks if the promotion is currently active.

        :return: True if the promotion is active, False otherwise
        """
        current_date = datetime.datetime.now()
        return self.start_date <= current_date <= self.end_date

    def generate_announcement(self):
        """
        Generates the promotional announcement message.

        :return: A string containing the promotional announcement
        """
        if not self.is_active():
            return "The promotion is not currently active."

        announcement = (
            f"🎉 Holiday Sale Alert! 🎉\n"
            f"Get {self.discount_percentage}% off on {self.product_name}!\n"
            f"🗓️ Sale starts on {self.start_date.strftime('%B %d, %Y')} "
            f"and ends on {self.end_date.strftime('%B %d, %Y')}.\n"
            f"⏰ Hurry, don't miss out on this limited-time offer!\n"
            f"Shop now and save big!"
        )
        return announcement

def main():
    """
    Main function to create a promotional announcement and display it.
    """
    try:
        # Define the promotion details
        product_name = "Deluxe Coffee Maker"
        discount_percentage = 20
        start_date = datetime.datetime(2023, 12, 1)  # Promotion starts on December 1, 2023
        end_date = datetime.datetime(2023, 12, 25)    # Promotion ends on December 25, 2023

        # Create a promotional announcement instance
        promo = PromotionalAnnouncement(product_name, discount_percentage, start_date, end_date)

        # Generate and print the announcement
        announcement = promo.generate_announcement()
        print(announcement)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
