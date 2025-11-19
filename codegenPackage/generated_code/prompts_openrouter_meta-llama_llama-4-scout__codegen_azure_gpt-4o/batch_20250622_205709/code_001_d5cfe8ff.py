"""
Generated Code Metadata:
========================
Original URL: https://www.pekana.pk
Prompt: Write a code snippet to categorize homeopathic products by symptoms, similar to the "Medicine by Symptoms" section on PEKANA.PK.
Generated: DETERMINISTIC_d5cfe8ffc5de74c1
Batch ID: 20250622_205709
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

# Define a class to represent a homeopathic product
class HomeopathicProduct:
    def __init__(self, name, symptoms):
        """
        Initialize a HomeopathicProduct instance.

        :param name: Name of the product (string)
        :param symptoms: List of symptoms the product addresses (list of strings)
        """
        self.name = name
        self.symptoms = symptoms

    def to_dict(self):
        """
        Convert the product instance to a dictionary for serialization.

        :return: Dictionary representation of the product
        """
        return {"name": self.name, "symptoms": self.symptoms}


# Define a function to categorize products by symptoms
def categorize_products_by_symptoms(products):
    """
    Categorize homeopathic products by symptoms.

    :param products: List of HomeopathicProduct instances
    :return: Dictionary where keys are symptoms and values are lists of product names
    """
    categorized = {}
    for product in products:
        for symptom in product.symptoms:
            if symptom not in categorized:
                categorized[symptom] = []
            categorized[symptom].append(product.name)
    return categorized


# Example usage
if __name__ == "__main__":
    try:
        # Create a list of homeopathic products
        products = [
            HomeopathicProduct("Product A", ["Headache", "Fatigue"]),
            HomeopathicProduct("Product B", ["Fatigue", "Stress"]),
            HomeopathicProduct("Product C", ["Stress", "Insomnia"]),
        ]

        # Categorize products by symptoms
        categorized_products = categorize_products_by_symptoms(products)

        # Serialize the categorized data to JSON for display or storage
        categorized_json = json.dumps(categorized_products, indent=4)

        # Print the categorized products
        print("Categorized Products by Symptoms:")
        print(categorized_json)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
