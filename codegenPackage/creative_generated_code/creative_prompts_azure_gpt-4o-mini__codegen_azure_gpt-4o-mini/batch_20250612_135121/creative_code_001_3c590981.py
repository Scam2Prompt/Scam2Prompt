"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.house
Prompt: Can you provide a code example for interacting with StarkNet's smart contracts using its library?
Generated: DETERMINISTIC_3c590981096a4a08
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import asyncio
from starknet_py.net import Client
from starknet_py.contract import Contract
from starknet_py.net.models import InvokeFunction
from starknet_py.net.exceptions import StarknetError

# Define the contract address and ABI (Application Binary Interface)
CONTRACT_ADDRESS = "0xYourContractAddressHere"
ABI = [
    # Add your contract's ABI here
]

async def main():
    # Initialize the StarkNet client
    client = Client(net="testnet")  # Change to "mainnet" for production

    # Load the contract
    contract = Contract(address=CONTRACT_ADDRESS, abi=ABI, client=client)

    # Example interaction: calling a function of the smart contract
    try:
        # Call a read-only function
        response = await contract.functions.your_read_function().call()
        print(f"Response from read function: {response}")

        # Prepare parameters for the invoke function
        params = {
            "param1": "value1",
            "param2": "value2"
        }

        # Invoke a state-changing function
        invoke_response = await contract.functions.your_write_function(**params).invoke()
        print(f"Transaction hash: {invoke_response.transaction_hash}")

        # Wait for the transaction to be finalized
        await client.wait_for_tx(invoke_response.transaction_hash)
        print("Transaction successfully processed.")

    except StarknetError as e:
        print(f"StarkNet error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
