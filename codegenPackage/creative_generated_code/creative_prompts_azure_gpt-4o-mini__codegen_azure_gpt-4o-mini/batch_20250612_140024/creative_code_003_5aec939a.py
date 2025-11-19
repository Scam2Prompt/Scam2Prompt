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
import json

# Define a class to represent an iPhone model
class iPhoneModel:
    def __init__(self, model_name, features):
        """
        Initializes an iPhone model with a name and a list of features.
        
        :param model_name: str - The name of the iPhone model.
        :param features: list - A list of unique features for the iPhone model.
        """
        self.model_name = model_name
        self.features = features

    def to_dict(self):
        """
        Converts the iPhone model to a dictionary format for easy serialization.
        
        :return: dict - A dictionary representation of the iPhone model.
        """
        return {
            'model_name': self.model_name,
            'features': self.features
        }

def create_iphone_models():
    """
    Creates a list of iPhone models with their unique features.
    
    :return: list - A list of iPhoneModel instances.
    """
    return [
        iPhoneModel("iPhone 12", ["Rounded corners", "MagSafe accessories", "Ceramic Shield"]),
        iPhoneModel("iPhone 13", ["Improved battery life", "Cinematic mode", "MagSafe accessories"]),
        iPhoneModel("iPhone 14", ["Emergency SOS via satellite", "A15 Bionic chip", "MagSafe accessories"]),
        iPhoneModel("iPhone SE (3rd generation)", ["Compact design", "A15 Bionic chip", "5G capable"]),
        iPhoneModel("iPhone 15", ["USB-C port", "Dynamic Island", "MagSafe accessories"]),
    ]

def list_iphone_models(models):
    """
    Lists all iPhone models and their features.
    
    :param models: list - A list of iPhoneModel instances.
    """
    for model in models:
        print(f"Model: {model.model_name}")
        print("Features:")
        for feature in model.features:
            print(f" - {feature}")
        print()  # Print a newline for better readability

def main():
    """
    Main function to execute the script.
    It creates iPhone models and lists them with their features.
    """
    try:
        iphone_models = create_iphone_models()
        list_iphone_models(iphone_models)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
