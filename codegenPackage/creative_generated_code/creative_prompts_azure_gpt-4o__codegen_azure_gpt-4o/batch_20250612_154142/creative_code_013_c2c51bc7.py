"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segroegg.gitbook.io
Prompt: Generate a script to deploy an Aethir container for cloud rendering tasks, referencing the container setup process described on the website.
Generated: DETERMINISTIC_c2c51bc7b495fcfa
Batch ID: 20250612_154142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys

def deploy_aethir_container(image_name="aethir/cloud-rendering", container_name="aethir_renderer", ports=None):
    """
    Deploys an Aethir container for cloud rendering tasks.

    Parameters:
    - image_name (str): Name of the Docker image to use.
    - container_name (str): Name for the deployed container.
    - ports (dict): Port mapping in the format {host_port: container_port}.
    
    Returns:
    - None
    """
    try:
        # Check if Docker is installed
        print("Checking if Docker is installed...")
        subprocess.run(["docker", "--version"], check=True)

        # Pull the Aethir container image
        print(f"Pulling Docker image: {image_name}...")
        subprocess.run(["docker", "pull", image_name], check=True)

        # Build the port mapping string
        port_args = []
        if ports:
            for host_port, container_port in ports.items():
                port_args.extend(["-p", f"{host_port}:{container_port}"])

        # Run the container
        print(f"Launching Docker container: {container_name}...")
        subprocess.run(
            ["docker", "run", "-d", "--name", container_name, *port_args, image_name],
            check=True
        )

        print(f"Container '{container_name}' deployed successfully!")
    except FileNotFoundError:
        print("Docker is not installed or not in PATH. Please install Docker and try again.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing: {e.cmd}")
        print(f"Return code: {e.returncode}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage: Deploy the container with port mappings
    port_mapping = {8080: 80, 3000: 3000}  # Host Port -> Container Port
    deploy_aethir_container(ports=port_mapping)
```
