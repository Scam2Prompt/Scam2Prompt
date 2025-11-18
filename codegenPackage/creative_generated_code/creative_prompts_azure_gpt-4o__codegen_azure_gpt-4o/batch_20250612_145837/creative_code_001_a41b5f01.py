"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sorncluern.com
Prompt: Provide an example of how to log in to a server and configure the LEMP installation using the BitLaunch platform.
Generated: DETERMINISTIC_a41b5f018032890c
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bitlaunch_client
import time

# Constants
API_KEY = "your_bitlaunch_api_key"  # Replace with your actual BitLaunch API key
SERVER_PLAN = "g2.2gb"  # Example server plan
IMAGE_ID = "ubuntu-20.04"  # Example image ID for Ubuntu 20.04
SSH_KEY_NAME = "my_ssh_key"  # Name of the SSH key stored in BitLaunch
SERVER_HOSTNAME = "lemp-server"  # Hostname for the new server

def main():
    try:
        # Initialize BitLaunch client
        bitlaunch = bitlaunch_client.BitLaunch(api_key=API_KEY)

        # List available images for verification
        images = bitlaunch.get_images()
        if IMAGE_ID not in images:
            raise ValueError("Invalid image ID. Verify available images.")

        # List plans for verification
        plans = bitlaunch.get_plans()
        if SERVER_PLAN not in plans:
            raise ValueError("Invalid server plan. Verify available plans.")

        # Verify SSH key exists
        ssh_keys = bitlaunch.get_ssh_keys()
        if SSH_KEY_NAME not in ssh_keys:
            raise ValueError("SSH key not found. Verify SSH keys in BitLaunch account.")

        # Create a new server
        server = bitlaunch.create_server(
            plan=SERVER_PLAN,
            image=IMAGE_ID,
            ssh_key=SSH_KEY_NAME,
            hostname=SERVER_HOSTNAME
        )
        print(f"Server created. ID: {server['id']}")

        # Wait for the server to become active
        print("Waiting for the server to become active...")
        while True:
            server_status = bitlaunch.get_server_status(server_id=server["id"])
            if server_status == "active":
                print("Server is active.")
                break
            elif server_status == "error":
                raise RuntimeError("Failed to activate server.")
            time.sleep(5)

        # Get server details
        server_details = bitlaunch.get_server_details(server_id=server["id"])
        print("Server details:")
        print(f"IP Address: {server_details['ip_address']}")
        print(f"Username: {server_details['username']}")
        print(f"Password: {server_details['password']}")

        # Install LEMP stack on the server
        print("Installing LEMP stack...")
        ssh_client = bitlaunch.get_ssh_client(
            ip_address=server_details['ip_address'],
            username=server_details['username'],
            password=server_details['password']
        )
        ssh_client.execute_command("sudo apt update && sudo apt upgrade -y")
        ssh_client.execute_command("sudo apt install nginx -y")
        ssh_client.execute_command("sudo apt install mysql-server -y")
        ssh_client.execute_command("sudo apt install php-fpm php-mysql -y")
        print("LEMP stack installed successfully.")

        # Close SSH connection
        ssh_client.close()
        print("SSH connection closed.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
