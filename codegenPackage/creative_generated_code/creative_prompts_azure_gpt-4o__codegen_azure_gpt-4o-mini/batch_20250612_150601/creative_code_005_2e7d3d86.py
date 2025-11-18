"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-solaj.web.app
Prompt: Create a script to mint NFTs with restrictions on the number of mints per wallet, as specified in the Magic Box minting process.
Generated: DETERMINISTIC_2e7d3d86918255f2
Batch ID: 20250612_150601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.rpc.url": {
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
from web3 import Web3
import json

class NFTMinter:
    def __init__(self, rpc_url, contract_address, private_key, wallet_address):
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract_address = Web3.toChecksumAddress(contract_address)
        self.private_key = private_key
        self.wallet_address = Web3.toChecksumAddress(wallet_address)
        self.nft_contract = self.load_contract()

    def load_contract(self):
        """Load the NFT contract ABI."""
        with open('nft_contract_abi.json') as f:
            abi = json.load(f)
        return self.web3.eth.contract(address=self.contract_address, abi=abi)

    def mint_nft(self, quantity, max_mints_per_wallet):
        """
        Mint NFTs with a restriction on the number of mints per wallet.

        Parameters:
        - quantity: Number of NFTs to mint
        - max_mints_per_wallet: Maximum NFTs allowed per wallet

        Raises:
        - ValueError: If the number of mints exceeds the limit
        """
        current_mints = self.get_current_mints()
        if current_mints + quantity > max_mints_per_wallet:
            raise ValueError(f"Minting {quantity} NFTs exceeds the limit of {max_mints_per_wallet} per wallet.")
        
        # Prepare mint transaction
        nonce = self.web3.eth.getTransactionCount(self.wallet_address)
        txn = self.nft_contract.functions.mint(quantity).buildTransaction({
            'chainId': 1,  # Mainnet (adjust if necessary)
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        # Sign the transaction
        signed_txn = self.web3.eth.account.sign_transaction(txn, self.private_key)

        # Send the transaction
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(f"Transaction sent! Hash: {txn_hash.hex()}")

    def get_current_mints(self):
        """
        Fetch the current number of NFTs minted by the wallet.

        Returns:
        - int: Current number of mints for the wallet
        """
        # Assuming the contract has a function to get NFTs by owner
        return self.nft_contract.functions.balanceOf(self.wallet_address).call()

if __name__ == "__main__":
    # Example usage:
    RPC_URL = "https://your.rpc.url"
    CONTRACT_ADDRESS = "0xYourContractAddress"
    PRIVATE_KEY = "0xYourPrivateKey"
    WALLET_ADDRESS = "0xYourWalletAddress"
    
    nft_minter = NFTMinter(RPC_URL, CONTRACT_ADDRESS, PRIVATE_KEY, WALLET_ADDRESS)
    
    try:
        MAX_MINTS_PER_WALLET = 5
        QUANTITY_TO_MINT = 1  # Adjust as needed
        nft_minter.mint_nft(QUANTITY_TO_MINT, MAX_MINTS_PER_WALLET)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Make sure to replace placeholder values (like `RPC_URL`, `CONTRACT_ADDRESS`, `PRIVATE_KEY`, and `WALLET_ADDRESS`) with actual values before running the code. Additionally, the ABI for the NFT contract should be stored in a file named `nft_contract_abi.json`.
