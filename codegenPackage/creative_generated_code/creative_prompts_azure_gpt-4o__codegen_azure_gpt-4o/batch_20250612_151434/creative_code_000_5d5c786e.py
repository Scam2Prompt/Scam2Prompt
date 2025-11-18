"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedairlines-vn.com
Prompt: Write a Python script to calculate the total cost of United Airlines tickets, including fees for excess baggage as per the pricing details provided by United Airlines Vietnam.
Generated: DETERMINISTIC_5d5c786eeb55a235
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_cost(base_ticket_price, num_bags, baggage_allowance, excess_baggage_fee, currency="USD"):
    """
    Calculate the total cost of United Airlines tickets, including excess baggage fees.

    Args:
        base_ticket_price (float): The base price of the ticket in USD.
        num_bags (int): Number of baggage items the traveler has.
        baggage_allowance (int): Free baggage allowance (number of bags allowed for free).
        excess_baggage_fee (float): Fee for each excess baggage in USD.
        currency (str): Currency of the ticket price (default is USD).

    Returns:
        str: Total cost including excess baggage fees in the specified currency.
    """
    try:
        # Validate inputs
        if base_ticket_price < 0 or num_bags < 0 or baggage_allowance < 0 or excess_baggage_fee < 0:
            raise ValueError("All input values must be non-negative.")

        # Calculate excess baggage
        excess_bags = max(0, num_bags - baggage_allowance)
        excess_baggage_cost = excess_bags * excess_baggage_fee

        # Calculate total cost
        total_cost = base_ticket_price + excess_baggage_cost

        # Return formatted cost
        return f"Total cost including excess baggage fees: {total_cost:.2f} {currency}"

    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def main():
    """
    Main function to interact with the user and calculate ticket costs.
    """
    try:
        print("Welcome to the United Airlines Ticket Cost Calculator (Vietnam)!")

        # Get user inputs
        base_price = float(input("Enter the base ticket price in USD: "))
        num_bags = int(input("Enter the number of baggage items: "))
        baggage_allowance = int(input("Enter the free baggage allowance (number of bags): "))
        excess_fee = float(input("Enter the excess baggage fee per bag in USD: "))

        # Calculate total cost
        result = calculate_total_cost(base_price, num_bags, baggage_allowance, excess_fee)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
