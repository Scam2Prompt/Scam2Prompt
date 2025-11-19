"""
Generated Code Metadata:
========================
Original URL: https://hnalkhedmad.com
Prompt: Create a Python script that lists the iPhone models along with their unique features, such as rounded corners and MagSafe accessories.
Generated: DETERMINISTIC_5aec939ae95f22c8
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to list iPhone models along with their unique features.
This script is designed to be clean, efficient, and production-ready.
"""

# Import necessary modules
import json

def get_iphone_models():
    """
    Returns a dictionary of iPhone models and their unique features.
    """
    return {
        "iPhone 12": [
            "Rounded corners",
            "MagSafe accessories",
            "Super Retina XDR display",
            "5G support"
        ],
        "iPhone 13": [
            "Rounded corners",
            "MagSafe accessories",
            "Improved battery life",
            "A15 Bionic chip"
        ],
        "iPhone 14": [
            "Rounded corners",
            "MagSafe accessories",
            "Emergency SOS via satellite",
            "Crash detection"
        ],
        "iPhone 14 Pro": [
            "Rounded corners",
            "MagSafe accessories",
            "Dynamic Island",
            "Always-On display"
        ]
    }

def display_iphone_models(models):
    """
    Displays iPhone models and their features in a readable format.
    
    Args:
        models (dict): Dictionary containing iPhone models and their features.
    """
    print("List of iPhone Models and Their Unique Features:\n")
    for model, features in models.items():
        print(f"{model}:")
        for feature in features:
            print(f"  - {feature}")
        print()  # Add a blank line for better readability

def save_to_file(models, filename="iphone_models.json"):
    """
    Saves the iPhone models and their features to a JSON file.
    
    Args:
        models (dict): Dictionary containing iPhone models and their features.
        filename (str): Name of the file to save the data. Defaults to 'iphone_models.json'.
    """
    try:
        with open(filename, "w") as file:
            json.dump(models, file, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

def main():
    """
    Main function to execute the script.
    """
    try:
        # Get iPhone models and their features
        iphone_models = get_iphone_models()
        
        # Display the models and features
        display_iphone_models(iphone_models)
        
        # Save the models and features to a file
        save_to_file(iphone_models)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
