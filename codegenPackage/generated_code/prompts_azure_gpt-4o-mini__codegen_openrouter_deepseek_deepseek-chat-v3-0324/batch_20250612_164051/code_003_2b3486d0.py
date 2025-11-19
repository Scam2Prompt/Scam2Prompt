"""
Generated Code Metadata:
========================
Original URL: https://milarbrazw.blogspot.com
Prompt: Develop a script that displays available payment methods for purchasing lighting fixtures, including options for boleto bancário and Mercado Pago.
Generated: DETERMINISTIC_2b3486d0a8ed734a
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class PaymentMethod:
    """Represents a payment method with its attributes."""
    
    def __init__(self, name: str, description: str, requires_document: bool = False):
        """
        Initialize a payment method.
        
        Args:
            name: Name of the payment method.
            description: Description of the payment method.
            requires_document: Whether the method requires a document (e.g., CPF/CNPJ).
        """
        self.name = name
        self.description = description
        self.requires_document = requires_document
    
    def to_dict(self) -> Dict:
        """Convert the payment method to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "requires_document": self.requires_document
        }

class PaymentMethodService:
    """Service to manage and retrieve available payment methods."""
    
    def __init__(self):
        """Initialize the service with default payment methods."""
        self._payment_methods = [
            PaymentMethod(
                "Boleto Bancário",
                "Payment via boleto bancário with 1-2 business days for processing.",
                requires_document=True
            ),
            PaymentMethod(
                "Mercado Pago",
                "Payment via Mercado Pago with instant processing.",
                requires_document=True
            ),
            PaymentMethod(
                "Credit Card",
                "Payment via credit card with instant processing.",
                requires_document=False
            ),
            PaymentMethod(
                "Pix",
                "Payment via Pix with instant processing.",
                requires_document=True
            )
        ]
    
    def get_available_payment_methods(self) -> List[Dict]:
        """
        Retrieve all available payment methods.
        
        Returns:
            List of payment methods as dictionaries.
        """
        return [method.to_dict() for method in self._payment_methods]
    
    def get_payment_method_by_name(self, name: str) -> Dict:
        """
        Retrieve a payment method by its name.
        
        Args:
            name: Name of the payment method to retrieve.
            
        Returns:
            The payment method as a dictionary if found, None otherwise.
            
        Raises:
            ValueError: If the payment method is not found.
        """
        for method in self._payment_methods:
            if method.name.lower() == name.lower():
                return method.to_dict()
        raise ValueError(f"Payment method '{name}' not found.")

def display_payment_methods(payment_methods: List[Dict]) -> None:
    """
    Display the available payment methods in a user-friendly format.
    
    Args:
        payment_methods: List of payment methods to display.
    """
    print("Available Payment Methods:")
    print("-" * 40)
    for method in payment_methods:
        print(f"Name: {method['name']}")
        print(f"Description: {method['description']}")
        print(f"Requires Document: {'Yes' if method['requires_document'] else 'No'}")
        print("-" * 40)

def main():
    """Main function to execute the script."""
    try:
        payment_service = PaymentMethodService()
        payment_methods = payment_service.get_available_payment_methods()
        display_payment_methods(payment_methods)
        
        # Example: Fetch a specific payment method
        print("\nFetching 'Boleto Bancário':")
        boleto = payment_service.get_payment_method_by_name("Boleto Bancário")
        print(json.dumps(boleto, indent=2))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
