"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ambassadors.org
Prompt: How can I use Starknet's tools and resources to build a decentralized application?
Generated: DETERMINISTIC_ff59c1b16df7f680
Batch ID: 20250612_135210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from starkware.starknet.public.abi import get_selectors
from starkware.starknet.business_logic.transaction.transaction import Transaction
from starkware.starknet.services.api.contract import ContractFunction
from starkware.starknet.services.api.gateway.transaction import InvokeFunction

# Define the Starknet contract address
CONTRACT_ADDRESS = "0xYourContractAddress"

# Function to get contract selectors
def get_contract_selectors(contract_abi):
    """
    Retrieve the function selectors from the given contract ABI.
    
    :param contract_abi: The Application Binary Interface of the contract.
    :return: A dictionary mapping function names to their selectors.
    """
    try:
        return get_selectors(contract_abi)
    except Exception as e:
        print(f"Error retrieving contract selectors: {e}")
        return {}

# Function to invoke a contract function
async def invoke_contract_function(function_name, params):
    """
    Invoke a function on a deployed Starknet contract.
    
    :param function_name: The name of the function to call.
    :param params: The parameters to pass to the function.
    :return: The response from the contract function.
    """
    try:
        # Create the transaction for invoking the function
        transaction = InvokeFunction(
            contract_address=CONTRACT_ADDRESS,
            function_name=function_name,
            calldata=params,
        )
        
        # Send the transaction
        response = await transaction.send()
        
        return response
    except Exception as e:
        print(f"Error invoking contract function '{function_name}': {e}")
        return None

# Main function to demonstrate usage
async def main():
    # Example contract ABI
    example_abi = [
        {
            "name": "increment",
            "type": "function",
            "inputs": [{"name": "value", "type": "felt"}],
            "outputs": []
        }
    ]
    
    # Retrieve contract selectors
    selectors = get_contract_selectors(example_abi)
    print("Contract Selectors:", selectors)
    
    # Invoke a contract function
    response = await invoke_contract_function("increment", [1])
    if response:
        print("Transaction Response:", response)
    else:
        print("Failed to invoke contract function.")

# Entry point for the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

Make sure to replace `"0xYourContractAddress"` with your actual Starknet contract address.
