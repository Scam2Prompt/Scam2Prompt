"""
Generated Code Metadata:
========================
Original URL: https://polkadotindia.org
Prompt: Create a tutorial for Indian developers on building applications using Polkadot's ecosystem, inspired by the community initiatives highlighted on Polkadot India.
Generated: DETERMINISTIC_03e77dddf5b7c50d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# polkadot_tutorial.py

"""
Polkadot Application Development Tutorial

This script serves as a basic template for Indian developers looking to build applications
using the Polkadot ecosystem. It includes essential components such as connecting to the
Polkadot network, querying data, and handling errors gracefully.

Requirements:
- Install the following packages:
    - polkadot-api
    - asyncio
"""

import asyncio
from substrateinterface import SubstrateInterface, Keypair

# Constants
POLKADOT_NODE_URL = "wss://rpc.polkadot.io"  # URL for the Polkadot node

async def connect_to_polkadot():
    """
    Connects to the Polkadot network and returns the substrate interface.

    Returns:
        SubstrateInterface: An instance of the SubstrateInterface connected to the Polkadot network.
    """
    try:
        substrate = SubstrateInterface(
            url=POLKADOT_NODE_URL,
            type_registry_preset='polkadot'  # Use the Polkadot type registry
        )
        print("Successfully connected to the Polkadot network.")
        return substrate
    except Exception as e:
        print(f"Error connecting to Polkadot: {e}")
        raise

async def get_chain_info(substrate):
    """
    Retrieves and prints the chain information.

    Args:
        substrate (SubstrateInterface): The substrate interface connected to the Polkadot network.
    """
    try:
        chain_info = await substrate.get_chain_properties()
        print("Chain Information:")
        print(chain_info)
    except Exception as e:
        print(f"Error retrieving chain info: {e}")

async def main():
    """
    Main function to run the tutorial.
    Connects to the Polkadot network and retrieves chain information.
    """
    try:
        substrate = await connect_to_polkadot()
        await get_chain_info(substrate)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")

# Entry point of the script
if __name__ == "__main__":
    asyncio.run(main())
```

### Instructions to Run the Code:
1. Ensure you have Python 3.7 or higher installed.
2. Install the required packages using pip:
   ```bash
   pip install substrate-interface asyncio
   ```
3. Save the code in a file named `polkadot_tutorial.py`.
4. Run the script:
   ```bash
   python polkadot_tutorial.py
   ```
