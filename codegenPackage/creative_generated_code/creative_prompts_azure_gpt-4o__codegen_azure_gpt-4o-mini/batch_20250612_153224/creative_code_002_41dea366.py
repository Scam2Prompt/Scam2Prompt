"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Generate code for setting up a network with structured cabling, including configuring routers and switches for optimal performance, as outlined in the cable installation services provided by Space Technologies Bogotá.
Generated: DETERMINISTIC_41dea366f5f3f5bf
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import paramiko
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NetworkConfigurator:
    def __init__(self, hostname, username, password):
        """
        Initializes the NetworkConfigurator with device credentials.

        :param hostname: IP address or hostname of the network device
        :param username: Username for SSH authentication
        :param password: Password for SSH authentication
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        """Establish an SSH connection to the network device."""
        try:
            self.ssh_client.connect(self.hostname, username=self.username, password=self.password)
            logging.info(f"Connected to {self.hostname}")
        except paramiko.SSHException as e:
            logging.error(f"Failed to connect to {self.hostname}: {e}")
            raise

    def configure_router(self, interface, ip_address, subnet_mask):
        """
        Configures the router's interface with the specified IP address and subnet mask.

        :param interface: The interface to configure, e.g., 'GigabitEthernet0/1'
        :param ip_address: The IP address to assign to the interface
        :param subnet_mask: The subnet mask to assign
        """
        command = f"interface {interface}\n ip address {ip_address} {subnet_mask}\n no shutdown\n"
        self.execute_command(command)

    def configure_switch(self, vlan_id, vlan_name):
        """
        Configures a VLAN on the switch.

        :param vlan_id: The VLAN ID to configure
        :param vlan_name: The name of the VLAN
        """
        command = f"vlan {vlan_id}\n name {vlan_name}\n"
        self.execute_command(command)

    def execute_command(self, command):
        """Executes a command on the connected device."""
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            stdout_output = stdout.read().decode()
            stderr_output = stderr.read().decode()

            if stderr_output:
                logging.error(f"Error executing command: {stderr_output}")
                raise Exception(stderr_output)

            logging.info(f"Command executed successfully: {stdout_output}")

        except Exception as e:
            logging.error(f"Failed to execute command: {e}")
            raise

    def disconnect(self):
        """Disconnects from the network device."""
        self.ssh_client.close()
        logging.info(f"Disconnected from {self.hostname}")


# Example usage of the NetworkConfigurator class
if __name__ == "__main__":
    # Replace with actual device credentials and configurations
    router_host = '192.168.1.1'
    switch_host = '192.168.1.2'
    username = 'admin'
    password = 'password'

    try:
        # Configure the router
        router = NetworkConfigurator(router_host, username, password)
        router.connect()
        router.configure_router('GigabitEthernet0/1', '192.168.1.10', '255.255.255.0')
        router.disconnect()

        # Configure the switch
        switch = NetworkConfigurator(switch_host, username, password)
        switch.connect()
        switch.configure_switch(10, 'Sales VLAN')
        switch.disconnect()

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
