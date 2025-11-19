"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astar-portal.vercel.app
Prompt: How can I use the Astar Portal to connect to the Astar and Shiden networks using a light client?
Generated: DETERMINISTIC_81cf1f9c712cb063
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import asyncio
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

# Function to connect to Astar or Shiden network using Astar Portal
async def connect_to_astar_network(network: str):
    """
    Connects to the Astar or Shiden network using a light client.

    :param network: The name of the network to connect to ('astar' or 'shiden').
    :return: None
    """
    # Define the network endpoints
    endpoints = {
        'astar': 'wss://rpc.astar.network',
        'shiden': 'wss://rpc.shiden.astar.network'
    }

    # Check if the network is supported
    if network not in endpoints:
        raise ValueError(f"Unsupported network '{network}'. Please use 'astar' or 'shiden'.")

    try:
        # Connect to the substrate interface for the specified network
        substrate = SubstrateInterface(url=endpoints[network])

        # Verify connection
        if substrate.is_connected:
            print(f"Successfully connected to the {network.capitalize()} network!")
            
            # Query the chain name and other metadata
            chain_name = substrate.chain
            node_name = substrate.node_name
            node_version = substrate.node_version
            
            print(f"Chain: {chain_name}")
            print(f"Node Name: {node_name}")
            print(f"Node Version: {node_version}")
        else:
            print(f"Failed to connect to the {network.capitalize()} network.")
    except SubstrateRequestException as e:
        # Handle any exceptions raised by the substrate interface
        print(f"An error occurred while connecting to the {network.capitalize()} network: {str(e)}")
    except ValueError as e:
        # Handle unsupported network
        print(f"Invalid input: {str(e)}")
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        # Perform cleanup if necessary
        if substrate.is_connected:
            substrate.close()

# Main function to execute the connection
async def main():
    """
    Main function to test connectivity to Astar Portal networks.
    """
    # Specify the network ('astar' or 'shiden')
    network_to_connect = 'astar'  # Change to 'shiden' to connect to Shiden network

    # Attempt to connect to the specified network
    await connect_to_astar_network(network_to_connect)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
