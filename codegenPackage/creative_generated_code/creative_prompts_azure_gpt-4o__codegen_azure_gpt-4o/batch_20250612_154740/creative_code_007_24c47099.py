"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write code to generate a free measure and quote for carpet installation, using the pricing and service details provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_24c470999be1b660
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_carpet_quote(room_length, room_width, carpet_price_per_sqm, installation_fee_per_sqm):
    """
    Calculate the total cost for carpet installation based on room dimensions, 
    carpet price per square meter, and installation fee.

    Parameters:
    room_length (float): The length of the room in meters.
    room_width (float): The width of the room in meters.
    carpet_price_per_sqm (float): Price of carpet per square meter.
    installation_fee_per_sqm (float): Installation fee per square meter.

    Returns:
    dict: A dictionary containing the area, carpet cost, installation cost, and total cost.
    """
    try:
        # Validate inputs
        if room_length <= 0 or room_width <= 0:
            raise ValueError("Room dimensions must be positive values.")
        if carpet_price_per_sqm < 0 or installation_fee_per_sqm < 0:
            raise ValueError("Carpet price and installation fee must be non-negative values.")

        # Calculate area
        area = room_length * room_width

        # Calculate costs
        carpet_cost = area * carpet_price_per_sqm
        installation_cost = area * installation_fee_per_sqm
        total_cost = carpet_cost + installation_cost

        # Return a summary as a dictionary
        return {
            "Area (sqm)": round(area, 2),
            "Carpet Cost ($)": round(carpet_cost, 2),
            "Installation Cost ($)": round(installation_cost, 2),
            "Total Cost ($)": round(total_cost, 2)
        }

    except ValueError as ve:
        # Handle validation errors
        return {"Error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"Error": "An unexpected error occurred: " + str(e)}


def main():
    """
    Main function to handle user input and display the carpet quote.
    """
    try:
        # Prompt user for input
        print("Welcome to Perfect Melbourne Carpet Measure & Quote Tool!")
        room_length = float(input("Enter the length of the room (in meters): "))
        room_width = float(input("Enter the width of the room (in meters): "))
        carpet_price_per_sqm = float(input("Enter the price of carpet per square meter (in dollars): "))
        installation_fee_per_sqm = float(input("Enter the installation fee per square meter (in dollars): "))

        # Calculate quote
        quote = calculate_carpet_quote(room_length, room_width, carpet_price_per_sqm, installation_fee_per_sqm)

        # Display the quote
        if "Error" in quote:
            print(f"Error: {quote['Error']}")
        else:
            print("\n--- Carpet Installation Quote ---")
            for key, value in quote.items():
                print(f"{key}: {value}")
            print("---------------------------------")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
