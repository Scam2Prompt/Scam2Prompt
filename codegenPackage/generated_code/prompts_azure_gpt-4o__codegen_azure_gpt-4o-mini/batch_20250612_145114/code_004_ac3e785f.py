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
import json
import uuid
from datetime import datetime

class Token:
    """
    A class to represent a token for product traceability.
    """

    def __init__(self, product_id, owner, metadata=None):
        """
        Initializes a new token instance.

        :param product_id: Unique identifier for the product.
        :param owner: Owner of the product.
        :param metadata: Additional information about the product (optional).
        """
        self.token_id = str(uuid.uuid4())  # Generate a unique token ID
        self.product_id = product_id
        self.owner = owner
        self.metadata = metadata if metadata else {}
        self.created_at = datetime.now()
        self.history = []

    def add_history(self, event):
        """
        Adds an event to the token's history.

        :param event: A dictionary containing event details.
        """
        event['timestamp'] = datetime.now()
        self.history.append(event)

    def to_dict(self):
        """
        Converts the token instance to a dictionary.

        :return: A dictionary representation of the token.
        """
        return {
            'token_id': self.token_id,
            'product_id': self.product_id,
            'owner': self.owner,
            'metadata': self.metadata,
            'created_at': self.created_at.isoformat(),
            'history': self.history
        }

    def to_json(self):
        """
        Converts the token instance to a JSON string.

        :return: A JSON string representation of the token.
        """
        return json.dumps(self.to_dict(), indent=4)


class TokenizationService:
    """
    A service to handle tokenization and traceability of products.
    """

    def __init__(self):
        self.tokens = {}

    def create_token(self, product_id, owner, metadata=None):
        """
        Creates a new token for a product.

        :param product_id: Unique identifier for the product.
        :param owner: Owner of the product.
        :param metadata: Additional information about the product (optional).
        :return: The created token instance.
        """
        if product_id in self.tokens:
            raise ValueError("Token for this product already exists.")
        
        token = Token(product_id, owner, metadata)
        self.tokens[product_id] = token
        return token

    def add_event_to_token(self, product_id, event):
        """
        Adds an event to the token's history.

        :param product_id: Unique identifier for the product.
        :param event: A dictionary containing event details.
        :raises ValueError: If the token does not exist.
        """
        if product_id not in self.tokens:
            raise ValueError("Token for this product does not exist.")
        
        self.tokens[product_id].add_history(event)

    def get_token(self, product_id):
        """
        Retrieves a token by product ID.

        :param product_id: Unique identifier for the product.
        :return: The token instance.
        :raises ValueError: If the token does not exist.
        """
        if product_id not in self.tokens:
            raise ValueError("Token for this product does not exist.")
        
        return self.tokens[product_id]

    def get_token_json(self, product_id):
        """
        Retrieves a token's JSON representation by product ID.

        :param product_id: Unique identifier for the product.
        :return: JSON string representation of the token.
        :raises ValueError: If the token does not exist.
        """
        token = self.get_token(product_id)
        return token.to_json()


# Example usage
if __name__ == "__main__":
    try:
        service = TokenizationService()
        
        # Create a new token
        token = service.create_token("product_123", "owner_abc", {"category": "electronics"})
        print("Token created:\n", token.to_json())
        
        # Add an event to the token
        service.add_event_to_token("product_123", {"event": "shipped", "location": "warehouse_1"})
        
        # Retrieve and print the token's JSON representation
        token_json = service.get_token_json("product_123")
        print("Updated Token:\n", token_json)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
