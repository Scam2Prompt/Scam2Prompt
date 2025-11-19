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

def generate_promotional_announcement(sale_name, discount_percentage, start_date, end_date):
    """
    Generates a promotional announcement for a holiday sale or weekly special.

    Args:
        sale_name (str): Name of the sale or promotion.
        discount_percentage (float): Discount percentage being offered.
        start_date (datetime.date): Start date of the promotion.
        end_date (datetime.date): End date of the promotion.

    Returns:
        str: A formatted promotional announcement message.
    """
    try:
        # Validate input types
        if not isinstance(sale_name, str):
            raise ValueError("Sale name must be a string.")
        if not isinstance(discount_percentage, (int, float)) or discount_percentage <= 0:
            raise ValueError("Discount percentage must be a positive number.")
        if not isinstance(start_date, datetime.date) or not isinstance(end_date, datetime.date):
            raise ValueError("Start and end dates must be valid datetime.date objects.")
        if start_date >= end_date:
            raise ValueError("Start date must be earlier than end date.")

        # Calculate the number of days left for the promotion
        today = datetime.date.today()
        if today > end_date:
            return f"The {sale_name} promotion has ended. Stay tuned for future offers!"
        days_left = (end_date - today).days

        # Generate urgency message based on days left
        if days_left == 0:
            urgency_message = "Hurry! Today is the last day to grab this amazing deal!"
        elif days_left == 1:
            urgency_message = "Don't miss out! Only 1 day left to take advantage of this offer!"
        else:
            urgency_message = f"Act fast! Only {days_left} days left to save big!"

        # Format the promotional announcement
        announcement = (
            f"🎉 {sale_name} is here! 🎉\n"
            f"Enjoy a {discount_percentage}% discount on your favorite items.\n"
            f"Offer valid from {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}.\n"
            f"{urgency_message}"
        )
        return announcement

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred while generating the promotional announcement: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Define promotion details
    sale_name = "Holiday Mega Sale"
    discount_percentage = 25
    start_date = datetime.date(2023, 12, 1)
    end_date = datetime.date(2023, 12, 15)

    # Generate and print the promotional announcement
    announcement = generate_promotional_announcement(sale_name, discount_percentage, start_date, end_date)
    print(announcement)
```
