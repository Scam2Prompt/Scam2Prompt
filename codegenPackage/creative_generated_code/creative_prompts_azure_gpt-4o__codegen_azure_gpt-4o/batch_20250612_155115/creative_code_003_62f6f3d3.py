"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://make1518999.cc
Prompt: Generate code for a "Batch Asset Processing" feature that collects wallet asset information, processes ERC20 tokens, NFTs, and native tokens, and executes transfers based on the webpage's description of `btngo5`.
Generated: DETERMINISTIC_62f6f3d37e6677ae
Batch ID: 20250612_155115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import logging
from web3 import Web3
from web3.exceptions import TransactionNotFound

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BatchAssetProcessor:
    def __init__(self, rpc_url, private_key):
        """
        Initialize the BatchAssetProcessor with RPC URL and private key for signing transactions.
        :param rpc_url: RPC endpoint URL of the Ethereum node
        :param private_key: Private key of the sender's wallet
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.is_connected():
            raise ConnectionError("Failed to connect to Ethereum node.")
        self.private_key = private_key
        self.sender_address = self.web3.eth.account.from_key(private_key).address

    def get_wallet_balance(self, address):
        """
        Retrieve native token balance of a wallet.
        :param address: Wallet address
        :return: Balance in Ether
        """
        try:
            balance_wei = self.web3.eth.get_balance(address)
            balance_eth = self.web3.from_wei(balance_wei, 'ether')
            return balance_eth
        except Exception as e:
            logger.error(f"Error fetching balance for {address}: {e}")
            return None

    def get_erc20_balance(self, token_contract_address, wallet_address):
        """
        Retrieve ERC-20 token balance for a wallet.
        :param token_contract_address: ERC-20 token contract address
        :param wallet_address: Wallet address
        :return: Token balance
        """
        try:
            # Define ERC-20 contract ABI (simplified to include balanceOf function)
            erc20_abi = [
                {
                    "constant": True,
                    "inputs": [{"name": "owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "type": "function"
                }
            ]
            token_contract = self.web3.eth.contract(address=token_contract_address, abi=erc20_abi)
            balance = token_contract.functions.balanceOf(wallet_address).call()
            return balance
        except Exception as e:
            logger.error(f"Error fetching ERC-20 balance for {wallet_address}: {e}")
            return None

    def transfer_native_token(self, recipient, amount_ether):
        """
        Transfer native token (Ether) to a recipient.
        :param recipient: Recipient wallet address
        :param amount_ether: Amount to transfer in Ether
        """
        try:
            amount_wei = self.web3.to_wei(amount_ether, 'ether')
            tx = {
                'to': recipient,
                'value': amount_wei,
                'gas': 21000,  # Standard gas for Ether transfer
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(self.sender_address)
            }
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            logger.info(f"Transaction sent successfully. Tx Hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            logger.error(f"Error transferring Ether: {e}")
            return None

    def transfer_erc20_token(self, token_contract_address, recipient, amount):
        """
        Transfer ERC-20 tokens to a recipient.
        :param token_contract_address: ERC-20 token contract address
        :param recipient: Recipient wallet address
        :param amount: Amount of tokens to transfer
        """
        try:
            erc20_abi = [
                {
                    "constant": False,
                    "inputs": [
                        {"name": "to", "type": "address"},
                        {"name": "value", "type": "uint256"}
                    ],
                    "name": "transfer",
                    "outputs": [{"name": "", "type": "bool"}],
                    "type": "function"
                }
            ]
            token_contract = self.web3.eth.contract(address=token_contract_address, abi=erc20_abi)
            tx = token_contract.functions.transfer(recipient, amount).build_transaction({
                'chainId': self.web3.eth.chain_id,
                'gas': 60000,  # Estimate gas price based on token contract
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(self.sender_address)
            })
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            logger.info(f"ERC-20 token transfer successful. Tx Hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            logger.error(f"Error transferring ERC-20 tokens: {e}")
            return None

    def transfer_nft(self, nft_contract_address, token_id, recipient):
        """
        Transfer NFT to a recipient.
        :param nft_contract_address: NFT (ERC-721/1155) contract address
        :param token_id: ID of the NFT token to transfer
        :param recipient: Recipient wallet address
        """
        try:
            nft_abi = [
                {
                    "constant": False,
                    "inputs": [
                        {"name": "from", "type": "address"},
                        {"name": "to", "type": "address"},
                        {"name": "tokenId", "type": "uint256"}
                    ],
                    "name": "safeTransferFrom",
                    "outputs": [],
                    "type": "function"
                }
            ]
            nft_contract = self.web3.eth.contract(address=nft_contract_address, abi=nft_abi)
            tx = nft_contract.functions.safeTransferFrom(self.sender_address, recipient, token_id).build_transaction({
                'chainId': self.web3.eth.chain_id,
                'gas': 100000,  # Estimate gas price for NFT transfer
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(self.sender_address)
            })
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            logger.info(f"NFT transfer successful. Tx Hash: {tx_hash.hex()}")
            return tx_hash.hex()
        except Exception as e:
            logger.error(f"Error transferring NFT: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your Ethereum node RPC URL and private key
    RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    PRIVATE_KEY = "YOUR_PRIVATE_KEY"

    processor = BatchAssetProcessor(RPC_URL, PRIVATE_KEY)

    # Example addresses
    recipient_address = "0xRecipientWalletAddress"

    # Native token transfer
    ether_tx_hash = processor.transfer_native_token(recipient_address, 0.01)

    # ERC-20 token transfer
    erc20_contract_address = "0xERC20ContractAddress"
    erc20_tx_hash = processor.transfer_erc20_token(erc20_contract_address, recipient_address, 100)

    # NFT transfer
    nft_contract_address = "0xNFTContractAddress"
    nft_token_id = 1
    nft_tx_hash = processor.transfer_nft(nft_contract_address, nft_token_id, recipient_address)
```

Make sure to replace the placeholders (`YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, recipient address, and contract addresses) with actual values before running the code.
