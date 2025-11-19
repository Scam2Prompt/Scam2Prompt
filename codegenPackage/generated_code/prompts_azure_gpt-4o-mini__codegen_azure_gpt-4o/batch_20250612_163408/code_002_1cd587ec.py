"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Create a DevOps automation tool using OpenStack, drawing on Andrew Mandula's experience in applied networking and systems administration.
Generated: DETERMINISTIC_1cd587ec639b7bbe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DevOps Automation Tool for OpenStack
Author: Inspired by Andrew Mandula's experience in applied networking and systems administration
Description: This script automates common OpenStack tasks such as instance creation, network setup, and resource management.
"""

import openstack
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("openstack_automation.log")
    ]
)

def connect_to_openstack():
    """
    Establish a connection to the OpenStack cloud.
    Returns:
        openstack.connection.Connection: An authenticated OpenStack connection object.
    """
    try:
        logging.info("Connecting to OpenStack...")
        conn = openstack.connect()
        logging.info("Successfully connected to OpenStack.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to OpenStack: {e}")
        sys.exit(1)

def create_network(conn, network_name, subnet_name, cidr):
    """
    Create a network and subnet in OpenStack.
    Args:
        conn (openstack.connection.Connection): OpenStack connection object.
        network_name (str): Name of the network to create.
        subnet_name (str): Name of the subnet to create.
        cidr (str): CIDR block for the subnet.
    Returns:
        dict: Details of the created network and subnet.
    """
    try:
        logging.info(f"Creating network '{network_name}'...")
        network = conn.network.create_network(name=network_name)
        logging.info(f"Network '{network_name}' created successfully.")

        logging.info(f"Creating subnet '{subnet_name}' with CIDR '{cidr}'...")
        subnet = conn.network.create_subnet(
            name=subnet_name,
            network_id=network.id,
            ip_version=4,
            cidr=cidr
        )
        logging.info(f"Subnet '{subnet_name}' created successfully.")
        return {"network": network, "subnet": subnet}
    except Exception as e:
        logging.error(f"Failed to create network or subnet: {e}")
        sys.exit(1)

def create_instance(conn, instance_name, flavor_name, image_name, network_name, key_name):
    """
    Create a virtual machine instance in OpenStack.
    Args:
        conn (openstack.connection.Connection): OpenStack connection object.
        instance_name (str): Name of the instance to create.
        flavor_name (str): Name of the flavor to use.
        image_name (str): Name of the image to use.
        network_name (str): Name of the network to attach the instance to.
        key_name (str): Name of the SSH key pair to use.
    Returns:
        openstack.compute.v2.server.Server: Details of the created instance.
    """
    try:
        logging.info(f"Creating instance '{instance_name}'...")
        flavor = conn.compute.find_flavor(flavor_name)
        image = conn.compute.find_image(image_name)
        network = conn.network.find_network(network_name)
        keypair = conn.compute.find_keypair(key_name)

        if not flavor or not image or not network or not keypair:
            raise ValueError("Invalid flavor, image, network, or key pair specified.")

        instance = conn.compute.create_server(
            name=instance_name,
            flavor_id=flavor.id,
            image_id=image.id,
            networks=[{"uuid": network.id}],
            key_name=keypair.name
        )
        logging.info(f"Instance '{instance_name}' created successfully.")
        return instance
    except Exception as e:
        logging.error(f"Failed to create instance: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the automation tasks.
    """
    # Configuration (replace with your own values)
    NETWORK_NAME = "devops-network"
    SUBNET_NAME = "devops-subnet"
    CIDR = "192.168.1.0/24"
    INSTANCE_NAME = "devops-instance"
    FLAVOR_NAME = "m1.small"
    IMAGE_NAME = "ubuntu-20.04"
    KEY_NAME = "devops-key"

    # Connect to OpenStack
    conn = connect_to_openstack()

    # Create network and subnet
    create_network(conn, NETWORK_NAME, SUBNET_NAME, CIDR)

    # Create instance
    create_instance(conn, INSTANCE_NAME, FLAVOR_NAME, IMAGE_NAME, NETWORK_NAME, KEY_NAME)

if __name__ == "__main__":
    main()
```
