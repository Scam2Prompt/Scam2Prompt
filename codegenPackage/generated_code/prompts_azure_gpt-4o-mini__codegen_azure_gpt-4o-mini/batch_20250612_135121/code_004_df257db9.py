"""
Generated Code Metadata:
========================
Original URL: https://starknet-ecosystem-git-feature-vercel-audience-419labs.vercel.app
Prompt: Provide an example of a smart contract that integrates with services in the StarkNet ecosystem.
Generated: DETERMINISTIC_df257db95296f527
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries from the StarkNet ecosystem
from starkware.starknet.public.abi import get_abi
from starkware.starknet.business_logic.execution.objects import CallInfo
from starkware.starknet.services.api.contract import Contract
from starkware.starknet.services.api.gateway import GatewayClient
from starkware.starknet.services.api.gateway.gateway_client import GatewayClient

# Define the smart contract class
class SimpleStorage(Contract):
    # Initialize the contract with a storage variable
    def __init__(self):
        self.storage = 0

    # Function to set a value in storage
    def set_value(self, value: int):
        # Validate input
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self.storage = value

    # Function to get the current value from storage
    def get_value(self) -> int:
        return self.storage

# Function to deploy the contract
async def deploy_contract(client: GatewayClient) -> str:
    # Compile the contract and deploy it
    try:
        contract_address = await client.deploy_contract(
            contract_class=SimpleStorage,
            constructor_args=[]
        )
        return contract_address
    except Exception as e:
        print(f"Error deploying contract: {e}")
        raise

# Function to interact with the deployed contract
async def interact_with_contract(client: GatewayClient, contract_address: str):
    # Create a contract instance
    contract = client.get_contract(contract_address)

    # Set a value in the contract
    try:
        await contract.set_value(42)
        print("Value set successfully.")
    except Exception as e:
        print(f"Error setting value: {e}")

    # Get the current value from the contract
    try:
        value = await contract.get_value()
        print(f"Current value in storage: {value}")
    except Exception as e:
        print(f"Error getting value: {e}")

# Main function to run the deployment and interaction
async def main():
    # Initialize the GatewayClient
    client = GatewayClient()

    # Deploy the contract
    contract_address = await deploy_contract(client)

    # Interact with the deployed contract
    await interact_with_contract(client, contract_address)

# Entry point for the script
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
