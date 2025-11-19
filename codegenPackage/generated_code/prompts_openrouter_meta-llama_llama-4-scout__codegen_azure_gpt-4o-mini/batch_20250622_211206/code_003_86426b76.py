"""
Generated Code Metadata:
========================
Original URL: https://obyssey.xyz
Prompt: How can I use a web server deployment tool to automate the setup and receive a "ready to use" message?
Generated: DETERMINISTIC_86426b76dd5337a6
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import sys

class WebServerDeployment:
    def __init__(self, server_name, port, document_root):
        """
        Initialize the web server deployment configuration.

        :param server_name: The name of the server (e.g., 'localhost').
        :param port: The port on which the server will run (e.g., 80).
        :param document_root: The directory where the web files are located.
        """
        self.server_name = server_name
        self.port = port
        self.document_root = document_root

    def create_server_config(self):
        """
        Create a configuration file for the web server.
        """
        config_content = f"""
        server {{
            listen {self.port};
            server_name {self.server_name};

            location / {{
                root {self.document_root};
                index index.html index.htm;
            }}
        }}
        """
        config_file_path = f"/etc/nginx/sites-available/{self.server_name}"
        
        try:
            with open(config_file_path, 'w') as config_file:
                config_file.write(config_content)
            os.symlink(config_file_path, f"/etc/nginx/sites-enabled/{self.server_name}")
            print(f"Configuration file created at {config_file_path}")
        except Exception as e:
            print(f"Error creating configuration file: {e}")
            sys.exit(1)

    def test_configuration(self):
        """
        Test the web server configuration for syntax errors.
        """
        try:
            result = subprocess.run(['nginx', '-t'], capture_output=True, text=True)
            if result.returncode == 0:
                print("Configuration test successful.")
            else:
                print(f"Configuration test failed: {result.stderr}")
                sys.exit(1)
        except Exception as e:
            print(f"Error testing configuration: {e}")
            sys.exit(1)

    def restart_server(self):
        """
        Restart the web server to apply the new configuration.
        """
        try:
            subprocess.run(['systemctl', 'restart', 'nginx'], check=True)
            print("Web server restarted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error restarting web server: {e}")
            sys.exit(1)

    def deploy(self):
        """
        Deploy the web server with the specified configuration.
        """
        self.create_server_config()
        self.test_configuration()
        self.restart_server()
        print("Web server is ready to use!")

if __name__ == "__main__":
    # Example usage
    server_name = "localhost"
    port = 80
    document_root = "/var/www/html"

    deployment = WebServerDeployment(server_name, port, document_root)
    deployment.deploy()
```
