"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Generate a function to parse and log `tlsExportedAuthenticator` values (`clientHandshake` and `serverHandshake`) from a network security dataset, referencing netsecurity.pages.dev.
Generated: DETERMINISTIC_3d47d65c147f04a8
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import Dict, Any

# Configure logging to output to the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_tls_exported_authenticator(data: str) -> Dict[str, Any]:
    """
    Parses the TLS Exported Authenticator values from a network security dataset.

    Args:
        data (str): A JSON string containing the network security dataset.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed 'clientHandshake' and 'serverHandshake' values.

    Raises:
        ValueError: If the input data is not a valid JSON string.
        KeyError: If the expected keys are not found in the parsed JSON.
    """
    try:
        # Parse the input JSON string
        dataset = json.loads(data)
    except json.JSONDecodeError as e:
        logging.error("Invalid JSON data: %s", e)
        raise ValueError("Input data is not a valid JSON string.") from e

    # Initialize an empty dictionary to hold the results
    tls_authenticators = {}

    try:
        # Extract clientHandshake and serverHandshake from the dataset
        tls_authenticators['clientHandshake'] = dataset['tlsExportedAuthenticator']['clientHandshake']
        tls_authenticators['serverHandshake'] = dataset['tlsExportedAuthenticator']['serverHandshake']
    except KeyError as e:
        logging.error("Missing expected key in data: %s", e)
        raise KeyError("Expected key not found in the dataset.") from e

    # Log the extracted values for debugging purposes
    logging.info("Parsed TLS Exported Authenticators: %s", tls_authenticators)

    return tls_authenticators

# Example usage
if __name__ == "__main__":
    example_data = '''
    {
        "tlsExportedAuthenticator": {
            "clientHandshake": "sampleClientAuthenticator",
            "serverHandshake": "sampleServerAuthenticator"
        }
    }
    '''

    try:
        result = parse_tls_exported_authenticator(example_data)
        print(result)
    except (ValueError, KeyError) as e:
        logging.error("Error parsing TLS exported authenticators: %s", e)
```
