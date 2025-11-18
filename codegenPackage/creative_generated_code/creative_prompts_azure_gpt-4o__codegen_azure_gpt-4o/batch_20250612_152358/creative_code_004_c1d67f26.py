"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiasw5dmpfqqr7panrkqsibus7vxltxmiroh4lh37diiwwftj6sz3e.ipfs.dweb.link
Prompt: Write a script to explore and scan the Bittensor network for active nodes and their staking activity, as described in the documentation.
Generated: DETERMINISTIC_c1d67f26d0fa3eb3
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import bittensor
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_bittensor_network():
    """
    Scans the Bittensor network for active nodes and their staking activity.

    Returns:
        - A list of dictionaries containing node information and staking details.
    """
    try:
        # Initialize a Bittensor wallet
        logging.info("Initializing Bittensor wallet...")
        wallet = bittensor.wallet(name="default", hotkey="default")
        
        # Connect to Bittensor network
        logging.info("Connecting to Bittensor network...")
        subtensor = bittensor.subtensor(network="nakamoto")  # Connect to the desired network (default: nakamoto)

        # Fetch all active nodes from the network
        logging.info("Fetching list of active nodes...")
        active_nodes = subtensor.get_active()
        
        # List to store node and staking details
        node_data = []

        logging.info("Scanning nodes for staking activity...")
        for node in active_nodes:
            # Get staking balance for each node
            staking_balance = subtensor.get_stake(node)
            
            # Append node details to the list
            node_data.append({
                "node_address": node.address,
                "stake": staking_balance
            })
        
        logging.info("Scanning complete. Found %d nodes.", len(node_data))
        return node_data

    except Exception as e:
        logging.error("An error occurred while scanning the Bittensor network: %s", str(e))
        sys.exit(1)

def main():
    """
    Main function to execute the network scan and output the results.
    """
    logging.info("Starting Bittensor network scan...")
    
    # Scan the network
    node_data = scan_bittensor_network()
    
    # Display results
    logging.info("Displaying results...")
    for node in node_data:
        print(f"Node Address: {node['node_address']}, Stake: {node['stake']}")

if __name__ == "__main__":
    main()
```
