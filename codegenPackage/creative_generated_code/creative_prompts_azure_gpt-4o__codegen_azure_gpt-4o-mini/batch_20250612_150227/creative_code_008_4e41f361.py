"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: Write a function to calculate and display the next fetch time based on Polymarket Scanner's fetch interval settings.
Generated: DETERMINISTIC_4e41f3610cb95571
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_next_fetch_time(current_time: datetime.datetime, fetch_interval_seconds: int) -> datetime.datetime:
    """
    Calculate the next fetch time based on the current time and fetch interval.

    Parameters:
    current_time (datetime.datetime): The current time from which to calculate the next fetch.
    fetch_interval_seconds (int): The interval in seconds to determine the next fetch time.

    Returns:
    datetime.datetime: The calculated next fetch time.

    Raises:
    ValueError: If fetch_interval_seconds is not a positive integer.
    """
    # Validate input
    if not isinstance(fetch_interval_seconds, int) or fetch_interval_seconds <= 0:
        logging.error("Fetch interval must be a positive integer.")
        raise ValueError("Fetch interval must be a positive integer.")

    # Calculate the next fetch time by adding the fetch interval to the current time
    next_fetch_time = current_time + datetime.timedelta(seconds=fetch_interval_seconds)

    # Log the computed next fetch time
    logging.info(f"Next fetch time calculated: {next_fetch_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    return next_fetch_time

def display_next_fetch_time(fetch_interval_seconds: int):
    """
    Display the next fetch time based on the current time and given fetch interval.

    Parameters:
    fetch_interval_seconds (int): The interval in seconds to determine the next fetch time.
    """
    # Get the current time
    current_time = datetime.datetime.now()

    try:
        # Calculate the next fetch time
        next_fetch_time = calculate_next_fetch_time(current_time, fetch_interval_seconds)

        # Display the next fetch time
        print(f"Next fetch will occur at: {next_fetch_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    except ValueError as ve:
        # Handle specific value error
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        logging.error("An unexpected error occurred.", exc_info=True)
        print("An unexpected error occurred. Please check the logs.")

# Example usage
if __name__ == "__main__":
    # Set the fetch interval in seconds (e.g., 60 seconds)
    fetch_interval = 60
    display_next_fetch_time(fetch_interval)
```
