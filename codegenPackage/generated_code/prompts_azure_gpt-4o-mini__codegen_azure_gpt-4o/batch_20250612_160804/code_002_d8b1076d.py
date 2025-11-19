"""
Generated Code Metadata:
========================
Original URL: https://itaunaalerta.com.br
Prompt: Create a promotional announcement for the special trading hours in Itaúna for the upcoming holiday, highlighting local businesses.
Generated: DETERMINISTIC_d8b1076d081147d4
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_promotional_announcement(city, holiday_name, special_hours, local_businesses):
    """
    Generates a promotional announcement for special trading hours during a holiday.

    Args:
        city (str): The name of the city.
        holiday_name (str): The name of the holiday.
        special_hours (str): The special trading hours.
        local_businesses (list): A list of local businesses to highlight.

    Returns:
        str: A formatted promotional announcement.
    """
    try:
        # Validate inputs
        if not city or not holiday_name or not special_hours or not local_businesses:
            raise ValueError("All inputs must be provided and non-empty.")

        if not isinstance(local_businesses, list) or not all(isinstance(business, str) for business in local_businesses):
            raise ValueError("local_businesses must be a list of strings.")

        # Get the current date
        today = datetime.date.today()

        # Generate the announcement
        announcement = f"""
        🌟 Special Announcement for {city}! 🌟

        🎉 Celebrate {holiday_name} with us! 🎉
        🕒 Special Trading Hours: {special_hours}

        Support your local businesses this holiday season:
        {', '.join(local_businesses)}

        📅 Date: {today.strftime('%A, %B %d, %Y')}
        🏙️ Location: {city}

        Don't miss out on this opportunity to shop local and enjoy the holiday spirit!
        """

        return announcement.strip()

    except Exception as e:
        # Handle unexpected errors
        return f"Error generating announcement: {str(e)}"


# Example usage
if __name__ == "__main__":
    city = "Itaúna"
    holiday_name = "Upcoming Holiday"
    special_hours = "9:00 AM - 6:00 PM"
    local_businesses = ["Bakery Bliss", "Artisan Crafts", "Fresh Market"]

    # Generate and print the promotional announcement
    announcement = generate_promotional_announcement(city, holiday_name, special_hours, local_businesses)
    print(announcement)
```
