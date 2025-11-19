"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hnalkhedmad.com
Prompt: Create a Python script that lists the iPhone models along with their unique features, such as rounded corners and MagSafe accessories.
Generated: DETERMINISTIC_5aec939ae95f22c8
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
iphone_models.py

This script lists various iPhone models along with their unique features.
It demonstrates clean and efficient coding practices. The script is well-documented
and includes error handling for potential issues. The data is stored in a structured
format for easy extension and querying.
"""

# Import necessary libraries
import json

def list_iphone_models():
    """
    Generates a list of iPhone models and their unique features.
    Returns:
        list: A list of dictionaries containing iPhone models and features.
    """
    try:
        # Data structure containing iPhone models and their unique features
        iphone_data = [
            {
                "model": "iPhone 12",
                "features": ["MagSafe accessories", "Super Retina XDR display", "Ceramic Shield front"],
            },
            {
                "model": "iPhone 13",
                "features": ["Improved battery life", "Smaller notch", "Cinematic mode"],
            },
            {
                "model": "iPhone 14",
                "features": ["Emergency SOS via satellite", "Crash Detection", "Always-on display"],
            },
            {
                "model": "iPhone SE (3rd Gen)",
                "features": ["Compact design", "A15 Bionic chip", "Touch ID"],
            },
        ]
        
        return iphone_data

    except Exception as e:
        # Error handling: Log the error and return an empty list
        print(f"An error occurred while generating iPhone models: {e}")
        return []

def display_iphone_models(models):
    """
    Displays the list of iPhone models and their features in a readable format.

    Args:
        models (list): A list of dictionaries containing iPhone models and features.
    """
    if not models:
        print("No iPhone models to display.")
        return

    print("iPhone Models and Their Unique Features:")
    print("-" * 40)
    for model in models:
        print(f"Model: {model['model']}")
        print("Features:")
        for feature in model['features']:
            print(f"  - {feature}")
        print("-" * 40)

def save_models_to_json_file(models, filename="iphone_models.json"):
    """
    Saves the iPhone models and their features to a JSON file.

    Args:
        models (list): A list of dictionaries containing iPhone models and features.
        filename (str): The name of the JSON file to save the data into.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(models, file, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        # Error handling: Log the error
        print(f"An error occurred while saving data to JSON file: {e}")

def main():
    """
    The main function to execute the script. It lists the iPhone models,
    displays them, and saves the data to a JSON file.
    """
    # Generate iPhone models and features
    iphone_models = list_iphone_models()

    # Display iPhone models to the user
    display_iphone_models(iphone_models)

    # Save models to a JSON file
    save_models_to_json_file(iphone_models)

if __name__ == "__main__":
    # Entry point of the script
    main()
```
