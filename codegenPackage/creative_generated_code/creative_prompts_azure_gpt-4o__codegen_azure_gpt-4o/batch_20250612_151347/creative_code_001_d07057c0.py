"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suspicious-euler-473151.netlify.app
Prompt: Recommend libraries or APIs for integrating a Mac email client with Microsoft Exchange, ensuring compatibility with Exchange-specific features like calendar synchronization.
Generated: DETERMINISTIC_d07057c079deed0c
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code demonstrating the use of `exchangelib`, a library for integrating with Microsoft Exchange. This library supports email, calendar, and other Exchange-specific features.

```python
# exchangelib_example.py

# Import necessary libraries
from exchangelib import Credentials, Account, Configuration, DELEGATE

def connect_to_exchange(email, password, server):
    """
    Connects to a Microsoft Exchange server using the provided credentials.

    Args:
        email (str): Email address for the Exchange account.
        password (str): Password for the Exchange account.
        server (str): The Exchange server address.

    Returns:
        Account: A valid Exchange account object if connection is successful.
    Raises:
        Exception: If connection fails due to authentication or server issues.
    """
    try:
        # Set up credentials
        credentials = Credentials(username=email, password=password)

        # Configure the connection to the Exchange server
        config = Configuration(server=server, credentials=credentials)

        # Connect to the account using delegate access
        account = Account(
            primary_smtp_address=email,
            config=config,
            autodiscover=False,  # Disable autodiscover for custom server address
            access_type=DELEGATE,
        )

        # Test the connection
        account.root.refresh()

        print("Successfully connected to Exchange server!")
        return account

    except Exception as e:
        print(f"Failed to connect to Exchange server: {str(e)}")
        raise

def sync_calendar(account, days=7):
    """
    Fetches calendar events for the next specified number of days.

    Args:
        account (Account): The Exchange account object.
        days (int): Number of days to fetch events for.

    Returns:
        list: List of calendar events within the specified date range.
    """
    try:
        from datetime import datetime, timedelta

        # Define the time range
        start = datetime.now()
        end = start + timedelta(days=days)

        # Fetch calendar items
        events = account.calendar.filter(start__gte=start, end__lte=end)

        print(f"Found {len(events)} event(s) in the next {days} day(s).")
        return list(events)

    except Exception as e:
        print(f"Failed to fetch calendar events: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    # Replace with your actual credentials and server address
    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"
    SERVER = "your_exchange_server.com"

    try:
        # Connect to the Exchange server
        exchange_account = connect_to_exchange(EMAIL, PASSWORD, SERVER)

        # Sync calendar events for the next 7 days
        calendar_events = sync_calendar(exchange_account, days=7)

        # Print event details
        for event in calendar_events:
            print(f"Subject: {event.subject}, Start: {event.start}, End: {event.end}")

    except Exception as e:
        print(f"Error: {str(e)}")
```

### Notes:
1. Install `exchangelib` via pip: `pip install exchangelib`.
2. Replace placeholders like `your_email@example.com`, `your_password`, and `your_exchange_server.com` with actual values.
3. Ensure proper security practices by not hardcoding sensitive credentials in production. Use environment variables or a secure credential manager.
4. This script includes error handling for connection and calendar synchronization processes.
