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
# homeopathic_categorizer.py

class HomeopathicProduct:
    """
    Represents a homeopathic product with its details.
    """
    def __init__(self, name, symptoms, manufacturer, potency=None):
        """
        Initialize a homeopathic product.
        
        Args:
            name (str): Name of the product
            symptoms (list): List of symptoms this product addresses
            manufacturer (str): Manufacturer name
            potency (str, optional): Potency of the product. Defaults to None.
        """
        self.name = name
        self.symptoms = symptoms
        self.manufacturer = manufacturer
        self.potency = potency

    def __str__(self):
        return f"{self.name} ({self.manufacturer}) - Symptoms: {', '.join(self.symptoms)}"


class HomeopathicCategorizer:
    """
    Categorizes homeopathic products by symptoms.
    """
    def __init__(self):
        self.products = []
        self.symptom_index = {}

    def add_product(self, product):
        """
        Add a product to the categorizer.
        
        Args:
            product (HomeopathicProduct): Product to add
            
        Raises:
            TypeError: If product is not a HomeopathicProduct instance
        """
        if not isinstance(product, HomeopathicProduct):
            raise TypeError("Only HomeopathicProduct instances can be added")
            
        self.products.append(product)
        
        # Update symptom index
        for symptom in product.symptoms:
            symptom_lower = symptom.lower()
            if symptom_lower not in self.symptom_index:
                self.symptom_index[symptom_lower] = []
            self.symptom_index[symptom_lower].append(product)

    def get_products_by_symptom(self, symptom):
        """
        Get all products that address a specific symptom.
        
        Args:
            symptom (str): Symptom to search for
            
        Returns:
            list: List of HomeopathicProduct objects matching the symptom
        """
        symptom_lower = symptom.lower()
        return self.symptom_index.get(symptom_lower, [])

    def get_all_symptoms(self):
        """
        Get all unique symptoms in the categorizer.
        
        Returns:
            set: Set of all unique symptoms
        """
        return set(self.symptom_index.keys())

    def get_products_by_multiple_symptoms(self, symptoms):
        """
        Get products that address all specified symptoms.
        
        Args:
            symptoms (list): List of symptoms to match
            
        Returns:
            list: List of HomeopathicProduct objects matching all symptoms
        """
        if not symptoms:
            return []
            
        symptom_set = set(s.lower() for s in symptoms)
        matching_products = []
        
        for product in self.products:
            product_symptoms = set(s.lower() for s in product.symptoms)
            if symptom_set.issubset(product_symptoms):
                matching_products.append(product)
                
        return matching_products


# Example usage
if __name__ == "__main__":
    # Create some sample products
    product1 = HomeopathicProduct(
        "Arnica Montana",
        ["Bruises", "Muscle pain", "Swelling"],
        "Pekana",
        "30C"
    )
    
    product2 = HomeopathicProduct(
        "Belladonna",
        ["Fever", "Inflammation", "Headache"],
        "Pekana",
        "200C"
    )
    
    product3 = HomeopathicProduct(
        "Nux Vomica",
        ["Indigestion", "Headache", "Constipation"],
        "Pekana",
        "6X"
    )
    
    # Create categorizer and add products
    categorizer = HomeopathicCategorizer()
    categorizer.add_product(product1)
    categorizer.add_product(product2)
    categorizer.add_product(product3)
    
    # Example queries
    print("Products for headache:")
    for product in categorizer.get_products_by_symptom("headache"):
        print(f"- {product}")
    
    print("\nProducts for both headache and fever:")
    for product in categorizer.get_products_by_multiple_symptoms(["headache", "fever"]):
        print(f"- {product}")
    
    print("\nAll available symptoms:")
    for symptom in sorted(categorizer.get_all_symptoms()):
        print(f"- {symptom}")
```
