"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://numerous-area-hundreds.on-fleek.app
Prompt: Provide an example of how to implement multi-chain token support for a cryptocurrency project, similar to the WEMIX token described on TrustPad.
Generated: DETERMINISTIC_675671d2dd6cd0b2
Batch ID: 20250612_150040
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/your_api_key": {
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
# Filename: multi_chain_token.py

from web3 import Web3
from web3.middleware import geth_poa_middleware

class MultiChainToken:
    """
    A class to handle multi-chain token support for a cryptocurrency.
    This example uses Web3.py to interact with Ethereum-like blockchains.
    """

    def __init__(self, rpc_urls):
        """
        Initialize the MultiChainToken instance.

        Args:
            rpc_urls (dict): A dictionary of chain names and their RPC URLs.
                             E.g., {"ethereum": "https://mainnet.infura.io/v3/your_api_key",
                                    "bsc": "https://bsc-dataseed.binance.org/"}
        """
        self.web3_instances = {}
        for chain_name, rpc_url in rpc_urls.items():
            web3 = Web3(Web3.HTTPProvider(rpc_url))
            # Add support for chains with Proof of Authority consensus (e.g., Binance Smart Chain)
            web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            if web3.is_connected():
                self.web3_instances[chain_name] = web3
            else:
                raise ConnectionError(f"Failed to connect to the {chain_name} chain using RPC URL: {rpc_url}")

    def get_token_balance(self, chain_name, token_contract_address, wallet_address):
        """
        Get the balance of a token on a specific chain.

        Args:
            chain_name (str): The name of the chain (e.g., "ethereum" or "bsc").
            token_contract_address (str): The contract address of the token.
            wallet_address (str): The wallet address to query the balance for.

        Returns:
            int: Token balance in the smallest unit (e.g., wei for Ethereum).
        """
        if chain_name not in self.web3_instances:
            raise ValueError(f"Chain {chain_name} is not supported.")

        web3 = self.web3_instances[chain_name]
        # ERC-20 token ABI (simplified for balanceOf function)
        erc20_abi = [
            {
                "constant": True,
                "inputs": [{"name": "_owner", "type": "address"}],
                "name": "balanceOf",
                "outputs": [{"name": "balance", "type": "uint256"}],
                "type": "function"
            }
        ]

        try:
            # Load the token contract
            token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_contract_address), abi=erc20_abi)
            # Query the balance
            balance = token_contract.functions.balanceOf(Web3.to_checksum_address(wallet_address)).call()
            return balance
        except Exception as e:
            raise RuntimeError(f"Failed to fetch token balance on {chain_name}: {e}")

    def transfer_token(self, chain_name, token_contract_address, sender_private_key, recipient_address, amount):
        """
        Transfer tokens from one address to another on a specific chain.

        Args:
            chain_name (str): The name of the chain (e.g., "ethereum" or "bsc").
            token_contract_address (str): The contract address of the token.
            sender_private_key (str): The private key of the sender's wallet.
            recipient_address (str): The recipient's wallet address.
            amount (int): The amount of tokens to transfer (in smallest unit).

        Returns:
            str: Transaction hash of the token transfer.
        """
        if chain_name not in self.web3_instances:
            raise ValueError(f"Chain {chain_name} is not supported.")

        web3 = self.web3_instances[chain_name]
        # ERC-20 token ABI (simplified for transfer function)
        erc20_abi = [
            {
                "constant": False,
                "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
                "name": "transfer",
                "outputs": [{"name": "", "type": "bool"}],
                "type": "function"
            }
        ]

        try:
            # Load the token contract
            token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_contract_address), abi=erc20_abi)
            # Get sender's wallet address
            sender_address = web3.eth.account.privateKeyToAccount(sender_private_key).address

            # Build the transaction
            tx = token_contract.functions.transfer(
                Web3.to_checksum_address(recipient_address), amount
            ).build_transaction({
                'chainId': web3.eth.chain_id,
                'gas': 200000,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(sender_address),
            })

            # Sign the transaction
            signed_tx = web3.eth.account.sign_transaction(tx, sender_private_key)
            # Send the transaction
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return web3.to_hex(tx_hash)
        except Exception as e:
            raise RuntimeError(f"Failed to transfer tokens on {chain_name}: {e}")


# Example usage:
if __name__ == "__main__":
    # Define RPC URLs for multiple chains
    rpc_urls = {
        "ethereum": "https://mainnet.infura.io/v3/your_api_key",
        "bsc": "https://bsc-dataseed.binance.org/"
    }

    try:
        # Initialize the MultiChainToken instance
        multi_chain = MultiChainToken(rpc_urls)

        # Example: Get token balance on Ethereum
        eth_balance = multi_chain.get_token_balance(
            chain_name="ethereum",
            token_contract_address="0xTokenContractAddressHere",
            wallet_address="0xWalletAddressHere"
        )
        print(f"Ethereum token balance: {eth_balance}")

        # Example: Transfer tokens on Binance Smart Chain
        tx_hash = multi_chain.transfer_token(
            chain_name="bsc",
            token_contract_address="0xTokenContractAddressHere",
            sender_private_key="YourPrivateKeyHere",
            recipient_address="0xRecipientAddressHere",
            amount=1000000000000000000  # 1 token in smallest unit (e.g., wei)
        )
        print(f"Transaction hash: {tx_hash}")

    except Exception as e:
        print(f"Error occurred: {e}")
```
