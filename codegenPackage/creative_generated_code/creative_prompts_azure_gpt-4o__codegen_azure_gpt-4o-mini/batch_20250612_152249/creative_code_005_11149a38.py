"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spores-buv.pages.dev
Prompt: Generate a Python script to calculate the remaining time for the "Agora IDO Sale 2 VIP Round" using the start and end timestamps provided on the Spores Network.
Generated: DETERMINISTIC_11149a38837fad41
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime

class IDOSaleTimer:
    def __init__(self, start_timestamp: str, end_timestamp: str):
        """
        Initializes the IDO Sale Timer with start and end timestamps.

        Args:
            start_timestamp (str): The start time of the IDO sale in ISO 8601 format.
            end_timestamp (str): The end time of the IDO sale in ISO 8601 format.
        """
        self.start_time = self.parse_timestamp(start_timestamp)
        self.end_time = self.parse_timestamp(end_timestamp)

    @staticmethod
    def parse_timestamp(timestamp: str) -> float:
        """
        Parses a timestamp string into a UNIX timestamp.

        Args:
            timestamp (str): The timestamp in ISO 8601 format.

        Returns:
            float: The UNIX timestamp.

        Raises:
            ValueError: If the timestamp format is incorrect.
        """
        try:
            dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            return dt.timestamp()
        except ValueError as e:
            raise ValueError(f"Invalid timestamp format: {timestamp}. Error: {e}")

    def time_remaining(self) -> str:
        """
        Calculates the remaining time until the IDO sale ends.

        Returns:
            str: A formatted string showing the remaining time in days, hours, minutes, and seconds.
        """
        current_time = time.time()

        if current_time < self.start_time:
            return "The IDO sale has not started yet."
        elif current_time > self.end_time:
            return "The IDO sale has already ended."

        remaining_seconds = self.end_time - current_time
        days, remainder = divmod(remaining_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"Time remaining: {int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"

if __name__ == "__main__":
    # Example timestamps for the sale; replace with actual timestamps
    START_TIMESTAMP = "2023-10-01T12:00:00Z"
    END_TIMESTAMP = "2023-10-10T12:00:00Z"

    try:
        ido_sale_timer = IDOSaleTimer(START_TIMESTAMP, END_TIMESTAMP)
        print(ido_sale_timer.time_remaining())
    except ValueError as e:
        print(e)
```
