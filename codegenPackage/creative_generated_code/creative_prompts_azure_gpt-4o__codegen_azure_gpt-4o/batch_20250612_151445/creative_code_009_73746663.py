"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Write a script to calculate fees for asbestos sample preparation and analysis, considering A & B Labs' step rules for overloading and layer-specific charges.
Generated: DETERMINISTIC_737466636139f8b1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# asbestos_fee_calculator.py
# This script calculates fees for asbestos sample preparation and analysis 
# based on A & B Labs' rules for overloading and layer-specific charges.

def calculate_asbestos_fees(num_layers, overloaded=False):
    """
    Calculate the fees for asbestos sample preparation and analysis.

    Parameters:
    - num_layers (int): The number of layers in the sample (must be >= 1).
    - overloaded (bool): Indicates if the sample is overloaded. Default is False.

    Returns:
    - float: The total fee for the sample preparation and analysis.

    Raises:
    - ValueError: If num_layers is less than 1.
    """
    # Constants for fee calculation
    BASE_FEE = 100.00  # Base fee per sample
    LAYER_FEE = 50.00  # Additional fee per layer
    OVERLOAD_FEE = 75.00  # Overloaded sample fee

    # Validate input
    if num_layers < 1:
        raise ValueError("Number of layers must be at least 1.")

    # Calculate layer-specific fees
    layer_fee = (num_layers - 1) * LAYER_FEE  # First layer has no additional fee

    # Calculate overload fee
    overload_fee = OVERLOAD_FEE if overloaded else 0.00

    # Compute total fee
    total_fee = BASE_FEE + layer_fee + overload_fee

    return total_fee


def main():
    """
    Main function to demonstrate the asbestos fee calculator.
    """
    try:
        # Example inputs
        num_layers = int(input("Enter the number of layers in the sample: "))
        overloaded_input = input("Is the sample overloaded? (yes/no): ").strip().lower()

        # Convert overloaded input to boolean
        overloaded = True if overloaded_input == 'yes' else False

        # Calculate fees
        total_fee = calculate_asbestos_fees(num_layers, overloaded)

        # Display the result
        print(f"The total fee for the sample is: ${total_fee:.2f}")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
