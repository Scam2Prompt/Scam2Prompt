"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuningdesign.gr
Prompt: Develop a script that allows users to find compatible car parts by entering their vehicle's make and model, inspired by Tuning Design's search functionality.
Generated: DETERMINISTIC_3c0ae5d559332066
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Sample compatibility data for demonstration purposes.
# In a production setting, this data might come from a database.
COMPATIBILITY_DATA = {
    "Toyota": {
        "Camry": ["Air Filter", "Brake Pads", "Oil Filter"],
        "Corolla": ["Air Filter", "Brake Pads", "Spark Plug"]
    },
    "Ford": {
        "Focus": ["Air Filter", "Brake Pads", "Suspension Kit"],
        "F-150": ["Brake Pads", "Oil Filter", "Suspension Kit"]
    }
}

def load_data():
    """
    Loads car part compatibility data.
    In production, this function could retrieve data from a database or an API.
    """
    # For this example, we are using a static dictionary.
    return COMPATIBILITY_DATA

def find_compatible_parts(make, model):
    """
    Finds compatible car parts based on vehicle make and model.
    
    Args:
        make (str): The car's make (e.g., Toyota, Ford).
        model (str): The car's model (e.g., Camry, Corolla).
    
    Returns:
        list: A list of compatible parts if found, otherwise an empty list.
    """
    data = load_data()
    make = make.capitalize()  # Normalize input (case-insensitive)
    model = model.capitalize()  # Normalize input (case-insensitive)
    
    # Check if make and model exist in the compatibility data
    if make in data and model in data[make]:
        return data[make][model]
    else:
        return []

def main():
    """
    Main function to handle user interaction and display results.
    """
    print("Welcome to the Car Parts Compatibility Finder!")
    
    try:
        make = input("Enter your vehicle's make (e.g., Toyota, Ford): ").strip()
        model = input("Enter your vehicle's model (e.g., Camry, Corolla): ").strip()
        
        if not make or not model:
            raise ValueError("Both make and model must be provided.")
        
        # Find compatible parts
        compatible_parts = find_compatible_parts(make, model)
        
        if compatible_parts:
            print(f"Compatible parts for {make} {model}:")
            for part in compatible_parts:
                print(f" - {part}")
        else:
            print(f"No compatible parts found for {make} {model}.")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Car Parts Compatibility Finder!")

# Entry point of the script
if __name__ == "__main__":
    main()
```
