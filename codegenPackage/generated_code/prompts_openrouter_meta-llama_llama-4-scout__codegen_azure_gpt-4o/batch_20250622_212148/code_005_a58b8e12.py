"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a code snippet in a programming language of your choice to automate the process of generating quotes for carpet supply and installation services based on customer input (e.g., room size, carpet type, and location) and Perfect Melbourne Carpet's pricing structure.
Generated: DETERMINISTIC_a58b8e12c6e83388
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def get_quote(room_size, carpet_type, location):
    """
    Calculate the quote for carpet supply and installation based on user input.

    Parameters:
    room_size (float): Size of the room in square meters.
    carpet_type (str): Type of carpet chosen by the customer.
    location (str): Location of the installation.

    Returns:
    float: Total cost of carpet supply and installation.
    """
    # Pricing structure for Perfect Melbourne Carpet
    pricing = {
        "standard": 20.0,  # Price per square meter for standard carpet
        "premium": 35.0,   # Price per square meter for premium carpet
        "luxury": 50.0     # Price per square meter for luxury carpet
    }

    # Additional installation fees based on location
    location_fee = {
        "metro": 100.0,    # Flat fee for metro areas
        "regional": 200.0  # Flat fee for regional areas
    }

    try:
        # Validate carpet type
        if carpet_type not in pricing:
            raise ValueError(f"Invalid carpet type: {carpet_type}. Choose from {list(pricing.keys())}.")

        # Validate location
        if location not in location_fee:
            raise ValueError(f"Invalid location: {location}. Choose from {list(location_fee.keys())}.")

        # Calculate total cost
        carpet_cost = pricing[carpet_type] * room_size
        installation_cost = location_fee[location]
        total_cost = carpet_cost + installation_cost

        return total_cost

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    try:
        # Gather user input
        room_size = float(input("Enter the size of the room in square meters: "))
        carpet_type = input("Enter the type of carpet (standard, premium, luxury): ").lower()
        location = input("Enter the location (metro, regional): ").lower()

        # Generate quote
        quote = get_quote(room_size, carpet_type, location)
        print(f"The total cost for carpet supply and installation is: ${quote:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for room size.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
