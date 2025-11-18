"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Generate a program to calculate the load capacity and lifting height for electric pallet trucks, referencing the specifications of Climax Polska's products.
Generated: DETERMINISTIC_713762c2828ce37d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate load capacity and lifting height for electric pallet trucks
# based on the specifications of Climax Polska's products.

# Import necessary libraries
import sys

def get_pallet_truck_specs():
    """
    Function to provide specifications for Climax Polska's electric pallet trucks.
    Returns:
        Dictionary containing model, load capacity (in kg), and lifting height (in mm).
    """
    return {
        "CP-500": {"load_capacity": 500, "lifting_height": 2000},
        "CP-1000": {"load_capacity": 1000, "lifting_height": 3000},
        "CP-1500": {"load_capacity": 1500, "lifting_height": 3500},
        "CP-2000": {"load_capacity": 2000, "lifting_height": 4000},
    }

def calculate_load_capacity_and_height(model, weight_to_lift):
    """
    Calculate whether the given electric pallet truck model can lift a specified weight
    and determine its maximum lifting height.

    Args:
        model (str): The model of the electric pallet truck.
        weight_to_lift (float): The weight to lift in kg.

    Returns:
        str: Result indicating whether the weight can be lifted and the lifting height.
    """
    # Fetch specifications
    specs = get_pallet_truck_specs()

    # Check if the model exists
    if model not in specs:
        return f"Error: Model {model} not found in specifications."

    # Fetch model specifications
    model_specs = specs[model]

    # Check load capacity
    if weight_to_lift > model_specs["load_capacity"]:
        return f"Error: Weight exceeds the load capacity of {model} ({model_specs['load_capacity']} kg)."

    # Return success message with lifting height
    return f"Success: {model} can lift {weight_to_lift} kg. Maximum lifting height: {model_specs['lifting_height']} mm."

def main():
    """
    Main function to interact with the user and calculate load capacity and lifting height.
    """
    # Print available models for reference
    print("Available electric pallet truck models:")
    specs = get_pallet_truck_specs()
    for model, spec in specs.items():
        print(f"Model: {model}, Load Capacity: {spec['load_capacity']} kg, Lifting Height: {spec['lifting_height']} mm")

    try:
        # Get user input
        model = input("Enter the model of the electric pallet truck: ").strip()
        weight_to_lift = float(input("Enter the weight to lift (in kg): "))

        # Calculate and display result
        result = calculate_load_capacity_and_height(model, weight_to_lift)
        print(result)

    except ValueError:
        print("Error: Invalid input. Weight must be a number.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the program
    main()
```
