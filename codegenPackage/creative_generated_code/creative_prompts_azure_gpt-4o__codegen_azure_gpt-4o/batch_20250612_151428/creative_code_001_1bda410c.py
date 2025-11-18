"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xmr.cz
Prompt: Generate code to set up a Monero node over TOR using the address `xfwshvp4mrn34a77yxw3wiksnwsra52uoaco7jcrypkjcc7l67fg4gid.onion:18081`.
Generated: DETERMINISTIC_1bda410c429f989e
Batch ID: 20250612_151428
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

def setup_monero_node_tor(monero_data_dir, tor_proxy_address):
    """
    Sets up a Monero node to run over TOR using the provided onion address.

    Args:
        monero_data_dir (str): Path to the Monero data directory.
        tor_proxy_address (str): TOR proxy onion address and port (e.g., <address>:<port>).
    """
    try:
        # Validate the TOR proxy address format
        if not tor_proxy_address.endswith('.onion') or ':' not in tor_proxy_address:
            raise ValueError("Invalid TOR address format. Expected '<address>.onion:<port>'.")

        # Check if monerod binary exists in PATH
        monerod_path = shutil.which('monerod')
        if not monerod_path:
            raise FileNotFoundError("monerod binary not found. Ensure Monero is installed and added to PATH.")

        # Build the monerod command
        command = [
            monerod_path,
            '--data-dir', monero_data_dir,  # Path to store blockchain data
            '--proxy', tor_proxy_address,  # Use TOR proxy for communication
            '--anonymous-inbound', f'{tor_proxy_address},127.0.0.1:18083',  # Enable anonymous inbound connections
            '--log-level', '1'  # Set log level (default: 1 for info)
        ]

        print(f"Starting Monero node with command: {' '.join(command)}")

        # Start the Monero node
        subprocess.run(command, check=True)
        print("Monero node is running over TOR.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("Failed to start Monero node. Check logs for more details.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # TOR onion proxy address
    tor_address = "xfwshvp4mrn34a77yxw3wiksnwsra52uoaco7jcrypkjcc7l67fg4gid.onion:18081"
    
    # Monero data directory
    data_directory = os.path.expanduser("~/monero_data")

    # Create data directory if it doesn't exist
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    # Setup Monero node over TOR
    setup_monero_node_tor(data_directory, tor_address)
```

In order to use this script:
1. Ensure Monero `monerod` binary is installed and available in your system's PATH.
2. Install Python (>=3.6) and required dependencies.
3. Run the script. It will start the Monero node using the specified TOR proxy address.
