"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.traveloagency.com
Prompt: Write a Python script to simulate a flight search widget similar to the one described on Traveloagency, allowing users to input origin, destination, travel dates, and passenger details.
Generated: DETERMINISTIC_6bd83b27ab294fb1
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import sys

def validate_date(input_date):
    """
    Validates the input date format and ensures it is not in the past.
    Args:
        input_date (str): Date string in 'YYYY-MM-DD' format.
    Returns:
        datetime.date: Validated date object.
    Raises:
        ValueError: If the date format is incorrect or the date is in the past.
    """
    try:
        date_obj = datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
        if date_obj < datetime.date.today():
            raise ValueError("Travel date cannot be in the past.")
        return date_obj
    except ValueError as ve:
        raise ValueError(f"Invalid date format or value: {ve}")


def validate_passenger_count(passenger_count):
    """
    Validates the passenger count to ensure it is a positive integer.
    Args:
        passenger_count (str): Passenger count as string input.
    Returns:
        int: Validated passenger count.
    Raises:
        ValueError: If passenger count is not a positive integer.
    """
    try:
        count = int(passenger_count)
        if count <= 0:
            raise ValueError("Passenger count must be a positive integer.")
        return count
    except ValueError as ve:
        raise ValueError(f"Invalid passenger count: {ve}")


def flight_search_widget():
    """
    Simulates a flight search widget to collect user input for flight search.
    - Origin City
    - Destination City
    - Travel Dates
    - Passenger Details
    Prints out the search criteria after collecting valid inputs.
    """
    print("Welcome to the Flight Search Widget!\n")
    
    try:
        # Collect origin city
        origin = input("Enter the origin city: ").strip()
        if not origin:
            raise ValueError("Origin city cannot be empty.")

        # Collect destination city
        destination = input("Enter the destination city: ").strip()
        if not destination:
            raise ValueError("Destination city cannot be empty.")

        # Collect departure date
        dep_date_input = input("Enter the departure date (YYYY-MM-DD): ").strip()
        dep_date = validate_date(dep_date_input)

        # Collect return date
        return_date_input = input("Enter the return date (YYYY-MM-DD) [Optional, press Enter to skip]: ").strip()
        return_date = None
        if return_date_input:
            return_date = validate_date(return_date_input)
            if return_date < dep_date:
                raise ValueError("Return date cannot be before the departure date.")

        # Collect passenger count
        passenger_count_input = input("Enter the number of passengers: ").strip()
        passenger_count = validate_passenger_count(passenger_count_input)

        # Display search criteria
        print("\nFlight Search Criteria:")
        print(f"Origin: {origin}")
        print(f"Destination: {destination}")
        print(f"Departure Date: {dep_date}")
        if return_date:
            print(f"Return Date: {return_date}")
        print(f"Passengers: {passenger_count}")

        print("\nThank you! Searching for flights...")
    except Exception as e:
        print(f"Error: {e}")
        print("Please try again.")
        sys.exit(1)


if __name__ == "__main__":
    # Execute the widget function
    flight_search_widget()
```
