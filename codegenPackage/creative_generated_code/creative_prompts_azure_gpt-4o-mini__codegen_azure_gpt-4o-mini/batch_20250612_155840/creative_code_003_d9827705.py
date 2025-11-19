"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alvibanda.cl
Prompt: Write a guide on configuring a web server for optimal performance on Alvibanda's hosting services.
Generated: DETERMINISTIC_d98277050581a1f9
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
import subprocess
import logging

# Set up logging for the configuration process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def configure_web_server(server_type, optimize_for='performance'):
    """
    Configures the specified web server for optimal performance.

    Parameters:
    server_type (str): Type of web server to configure (e.g., 'nginx', 'apache').
    optimize_for (str): The optimization goal, default is 'performance'.

    Raises:
    ValueError: If an unsupported server type is provided.
    Exception: If the server configuration fails.
    """

    # Define available server configurations
    server_configs = {
        'nginx': {
            'config_path': '/etc/nginx/nginx.conf',
            'settings': [
                "worker_processes auto;",
                "worker_connections 1024;",
                "keepalive_timeout 65;",
                "gzip on;",
                "gzip_types text/plain application/json application/javascript text/css text/xml;",
            ]
        },
        'apache': {
            'config_path': '/etc/httpd/conf/httpd.conf',
            'settings': [
                "KeepAlive On",
                "MaxKeepAliveRequests 100",
                "KeepAliveTimeout 5",
                "Timeout 300",
                "LimitRequestBody 10485760"
            ]
        }
    }

    # Check if the server type is supported
    if server_type not in server_configs:
        logging.error("Unsupported server type: %s", server_type)
        raise ValueError(f"Unsupported server type: {server_type}")

    try:
        # Fetch the configuration details
        config_details = server_configs[server_type]
        
        # Write optimized settings to the server configuration file
        with open(config_details['config_path'], 'a') as config_file:
            logging.info("Appending optimization settings to %s", config_details['config_path'])
            for setting in config_details['settings']:
                config_file.write(setting + "\n")

        # Restart the web server to apply changes
        if server_type == 'nginx':
            subprocess.run(['systemctl', 'restart', 'nginx'], check=True)
        elif server_type == 'apache':
            subprocess.run(['systemctl', 'restart', 'httpd'], check=True)

        logging.info("Successfully configured and restarted %s server", server_type)

    except Exception as e:
        logging.error("An error occurred while configuring the web server: %s", e)
        raise

# Example usage
if __name__ == "__main__":
    try:
        configure_web_server('nginx')  # Change 'nginx' to 'apache' if configuring Apache server
    except Exception as e:
        logging.critical("Failed to configure web server: %s", e)
```
