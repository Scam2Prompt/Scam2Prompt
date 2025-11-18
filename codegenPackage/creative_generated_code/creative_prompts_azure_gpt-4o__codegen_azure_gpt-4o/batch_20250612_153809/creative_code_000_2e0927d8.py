"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.news
Prompt: Write a Python script using Starknet's API to deploy a smart contract that utilizes zk-STARKs for secure transactions. Include specific steps for interacting with Starknet's Layer 2 scaling solution.
Generated: DETERMINISTIC_2e0927d89222b329
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# starknet_deploy.py
"""
This script deploys a StarkNet smart contract using StarkNet's Python SDK.
The smart contract utilizes zk-STARKs for secure transactions. It follows best practices,
contains error handling, and demonstrates interaction with StarkNet's Layer 2 scaling solution.
"""

import asyncio
import os
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import TESTNET
from starknet_py.contract import Contract
from starknet_py.compile.compiler import compile_starknet_files
from starknet_py.transaction_exceptions import TransactionFailed

# Path to the smart contract
SMART_CONTRACT_FILE = "path/to/your/smart_contract.cairo"

# Gateway client for interacting with StarkNet
client = GatewayClient(net=TESTNET)

async def deploy_contract():
    """
    Compiles and deploys the StarkNet smart contract to the Testnet.
    Handles transaction errors and logs deployment details.
    """
    try:
        # Compile the Cairo smart contract
        print("Compiling the smart contract...")
        compiled_contract = compile_starknet_files([SMART_CONTRACT_FILE], debug_info=True)

        # Estimate fee for deployment
        print("Estimating deployment fee...")
        deployment_result = await Contract.deploy(
            client=client, compiled_contract=compiled_contract
        )
        await deployment_result.wait_for_acceptance()

        # Retrieve contract details
        contract_address = deployment_result.deployed_contract.address
        print(f"Smart contract successfully deployed at address: {contract_address}")

        # Return the contract instance and address
        return deployment_result.deployed_contract, contract_address

    except TransactionFailed as e:
        print(f"Transaction failed: {str(e)}")
    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")
    

async def main():
    """
    Main entry point for the script. Deploys the contract and logs deployment details.
    """
    print("Starting StarkNet smart contract deployment...")
    contract, address = await deploy_contract()
    if contract and address:
        print("Deployment complete.")
        print(f"Contract address: {address}")
    else:
        print("Deployment failed.")

if __name__ == "__main__":
    # Run the script using asyncio
    asyncio.run(main())
```

**Note:**
- Replace `"path/to/your/smart_contract.cairo"` with the actual path to your Cairo smart contract file.
- Ensure StarkNet's Python SDK (`starknet_py`) is installed in your environment: `pip install starknet_py`.
- This script targets the StarkNet Testnet. For Mainnet deployment, replace `TESTNET` with `MAINNET` from `starknet_py.net.networks`.
