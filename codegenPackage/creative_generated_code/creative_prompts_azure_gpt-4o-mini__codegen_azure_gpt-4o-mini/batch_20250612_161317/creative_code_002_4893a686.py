"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mrspongy.com
Prompt: What are the steps to set up a root domain record using the Cloudflare Dashboard?
Generated: DETERMINISTIC_4893a686c4039656
Batch ID: 20250612_161317
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cloudflare.com/client/v4": {
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

class CloudflareAPI:
    def __init__(self, api_token, account_id):
        """
        Initialize the Cloudflare API client.

        :param api_token: Your Cloudflare API token
        :param account_id: Your Cloudflare account ID
        """
        self.api_token = api_token
        self.account_id = account_id
        self.base_url = "https://api.cloudflare.com/client/v4"

    def add_root_domain_record(self, zone_id, record_name, record_type, record_content, ttl=3600, proxied=False):
        """
        Add a root domain record to the specified zone.

        :param zone_id: The ID of the zone to which the record will be added
        :param record_name: The name of the record (e.g., "example.com")
        :param record_type: The type of record (e.g., "A", "CNAME")
        :param record_content: The content for the record (e.g., "192.0.2.1")
        :param ttl: Time to live for the record (default is 3600 seconds)
        :param proxied: Boolean indicating if the record is proxied through Cloudflare
        :return: Response JSON if successful, otherwise raises an error
        """
        url = f"{self.base_url}/zones/{zone_id}/dns_records"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
        data = {
            "type": record_type,
            "name": record_name,
            "content": record_content,
            "ttl": ttl,
            "proxied": proxied
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()  # Return the JSON response if the request is successful
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

# Example usage (make sure to replace with valid values):
if __name__ == "__main__":
    # Replace with your actual Cloudflare API token and account ID
    api_token = "YOUR_API_TOKEN"
    account_id = "YOUR_ACCOUNT_ID"
    zone_id = "YOUR_ZONE_ID"  # The ID of the zone to modify
    record_name = "example.com"  # The root domain name to add
    record_type = "A"  # The type of record
    record_content = "192.0.2.1"  # The IP address or content of the record

    # Initialize Cloudflare API client
    cloudflare_api = CloudflareAPI(api_token, account_id)

    # Add the root domain record
    try:
        result = cloudflare_api.add_root_domain_record(zone_id, record_name, record_type, record_content)
        print("Record added successfully:", result)
    except Exception as e:
        print("Failed to add record:", e)
```

This code snippet demonstrates how to set up a root domain record using the Cloudflare API within a Python application. Adjust the parameters accordingly to fit your specific use case.
