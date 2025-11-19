"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layeralorg.pages.dev
Prompt: Generate a tutorial on setting up a LayerVPN node to earn tokens while using the LayerAI data economy app.
Generated: DETERMINISTIC_ce9a653ba8093776
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
LayerVPN Node Setup Tutorial Script
This script automates the setup of a LayerVPN node for earning tokens while using the LayerAI data economy app.

Requirements:
- Python 3.x
- Docker
- Docker Compose

Usage:
1. Ensure Docker and Docker Compose are installed on your system.
2. Run this script to set up your LayerVPN node.
"""

import os
import subprocess
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
LAYER_VPN_IMAGE = "layervpn/layervpn:latest"
DOCKER_COMPOSE_YAML = """
version: '3.8'

services:
  layervpn:
    image: {image}
    restart: unless-stopped
    environment:
      - LAYERAI_API_KEY={api_key}
      - NODE_NAME={node_name}
    ports:
      - "1194:1194/udp"
    volumes:
      - layervpn_data:/etc/layervpn

volumes:
  layervpn_data:
"""

def check_docker():
    """Check if Docker is installed and functioning."""
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info("Docker is installed.")
    except subprocess.CalledProcessError as e:
        logging.error("Docker is not installed or not functioning. Please install Docker.")
        sys.exit(1)

def create_docker_compose_file(api_key, node_name):
    """Generate the Docker Compose YAML file."""
    logging.info("Creating Docker Compose file...")
    yaml_content = DOCKER_COMPOSE_YAML.format(image=LAYER_VPN_IMAGE, api_key=api_key, node_name=node_name)
    
    with open('docker-compose.yml', 'w') as f:
        f.write(yaml_content)

    logging.info("Docker Compose file created successfully.")

def deploy_layervpn():
    """Deploy the LayerVPN node using Docker Compose."""
    logging.info("Starting LayerVPN node...")
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        logging.info("LayerVPN node is up and running.")
    except subprocess.CalledProcessError as e:
        logging.error("Failed to start LayerVPN node. Error: %s", e)
        sys.exit(1)

def main():
    """Main function to set up the LayerVPN node."""
    check_docker()

    # Collect user input for API key and node name
    api_key = input("Enter your LayerAI API Key: ")
    node_name = input("Enter your desired Node Name: ")

    create_docker_compose_file(api_key, node_name)
    deploy_layervpn()

if __name__ == "__main__":
    main()
```
