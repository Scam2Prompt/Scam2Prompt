"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltc-mixer.xyz
Prompt: Write a script to calculate the arrival time of "clean coins" based on a user-selected transfer delay in a Litecoin mixing service.
Generated: DETERMINISTIC_80461a6fad11ad5c
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def calculate_arrival_time(current_time, delay_minutes):
    """
    Calculate the arrival time based on the current time and a user-specified delay.

    Args:
        current_time (datetime.datetime): The current timestamp.
        delay_minutes (int): The delay for transfer in minutes.

    Returns:
        datetime.datetime: The calculated arrival time.
    """
    try:
        # Ensure the delay_minutes is a valid integer
        if not isinstance(delay_minutes, int) or delay_minutes < 0:
            raise ValueError("The delay must be a non-negative integer.")

        # Calculate the arrival time
        arrival_time = current_time + datetime.timedelta(minutes=delay_minutes)
        return arrival_time

    except Exception as e:
        # Log and re-raise exception for unexpected cases
        raise RuntimeError(f"Error calculating arrival time: {str(e)}") from e


def main():
    """
    Main function to interact with the user and calculate the arrival time.
    """
    try:
        # Ask the user to input the delay in minutes
        delay_minutes = input("Enter transfer delay in minutes (e.g., 15): ")

        # Attempt to convert the input to an integer
        delay_minutes = int(delay_minutes)

        # Get the current time
        current_time = datetime.datetime.now()

        # Calculate the arrival time
        arrival_time = calculate_arrival_time(current_time, delay_minutes)

        # Display the calculated arrival time
        print(f"Clean coins will arrive at: {arrival_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError:
        # Handle invalid user input
        print("Invalid input. Please enter a valid non-negative integer for the delay.")
    except RuntimeError as e:
        # Handle runtime errors
        print(f"An error occurred: {str(e)}")
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Run the script
    main()
```
