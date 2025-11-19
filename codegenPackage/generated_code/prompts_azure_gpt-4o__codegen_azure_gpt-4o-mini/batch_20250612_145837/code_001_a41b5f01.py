"""
Generated Code Metadata:
========================
Original URL: https://sorncluern.com
Prompt: Provide an example of how to log in to a server and configure the LEMP installation using the BitLaunch platform.
Generated: DETERMINISTIC_a41b5f018032890c
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import paramiko
import time

class LEMPInstaller:
    def __init__(self, hostname, username, password):
        """
        Initialize the LEMPInstaller with server credentials.

        :param hostname: The server's hostname or IP address.
        :param username: The username for SSH login.
        :param password: The password for SSH login.
        """
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        """
        Establish an SSH connection to the server.
        """
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname, username=self.username, password=self.password)
            print("Successfully connected to the server.")
        except paramiko.SSHException as e:
            print(f"Failed to connect to the server: {e}")
            raise

    def install_lemp(self):
        """
        Install LEMP stack (Linux, Nginx, MySQL, PHP) on the server.
        """
        try:
            commands = [
                "sudo apt update",
                "sudo apt install -y nginx",
                "sudo apt install -y mysql-server",
                "sudo mysql_secure_installation",
                "sudo apt install -y php-fpm php-mysql",
                "sudo systemctl start nginx",
                "sudo systemctl enable nginx",
                "sudo systemctl start mysql",
                "sudo systemctl enable mysql"
            ]

            for command in commands:
                stdin, stdout, stderr = self.client.exec_command(command)
                time.sleep(1)  # Wait for command to execute
                print(stdout.read().decode())
                error = stderr.read().decode()
                if error:
                    print(f"Error executing command '{command}': {error}")

            print("LEMP stack installation completed successfully.")
        except Exception as e:
            print(f"An error occurred during LEMP installation: {e}")
            raise

    def close_connection(self):
        """
        Close the SSH connection to the server.
        """
        if self.client:
            self.client.close()
            print("SSH connection closed.")

if __name__ == "__main__":
    # Replace with your server details
    HOSTNAME = "your_server_ip"
    USERNAME = "your_username"
    PASSWORD = "your_password"

    lemp_installer = LEMPInstaller(HOSTNAME, USERNAME, PASSWORD)

    try:
        lemp_installer.connect()
        lemp_installer.install_lemp()
    finally:
        lemp_installer.close_connection()
```
