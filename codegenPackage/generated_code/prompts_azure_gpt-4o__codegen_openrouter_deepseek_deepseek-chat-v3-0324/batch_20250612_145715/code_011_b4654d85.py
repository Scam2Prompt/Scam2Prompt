"""
Generated Code Metadata:
========================
Original URL: https://gelato-network-cqz.pages.dev
Prompt: How can I use Gelato's tools to create a decentralized application that interoperates with multiple ZK-powered chains? Provide code examples.
Generated: DETERMINISTIC_b4654d850f2bd6d2
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from web3 import Web3
from gelato import GelatoRelay
from eth_account import Account
import json
import os
from typing import Dict, Any

# Initialize Gelato Relay
gelato_relay = GelatoRelay()

# Load configuration for multiple ZK chains
def load_config() -> Dict[str, Any]:
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as f:
        return json.load(f)

# Initialize Web3 providers for multiple chains
def initialize_providers(config: Dict[str, Any]) -> Dict[str, Web3]:
    providers = {}
    for chain in config['chains']:
        providers[chain['name']] = Web3(Web3.HTTPProvider(chain['rpc_url']))
    return providers

# Example contract ABI (replace with your actual contract ABI)
CONTRACT_ABI = [
    {
        "inputs": [],
        "name": "exampleFunction",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]

# Get contract instance
def get_contract(provider: Web3, contract_address: str) -> Any:
    return provider.eth.contract(address=contract_address, abi=CONTRACT_ABI)

# Build transaction for cross-chain operation
def build_transaction(
    provider: Web3,
    contract_address: str,
    function_name: str,
    args: list,
    sender_address: str,
    value: int = 0
) -> Dict[str, Any]:
    contract = get_contract(provider, contract_address)
    function = contract.get_function_by_name(function_name)(*args)
    return function.build_transaction({
        'from': sender_address,
        'value': value,
        'gas': 2000000,
        'nonce': provider.eth.get_transaction_count(sender_address),
    })

# Submit transaction via Gelato Relay
async def submit_via_gelato(
    chain_id: int,
    transaction: Dict[str, Any],
    sponsor_api_key: str
) -> str:
    response = await gelato_relay.sponsored_call(
        chain_id=chain_id,
        data=transaction['data'],
        target=transaction['to'],
        sponsor_api_key=sponsor_api_key
    )
    return response['taskId']

# Main function to demonstrate cross-chain operation
async def main():
    try:
        # Load configuration
        config = load_config()
        
        # Initialize providers
        providers = initialize_providers(config)
        
        # Get sender account (in production, use proper key management)
        sender_account = Account.from_key(os.getenv('PRIVATE_KEY'))
        
        # Example: Build transaction on Chain A
        chain_a = config['chains'][0]
        provider_a = providers[chain_a['name']]
        
        tx = build_transaction(
            provider=provider_a,
            contract_address=chain_a['contract_address'],
            function_name='exampleFunction',
            args=[],
            sender_address=sender_account.address
        )
        
        # Sign transaction
        signed_tx = sender_account.sign_transaction(tx)
        
        # Submit via Gelato
        task_id = await submit_via_gelato(
            chain_id=chain_a['chain_id'],
            transaction=signed_tx,
            sponsor_api_key=config['gelato_api_key']
        )
        
        print(f"Transaction submitted to Gelato with task ID: {task_id}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

# Run the main function (in async context)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
