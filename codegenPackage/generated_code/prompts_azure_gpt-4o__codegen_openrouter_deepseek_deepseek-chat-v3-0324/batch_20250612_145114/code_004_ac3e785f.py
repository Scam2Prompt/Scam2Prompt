"""
Generated Code Metadata:
========================
Original URL: https://uni-token.com
Prompt: Write a program to simulate the tokenization process for enhancing product portability and transparent traceability, inspired by Unitoken's services.
Generated: DETERMINISTIC_ac3e785f282f1367
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class ProductToken:
    """
    Represents a tokenized product with attributes for portability and traceability.
    """
    
    def __init__(self, product_id: str, name: str, description: str, manufacturer: str):
        """
        Initialize a ProductToken with basic product information.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            description: Description of the product.
            manufacturer: Manufacturer of the product.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.manufacturer = manufacturer
        self.token_id = self._generate_token_id()
        self.creation_date = datetime.utcnow().isoformat()
        self.transaction_history: List[Dict] = []
        
    def _generate_token_id(self) -> str:
        """
        Generate a unique token ID using SHA-256 hashing of product attributes.
        
        Returns:
            str: A unique token ID.
        """
        data = f"{self.product_id}{self.name}{self.description}{self.manufacturer}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    def add_transaction(self, transaction_type: str, from_party: str, to_party: str, metadata: Optional[Dict] = None) -> None:
        """
        Add a transaction record to the product's history.
        
        Args:
            transaction_type: Type of transaction (e.g., 'manufacture', 'shipment', 'sale').
            from_party: The party transferring the product.
            to_party: The party receiving the product.
            metadata: Optional additional transaction details.
        """
        transaction = {
            'timestamp': datetime.utcnow().isoformat(),
            'transaction_type': transaction_type,
            'from': from_party,
            'to': to_party,
            'metadata': metadata or {}
        }
        self.transaction_history.append(transaction)
    
    def to_dict(self) -> Dict:
        """
        Convert the ProductToken to a dictionary for serialization.
        
        Returns:
            Dict: Dictionary representation of the ProductToken.
        """
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'manufacturer': self.manufacturer,
            'token_id': self.token_id,
            'creation_date': self.creation_date,
            'transaction_history': self.transaction_history
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ProductToken':
        """
        Create a ProductToken from a dictionary.
        
        Args:
            data: Dictionary containing ProductToken attributes.
            
        Returns:
            ProductToken: A new ProductToken instance.
        """
        product = cls(
            product_id=data['product_id'],
            name=data['name'],
            description=data['description'],
            manufacturer=data['manufacturer']
        )
        product.token_id = data['token_id']
        product.creation_date = data['creation_date']
        product.transaction_history = data['transaction_history']
        return product

class TokenizationService:
    """
    Service for managing product tokenization and traceability.
    """
    
    def __init__(self):
        self.token_registry: Dict[str, ProductToken] = {}
    
    def tokenize_product(self, product_id: str, name: str, description: str, manufacturer: str) -> Tuple[bool, str]:
        """
        Tokenize a new product and add it to the registry.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            description: Description of the product.
            manufacturer: Manufacturer of the product.
            
        Returns:
            Tuple[bool, str]: (success status, message or token ID)
        """
        if product_id in self.token_registry:
            return False, "Product ID already exists in registry"
            
        product_token = ProductToken(product_id, name, description, manufacturer)
        self.token_registry[product_id] = product_token
        return True, product_token.token_id
    
    def get_product_token(self, product_id: str) -> Optional[ProductToken]:
        """
        Retrieve a product token from the registry.
        
        Args:
            product_id: The product ID to look up.
            
        Returns:
            Optional[ProductToken]: The ProductToken if found, else None.
        """
        return self.token_registry.get(product_id)
    
    def record_transaction(self, product_id: str, transaction_type: str, from_party: str, to_party: str, metadata: Optional[Dict] = None) -> bool:
        """
        Record a transaction for a tokenized product.
        
        Args:
            product_id: The product ID involved in the transaction.
            transaction_type: Type of transaction.
            from_party: The party transferring the product.
            to_party: The party receiving the product.
            metadata: Optional additional transaction details.
            
        Returns:
            bool: True if transaction was recorded successfully, False otherwise.
        """
        product_token = self.get_product_token(product_id)
        if not product_token:
            return False
            
        product_token.add_transaction(transaction_type, from_party, to_party, metadata)
        return True
    
    def export_token_data(self, product_id: str) -> Optional[Dict]:
        """
        Export token data for a product as a dictionary.
        
        Args:
            product_id: The product ID to export.
            
        Returns:
            Optional[Dict]: Dictionary of token data if product exists, else None.
        """
        product_token = self.get_product_token(product_id)
        return product_token.to_dict() if product_token else None
    
    def import_token_data(self, data: Dict) -> Tuple[bool, str]:
        """
        Import token data for a product.
        
        Args:
            data: Dictionary containing ProductToken attributes.
            
        Returns:
            Tuple[bool, str]: (success status, message or token ID)
        """
        try:
            product_token = ProductToken.from_dict(data)
            if product_token.product_id in self.token_registry:
                return False, "Product ID already exists in registry"
                
            self.token_registry[product_token.product_id] = product_token
            return True, product_token.token_id
        except KeyError as e:
            return False, f"Invalid token data: missing {str(e)}"
    
    def save_registry_to_file(self, filename: str) -> bool:
        """
        Save the token registry to a JSON file.
        
        Args:
            filename: Path to the output file.
            
        Returns:
            bool: True if save was successful, False otherwise.
        """
        try:
            with open(filename, 'w') as f:
                registry_data = {
                    product_id: product_token.to_dict()
                    for product_id, product_token in self.token_registry.items()
                }
                json.dump(registry_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving registry: {str(e)}")
            return False
    
    def load_registry_from_file(self, filename: str) -> bool:
        """
        Load the token registry from a JSON file.
        
        Args:
            filename: Path to the input file.
            
        Returns:
            bool: True if load was successful, False otherwise.
        """
        try:
            with open(filename, 'r') as f:
                registry_data = json.load(f)
                self.token_registry = {
                    product_id: ProductToken.from_dict(token_data)
                    for product_id, token_data in registry_data.items()
                }
            return True
        except Exception as e:
            print(f"Error loading registry: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    service = TokenizationService()
    
    # Tokenize a new product
    success, token_id = service.tokenize_product(
        "prod123",
        "Premium Coffee",
        "Organic Arabica Beans, 1kg",
        "Green Valley Farms"
    )
    
    if success:
        print(f"Product tokenized successfully. Token ID: {token_id}")
        
        # Record a transaction
        service.record_transaction(
            "prod123",
            "manufacture",
            "Green Valley Farms",
            "Warehouse A",
            {"batch": "B2023-05-01", "quantity": 1000}
        )
        
        # Export token data
        token_data = service.export_token_data("prod123")
        print("Token data:", json.dumps(token_data, indent=2))
        
        # Save registry
        service.save_registry_to_file("token_registry.json")
    else:
        print("Tokenization failed:", token_id)
```
