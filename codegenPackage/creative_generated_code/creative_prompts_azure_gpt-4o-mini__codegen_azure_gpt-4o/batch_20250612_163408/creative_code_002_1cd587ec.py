"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Create a DevOps automation tool using OpenStack, drawing on Andrew Mandula's experience in applied networking and systems administration.
Generated: DETERMINISTIC_1cd587ec639b7bbe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
DevOps Automation Tool: OpenStack Resource Manager
This script automates the provisioning, management, and monitoring of OpenStack resources.
Author: Inspired by Andrew Mandula's applied networking and systems administration expertise.

Requirements:
- OpenStack Python SDK installed
- Appropriate OpenStack authentication credentials in the environmental variables or a configuration file
"""

import openstack
import logging
import sys

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("openstack_devops.log"),  # Log to a file
        logging.StreamHandler(sys.stdout),  # Log to console
    ],
)

def connect_to_openstack():
    """
    Establish a connection to the OpenStack cloud.

    Returns:
        conn (openstack.connection.Connection): Connection object to interact with OpenStack.
    """
    try:
        # Load OpenStack connection from environment variables or config file
        conn = openstack.connect()
        logging.info("Successfully connected to OpenStack.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to OpenStack: {e}")
        sys.exit(1)

def list_servers(conn):
    """
    List all servers in the OpenStack cloud.

    Args:
        conn (openstack.connection.Connection): OpenStack connection object.
    """
    try:
        logging.info("Fetching server list...")
        servers = conn.compute.servers()
        for server in servers:
            logging.info(f"Server: {server.name} - Status: {server.status}")
    except Exception as e:
        logging.error(f"Failed to list servers: {e}")

def create_server(conn, name, image, flavor, network, key_name):
    """
    Create a new server in OpenStack.

    Args:
        conn (openstack.connection.Connection): OpenStack connection object.
        name (str): Name of the server.
        image (str): Image name or ID.
        flavor (str): Flavor name or ID.
        network (str): Network name or ID.
        key_name (str): Key pair name.

    Returns:
        server (openstack.compute.v2.server.Server): Created server object.
    """
    try:
        logging.info(f"Creating server '{name}'...")
        image_obj = conn.compute.find_image(image)
        flavor_obj = conn.compute.find_flavor(flavor)
        network_obj = conn.network.find_network(network)

        if not image_obj or not flavor_obj or not network_obj:
            raise ValueError("Invalid image, flavor, or network specified.")

        server = conn.compute.create_server(
            name=name,
            image_id=image_obj.id,
            flavor_id=flavor_obj.id,
            networks=[{"uuid": network_obj.id}],
            key_name=key_name
        )
        conn.compute.wait_for_server(server)
        logging.info(f"Server '{name}' created successfully.")
        return server
    except Exception as e:
        logging.error(f"Failed to create server '{name}': {e}")
        return None

def delete_server(conn, server_name):
    """
    Delete a server by name.

    Args:
        conn (openstack.connection.Connection): OpenStack connection object.
        server_name (str): Name of the server to delete.
    """
    try:
        logging.info(f"Deleting server '{server_name}'...")
        server = conn.compute.find_server(server_name)
        if not server:
            logging.warning(f"Server '{server_name}' not found.")
            return
        conn.compute.delete_server(server)
        logging.info(f"Server '{server_name}' deleted successfully.")
    except Exception as e:
        logging.error(f"Failed to delete server '{server_name}': {e}")

def main():
    """
    Main function to execute the DevOps automation tasks.
    """
    conn = connect_to_openstack()

    # Example: List all servers
    list_servers(conn)

    # Example: Create a server
    server = create_server(
        conn,
        name="devops-server",
        image="ubuntu-20.04",
        flavor="m1.small",
        network="private-network",
        key_name="default-key"
    )

    # Example: Delete the server
    if server:
        delete_server(conn, server.name)

if __name__ == "__main__":
    main()
```
