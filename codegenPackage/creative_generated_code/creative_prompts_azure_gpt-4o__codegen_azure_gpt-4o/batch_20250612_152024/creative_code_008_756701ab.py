"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetfoundation.io
Prompt: Recommend tools for debugging and testing StarkNet smart contracts written in Cairo. Provide examples of their usage.
Generated: DETERMINISTIC_756701ab747c28d4
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: starknet_debug_testing_tools.py

"""
This script demonstrates tools and techniques for debugging and testing StarkNet smart contracts written in Cairo.
"""

# Import required libraries
import subprocess
import os
from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.client import Client

# Constants
STARKNET_NETWORK = "testnet"  # Available options: "testnet" or "mainnet"
MAX_RETRIES = 3  # Maximum retries for network calls

# Tool 1: Debugging with StarkNet CLI
def debug_with_starknet_cli(contract_path: str, input_values: list):
    """
    Debug a StarkNet smart contract using the StarkNet CLI.

    Args:
        contract_path (str): Path to the compiled Cairo contract (.json file).
        input_values (list): List of input values for the contract function.
    """
    try:
        # Construct the CLI command for debugging
        command = [
            "starknet",
            "invoke",
            "--contract",
            contract_path,
            "--inputs",
            " ".join(map(str, input_values)),
            "--network",
            STARKNET_NETWORK
        ]
        
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Print the debugging output
        print(f"Debugging output:\n{result.stdout}")
        if result.stderr:
            print(f"Error output:\n{result.stderr}")
    except Exception as e:
        print(f"Error during debugging: {str(e)}")


# Tool 2: Testing with StarkNet.py
async def test_with_starknet_py(contract_address: str, function_name: str, inputs: list, account: Account):
    """
    Test a deployed StarkNet smart contract using starknet.py.

    Args:
        contract_address (str): Address of the deployed smart contract.
        function_name (str): Name of the function to call.
        inputs (list): List of input values for the contract function.
        account (Account): StarkNet account object for interacting with the network.
    """
    try:
        # Create a client instance for the StarkNet network
        client = Client(net=STARKNET_NETWORK)

        # Fetch the contract object
        contract = await Contract.from_address(contract_address, client)

        # Perform the contract function call
        result = await contract.functions[function_name].call(*inputs)

        # Print the test result
        print(f"Test result for function '{function_name}': {result}")
    except Exception as e:
        print(f"Error during testing: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Example for debugging
    contract_file_path = "path/to/compiled_contract.json"
    debugging_inputs = [123, 456]
    debug_with_starknet_cli(contract_file_path, debugging_inputs)

    # Example for testing
    import asyncio
    contract_address = "0x123abc..."  # Replace with actual contract address
    function_to_call = "get_balance"
    testing_inputs = [789]
    my_account = Account()  # Replace with actual account initialization
    asyncio.run(test_with_starknet_py(contract_address, function_to_call, testing_inputs, my_account))
```

Make sure to update placeholders like file paths, contract addresses, and account objects with actual values before running the code.
