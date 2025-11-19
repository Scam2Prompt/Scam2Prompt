"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavanderiacallezaragoza.com
Prompt: Generate a Python script that automates the process of calculating laundry costs based on the pricing table from Lavandería Autoservicio Zaragoza.
Generated: DETERMINISTIC_82096039101ca5f6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_laundry_cost(clothing_weight, is_drying_needed):
    """
    Calculate the laundry cost based on weight and drying option.

    Pricing Table from Lavandería Autoservicio Zaragoza:
    - Washing: €5 for up to 6 kg, and an additional €0.5 per kg for weight above 6 kg.
    - Drying: €3 flat fee if drying is requested.

    Arguments:
    clothing_weight -- float: Weight of clothes in kilograms.
    is_drying_needed -- bool: Whether drying is needed.

    Returns:
    float: Total laundry cost.
    """
    if clothing_weight <= 0:
        raise ValueError("Clothing weight must be greater than 0 kg.")

    # Base washing cost
    washing_cost = 5

    # If weight exceeds 6 kg, add extra charges
    if clothing_weight > 6:
        washing_cost += (clothing_weight - 6) * 0.5

    # Drying cost if requested
    drying_cost = 3 if is_drying_needed else 0

    # Total cost
    return washing_cost + drying_cost


def main():
    """
    Main function to calculate laundry cost.
    Prompts user for input and displays the total cost.
    """
    try:
        # Prompt user for weight of clothes
        clothing_weight = float(input("Enter the weight of clothes (in kg): "))
        
        # Prompt user for drying option
        drying_choice = input("Do you need drying? (yes/no): ").strip().lower()
        is_drying_needed = drying_choice in ['yes', 'y']

        # Calculate total cost
        total_cost = calculate_laundry_cost(clothing_weight, is_drying_needed)

        # Display result
        print(f"Total laundry cost: €{total_cost:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    # Entry point for the script
    main()
```
