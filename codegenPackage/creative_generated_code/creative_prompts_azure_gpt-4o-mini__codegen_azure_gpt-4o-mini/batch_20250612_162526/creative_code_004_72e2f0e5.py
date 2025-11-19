"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesecoinbase.com
Prompt: Write a script to automate the deployment of a web service on LiteSpeed Web Server.
Generated: DETERMINISTIC_72e2f0e5112fde51
Batch ID: 20250612_162526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_command_output(command):
    """Execute a command and return the output, handling errors appropriately."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{' '.join(command)}' failed with error: {e.stderr.strip()}")
        sys.exit(1)

def create_service_config(service_name, document_root, port):
    """Generate a LiteSpeed web service configuration file."""
    config_content = f"""
    docRoot {document_root}
    vhDomain {service_name}
    vhAliases www.{service_name}
    vhRoot {document_root}
    vhPort {port}
    """
    config_file = f"/usr/local/lsws/conf/{service_name}.conf"
    with open(config_file, 'w') as f:
        f.write(config_content.strip())
    logging.info(f"Configuration file created at {config_file}")

def start_litespeed_service():
    """Start the LiteSpeed web server service."""
    command = ["/usr/local/lsws/bin/lswsctrl", "start"]
    logging.info("Starting LiteSpeed web server...")
    check_command_output(command)
    logging.info("LiteSpeed web server started successfully.")

def deploy_web_service(service_name, document_root, port):
    """Deploy a web service on LiteSpeed Web Server."""
    logging.info(f"Deploying web service '{service_name}'...")
    create_service_config(service_name, document_root, port)
    
    # Here you would include steps to copy files to the document root, e.g.:
    # os.makedirs(document_root, exist_ok=True)
    # shutil.copy('path/to/source/files/*', document_root)

    start_litespeed_service()
    logging.info(f"Web service '{service_name}' deployed successfully.")

if __name__ == "__main__":
    # Example usage: python deploy_service.py myservice /var/www/myservice 8080
    if len(sys.argv) != 4:
        logging.error("Usage: python deploy_service.py <service_name> <document_root> <port>")
        sys.exit(1)

    service_name = sys.argv[1]
    document_root = sys.argv[2]
    port = sys.argv[3]

    # Validate port number
    if not port.isdigit() or not (1024 <= int(port) <= 65535):
        logging.error("Port must be a number between 1024 and 65535.")
        sys.exit(1)

    deploy_web_service(service_name, document_root, port)
```
