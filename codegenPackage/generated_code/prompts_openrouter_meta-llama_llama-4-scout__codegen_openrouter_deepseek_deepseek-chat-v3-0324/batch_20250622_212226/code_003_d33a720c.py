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
class ProductCatalogEntry:
    """
    Represents a product catalog entry for a lock product.
    """
    
    def __init__(self, product_id: str, name: str, description: str, 
                 features: list, specifications: dict, price: float):
        """
        Initialize a product catalog entry.
        
        Args:
            product_id (str): Unique product identifier
            name (str): Product name
            description (str): Product description
            features (list): List of product features
            specifications (dict): Dictionary of product specifications
            price (float): Product price
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.features = features
        self.specifications = specifications
        self.price = price
        
    def to_dict(self) -> dict:
        """
        Convert the product entry to a dictionary.
        
        Returns:
            dict: Dictionary representation of the product entry
        """
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'features': self.features,
            'specifications': self.specifications,
            'price': self.price
        }
        
    def __str__(self) -> str:
        """
        String representation of the product entry.
        
        Returns:
            str: Formatted string with product information
        """
        features_str = "\n- ".join(self.features)
        specs_str = "\n".join(f"{k}: {v}" for k, v in self.specifications.items())
        
        return f"""
        DEVA Lock Product: {self.name}
        Product ID: {self.product_id}
        Description: {self.description}
        Price: ${self.price:.2f}
        
        Features:
        - {features_str}
        
        Specifications:
        {specs_str}
        """


def create_deva_lock_entry():
    """
    Create a catalog entry for DEVA's new lock product.
    
    Returns:
        ProductCatalogEntry: The created product entry
    """
    product_id = "DL-2023-X1"
    name = "DEVA X1 Smart Lock"
    description = "Next-generation smart lock with biometric authentication and remote access"
    price = 249.99
    
    features = [
        "Biometric fingerprint recognition",
        "Bluetooth and WiFi connectivity",
        "Remote access via mobile app",
        "Auto-locking feature",
        "Tamper alarm system",
        "Weather-resistant design",
        "Battery backup"
    ]
    
    specifications = {
        "Material": "Grade 304 stainless steel",
        "Dimensions": "3.5 x 2.2 x 6.0 inches",
        "Weight": "1.8 lbs",
        "Power Source": "4 AA batteries (included) + emergency USB-C port",
        "Battery Life": "12 months (typical usage)",
        "Compatibility": "Works with iOS and Android",
        "Security Rating": "ANSI Grade 1",
        "Warranty": "3 years limited"
    }
    
    return ProductCatalogEntry(
        product_id=product_id,
        name=name,
        description=description,
        features=features,
        specifications=specifications,
        price=price
    )


# Example usage
if __name__ == "__main__":
    try:
        lock_entry = create_deva_lock_entry()
        print(lock_entry)
        print("\nDictionary representation:")
        print(lock_entry.to_dict())
    except Exception as e:
        print(f"Error creating product entry: {str(e)}")
```
