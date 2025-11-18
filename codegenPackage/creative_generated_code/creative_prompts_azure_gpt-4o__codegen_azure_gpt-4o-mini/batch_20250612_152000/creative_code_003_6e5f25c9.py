"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: How can Plesk be used to automate the management of DNS records? Write a script demonstrating this functionality.
Generated: DETERMINISTIC_6e5f25c9caec19c8
Batch ID: 20250612_152000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/enterprise/control/agent.php": {
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
import json

# Define the base URL for the Plesk API
BASE_URL = "https://your-plesk-server:8443/enterprise/control/agent.php"

# Replace these with your actual Plesk credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Function to create a session for the Plesk API
def create_session():
    """Create an API session using Basic Authentication."""
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    session.headers.update({'Content-Type': 'application/json'})
    return session

# Function to add a DNS record
def add_dns_record(domain, record_type, record_data):
    """
    Add a DNS record to the specified domain.
    
    :param domain: The domain to which the DNS record will be added
    :param record_type: The type of DNS record (e.g., A, CNAME)
    :param record_data: The data for the DNS record
    """
    session = create_session()
    
    # Define the API request payload
    payload = {
        "packet": {
            "dns": {
                "add": {
                    "domain": domain,
                    "type": record_type,
                    "host": domain,
                    "data": record_data,
                    "ttl": 3600  # Time to live
                }
            }
        }
    }
    
    try:
        response = session.post(BASE_URL, json=payload, verify=False)
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Successfully added DNS record: {record_type} for {domain} with data {record_data}")
    except requests.exceptions.RequestException as e:
        print(f"Error adding DNS record: {e}")

# Function to delete a DNS record
def delete_dns_record(domain, record_id):
    """
    Delete a DNS record from the specified domain.

    :param domain: The domain where the DNS record will be deleted
    :param record_id: The ID of the DNS record to be deleted
    """
    session = create_session()
    
    # Define the API request payload
    payload = {
        "packet": {
            "dns": {
                "del": {
                    "id": record_id
                }
            }
        }
    }

    try:
        response = session.post(BASE_URL, json=payload, verify=False)
        response.raise_for_status()  # Raise an error for bad responses
        print(f"Successfully deleted DNS record with ID {record_id} from {domain}")
    except requests.exceptions.RequestException as e:
        print(f"Error deleting DNS record: {e}")

# Example usage:
if __name__ == "__main__":
    # Add a new A record for example.com
    add_dns_record("example.com", "A", "192.0.2.1")
    
    # Delete a DNS record with ID 12345 (you need to get this ID first)
    delete_dns_record("example.com", 12345)
```

**Note:**
- Ensure to replace `your_username` and `your_password` with actual Plesk credentials.
- Adjust the `BASE_URL` to match your Plesk server address.
- The `verify=False` parameter is used to ignore SSL certificate warnings; this should be handled appropriately in production environments.
- The record ID for deletion must be obtained by querying existing records through another API call (not implemented here for brevity).
