"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-bitcoin.org
Prompt: How can I implement a Bitcoin Core full node to enhance the decentralization of Bitcoin transactions?
Generated: DETERMINISTIC_16c772d59942caba
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Bitcoin Core Full Node Setup Script
# This script automates the installation and configuration of a Bitcoin Core full node
# to enhance the decentralization of Bitcoin transactions.

import os
import subprocess
import sys

def install_bitcoin_core():
    """
    Install Bitcoin Core from the official repository.
    This function checks the OS type and installs the appropriate package.
    """
    try:
        if sys.platform.startswith('linux'):
            # For Debian/Ubuntu systems
            print("Detected Linux OS. Installing Bitcoin Core...")
            subprocess.run(["sudo", "add-apt-repository", "ppa:bitcoin/bitcoin"], check=True)
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "bitcoin-qt", "bitcoind"], check=True)
        elif sys.platform == 'darwin':
            # For macOS systems
            print("Detected macOS. Installing Bitcoin Core...")
            subprocess.run(["brew", "tap", "bitcoin/bitcoin"], check=True)
            subprocess.run(["brew", "install", "bitcoin"], check=True)
        else:
            print("Unsupported OS. Please install Bitcoin Core manually.")
            sys.exit(1)

        print("Bitcoin Core installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")
        sys.exit(1)

def configure_bitcoin_core(data_directory):
    """
    Create a configuration file for Bitcoin Core.
    
    Args:
        data_directory (str): The directory where Bitcoin blockchain data will be stored.
    """
    try:
        config_content = f"""
        # Bitcoin Core Configuration File
        server=1
        daemon=1
        txindex=1
        datadir={data_directory}
        """
        
        config_file_path = os.path.join(data_directory, "bitcoin.conf")
        
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)
        
        print(f"Configuration file created at {config_file_path}.")
    except IOError as e:
        print(f"Failed to create configuration file: {e}")
        sys.exit(1)

def start_bitcoin_node():
    """
    Start the Bitcoin Core daemon.
    """
    try:
        print("Starting Bitcoin Core daemon...")
        subprocess.Popen(["bitcoind"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Bitcoin Core daemon started successfully.")
    except Exception as e:
        print(f"Failed to start Bitcoin Core daemon: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Set the data directory for storing blockchain data
    data_directory = os.path.expanduser("~/.bitcoin")
    
    # Create the data directory if it does not exist
    os.makedirs(data_directory, exist_ok=True)

    # Install Bitcoin Core
    install_bitcoin_core()

    # Configure Bitcoin Core
    configure_bitcoin_core(data_directory)

    # Start Bitcoin Core node
    start_bitcoin_node()
```

**Note**: Ensure you have the necessary permissions to execute this script (e.g., it may require sudo privileges for installation). Adjust the script as necessary for your OS and environment.
