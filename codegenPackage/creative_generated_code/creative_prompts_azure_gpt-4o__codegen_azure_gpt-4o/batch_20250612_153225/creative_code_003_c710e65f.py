"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Provide a Python script to analyze the compatibility of oil seals with Asian, European, and American brand engines, as referenced in the Silver Seals product categories.
Generated: DETERMINISTIC_c710e65fda6b0969
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
oil_seal_compatibility.py

This script analyzes the compatibility of oil seals with Asian, European, 
and American brand engines based on Silver Seals product categories.

Usage:
    Run the script and provide engine brand and oil seal type as input.
"""

import sys

# Define compatibility data for oil seals and engine brands
COMPATIBILITY_MATRIX = {
    "Asian": ["Seal_A", "Seal_B", "Seal_C"],
    "European": ["Seal_B", "Seal_D", "Seal_E"],
    "American": ["Seal_A", "Seal_E", "Seal_F"]
}

def check_compatibility(engine_brand, oil_seal_type):
    """
    Checks if the given oil seal type is compatible with the specified engine brand.

    :param engine_brand: (str) Engine brand ("Asian", "European", "American")
    :param oil_seal_type: (str) Oil seal type (e.g., "Seal_A", "Seal_B", etc.)
    :return: (bool) True if compatible, False otherwise
    """
    if engine_brand not in COMPATIBILITY_MATRIX:
        raise ValueError(f"Invalid engine brand! Supported brands: {list(COMPATIBILITY_MATRIX.keys())}")

    return oil_seal_type in COMPATIBILITY_MATRIX[engine_brand]

def main():
    """
    Main function for handling user input and displaying compatibility results.
    """
    try:
        # User input for engine brand and oil seal type
        engine_brand = input("Enter the engine brand (Asian/European/American): ").strip()
        oil_seal_type = input("Enter the oil seal type (e.g., Seal_A, Seal_B): ").strip()

        # Validate and check compatibility
        is_compatible = check_compatibility(engine_brand, oil_seal_type)

        if is_compatible:
            print(f"The oil seal '{oil_seal_type}' is compatible with '{engine_brand}' engines.")
        else:
            print(f"The oil seal '{oil_seal_type}' is NOT compatible with '{engine_brand}' engines.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Compatibility check completed.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
