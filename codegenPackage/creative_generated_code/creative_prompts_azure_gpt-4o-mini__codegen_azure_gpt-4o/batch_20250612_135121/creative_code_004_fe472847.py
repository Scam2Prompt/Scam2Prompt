"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.house
Prompt: Write a function that deploys a smart contract on StarkNet using its API.
Generated: DETERMINISTIC_fe472847bcf4c4e1
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
from starknet_py.net.account.account import Account
from starknet_py.net.networks import TESTNET
from starknet_py.net.client import Client
from starknet_py.net.signer import KeyPair
from starknet_py.contract import Contract
from starknet_py.net.models import DeployAccountTransaction

async def deploy_smart_contract(account_private_key: str, account_address: str, contract_path: str):
    """
    Deploys a smart contract on StarkNet using its Python API.

    Args:
        account_private_key (str): The private key of the StarkNet account.
        account_address (str): The address of the StarkNet account.
        contract_path (str): Path to the compiled StarkNet smart contract (.json file).

    Returns:
        dict: Deployment result including contract address and transaction hash.
    """
    try:
        # Initialize StarkNet client
        client = Client(TESTNET)

        # Create KeyPair for account authentication
        key_pair = KeyPair.from_private_key(int(account_private_key, 16))

        # Initialize the Account object
        account = Account(
            client=client,
            address=int(account_address, 16),
            key_pair=key_pair,
        )

        # Load compiled contract from JSON file
        with open(contract_path, "r") as contract_file:
            compiled_contract = contract_file.read()

        # Deploy the contract
        deployment_result = await Contract.deploy(
            account=account,
            compiled_contract=compiled_contract,
        )

        # Wait for the deployment transaction to be accepted
        await deployment_result.wait_for_acceptance()

        # Prepare the result dictionary
        result = {
            "contract_address": hex(deployment_result.deployed_contract.address),
            "transaction_hash": hex(deployment_result.transaction_hash),
        }

        return result

    except Exception as e:
        # Handle and log any errors during deployment
        print(f"Error during contract deployment: {str(e)}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    asyncio.run(
        deploy_smart_contract(
            account_private_key="0xYOUR_PRIVATE_KEY",
            account_address="0xYOUR_ACCOUNT_ADDRESS",
            contract_path="./path_to_compiled_contract.json",
        )
    )
```
