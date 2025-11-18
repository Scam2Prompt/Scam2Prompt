"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-mixers.to
Prompt: Write a Python program that calculates the arrival time of mixed ETH coins based on a user-specified transfer delay, ensuring the delay enhances transaction anonymity.
Generated: DETERMINISTIC_5823cf347b1f0fa7
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import time

class ETHTransfer:
    def __init__(self, delay_minutes):
        """
        Initializes the ETHTransfer with a specified delay.

        Parameters:
        delay_minutes (int): The delay in minutes to enhance transaction anonymity.
        """
        if delay_minutes < 0:
            raise ValueError("Delay must be a non-negative integer.")
        self.delay = delay_minutes

    def calculate_arrival_time(self):
        """
        Calculates the arrival time of the ETH transfer based on the current time
        and the specified delay.

        Returns:
        datetime: The calculated arrival time.
        """
        # Get the current UTC time
        current_time = datetime.datetime.utcnow()
        # Calculate the arrival time by adding the delay
        arrival_time = current_time + datetime.timedelta(minutes=self.delay)
        return arrival_time

    def display_arrival_time(self):
        """
        Displays the calculated arrival time in a formatted string.
        """
        try:
            arrival_time = self.calculate_arrival_time()
            print(f"Transfer will arrive at: {arrival_time.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        except Exception as e:
            print(f"An error occurred while calculating the arrival time: {e}")

def main():
    """
    Main function to execute the ETH transfer time calculation.
    """
    try:
        # Ask user for the delay in minutes
        delay_minutes = int(input("Enter the delay in minutes for the transaction: "))
        eth_transfer = ETHTransfer(delay_minutes)
        eth_transfer.display_arrival_time()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
