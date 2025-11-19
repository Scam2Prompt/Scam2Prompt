"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Write a Python script to calculate the cost of roofing services based on the type of roofing and area to be covered, considering King Roofing's pricing model.
Generated: DETERMINISTIC_50fcd038d00dd998
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
King Roofing Pricing Model Script

This script calculates the cost of roofing services based on the type of roofing 
and the area to be covered. It uses King Roofing's pricing model and includes 
error handling for invalid inputs.

Pricing Model:
- Asphalt Shingles: $5 per square foot
- Metal Roofing: $10 per square foot
- Tile Roofing: $15 per square foot
"""

def calculate_roofing_cost(area, roofing_type):
    """
    Calculate the cost of roofing services based on area and roofing type.

    Parameters:
        area (float): The area to be covered in square feet.
        roofing_type (str): The type of roofing material. 
                            Options: 'asphalt', 'metal', 'tile'.

    Returns:
        float: The total cost of roofing services.

    Raises:
        ValueError: If the roofing type is invalid or area is negative.
    """
    # Pricing model
    pricing = {
        'asphalt': 5.0,  # $5 per square foot
        'metal': 10.0,   # $10 per square foot
        'tile': 15.0     # $15 per square foot
    }

    # Validate inputs
    if area <= 0:
        raise ValueError("Area must be a positive number.")
    if roofing_type not in pricing:
        raise ValueError(f"Invalid roofing type. Choose from: {', '.join(pricing.keys())}")

    # Calculate cost
    cost_per_square_foot = pricing[roofing_type]
    total_cost = area * cost_per_square_foot

    return total_cost


def main():
    """
    Main function to interact with the user and calculate roofing costs.
    """
    print("Welcome to King Roofing's Cost Calculator!")
    print("Available roofing types: asphalt, metal, tile")

    try:
        # Get user input
        area = float(input("Enter the area to be covered (in square feet): "))
        roofing_type = input("Enter the type of roofing material: ").strip().lower()

        # Calculate cost
        total_cost = calculate_roofing_cost(area, roofing_type)

        # Display result
        print(f"The total cost for {roofing_type} roofing over {area} square feet is: ${total_cost:.2f}")

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
