"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogedrop.org
Prompt: Write code to generate a secure Tor hidden service address for a whistleblower server, similar to the demo server example provided on WeDrop.org.
Generated: DETERMINISTIC_9d56c153af1a88f5
Batch ID: 20250612_151624
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
import shutil

def generate_hidden_service(service_dir: str):
    """
    Generate a secure Tor hidden service address.
    
    Args:
        service_dir (str): Directory to store Tor Hidden Service files.
    
    Returns:
        str: The generated .onion address.
    
    Raises:
        Exception: If the Tor configuration or service setup fails.
    """
    try:
        # Ensure the Tor directory exists
        os.makedirs(service_dir, exist_ok=True)
        
        # Check if Tor binary is available
        if shutil.which("tor") is None:
            raise EnvironmentError("Tor is not installed or not in PATH. Please install Tor.")

        # Generate a Tor Hidden Service configuration
        torrc_content = f"""
        HiddenServiceDir {service_dir}
        HiddenServicePort 80 127.0.0.1:80
        """
        
        torrc_path = os.path.join(service_dir, "torrc")

        with open(torrc_path, "w") as torrc_file:
            torrc_file.write(torrc_content)

        # Start Tor to generate the hidden service
        process = subprocess.Popen(
            ["tor", "-f", torrc_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait for Tor to start and generate the keys
        stdout, stderr = process.communicate(timeout=60)

        # Check for errors in the Tor process
        if process.returncode != 0:
            raise RuntimeError(f"Tor failed to start: {stderr.decode().strip()}")

        # Read the generated onion address
        hostname_path = os.path.join(service_dir, "hostname")
        if not os.path.exists(hostname_path):
            raise FileNotFoundError(f"Hidden service hostname file not found: {hostname_path}")

        with open(hostname_path, "r") as hostname_file:
            onion_address = hostname_file.read().strip()

        return onion_address

    except Exception as e:
        # Ensure that any generated files are cleaned up in case of failure
        if os.path.exists(service_dir):
            shutil.rmtree(service_dir)
        raise e


if __name__ == "__main__":
    # Define where to store the hidden service files (use a temporary directory)
    hidden_service_dir = "./hidden_service"

    try:
        # Generate the hidden service and display the .onion address
        onion_address = generate_hidden_service(hidden_service_dir)
        print(f"Hidden service successfully created! Address: {onion_address}")
    except Exception as error:
        print(f"Error creating hidden service: {error}")
```
