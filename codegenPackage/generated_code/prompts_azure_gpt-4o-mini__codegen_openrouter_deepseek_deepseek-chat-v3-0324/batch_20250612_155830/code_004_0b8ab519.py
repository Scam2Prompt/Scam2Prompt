"""
Generated Code Metadata:
========================
Original URL: https://segroegg.gitbook.io
Prompt: Generate a sample API call to retrieve statistics on the number of GPUs registered with Aethir.
Generated: DETERMINISTIC_0b8ab5196ce93ada
Batch ID: 20250612_155830
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aethir.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Any

# Configuration
API_BASE_URL = "https://api.aethir.com/v1"
API_ENDPOINT = "/gpu/statistics"
API_KEY = "your_api_key_here"  # Replace with your actual API key

def get_gpu_statistics() -> Dict[str, Any]:
    """
    Retrieve GPU statistics from Aethir API.
    
    Returns:
        Dict[str, Any]: Dictionary containing the response data from the API.
    
    Raises:
        requests.exceptions.RequestException: If the API request fails.
        ValueError: If the API response is invalid or cannot be parsed.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(
            f"{API_BASE_URL}{API_ENDPOINT}",
            headers=headers
        )
        response.raise_for_status()  # Raises HTTPError for bad responses
        
        # Parse JSON response
        data = response.json()
        
        # Validate response structure
        if not isinstance(data, dict):
            raise ValueError("Invalid API response format")
            
        return data
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse API response: {str(e)}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"API request failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        stats = get_gpu_statistics()
        print("GPU Statistics:")
        print(json.dumps(stats, indent=2))
    except Exception as e:
        print(f"Error retrieving GPU statistics: {str(e)}")
```
