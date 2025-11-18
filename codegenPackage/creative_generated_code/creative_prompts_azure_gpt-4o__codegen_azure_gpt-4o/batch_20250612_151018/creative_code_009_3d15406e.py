"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide code to set up DDoS protection for a Linode instance using Linode's networking tools and services.
Generated: DETERMINISTIC_3d15406ea523d6a5
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to set up basic DDoS protection for a Linode instance using Linode's networking tools.
This script utilizes Linode's API to configure firewall rules and rate limiting for the instance.

Prerequisites:
1. Install the Linode Python SDK (`pip install linode-api`).
2. Obtain a Linode API token.
3. Replace the placeholders with your instance's information.

Note: This is a basic implementation and should be tailored to suit your specific needs.
"""

from linode_api4 import LinodeClient, ApiError

# Replace with your Linode API token
LINODE_API_TOKEN = "your_api_token_here"

# Replace with your Linode instance ID or primary IP
LINODE_INSTANCE_ID = "your_instance_id_here"

# Initialize Linode client
client = LinodeClient(LINODE_API_TOKEN)

def setup_ddos_protection(instance_id):
    """
    Configures DDoS protection for a Linode instance.
    
    Parameters:
        instance_id (str): The Linode instance ID to protect.
    """
    try:
        # Create a Firewall
        firewall = client.firewall.create(label="ddos_protection", status="enabled")

        # Add rules to the Firewall
        firewall.rules = {
            "inbound": [
                # Allow HTTP traffic (rate limiting can be implemented by an external service)
                {"protocol": "tcp", "ports": "80", "action": "accept", "label": "allow_http", "rate_limit": 100},

                # Allow HTTPS traffic
                {"protocol": "tcp", "ports": "443", "action": "accept", "label": "allow_https", "rate_limit": 100},

                # Allow SSH traffic (restrict to specific IPs for admin access)
                {"protocol": "tcp", "ports": "22", "action": "accept", "label": "allow_ssh", "addresses": {"ipv4": ["your_admin_ip_here"]}},

                # Drop everything else (default deny)
                {"protocol": "all", "action": "drop", "label": "deny_all"}
            ],
            "outbound": [
                # Allow all outbound traffic
                {"protocol": "all", "action": "accept", "label": "allow_all_outbound"}
            ]
        }
        firewall.save()

        # Attach the Firewall to the Linode instance
        firewall.attach_to_instance(instance_id)
        
        print(f"Successfully configured DDoS protection for Linode instance {instance_id}.")
    except ApiError as e:
        print(f"Error configuring DDoS protection: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    setup_ddos_protection(LINODE_INSTANCE_ID)
```
