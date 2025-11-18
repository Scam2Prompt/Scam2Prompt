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
import sys
import socket

def generate_hidden_service(service_dir, port=80):
    """
    Generates a secure Tor hidden service address.

    Args:
        service_dir (str): The directory where the hidden service files will be stored.
        port (int): The port on which the hidden service will listen. Default is 80.

    Returns:
        str: The generated .onion address.
    """
    try:
        # Ensure the service directory exists
        os.makedirs(service_dir, exist_ok=True)

        # Write the torrc configuration for the hidden service
        torrc_content = f"""
        HiddenServiceDir {service_dir}
        HiddenServicePort {port} 127.0.0.1:{port}
        """
        
        with open(os.path.join(service_dir, 'torrc'), 'w') as f:
            f.write(torrc_content.strip())

        # Start Tor service (assuming Tor is installed and in the PATH)
        subprocess.run(['tor', '-f', os.path.join(service_dir, 'torrc')], check=True)

        # Give Tor some time to generate the hidden service keys and address
        print("Starting Tor service...")
        # Wait for the address to be generated
        for _ in range(10):
            onion_address_file = os.path.join(service_dir, 'hostname')
            if os.path.exists(onion_address_file):
                with open(onion_address_file, 'r') as f:
                    onion_address = f.read().strip()
                return onion_address
            else:
                print("Waiting for Tor to generate the hidden service address...")
                time.sleep(1)

        raise RuntimeError("Failed to generate the hidden service address within the expected time.")
    
    except subprocess.CalledProcessError as e:
        print(f"Error starting Tor: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    hidden_service_dir = "/path/to/your/hidden_service"  # Change to your desired directory
    port = 80  # Change to your desired port if needed
    
    address = generate_hidden_service(hidden_service_dir, port)
    print(f"Your hidden service address is: {address}")
```

Make sure to replace `"/path/to/your/hidden_service"` with the actual path where you want to store the hidden service files. This script requires that Tor is installed and accessible from the command line. Adjust permissions and ensure that your environment is secure before deploying a whistleblower server.
