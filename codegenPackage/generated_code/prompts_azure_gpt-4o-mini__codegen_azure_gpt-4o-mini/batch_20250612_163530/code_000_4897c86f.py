"""
Generated Code Metadata:
========================
Original URL: https://p-1px.pages.dev
Prompt: How can I run a lightweight full node using Over Protocol on my PC, and what are the benefits of home staking?
Generated: DETERMINISTIC_4897c86f66ec782c
Batch ID: 20250612_163530
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

def install_over_protocol():
    """
    Install Over Protocol dependencies and set up a lightweight full node.
    """
    try:
        # Check if Over Protocol is already installed
        if subprocess.call(['which', 'over-protocol']) != 0:
            logging.info("Installing Over Protocol...")
            subprocess.check_call(['pip', 'install', 'over-protocol'])
        else:
            logging.info("Over Protocol is already installed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during installation: {e}")
        sys.exit(1)

def setup_lightweight_node():
    """
    Set up a lightweight full node for Over Protocol.
    """
    try:
        logging.info("Setting up lightweight full node...")
        # Create a directory for the node data
        os.makedirs('over_protocol_node', exist_ok=True)
        
        # Start the Over Protocol node
        subprocess.Popen(['over-protocol', 'start', '--data-dir', 'over_protocol_node'])
        logging.info("Lightweight full node is running.")
    except Exception as e:
        logging.error(f"Error setting up the node: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the Over Protocol lightweight full node.
    """
    install_over_protocol()
    setup_lightweight_node()

if __name__ == "__main__":
    main()
```

### Benefits of Home Staking:
# 1. **Passive Income**: Earn rewards for staking your tokens.
# 2. **Network Security**: Contribute to the security and stability of the network.
# 3. **Control**: Maintain control over your assets without relying on third parties.
# 4. **Community Engagement**: Participate actively in the governance of the protocol.
