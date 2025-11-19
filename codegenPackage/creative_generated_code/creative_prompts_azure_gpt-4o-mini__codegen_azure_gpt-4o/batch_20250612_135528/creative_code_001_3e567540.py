"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetvietnam.wordpress.com
Prompt: How can I integrate NFT functionality into a StarkNet-based application? Provide a sample implementation.
Generated: DETERMINISTIC_3e56754004cfe3ad
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/token-metadata": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import asyncio
from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.networks import MAINNET
from starknet_py.contract import Contract
from starknet_py.transactions.deploy import DeployTransaction

# Constants
CONTRACT_PATH = "contracts/nft.json"  # Path to the compiled NFT contract
NFT_CONTRACT_NAME = "MyNFT"           # Name of your NFT contract
NETWORK = MAINNET                     # Network to deploy and interact with
PRIVATE_KEY = "your_private_key"      # Replace with your account private key
ACCOUNT_ADDRESS = "your_account_address"  # Replace with your StarkNet account address

# Async function to deploy an NFT contract
async def deploy_nft_contract():
    """
    Deploys an NFT contract to StarkNet.
    """
    # Create GatewayClient for StarkNet network
    client = GatewayClient(NETWORK)

    # Initialize Account object
    account = Account(
        client=client,
        address=ACCOUNT_ADDRESS,
        key_pair=Account.generate_key_pair(private_key=PRIVATE_KEY)
    )

    # Deploy the NFT contract
    deploy_tx = await DeployTransaction.deploy(
        account=account,
        compiled_contract=CONTRACT_PATH,
        constructor_args={
            "name": NFT_CONTRACT_NAME,
            "symbol": "NFT",
            "owner": account.address
        }
    )
    await deploy_tx.wait_for_acceptance()

    print(f"NFT Contract deployed successfully! Address: {deploy_tx.address}")
    return deploy_tx.address

# Async function to mint an NFT
async def mint_nft(contract_address, recipient, token_id, token_uri):
    """
    Mints a new NFT on the deployed contract.
    :param contract_address: Address of the deployed NFT contract
    :param recipient: Address of the recipient
    :param token_id: Unique ID of the token
    :param token_uri: Metadata URI for the token
    """
    client = GatewayClient(NETWORK)

    # Initialize Account object
    account = Account(
        client=client,
        address=ACCOUNT_ADDRESS,
        key_pair=Account.generate_key_pair(private_key=PRIVATE_KEY)
    )

    # Load the contract
    contract = await Contract.from_address(
        address=contract_address,
        client=client
    )

    # Call the mint function
    mint_tx = await contract.functions["mint"].invoke(
        recipient=recipient,
        token_id=token_id,
        token_uri=token_uri,
        account=account,
        max_fee=int(1e16)  # Example max fee, adjust accordingly
    )
    await mint_tx.wait_for_acceptance()

    print(f"NFT Minted successfully! Token ID: {token_id}")


# Main entry point
async def main():
    try:
        # Deploy NFT Contract
        nft_contract_address = await deploy_nft_contract()

        # Example: Mint an NFT
        recipient = "0xRecipientAddress"
        token_id = 1
        token_uri = "https://example.com/token-metadata"
        await mint_nft(nft_contract_address, recipient, token_id, token_uri)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
```
