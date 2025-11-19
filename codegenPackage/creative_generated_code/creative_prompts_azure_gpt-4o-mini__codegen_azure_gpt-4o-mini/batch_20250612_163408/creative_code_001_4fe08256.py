"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3338--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a tutorial on how to set up a dedicated CPU instance on Linode for CPU-intensive applications, including code snippets for API calls.
Generated: DETERMINISTIC_4fe082567a4daf90
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.linode.com/v4/": {
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

# Constants for Linode API access
API_TOKEN = 'YOUR_API_TOKEN'  # Replace with your Linode API token
API_URL = 'https://api.linode.com/v4/'

# Function to set up a dedicated CPU instance
def create_dedicated_cpu_instance(label, region='us-east', type='g6-standard-1', image='linode/ubuntu22.04'):
    """
    Create a dedicated CPU Linode instance.

    :param label: The label for your Linode instance.
    :param region: The region to create the instance in. Defaults to 'us-east'.
    :param type: The type of Linode instance to create. Defaults to 'g6-standard-1'.
    :param image: The image to use for the instance. Defaults to 'linode/ubuntu22.04'.
    :return: Response from the API call or error message.
    """
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json',
    }

    # Payload for the API request
    payload = {
        'label': label,
        'region': region,
        'type': type,
        'image': image,
        'specs': {
            'dedicated': True  # Ensure dedicated CPU
        }
    }

    try:
        # Making the API call to create the instance
        response = requests.post(f"{API_URL}linode/instances", headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response if successful
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
        return None
    except Exception as err:
        print(f"An error occurred: {err}")  # Log any other exceptions
        return None

# Main function to execute the instance creation
if __name__ == '__main__':
    instance_label = 'MyDedicatedCPUInstance'  # Label for the new instance
    instance = create_dedicated_cpu_instance(instance_label)
    
    if instance:
        print(f"Instance created successfully: {instance}")
    else:
        print("Failed to create the instance.")
```

**Note:** Replace `'YOUR_API_TOKEN'` with your actual Linode API token before running the code.
