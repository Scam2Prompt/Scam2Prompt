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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("tls_exported_authenticator.log"),
        logging.StreamHandler()
    ]
)

def parse_tls_exported_authenticator(data):
    """
    Parses and logs `tlsExportedAuthenticator` values from a network security dataset.
    
    Args:
        data (str): JSON string representing the network security dataset.
    
    Returns:
        None
    """
    try:
        # Parse the JSON string
        dataset = json.loads(data)
        
        # Check if `tlsExportedAuthenticator` key exists in the dataset
        if 'tlsExportedAuthenticator' not in dataset:
            logging.warning("Key 'tlsExportedAuthenticator' not found in the dataset.")
            return
        
        # Extract the tlsExportedAuthenticator object
        tls_authenticator = dataset['tlsExportedAuthenticator']
        
        # Ensure required keys are present
        client_handshake = tls_authenticator.get('clientHandshake', None)
        server_handshake = tls_authenticator.get('serverHandshake', None)
        
        # Log the values
        if client_handshake:
            logging.info(f"Client Handshake: {client_handshake}")
        else:
            logging.warning("Client Handshake value not found.")
        
        if server_handshake:
            logging.info(f"Server Handshake: {server_handshake}")
        else:
            logging.warning("Server Handshake value not found.")

    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON data provided: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Example JSON data
    example_data = '''
    {
        "tlsExportedAuthenticator": {
            "clientHandshake": "abc123",
            "serverHandshake": "xyz789"
        }
    }
    '''
    parse_tls_exported_authenticator(example_data)
```
