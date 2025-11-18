"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythorg.com
Prompt: Write a Python function to validate and parse market data from Pythorg's price feed oracles for use in Ethereum smart contracts.
Generated: DETERMINISTIC_df2f42a2bc29b57b
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

def validate_and_parse_pythorg_data(data: str) -> dict:
    """
    Validates and parses market data from Pythorg's price feed oracles.
    
    Args:
        data (str): JSON string containing market data from Pythorg's price feed.
        
    Returns:
        dict: Parsed and validated market data.
        
    Raises:
        ValueError: If the input data is not valid JSON or fails validation criteria.
    """
    try:
        # Attempt to parse the JSON string into a Python dictionary
        parsed_data = json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode JSON data: {e}")
    
    # Required keys for market data
    required_keys = {"symbol", "price", "timestamp", "confidence"}
    
    # Ensure all required keys are present in the parsed data
    if not required_keys.issubset(parsed_data.keys()):
        raise ValueError(f"Missing required keys in market data. Expected keys: {required_keys}")
    
    # Validate each field for expected data types and ranges
    if not isinstance(parsed_data["symbol"], str) or len(parsed_data["symbol"]) == 0:
        raise ValueError("Invalid 'symbol' value. Must be a non-empty string.")
    
    if not isinstance(parsed_data["price"], (int, float)) or parsed_data["price"] <= 0:
        raise ValueError("Invalid 'price' value. Must be a positive number.")
    
    if not isinstance(parsed_data["timestamp"], int) or parsed_data["timestamp"] <= 0:
        raise ValueError("Invalid 'timestamp' value. Must be a positive integer representing Unix time.")
    
    if not isinstance(parsed_data["confidence"], (int, float)) or parsed_data["confidence"] < 0:
        raise ValueError("Invalid 'confidence' value. Must be a non-negative number.")
    
    # Additional checks can be added here based on specific business logic
    
    # Return the validated and parsed market data
    return {
        "symbol": parsed_data["symbol"],
        "price": float(parsed_data["price"]),
        "timestamp": int(parsed_data["timestamp"]),
        "confidence": float(parsed_data["confidence"]),
    }

# Example usage:
# try:
#     market_data = validate_and_parse_pythorg_data('{"symbol": "ETH", "price": 2000.5, "timestamp": 1697046345, "confidence": 0.02}')
#     print(market_data)
# except ValueError as e:
#     print(f"Error: {e}")
```
