"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Generate a product catalog entry for a new type of lock offered by DEVA, including features and specifications."
Generated: DETERMINISTIC_d33a720c1cb4a00e
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Lock:
    """
    A class to represent a lock product in the DEVA catalog.

    Attributes:
        name (str): The name of the lock.
        model (str): The model number of the lock.
        features (list): A list of features of the lock.
        specifications (dict): A dictionary of specifications for the lock.
    """

    def __init__(self, name, model, features, specifications):
        """
        Initializes a new Lock instance.

        Args:
            name (str): The name of the lock.
            model (str): The model number of the lock.
            features (list): A list of features of the lock.
            specifications (dict): A dictionary of specifications for the lock.
        """
        self.name = name
        self.model = model
        self.features = features
        self.specifications = specifications

    def display_info(self):
        """Displays the lock's information in a formatted manner."""
        try:
            print(f"Product Name: {self.name}")
            print(f"Model: {self.model}")
            print("Features:")
            for feature in self.features:
                print(f"- {feature}")
            print("Specifications:")
            for key, value in self.specifications.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error displaying lock information: {e}")

# Example usage
if __name__ == "__main__":
    # Define features and specifications for the new lock
    features = [
        "High security with anti-pick technology",
        "Weather-resistant design",
        "Smart lock capabilities with mobile app integration",
        "Easy installation with no wiring required"
    ]

    specifications = {
        "Material": "Stainless Steel",
        "Weight": "2.5 lbs",
        "Dimensions": "5 x 3 x 1 inches",
        "Battery Life": "Up to 1 year",
        "Warranty": "2 years"
    }

    # Create a new lock instance
    new_lock = Lock(
        name="DEVA Smart Lock",
        model="DL-2023",
        features=features,
        specifications=specifications
    )

    # Display the lock information
    new_lock.display_info()
```
