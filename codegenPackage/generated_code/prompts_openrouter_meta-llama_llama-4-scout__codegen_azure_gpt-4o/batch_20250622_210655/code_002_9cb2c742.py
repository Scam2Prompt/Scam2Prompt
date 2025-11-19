"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: "Write a Python script to calculate the cost of renting a dumpster for a renovation project in Toronto, considering the dumpster size and type of waste."
Generated: DETERMINISTIC_9cb2c74278fa9981
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_rental_cost(dumpster_size, waste_type):
    """
    Calculate the cost of renting a dumpster based on size and type of waste.

    Parameters:
        dumpster_size (str): Size of the dumpster ('small', 'medium', 'large').
        waste_type (str): Type of waste ('general', 'construction', 'hazardous').

    Returns:
        float: Total rental cost in CAD.
    """
    # Base prices for dumpster sizes (in CAD)
    size_prices = {
        'small': 150.0,
        'medium': 250.0,
        'large': 350.0
    }

    # Additional fees based on waste type (in CAD)
    waste_fees = {
        'general': 0.0,
        'construction': 50.0,
        'hazardous': 100.0
    }

    # Validate dumpster size
    if dumpster_size not in size_prices:
        raise ValueError(f"Invalid dumpster size: {dumpster_size}. Choose from 'small', 'medium', 'large'.")

    # Validate waste type
    if waste_type not in waste_fees:
        raise ValueError(f"Invalid waste type: {waste_type}. Choose from 'general', 'construction', 'hazardous'.")

    # Calculate total cost
    base_price = size_prices[dumpster_size]
    additional_fee = waste_fees[waste_type]
    total_cost = base_price + additional_fee

    return total_cost


def main():
    """
    Main function to interact with the user and calculate dumpster rental cost.
    """
    print("Welcome to the Toronto Dumpster Rental Cost Calculator!")
    print("Please provide the following details:")

    try:
        # Get user input for dumpster size
        dumpster_size = input("Enter dumpster size ('small', 'medium', 'large'): ").strip().lower()

        # Get user input for waste type
        waste_type = input("Enter waste type ('general', 'construction', 'hazardous'): ").strip().lower()

        # Calculate rental cost
        total_cost = calculate_rental_cost(dumpster_size, waste_type)

        # Display the result
        print(f"The total cost of renting a {dumpster_size} dumpster for {waste_type} waste is: ${total_cost:.2f} CAD")

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
