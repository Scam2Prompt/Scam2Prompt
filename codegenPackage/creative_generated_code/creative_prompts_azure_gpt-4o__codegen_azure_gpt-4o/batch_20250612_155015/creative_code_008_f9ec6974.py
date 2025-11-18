"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythsite.com
Prompt: Provide code to validate the integrity of market data retrieved from Pyth price feed oracles in a blockchain application.
Generated: DETERMINISTIC_f9ec6974131c687e
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib

class MarketDataValidator:
    """
    A class to validate the integrity of market data retrieved from Pyth price feed oracles.
    """

    def __init__(self, expected_schema: dict, trusted_hashes: list):
        """
        Initialize the MarketDataValidator.
        
        :param expected_schema: A dictionary defining the expected schema of the market data.
        :param trusted_hashes: A list of trusted SHA256 hashes to validate data integrity.
        """
        self.expected_schema = expected_schema
        self.trusted_hashes = trusted_hashes

    def validate_schema(self, data: dict) -> bool:
        """
        Validate the schema of the market data against the expected schema.
        
        :param data: The market data dictionary.
        :return: True if the schema matches; False otherwise.
        """
        for key, value_type in self.expected_schema.items():
            if key not in data or not isinstance(data[key], value_type):
                return False
        return True

    def validate_integrity(self, data: dict) -> bool:
        """
        Validate the integrity of the market data by checking its hash against trusted hashes.
        
        :param data: The market data dictionary.
        :return: True if the integrity is intact; False otherwise.
        """
        try:
            # Serialize the data into a JSON string
            serialized_data = json.dumps(data, sort_keys=True)
            
            # Compute the SHA256 hash of the serialized data
            data_hash = hashlib.sha256(serialized_data.encode('utf-8')).hexdigest()
            
            # Check if the hash exists in the trusted hashes list
            if data_hash in self.trusted_hashes:
                return True
        except (TypeError, ValueError) as e:
            # Log or handle serialization issues (optional: add logging here)
            print(f"Error during hash validation: {e}")
        
        return False

    def validate_market_data(self, data: dict) -> bool:
        """
        Perform full validation of market data, including schema and integrity checks.
        
        :param data: The market data dictionary.
        :return: True if the data passes all validations; False otherwise.
        """
        # Validate the schema
        if not self.validate_schema(data):
            print("Schema validation failed.")
            return False
        
        # Validate the integrity
        if not self.validate_integrity(data):
            print("Integrity validation failed.")
            return False
        
        # If both validations pass, return True
        return True


# Example Usage:

# Define the expected schema for market data (key: expected value type)
expected_schema = {
    "price": float,
    "timestamp": int,
    "product_id": str,
}

# Define a list of trusted SHA256 hashes (in a real application, retrieve these from a secure source)
trusted_hashes = [
    "abc123def4567890abcdef1234567890abcdef1234567890abcdef1234567890",  # Example hash
    "123456abcdef7890abcdef1234567890abcdef1234567890abcdef1234567890",  # Example hash
]

# Sample market data dictionary
market_data = {
    "price": 123.45,
    "timestamp": 1697020800,
    "product_id": "BTC/USD",
}

# Create an instance of MarketDataValidator
validator = MarketDataValidator(expected_schema, trusted_hashes)

# Validate the market data
if validator.validate_market_data(market_data):
    print("Market data is valid.")
else:
    print("Market data is invalid.")
```
