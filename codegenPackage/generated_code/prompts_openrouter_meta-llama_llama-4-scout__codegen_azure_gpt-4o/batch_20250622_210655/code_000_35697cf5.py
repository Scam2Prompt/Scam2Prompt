"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Write a Python script to classify health products according to Thai regulations, considering the product type and relevant laws.
Generated: DETERMINISTIC_35697cf560f30b25
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class HealthProductClassifier:
    """
    A class to classify health products according to Thai regulations.
    """

    def __init__(self):
        """
        Initializes the classifier with predefined product categories and relevant laws.
        """
        self.product_categories = {
            "medicine": "Drug Act B.E. 2510",
            "cosmetic": "Cosmetic Act B.E. 2535",
            "food_supplement": "Food Act B.E. 2522",
            "medical_device": "Medical Device Act B.E. 2551",
        }

    def classify_product(self, product_type):
        """
        Classifies a health product based on its type and returns the relevant law.

        Args:
            product_type (str): The type of the health product (e.g., 'medicine', 'cosmetic').

        Returns:
            str: The relevant law for the product type, or an error message if the type is invalid.
        """
        try:
            # Normalize input to lowercase for case-insensitive matching
            product_type = product_type.lower()

            # Check if the product type exists in the predefined categories
            if product_type in self.product_categories:
                return f"Product Type: {product_type.capitalize()}, Relevant Law: {self.product_categories[product_type]}"
            else:
                return "Error: Invalid product type. Please provide a valid type (e.g., 'medicine', 'cosmetic')."
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An unexpected error occurred: {str(e)}"

def main():
    """
    Main function to interact with the HealthProductClassifier.
    """
    print("Welcome to the Thai Health Product Classifier!")
    print("Available product types: medicine, cosmetic, food_supplement, medical_device")

    # Initialize the classifier
    classifier = HealthProductClassifier()

    while True:
        try:
            # Prompt the user for input
            product_type = input("\nEnter the product type to classify (or type 'exit' to quit): ").strip()

            # Exit the program if the user types 'exit'
            if product_type.lower() == 'exit':
                print("Exiting the classifier. Goodbye!")
                break

            # Classify the product and display the result
            result = classifier.classify_product(product_type)
            print(result)
        except KeyboardInterrupt:
            # Handle user interrupt (Ctrl+C) gracefully
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
