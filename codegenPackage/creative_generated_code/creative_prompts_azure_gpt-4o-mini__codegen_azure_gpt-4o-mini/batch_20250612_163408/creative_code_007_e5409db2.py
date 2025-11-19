"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a tutorial on setting up backups for a Linode instance using their API.
Generated: DETERMINISTIC_e5409db2b1d895d0
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4": {
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
import time

# Linode API token
API_TOKEN = 'YOUR_API_TOKEN_HERE'  # Replace with your Linode API token
API_URL = 'https://api.linode.com/v4'

# Set headers for API requests
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

def get_linodes():
    """Retrieve a list of Linode instances."""
    response = requests.get(f'{API_URL}/linode/instances', headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error fetching Linodes: {response.status_code}, {response.text}")

    return response.json()['data']

def create_backup(linode_id):
    """Create a backup for a specified Linode instance."""
    backup_payload = {
        "type": "backups"
    }
    response = requests.post(f'{API_URL}/linode/instances/{linode_id}/backups', 
                             headers=headers, json=backup_payload)
    
    if response.status_code != 201:
        raise Exception(f"Error creating backup for Linode {linode_id}: {response.status_code}, {response.text}")

    return response.json()

def backup_linodes(linodes):
    """Backup all Linode instances."""
    for linode in linodes:
        linode_id = linode['id']
        linode_label = linode['label']
        print(f'Creating backup for Linode: {linode_label} (ID: {linode_id})')
        try:
            backup = create_backup(linode_id)
            print(f'Successfully created backup: {backup}')
        except Exception as e:
            print(e)

def main():
    """Main function to initiate backup process."""
    try:
        linodes = get_linodes()
        if not linodes:
            print("No Linode instances found.")
            return

        backup_linodes(linodes)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

**Note**: 
- Replace `YOUR_API_TOKEN_HERE` with your actual Linode API token before running the code.
- Ensure you have the `requests` library installed. You can install it using `pip install requests`.
