"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-update-doc-419labs.vercel.app
Prompt: Provide an example of how to use StarkEx for scaling infrastructure on StarkNet L2, referencing the StarkNet ecosystem projects.
Generated: DETERMINISTIC_65861097cf6fd9f2
Batch ID: 20250612_145430
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.public.abi import get_selector_from_name
from starkware.starknet.business_logic.state.state import BlockInfo
import asyncio
import os

# Constants
CONTRACT_FILE = os.path.join("contracts", "example.cairo")
CONTRACT_NAME = "example_contract"

class StarkExExample:
    """
    Example class demonstrating StarkEx usage for scaling infrastructure on StarkNet L2.
    """
    
    def __init__(self):
        self.starknet = None
        self.contract = None
    
    async def initialize(self):
        """
        Initialize StarkNet and deploy the example contract.
        """
        # Initialize StarkNet state
        self.starknet = await Starknet.empty()
        
        # Set block information (timestamp and block number)
        self.starknet.state.state.block_info = BlockInfo(
            block_number=1,
            block_timestamp=1640995200,  # Jan 1, 2022
            gas_price=10**9
        )
        
        # Compile and deploy contract
        contract_definition = compile_starknet_files([CONTRACT_FILE], debug_info=True)
        self.contract = await self.starknet.deploy(
            contract_def=contract_definition,
            constructor_calldata=[]
        )
    
    async def invoke_contract_function(self, function_name, calldata):
        """
        Invoke a contract function.
        
        Args:
            function_name (str): Name of the function to call
            calldata (list): List of arguments for the function
        """
        try:
            selector = get_selector_from_name(function_name)
            await self.contract.invoke(
                selector=selector,
                calldata=calldata
            )
            print(f"Successfully invoked {function_name}")
        except Exception as e:
            print(f"Error invoking {function_name}: {str(e)}")
            raise
    
    async def call_contract_function(self, function_name, calldata):
        """
        Call a contract function (read-only).
        
        Args:
            function_name (str): Name of the function to call
            calldata (list): List of arguments for the function
            
        Returns:
            The result of the function call
        """
        try:
            selector = get_selector_from_name(function_name)
            result = await self.contract.call(
                selector=selector,
                calldata=calldata
            )
            return result
        except Exception as e:
            print(f"Error calling {function_name}: {str(e)}")
            raise

async def main():
    """
    Main function to demonstrate StarkEx usage.
    """
    try:
        # Initialize StarkEx example
        starkex = StarkExExample()
        await starkex.initialize()
        
        # Example contract interactions
        await starkex.invoke_contract_function("increment", [10])
        result = await starkex.call_contract_function("get_value", [])
        print(f"Current value: {result}")
        
        # Example of interacting with StarkNet ecosystem projects
        # (This would require actual project integration in a real implementation)
        print("Interacting with StarkNet ecosystem projects...")
        
    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
```
