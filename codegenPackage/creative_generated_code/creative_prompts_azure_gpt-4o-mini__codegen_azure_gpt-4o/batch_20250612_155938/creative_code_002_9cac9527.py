"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Create a configuration example for setting up a secure network infrastructure, including routers and firewalls, based on IMTS's network management services.
Generated: DETERMINISTIC_9cac9527c49e6c8b
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Secure Network Infrastructure Configuration Script
# This script sets up a secure network infrastructure including routers and firewalls
# using IMTS's network management services.

import imts_network_management as imts  # Hypothetical library for IMTS network services
import logging
import sys

# Configure logging for the script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# Define constants for the network configuration
ROUTER_ID = "router-001"
FIREWALL_ID = "firewall-001"
NETWORK_SUBNET = "192.168.1.0/24"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "secure_password"  # Replace with a strong password in production
ALLOWED_PORTS = [22, 80, 443]  # SSH, HTTP, HTTPS

def configure_router(router_id, subnet, username, password):
    """
    Configures the router with basic settings.
    
    :param router_id: Unique identifier for the router.
    :param subnet: Subnet address for the network.
    :param username: Admin username for authentication.
    :param password: Admin password for authentication.
    """
    try:
        logging.info("Configuring router with ID: %s", router_id)
        router = imts.Router(router_id)
        
        # Authenticate with the router
        router.authenticate(username, password)
        
        # Set up the subnet
        router.set_subnet(subnet)
        logging.info("Router configured successfully.")
    
    except imts.NetworkError as e:
        logging.error("Error configuring router: %s", e)
        raise

def configure_firewall(firewall_id, allowed_ports, username, password):
    """
    Configures the firewall with security rules.
    
    :param firewall_id: Unique identifier for the firewall.
    :param allowed_ports: List of ports to allow traffic through.
    :param username: Admin username for authentication.
    :param password: Admin password for authentication.
    """
    try:
        logging.info("Configuring firewall with ID: %s", firewall_id)
        firewall = imts.Firewall(firewall_id)
        
        # Authenticate with the firewall
        firewall.authenticate(username, password)
        
        # Set up security rules
        firewall.block_all_ports()
        for port in allowed_ports:
            firewall.allow_port(port)
        logging.info("Firewall configured successfully.")
    
    except imts.NetworkError as e:
        logging.error("Error configuring firewall: %s", e)
        raise

def main():
    """
    Main function to execute the network infrastructure setup.
    """
    try:
        logging.info("Starting network infrastructure configuration...")
        
        # Configure the router
        configure_router(ROUTER_ID, NETWORK_SUBNET, ADMIN_USERNAME, ADMIN_PASSWORD)
        
        # Configure the firewall
        configure_firewall(FIREWALL_ID, ALLOWED_PORTS, ADMIN_USERNAME, ADMIN_PASSWORD)
        
        logging.info("Network infrastructure setup completed successfully.")
    
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
