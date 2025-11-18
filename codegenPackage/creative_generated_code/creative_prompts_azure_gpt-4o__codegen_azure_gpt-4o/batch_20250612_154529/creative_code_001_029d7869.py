"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Create a function that parses the JSON response from an Arweave node and extracts the `current` block hash and `height` values.
Generated: DETERMINISTIC_029d7869c7643992
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def parse_arweave_response(response_json):
    """
    Parses the JSON response from an Arweave node and extracts the `current` block hash and `height` values.

    Args:
        response_json (str): A JSON string returned from the Arweave node.

    Returns:
        dict: A dictionary containing the `current` block hash and `height` values.
              Example: {'current': 'block_hash_value', 'height': 12345}

    Raises:
        ValueError: If the input is not valid JSON or if the required keys are missing.
    """
    try:
        # Parse the JSON string into a Python dictionary
        response_data = json.loads(response_json)
        
        # Ensure the required keys are present in the parsed JSON
        if 'current' not in response_data or 'height' not in response_data:
            raise ValueError("Missing required keys: 'current' and/or 'height' in the response JSON.")
        
        # Extract the values for `current` and `height`
        current_block = response_data['current']
        block_height = response_data['height']
        
        # Return the extracted values as a dictionary
        return {'current': current_block, 'height': block_height}
    
    except json.JSONDecodeError as e:
        # Handle invalid JSON format
        raise ValueError(f"Invalid JSON format: {e}")
    except Exception as e:
        # Catch any other exceptions and re-raise them with context
        raise ValueError(f"An error occurred while parsing the response: {e}")
```

This code is ready for production use and adheres to best practices for Python development.
