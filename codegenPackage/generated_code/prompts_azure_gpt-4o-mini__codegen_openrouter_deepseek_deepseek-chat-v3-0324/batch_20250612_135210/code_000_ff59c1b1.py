"""
Generated Code Metadata:
========================
Original URL: https://starknet-ambassadors.org
Prompt: How can I use Starknet's tools and resources to build a decentralized application?
Generated: DETERMINISTIC_ff59c1b16df7f680
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.public.abi import get_selector_from_name
from starkware.starknet.business_logic.state.state import BlockInfo
import asyncio
import os

# Path to the contract source file
CONTRACT_FILE = os.path.join("contracts", "my_contract.cairo")

async def deploy_contract():
    """
    Deploys a Starknet contract and returns the contract object.
    """
    try:
        # Initialize Starknet
        starknet = await Starknet.empty()
        
        # Set block information (timestamp and block number)
        starknet.state.state.block_info = BlockInfo(
            block_number=1,
            block_timestamp=1
        )
        
        # Compile the contract
        contract_definition = compile_starknet_files(
            [CONTRACT_FILE],
            debug_info=True
        )
        
        # Deploy the contract
        contract = await starknet.deploy(
            contract_definition=contract_definition
        )
        
        return contract
    
    except Exception as e:
        print(f"Error deploying contract: {e}")
        raise

async def call_contract_function(contract, function_name, *args):
    """
    Calls a function on the deployed contract.
    """
    try:
        selector = get_selector_from_name(function_name)
        result = await contract.invoke(
            selector=selector,
            calldata=list(args)
        )
        return result
        
    except Exception as e:
        print(f"Error calling function {function_name}: {e}")
        raise

async def main():
    """
    Main function to deploy and interact with the contract.
    """
    try:
        # Deploy the contract
        contract = await deploy_contract()
        print(f"Contract deployed at: {contract.contract_address}")
        
        # Example: Call a function named 'get_balance'
        result = await call_contract_function(contract, "get_balance")
        print(f"Function call result: {result}")
        
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```
