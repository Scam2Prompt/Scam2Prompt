"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Write a Python script to generate a quote for a custom cue stick with a Gabon Ebony forearm and 6-point Hoppe style design."
Generated: DETERMINISTIC_a0ab3b9cee2e17cb
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_quote(material, design, length, wrap_type):
    """
    Calculate the quote for a custom cue stick based on material, design, length, and wrap type.

    Args:
        material (str): The material of the forearm (e.g., "Gabon Ebony").
        design (str): The design style (e.g., "6-point Hoppe style").
        length (int): The length of the cue stick in inches.
        wrap_type (str): The type of wrap (e.g., "Irish Linen", "Leather").

    Returns:
        float: The total cost of the custom cue stick.
    """
    # Base prices for materials
    material_prices = {
        "Gabon Ebony": 300.0,
        "Maple": 150.0,
        "Rosewood": 200.0
    }

    # Base prices for designs
    design_prices = {
        "6-point Hoppe style": 250.0,
        "4-point traditional": 200.0,
        "8-point modern": 300.0
    }

    # Wrap type prices
    wrap_prices = {
        "Irish Linen": 50.0,
        "Leather": 100.0,
        "No Wrap": 0.0
    }

    # Validate inputs
    if material not in material_prices:
        raise ValueError(f"Invalid material: {material}. Available options: {', '.join(material_prices.keys())}")
    if design not in design_prices:
        raise ValueError(f"Invalid design: {design}. Available options: {', '.join(design_prices.keys())}")
    if wrap_type not in wrap_prices:
        raise ValueError(f"Invalid wrap type: {wrap_type}. Available options: {', '.join(wrap_prices.keys())}")
    if not (55 <= length <= 60):
        raise ValueError("Invalid length. Cue stick length must be between 55 and 60 inches.")

    # Calculate total cost
    material_cost = material_prices[material]
    design_cost = design_prices[design]
    wrap_cost = wrap_prices[wrap_type]
    base_cost = material_cost + design_cost + wrap_cost

    # Add length adjustment cost (e.g., $10 per inch over 58 inches)
    length_adjustment_cost = max(0, (length - 58) * 10)

    total_cost = base_cost + length_adjustment_cost
    return total_cost


def main():
    """
    Main function to interact with the user and generate a quote for a custom cue stick.
    """
    print("Welcome to the Custom Cue Stick Quote Generator!")
    try:
        # Gather user input
        material = input("Enter the forearm material (e.g., Gabon Ebony): ").strip()
        design = input("Enter the design style (e.g., 6-point Hoppe style): ").strip()
        length = int(input("Enter the cue stick length in inches (55-60): ").strip())
        wrap_type = input("Enter the wrap type (e.g., Irish Linen, Leather, No Wrap): ").strip()

        # Generate quote
        total_cost = calculate_quote(material, design, length, wrap_type)
        print(f"\nThe total cost for your custom cue stick is: ${total_cost:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
