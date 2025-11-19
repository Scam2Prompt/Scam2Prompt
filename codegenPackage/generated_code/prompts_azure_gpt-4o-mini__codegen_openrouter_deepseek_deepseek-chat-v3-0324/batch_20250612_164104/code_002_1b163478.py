"""
Generated Code Metadata:
========================
Original URL: https://villachandon.com.br
Prompt: Write a Python function that connects to a veterinary service API to retrieve vaccination records for pets.
Generated: DETERMINISTIC_1b163478b2608044
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class VeterinaryAPIError(Exception):
    """Custom exception for veterinary API errors."""
    pass

def get_vaccination_records(
    api_base_url: str,
    api_key: str,
    pet_id: Optional[str] = None,
    owner_id: Optional[str] = None,
    timeout: int = 10
) -> List[Dict]:
    """
    Retrieve vaccination records from a veterinary service API.
    
    Args:
        api_base_url: Base URL of the veterinary API
        api_key: API key for authentication
        pet_id: Optional unique identifier for a specific pet
        owner_id: Optional unique identifier for a pet owner
        timeout: Request timeout in seconds (default: 10)
    
    Returns:
        List of vaccination records as dictionaries
        
    Raises:
        VeterinaryAPIError: If there's an error fetching the records
        ValueError: If neither pet_id nor owner_id is provided
        requests.exceptions.RequestException: For request-related errors
    """
    
    if not pet_id and not owner_id:
        raise ValueError("At least one of pet_id or owner_id must be provided")
    
    endpoint = "vaccination-records"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    params = {}
    
    if pet_id:
        params["pet_id"] = pet_id
    if owner_id:
        params["owner_id"] = owner_id
    
    try:
        response = requests.get(
            f"{api_base_url}/{endpoint}",
            headers=headers,
            params=params,
            timeout=timeout
        )
        response.raise_for_status()
        
        logger.info(
            f"Successfully retrieved vaccination records for pet_id={pet_id} "
            f"owner_id={owner_id}"
        )
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        error_msg = (
            f"HTTP error occurred while fetching vaccination records: {http_err}"
        )
        logger.error(error_msg)
        raise VeterinaryAPIError(error_msg) from http_err
    except requests.exceptions.RequestException as req_err:
        error_msg = (
            f"Request error occurred while fetching vaccination records: {req_err}"
        )
        logger.error(error_msg)
        raise VeterinaryAPIError(error_msg) from req_err
    except (ValueError, KeyError) as parse_err:
        error_msg = f"Error parsing vaccination records: {parse_err}"
        logger.error(error_msg)
        raise VeterinaryAPIError(error_msg) from parse_err
```
