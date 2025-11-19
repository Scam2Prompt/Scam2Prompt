"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: "Write a Python script to calculate the cost of stainless steel materials for a custom machinery project, considering factors like material type, quantity, and fabrication process."
Generated: DETERMINISTIC_03aecad4e292159b
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_material_cost(material_type, quantity, fabrication_process):
    """
    Calculate the cost of stainless steel materials based on type, quantity, and fabrication process.

    Args:
        material_type (str): Type of stainless steel (e.g., "304", "316").
        quantity (float): Quantity of material in kilograms.
        fabrication_process (str): Fabrication process (e.g., "cutting", "welding", "polishing").

    Returns:
        float: Total cost of the materials and fabrication process.
    """
    # Base cost per kilogram for different stainless steel types
    material_cost_per_kg = {
        "304": 5.0,  # Example cost per kg for type 304
        "316": 7.0   # Example cost per kg for type 316
    }

    # Additional cost per kilogram for different fabrication processes
    fabrication_cost_per_kg = {
        "cutting": 2.0,   # Example cost per kg for cutting
        "welding": 3.5,   # Example cost per kg for welding
        "polishing": 1.5  # Example cost per kg for polishing
    }

    # Validate material type
    if material_type not in material_cost_per_kg:
        raise ValueError(f"Invalid material type: {material_type}. Supported types are: {', '.join(material_cost_per_kg.keys())}")

    # Validate fabrication process
    if fabrication_process not in fabrication_cost_per_kg:
        raise ValueError(f"Invalid fabrication process: {fabrication_process}. Supported processes are: {', '.join(fabrication_cost_per_kg.keys())}")

    # Calculate total cost
    material_cost = material_cost_per_kg[material_type] * quantity
    fabrication_cost = fabrication_cost_per_kg[fabrication_process] * quantity
    total_cost = material_cost + fabrication_cost

    return total_cost


def main():
    """
    Main function to interact with the user and calculate the cost of stainless steel materials.
    """
    try:
        # Get user input
        material_type = input("Enter the material type (e.g., '304', '316'): ").strip()
        quantity = float(input("Enter the quantity in kilograms: ").strip())
        fabrication_process = input("Enter the fabrication process (e.g., 'cutting', 'welding', 'polishing'): ").strip()

        # Calculate cost
        total_cost = calculate_material_cost(material_type, quantity, fabrication_process)

        # Display the result
        print(f"The total cost for {quantity} kg of {material_type} stainless steel with {fabrication_process} is: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
