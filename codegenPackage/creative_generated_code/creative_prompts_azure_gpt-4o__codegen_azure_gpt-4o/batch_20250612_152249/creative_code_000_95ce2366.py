"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Write code to interact with the Rivalz TESTNET API for registering an rNode and tracking its uptime, storage, and computational resources to calculate $xRIZ emissions.
Generated: DETERMINISTIC_95ce2366cf089ebe
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.testnet.rivalz.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import logging
from typing import Any, Dict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for Rivalz TESTNET API
API_BASE_URL = "https://api.testnet.rivalz.com"
REGISTER_NODE_ENDPOINT = "/v1/rnode/register"
TRACK_RESOURCES_ENDPOINT = "/v1/rnode/resources"
API_KEY = "your-api-key-here"  # Replace with your actual API key

# Error handling classes
class APIError(Exception):
    """Custom exception for API errors."""
    pass

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def register_rnode(rnode_id: str, owner_address: str) -> Dict[str, Any]:
    """
    Register an rNode with Rivalz TESTNET.
    
    Args:
        rnode_id (str): Unique identifier for the rNode.
        owner_address (str): Blockchain address of the rNode owner.
    
    Returns:
        dict: Response data from the API.
    
    Raises:
        APIError: If the API request fails.
        ValidationError: If the input data is invalid.
    """
    # Validate input
    if not rnode_id or not owner_address:
        raise ValidationError("rNode ID and Owner Address are required.")
    
    # Prepare request payload
    payload = {
        "rnode_id": rnode_id,
        "owner_address": owner_address
    }

    # Make the API request
    try:
        response = requests.post(
            API_BASE_URL + REGISTER_NODE_ENDPOINT,
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to register rNode: {e}")
        raise APIError("Error during rNode registration.") from e

def track_resources(rnode_id: str) -> Dict[str, Any]:
    """
    Track uptime, storage, and computational resources of the rNode.
    
    Args:
        rnode_id (str): Unique identifier for the rNode.
    
    Returns:
        dict: Response data from the API containing resource usage and emissions.
    
    Raises:
        APIError: If the API request fails.
        ValidationError: If the input data is invalid.
    """
    # Validate input
    if not rnode_id:
        raise ValidationError("rNode ID is required.")
    
    # Prepare request payload
    payload = {
        "rnode_id": rnode_id
    }

    # Make the API request
    try:
        response = requests.get(
            API_BASE_URL + TRACK_RESOURCES_ENDPOINT,
            params=payload,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to track resources for rNode {rnode_id}: {e}")
        raise APIError("Error during resource tracking.") from e

def main():
    """
    Main function to register an rNode and track its resources periodically.
    """
    try:
        # Example rNode details
        rnode_id = "example-rnode-id"
        owner_address = "0x123456789abcdef"

        # Step 1: Register the rNode
        logging.info("Registering the rNode...")
        registration_response = register_rnode(rnode_id, owner_address)
        logging.info(f"Registration successful: {registration_response}")

        # Step 2: Track resources periodically
        logging.info("Starting resource tracking...")
        while True:
            resource_response = track_resources(rnode_id)
            logging.info(f"Resource tracking data: {resource_response}")
            
            # Wait for a specific interval before tracking again
            time.sleep(3600)  # Example: Track every hour
    except ValidationError as ve:
        logging.error(f"Validation error: {ve}")
    except APIError as ae:
        logging.error(f"API error: {ae}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
