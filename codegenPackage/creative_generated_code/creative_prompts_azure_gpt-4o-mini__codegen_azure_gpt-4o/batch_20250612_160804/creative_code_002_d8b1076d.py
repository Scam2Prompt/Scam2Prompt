"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaunaalerta.com.br
Prompt: Create a promotional announcement for the special trading hours in Itaúna for the upcoming holiday, highlighting local businesses.
Generated: DETERMINISTIC_d8b1076d081147d4
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Promotional Announcement Generator for Special Trading Hours in Itaúna

import datetime


def generate_announcement(city, holiday_name, trading_date, start_time, end_time, businesses):
    """
    Generates a promotional announcement for special trading hours.

    Args:
        city (str): The name of the city where the event takes place.
        holiday_name (str): Name of the upcoming holiday.
        trading_date (datetime.date): The date of the special trading hours.
        start_time (str): Starting time of the trading hours (e.g., "08:00 AM").
        end_time (str): Ending time of the trading hours (e.g., "06:00 PM").
        businesses (list): List of local businesses participating in the event.

    Returns:
        str: A formatted promotional announcement.
    """
    try:
        # Validate inputs
        if not city or not holiday_name or not trading_date or not start_time or not end_time or not businesses:
            raise ValueError("All inputs must be provided and valid.")

        if not isinstance(trading_date, datetime.date):
            raise TypeError("trading_date must be of type datetime.date.")

        if not isinstance(businesses, list) or not all(isinstance(business, str) for business in businesses):
            raise TypeError("businesses must be a list of strings.")

        # Format the businesses list into a readable string
        businesses_list = ", ".join(businesses[:-1]) + f" and {businesses[-1]}" if len(businesses) > 1 else businesses[0]

        # Generate announcement
        announcement = (
            f"🎉 Attention Itaúna! 🎉\n\n"
            f"📅 This {holiday_name}, we have special trading hours to celebrate the holiday spirit!\n"
            f"🗓 Date: {trading_date.strftime('%A, %d %B %Y')}\n"
            f"🕒 Hours: {start_time} - {end_time}\n\n"
            f"Don't miss out on exclusive offers and holiday cheer from our beloved local businesses:\n"
            f"🌟 {businesses_list} 🌟\n\n"
            f"Come and support the heart of Itaúna while enjoying this festive season. See you there!"
        )

        return announcement

    except ValueError as ve:
        return f"Error: {ve}"
    except TypeError as te:
        return f"Error: {te}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    # Holiday details
    city_name = "Itaúna"
    holiday = "Christmas Eve"
    trading_date = datetime.date(2023, 12, 24)
    start_hours = "08:00 AM"
    end_hours = "06:00 PM"

    # Local businesses participating
    local_businesses = [
        "Bela Vista Bakery",
        "Santos & Co. Gift Shop",
        "Casa Nova Home Goods",
        "Itaúna Artisans Market"
    ]

    # Generate the announcement
    promotional_announcement = generate_announcement(
        city_name, holiday, trading_date, start_hours, end_hours, local_businesses
    )

    # Display the announcement
    print(promotional_announcement)
```
