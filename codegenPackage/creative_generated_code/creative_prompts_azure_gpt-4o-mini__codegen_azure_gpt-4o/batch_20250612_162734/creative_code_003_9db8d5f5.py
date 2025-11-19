"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakingstory.org
Prompt: Describe how to set up a multi-chain staking environment using the features of Story Staking for enhanced accessibility.
Generated: DETERMINISTIC_9db8d5f5b407896d
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for setting up a multi-chain staking environment with enhanced accessibility using the concept of "Story Staking". This code assumes the use of popular web3 libraries such as `web3.py` for Ethereum and similar blockchains, and a hypothetical library for handling Story Staking logic.

```python
import json
import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables (e.g., API keys, private keys, etc.)
load_dotenv()

# Constants for multi-chain support
MULTICHAIN_CONFIG = {
    "ethereum": {
        "rpc_url": os.getenv("ETHEREUM_RPC_URL"),
        "staking_contract_address": os.getenv("ETHEREUM_STAKING_CONTRACT"),
    },
    "polygon": {
        "rpc_url": os.getenv("POLYGON_RPC_URL"),
        "staking_contract_address": os.getenv("POLYGON_STAKING_CONTRACT"),
    },
    "binance_smart_chain": {
        "rpc_url": os.getenv("BSC_RPC_URL"),
        "staking_contract_address": os.getenv("BSC_STAKING_CONTRACT"),
    },
}

# Story Staking metadata (hypothetical data structure)
STORY_STAKING_METADATA = {
    "stories": [
        {
            "id": "story_1",
            "title": "The Tale of Two Chains",
            "description": "Stake across Ethereum and Polygon.",
            "reward_multiplier": 1.5,
        },
        {
            "id": "story_2",
            "title": "The Binance Chronicles",
            "description": "Exclusive rewards for Binance Smart Chain staking!",
            "reward_multiplier": 2.0,
        },
    ]
}


class MultiChainStaking:
    def __init__(self):
        """Initialize MultiChainStaking with connections to multiple blockchains."""
        self.chain_connections = self._setup_connections()

    def _setup_connections(self):
        """Set up Web3 connections for supported chains."""
        connections = {}
        for chain, config in MULTICHAIN_CONFIG.items():
            try:
                web3_instance = Web3(Web3.HTTPProvider(config["rpc_url"]))
                if not web3_instance.isConnected():
                    raise ConnectionError(f"Failed to connect to {chain} RPC.")
                connections[chain] = {
                    "web3": web3_instance,
                    "staking_contract_address": config["staking_contract_address"],
                }
            except Exception as e:
                print(f"Error setting up connection for {chain}: {e}")
        return connections

    def get_story_metadata(self):
        """Fetch Story Staking metadata."""
        # In production, this might fetch data from a database or external API.
        return STORY_STAKING_METADATA

    def stake(self, chain_name, amount, private_key):
        """
        Stake tokens on a specific chain.

        Args:
            chain_name (str): Name of the chain (e.g., 'ethereum', 'polygon').
            amount (int): Amount of tokens to stake.
            private_key (str): Private key of the staker's wallet.

        Returns:
            str: Transaction hash if successful, or an error message.
        """
        if chain_name not in self.chain_connections:
            return f"Error: Unsupported chain '{chain_name}'."

        chain_info = self.chain_connections[chain_name]
        web3_instance = chain_info["web3"]
        contract_address = chain_info["staking_contract_address"]

        try:
            # Load the staking contract ABI (example ABI could be stored locally or fetched dynamically)
            with open(f"./abis/{chain_name}_staking_abi.json", "r") as abi_file:
                staking_abi = json.load(abi_file)

            staking_contract = web3_instance.eth.contract(
                address=contract_address, abi=staking_abi
            )

            # Prepare transaction
            account = web3_instance.eth.account.from_key(private_key)
            tx = staking_contract.functions.stake(amount).buildTransaction({
                "from": account.address,
                "nonce": web3_instance.eth.get_transaction_count(account.address),
                "gasPrice": web3_instance.eth.gas_price,
            })

            # Sign and send transaction
            signed_tx = web3_instance.eth.account.sign_transaction(tx, private_key)
            tx_hash = web3_instance.eth.send_raw_transaction(signed_tx.rawTransaction)

            return f"Transaction sent successfully! Tx Hash: {web3_instance.toHex(tx_hash)}"
        except Exception as e:
            return f"Error during staking on {chain_name}: {e}"

    def check_rewards(self, chain_name, wallet_address):
        """
        Check staking rewards for a specific chain.

        Args:
            chain_name (str): Name of the chain (e.g., 'ethereum', 'polygon').
            wallet_address (str): Address of the wallet to check rewards for.

        Returns:
            str: Reward details or an error message.
        """
        if chain_name not in self.chain_connections:
            return f"Error: Unsupported chain '{chain_name}'."

        chain_info = self.chain_connections[chain_name]
        web3_instance = chain_info["web3"]
        contract_address = chain_info["staking_contract_address"]

        try:
            # Load the staking contract ABI
            with open(f"./abis/{chain_name}_staking_abi.json", "r") as abi_file:
                staking_abi = json.load(abi_file)

            staking_contract = web3_instance.eth.contract(
                address=contract_address, abi=staking_abi
            )

            # Query rewards
            rewards = staking_contract.functions.checkRewards(wallet_address).call()
            return f"Rewards for {wallet_address} on {chain_name}: {rewards} tokens"
        except Exception as e:
            return f"Error checking rewards on {chain_name}: {e}"


if __name__ == "__main__":
    # Example usage of MultiChainStaking
    staking = MultiChainStaking()

    # Print available story metadata
    print("Available Story Staking Metadata:")
    print(json.dumps(staking.get_story_metadata(), indent=4))

    # Attempt staking on Ethereum
    private_key = os.getenv("PRIVATE_KEY")  # Ensure you store private keys securely!
    stake_result = staking.stake("ethereum", 100, private_key)
    print(stake_result)

    # Check rewards on Polygon
    wallet_address = os.getenv("WALLET_ADDRESS")
    rewards_result = staking.check_rewards("polygon", wallet_address)
    print(rewards_result)
```

### Key Features of the Code:
- **Multi-Chain Support**: The code dynamically connects to multiple blockchains by reading configuration from environment variables.
- **Story Staking Metadata**: Metadata is defined in a structured JSON-like format for accessibility and integration into UI/UX.
- **Error Handling**: Proper try-except blocks are included to catch and handle errors for RPC connectivity, contract interaction, and transaction submission.
- **Environment Variables**: Sensitive data like RPC URLs and private keys are securely loaded from `.env` files.
- **Modular Design**: The `MultiChainStaking` class provides reusable methods for staking and querying rewards across chains.

### Requirements:
- Install required libraries: `pip install web3 python-dotenv`
- Ensure `.env` file contains necessary variables (e.g., RPC URLs, private keys, wallet addresses).
- ABI files for staking contracts should be stored in the `./abis/` directory.
