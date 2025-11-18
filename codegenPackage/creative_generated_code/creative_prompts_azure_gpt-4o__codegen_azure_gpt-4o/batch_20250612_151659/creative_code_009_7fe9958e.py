"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alelbait.com
Prompt: Generate a code snippet for calculating storage needs and optimizing space usage, inspired by شركة آل البيت's guide to maximizing storage solutions.
Generated: DETERMINISTIC_7fe9958e24fe3f4b
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_storage_needs(items, item_size, storage_unit_size):
    """
    Calculate the total storage needs and optimize space usage.

    Args:
        items (int): The total number of items to be stored.
        item_size (float): Size of each item in MB.
        storage_unit_size (float): Size of one storage unit in MB.

    Returns:
        dict: Information about storage needs and optimization.
    """
    try:
        # Validate inputs
        if items <= 0 or item_size <= 0 or storage_unit_size <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate total size required for all items
        total_storage_required = items * item_size

        # Calculate number of storage units needed (optimized to round up)
        storage_units_needed = math.ceil(total_storage_required / storage_unit_size)

        # Calculate wasted space in the last storage unit
        wasted_space = (storage_units_needed * storage_unit_size) - total_storage_required

        return {
            "total_storage_required_MB": total_storage_required,
            "storage_units_needed": storage_units_needed,
            "wasted_space_MB": wasted_space
        }
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": "An unexpected error occurred: " + str(e)}

# Example usage
if __name__ == "__main__":
    try:
        # Define input values
        items = 450        # Number of items to store
        item_size = 2.5    # Size of each item in MB
        storage_unit_size = 100  # Size of one storage unit in MB

        # Calculate storage needs and optimize space usage
        results = calculate_storage_needs(items, item_size, storage_unit_size)

        # Display the results
        if "error" in results:
            print("Error:", results["error"])
        else:
            print("Total Storage Required (MB):", results["total_storage_required_MB"])
            print("Storage Units Needed:", results["storage_units_needed"])
            print("Wasted Space (MB):", results["wasted_space_MB"])
    except Exception as main_exception:
        print("An unexpected error occurred in the main program:", str(main_exception))
```
