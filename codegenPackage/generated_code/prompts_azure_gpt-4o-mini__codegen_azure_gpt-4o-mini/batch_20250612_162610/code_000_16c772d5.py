"""
Generated Code Metadata:
========================
Original URL: https://en-bitcoin.org
Prompt: How can I implement a Bitcoin Core full node to enhance the decentralization of Bitcoin transactions?
Generated: DETERMINISTIC_16c772d59942caba
Batch ID: 20250612_162610
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BitcoinNode:
    def __init__(self, data_dir, rpc_user, rpc_password):
        """
        Initialize the BitcoinNode with the specified data directory and RPC credentials.

        :param data_dir: Directory where Bitcoin data will be stored
        :param rpc_user: RPC username for authentication
        :param rpc_password: RPC password for authentication
        """
        self.data_dir = data_dir
        self.rpc_user = rpc_user
        self.rpc_password = rpc_password
        self.process = None

    def start_node(self):
        """
        Start the Bitcoin Core full node process.
        """
        try:
            # Ensure the data directory exists
            os.makedirs(self.data_dir, exist_ok=True)

            # Command to start Bitcoin Core
            command = [
                'bitcoind',
                f'-datadir={self.data_dir}',
                f'-rpcuser={self.rpc_user}',
                f'-rpcpassword={self.rpc_password}',
                '-server',
                '-printtoconsole'
            ]

            # Start the Bitcoin Core process
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            logging.info("Bitcoin Core node started successfully.")
        except Exception as e:
            logging.error(f"Failed to start Bitcoin Core node: {e}")
            sys.exit(1)

    def stop_node(self):
        """
        Stop the Bitcoin Core full node process.
        """
        if self.process:
            try:
                # Send the stop command to the Bitcoin Core process
                subprocess.run(['bitcoin-cli', '-datadir=' + self.data_dir, 'stop'], check=True)
                self.process.wait()
                logging.info("Bitcoin Core node stopped successfully.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Error stopping Bitcoin Core node: {e}")
        else:
            logging.warning("No Bitcoin Core process to stop.")

    def is_running(self):
        """
        Check if the Bitcoin Core node is running.

        :return: True if the node is running, False otherwise
        """
        return self.process is not None and self.process.poll() is None

if __name__ == "__main__":
    # Example usage
    DATA_DIR = '/path/to/bitcoin/data'  # Change this to your desired data directory
    RPC_USER = 'your_rpc_user'           # Change this to your desired RPC username
    RPC_PASSWORD = 'your_rpc_password'   # Change this to your desired RPC password

    bitcoin_node = BitcoinNode(DATA_DIR, RPC_USER, RPC_PASSWORD)

    # Start the Bitcoin node
    bitcoin_node.start_node()

    # Check if the node is running
    if bitcoin_node.is_running():
        logging.info("Bitcoin Core node is running.")
    else:
        logging.error("Bitcoin Core node is not running.")

    # Stop the Bitcoin node (for demonstration purposes, you may want to run this separately)
    # bitcoin_node.stop_node()
```

Make sure to replace `/path/to/bitcoin/data`, `your_rpc_user`, and `your_rpc_password` with your actual values before running the code.
