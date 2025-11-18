"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolveprocess.com
Prompt: Write code to utilize Resolve.io’s CMDB Auto-Discovery feature for mapping dependencies in a multi-vendor IT environment.
Generated: DETERMINISTIC_5248ee2047602a9f
Batch ID: 20250612_151158
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.resolve.io`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.resolve.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's the requested code. This example assumes `Resolve.io` provides an API or SDK for its CMDB Auto-Discovery feature. Replace placeholders with appropriate values and ensure any required dependencies or libraries are properly installed.

```python
import requests
import json

# Constants
RESOLVE_BASE_URL = "https://api.resolve.io"  # Replace with the actual Resolve.io API base URL
API_KEY = "your_api_key_here"  # Replace with your Resolve.io API key

# Endpoints
AUTO_DISCOVERY_ENDPOINT = f"{RESOLVE_BASE_URL}/cmdb/autodiscovery"

# Error classes
class ResolveAPIError(Exception):
    """Custom exception for Resolve.io API errors."""
    pass

def perform_cmdb_auto_discovery(vendor_name):
    """
    Perform CMDB auto-discovery to map dependencies in a multi-vendor IT environment.

    Args:
        vendor_name (str): The name of the vendor whose dependencies need to be mapped.

    Returns:
        dict: A dictionary containing the auto-discovery results.

    Raises:
        ResolveAPIError: If the API request fails or returns an error response.
    """
    
    # Prepare headers for the API request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Prepare payload for the API request
    payload = {
        "vendor_name": vendor_name  # Replace or extend if additional parameters are required
    }
    
    try:
        # Make POST request to the auto-discovery endpoint
        response = requests.post(AUTO_DISCOVERY_ENDPOINT, headers=headers, json=payload)
        
        # Raise an exception if the response status code is not 200 (OK)
        response.raise_for_status()
        
    except requests.exceptions.RequestException as e:
        # Handle network or HTTP request errors
        raise ResolveAPIError(f"Failed to perform auto-discovery: {e}")

    # Parse the response JSON
    try:
        discovery_results = response.json()
    except json.JSONDecodeError as e:
        raise ResolveAPIError(f"Failed to parse response JSON: {e}")

    # Check for errors in the API response
    if "error" in discovery_results:
        raise ResolveAPIError(f"API returned an error: {discovery_results['error']}")

    # Return the discovery results
    return discovery_results


def main():
    """
    Main function to execute the CMDB auto-discovery process.
    """
    # Example: replace with real vendor names or input
    vendor_name = "example_vendor"

    print(f"Performing CMDB Auto-Discovery for vendor: {vendor_name}...")
    
    try:
        # Perform auto-discovery
        results = perform_cmdb_auto_discovery(vendor_name)
        
        # Print the results in a human-readable format
        # (Use or store the results as needed in your application.)
        print("Auto-Discovery Results:")
        print(json.dumps(results, indent=4))
    
    except ResolveAPIError as e:
        # Handle API errors gracefully
        print(f"Error: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```

### Notes:
- Replace `your_api_key_here` and `https://api.resolve.io` with actual credentials and URL provided by Resolve.io.
- Ensure the required Python libraries (`requests`) are installed (`pip install requests`).
- Vendors and their configurations should be updated dynamically based on your specific environment.
