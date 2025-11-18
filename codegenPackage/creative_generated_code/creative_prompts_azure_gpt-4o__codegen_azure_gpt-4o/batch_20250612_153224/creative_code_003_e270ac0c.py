"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Create a script to automate the selection of facade system components, such as "کلپیس ابتدایی استیل 1.2 میلی متر رنگی," based on building dimensions and environmental conditions.
Generated: DETERMINISTIC_e270ac0cc3e407ef
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants and facade component options
FAÇADE_COMPONENTS = [
    {
        "name": "کلپیس ابتدایی استیل 1.2 میلی متر رنگی",
        "material": "steel",
        "thickness_mm": 1.2,
        "environment_suitability": ["urban", "coastal"],
        "max_building_height_m": 50,
        "color_options": ["colored"]
    },
    {
        "name": "کلپیس ابتدایی آلومینیوم 1.5 میلی متر خام",
        "material": "aluminum",
        "thickness_mm": 1.5,
        "environment_suitability": ["urban"],
        "max_building_height_m": 30,
        "color_options": ["raw"]
    },
    {
        "name": "کلپیس پیشرفته PVC 2 میلی متر رنگی",
        "material": "PVC",
        "thickness_mm": 2.0,
        "environment_suitability": ["residential"],
        "max_building_height_m": 20,
        "color_options": ["colored"]
    }
]

def select_facade_components(building_height, environment, color_preference):
    """
    Select appropriate facade system components based on building dimensions and environmental conditions.

    Args:
        building_height (float): The height of the building in meters.
        environment (str): The environmental condition (e.g., 'urban', 'coastal', 'residential').
        color_preference (str): Desired color type (e.g., 'colored', 'raw').

    Returns:
        list: A list of selected components matching the criteria.
    """
    try:
        if not isinstance(building_height, (int, float)) or building_height <= 0:
            raise ValueError("Building height must be a positive number.")
        
        if not isinstance(environment, str) or not environment:
            raise ValueError("Environment must be a valid non-empty string.")
        
        if not isinstance(color_preference, str) or not color_preference:
            raise ValueError("Color preference must be a valid non-empty string.")

        # Filter components based on the criteria
        selected_components = [
            component for component in FAÇADE_COMPONENTS
            if building_height <= component["max_building_height_m"]
            and environment in component["environment_suitability"]
            and color_preference in component["color_options"]
        ]
        
        return selected_components

    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    Main function to interact with the user and automate facade component selection.
    """
    print("Welcome to the Façade Component Selector!")
    
    try:
        # Gather user inputs
        building_height = float(input("Enter the building height (in meters): "))
        environment = input("Enter the environmental condition (e.g., 'urban', 'coastal', 'residential'): ").strip().lower()
        color_preference = input("Enter your color preference ('colored' or 'raw'): ").strip().lower()

        # Get selected components
        selected_components = select_facade_components(building_height, environment, color_preference)

        # Display the results
        if selected_components:
            print("\nSelected Façade Components:")
            print(json.dumps(selected_components, indent=4, ensure_ascii=False))
        else:
            print("No suitable components found for the given criteria.")
    
    except ValueError:
        print("Invalid input. Please enter the correct data types.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
