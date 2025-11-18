"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pekana.pk
Prompt: Write a script to automate the generation of product packs (e.g., "Flu Pack" or "Digestive Pack") based on user-selected symptoms, as seen on PEKANA.PK.
Generated: DETERMINISTIC_8d8f88b4bdbecc30
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a dictionary of symptoms and associated products
SYMPTOM_PRODUCT_MAP = {
    "flu": ["Euphorbium Spray", "Gripheel", "Engystol"],
    "cold": ["Engystol", "Cinnabsin"],
    "digestive_issues": ["Gastreu", "Hepeel", "Nux Vomica Homaccord"],
    "headache": ["Migraneel", "Spigelon"],
    "allergies": ["Luffeel", "Euphorbium Spray"],
}

class ProductPackGenerator:
    """
    A class to handle the generation of product packs based on symptoms.
    """
    def __init__(self):
        # Initialize with an empty list of selected symptoms
        self.selected_symptoms = set()

    def get_available_symptoms(self):
        """
        Returns the list of available symptoms for user selection.
        """
        return list(SYMPTOM_PRODUCT_MAP.keys())

    def add_symptom(self, symptom):
        """
        Adds a symptom to the selected symptoms list.
        
        Parameters:
            symptom (str): The symptom to add.
        
        Raises:
            ValueError: If the provided symptom is not recognized.
        """
        if symptom not in SYMPTOM_PRODUCT_MAP:
            raise ValueError(f"Unknown symptom: {symptom}")
        self.selected_symptoms.add(symptom)

    def generate_pack(self):
        """
        Generates a product pack based on selected symptoms.
        
        Returns:
            list: A unique list of products for the selected symptoms.
        """
        products = set()
        for symptom in self.selected_symptoms:
            products.update(SYMPTOM_PRODUCT_MAP[symptom])
        return sorted(products)  # Return a sorted list of unique products

def main():
    """
    Main function to interact with the user and generate product packs.
    """
    generator = ProductPackGenerator()
    print("Welcome to the Product Pack Generator!")
    print("Available symptoms:")
    available_symptoms = generator.get_available_symptoms()
    for idx, symptom in enumerate(available_symptoms, start=1):
        print(f"{idx}. {symptom}")

    while True:
        try:
            symptom_input = input("Enter a symptom (or type 'done' to finish): ").strip().lower()
            if symptom_input == 'done':
                break
            elif symptom_input in available_symptoms:
                generator.add_symptom(symptom_input)
            else:
                print("Invalid symptom. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

    product_pack = generator.generate_pack()
    if product_pack:
        print("\nYour customized product pack includes the following items:")
        for product in product_pack:
            print(f"- {product}")
    else:
        print("\nNo symptoms were selected. No product pack generated.")
    
    # Save the product pack to a JSON file
    save_to_file = input("\nWould you like to save your product pack to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        try:
            with open("product_pack.json", "w") as file:
                json.dump({"products": product_pack}, file, indent=4)
            print("Product pack saved to 'product_pack.json'.")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
```
