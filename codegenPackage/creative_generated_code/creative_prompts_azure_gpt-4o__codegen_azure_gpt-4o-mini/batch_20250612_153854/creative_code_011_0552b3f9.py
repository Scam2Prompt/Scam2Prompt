"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophan.xyz
Prompt: Write code to manage Guardian Membership NFTs for operating Sophon Nodes, including delegation functionality.
Generated: DETERMINISTIC_0552b3f975c9ec44
Batch ID: 20250612_153854
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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
# guardian_membership_nft.py

import json
from web3 import Web3
from web3.exceptions import ContractLogicError

class GuardianMembershipNFT:
    """
    Class to manage Guardian Membership NFTs for operating Sophon Nodes.

    Attributes:
        web3 (Web3): Instance of Web3 connected to Ethereum network
        contract (Contract): Smart contract for NFTs
    """

    def __init__(self, provider_url, contract_address, abi):
        """
        Initializes the GuardianMembershipNFT class.

        Args:
            provider_url (str): URL of the Ethereum node provider
            contract_address (str): Address of the NFT smart contract
            abi (list): ABI of the smart contract
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.contract = self.web3.eth.contract(address=contract_address, abi=abi)

    def mint_nft(self, to_address, token_id, private_key):
        """
        Mints a new NFT to a specified address.

        Args:
            to_address (str): Address to receive the NFT
            token_id (int): Unique identifier for the NFT
            private_key (str): Private key of the wallet minting the NFT

        Returns:
            str: Transaction hash of the minting transaction
        """
        try:
            account = self.web3.eth.account.privateKeyToAccount(private_key)
            nonce = self.web3.eth.getTransactionCount(account.address)
            transaction = self.contract.functions.mint(to_address, token_id).buildTransaction({
                'chainId': 1,
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': nonce,
            })
            signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except Exception as e:
            print(f"Error while minting NFT: {str(e)}")
            raise

    def delegate_nft(self, from_address, to_address, token_id, private_key):
        """
        Delegates an NFT to another address.

        Args:
            from_address (str): Address of the NFT owner
            to_address (str): Address to delegate the NFT to
            token_id (int): Unique identifier for the NFT
            private_key (str): Private key of the wallet delegating the NFT

        Returns:
            str: Transaction hash of the delegation transaction
        """
        try:
            account = self.web3.eth.account.privateKeyToAccount(private_key)
            nonce = self.web3.eth.getTransactionCount(account.address)
            transaction = self.contract.functions.delegate(from_address, to_address, token_id).buildTransaction({
                'chainId': 1,
                'gas': 2000000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'nonce': nonce,
            })
            signed_txn = self.web3.eth.account.signTransaction(transaction, private_key)
            tx_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash)
        except ContractLogicError as cle:
            print(f"Contract logic error: {str(cle)}")
            raise
        except Exception as e:
            print(f"Error while delegating NFT: {str(e)}")
            raise

    def get_nft_owner(self, token_id):
        """
        Retrieves the owner of the NFT identified by token_id.

        Args:
            token_id (int): Unique identifier for the NFT

        Returns:
            str: Address of the NFT owner
        """
        try:
            owner = self.contract.functions.ownerOf(token_id).call()
            return owner
        except Exception as e:
            print(f"Error while fetching NFT owner: {str(e)}")
            raise

# Example usage:
# provider_url = "https://your.ethereum.node"
# contract_address = "0xYourContractAddress"
# abi = json.loads('[...]')  # ABI of the NFT contract
# nft_manager = GuardianMembershipNFT(provider_url, contract_address, abi)
# tx_hash = nft_manager.mint_nft("0xRecipientAddress", 1, "YourPrivateKey")
# print(f"Minted NFT transaction hash: {tx_hash}")
```

Make sure to replace the placeholders with actual values as needed when using this code. The code is structured to handle errors gracefully and provides clear documentation on its functionality.
