"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Generate a list of Hevestherm window models that meet specific energy efficiency standards, and provide a code snippet in Python to filter the list based on user input."
Generated: DETERMINISTIC_71f54abe4e69591b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

# Sample data: List of Hevestherm window models with their energy efficiency ratings
window_models = [
    {"model": "HT-100", "energy_efficiency": 0.85},
    {"model": "HT-200", "energy_efficiency": 0.90},
    {"model": "HT-300", "energy_efficiency": 0.95},
    {"model": "HT-400", "energy_efficiency": 0.80},
    {"model": "HT-500", "energy_efficiency": 0.92},
]

def filter_window_models(models, min_efficiency):
    """
    Filters the list of window models based on the minimum energy efficiency standard.

    Args:
        models (list): List of dictionaries containing window model data.
        min_efficiency (float): Minimum energy efficiency threshold.

    Returns:
        list: Filtered list of window models meeting the energy efficiency standard.
    """
    try:
        # Validate input
        if not isinstance(min_efficiency, (int, float)) or min_efficiency < 0 or min_efficiency > 1:
            raise ValueError("Energy efficiency must be a number between 0 and 1.")

        # Filter models based on energy efficiency
        filtered_models = [model for model in models if model["energy_efficiency"] >= min_efficiency]
        return filtered_models
    except Exception as e:
        print(f"Error: {e}")
        return []

def main():
    """
    Main function to execute the filtering logic based on user input.
    """
    try:
        # Prompt user for minimum energy efficiency standard
        user_input = input("Enter the minimum energy efficiency standard (0 to 1): ")
        min_efficiency = float(user_input)

        # Filter window models
        filtered_models = filter_window_models(window_models, min_efficiency)

        # Display results
        if filtered_models:
            print("Window models meeting the energy efficiency standard:")
            print(json.dumps(filtered_models, indent=4))
        else:
            print("No window models meet the specified energy efficiency standard.")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 1.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
