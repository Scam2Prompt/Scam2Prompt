"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni-token.com
Prompt: Write a program to simulate the tokenization process for enhancing product portability and transparent traceability, inspired by Unitoken's services.
Generated: DETERMINISTIC_ac3e785f282f1367
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from typing import List, Dict, Any

class TokenizationError(Exception):
    """Custom exception for tokenization errors."""
    pass

class Token:
    """Class to represent a token."""
    
    def __init__(self, product_id: str, token_id: str):
        self.product_id = product_id
        self.token_id = token_id

    def to_dict(self) -> Dict[str, Any]:
        """Convert token to dictionary for JSON serialization."""
        return {
            'product_id': self.product_id,
            'token_id': self.token_id
        }

class TokenizationService:
    """Service to handle tokenization of products."""

    def __init__(self):
        self.tokens: List[Token] = []

    def tokenize_product(self, product_id: str) -> Token:
        """Generate a token for a given product ID.

        Args:
            product_id (str): The ID of the product to be tokenized.

        Returns:
            Token: The generated token for the product.

        Raises:
            TokenizationError: If the tokenization process fails.
        """
        if not product_id:
            raise TokenizationError("Product ID cannot be empty")

        token_id = str(uuid.uuid4())  # Generate a unique token ID
        token = Token(product_id, token_id)
        self.tokens.append(token)  # Store the token
        
        return token

    def get_tokens(self) -> List[Dict[str, Any]]:
        """Get a list of all tokens in a serializable format.

        Returns:
            List[Dict[str, Any]]: A list of tokens represented as dictionaries.
        """
        return [token.to_dict() for token in self.tokens]

def main():
    """Main function to simulate tokenization process."""
    try:
        service = TokenizationService()
        
        # Sample product IDs to tokenize
        product_ids = ["product_1", "product_2", "product_3"]
        
        # Tokenizing products
        for product_id in product_ids:
            token = service.tokenize_product(product_id)
            print(f"Tokenized Product ID {token.product_id} to Token ID {token.token_id}")

        # Output all tokens as JSON
        tokens_json = json.dumps(service.get_tokens(), indent=4)
        print("All Tokens:")
        print(tokens_json)

    except TokenizationError as e:
        print(f"Error during tokenization: {e}")

if __name__ == "__main__":
    main()
```
