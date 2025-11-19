"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ivbwkx2fp-offchain-labs.vercel.app
Prompt: Can you provide a code snippet for interacting with the Arbitrum token bridge API for token transfers?
Generated: DETERMINISTIC_78c171a82443deeb
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct

class ArbitrumTokenBridge:
    """
    A class to interact with the Arbitrum token bridge API for token transfers.
    Handles both deposit and withdrawal operations with proper error handling.
    """
    
    def __init__(self, rpc_url, bridge_api_url, private_key=None):
        """
        Initialize the bridge client.
        
        Args:
            rpc_url (str): Ethereum RPC URL
            bridge_api_url (str): Arbitrum bridge API endpoint
            private_key (str, optional): Private key for signing transactions
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.bridge_api_url = bridge_api_url
        self.private_key = private_key
        self.account = Account.from_key(private_key) if private_key else None
        
    def get_balance(self, token_address, wallet_address):
        """
        Get token balance for a wallet.
        
        Args:
            token_address (str): ERC20 token contract address
            wallet_address (str): Wallet address to check balance
            
        Returns:
            int: Token balance in wei
        """
        if not self.web3.is_checksum_address(token_address):
            token_address = self.web3.to_checksum_address(token_address)
        if not self.web3.is_checksum_address(wallet_address):
            wallet_address = self.web3.to_checksum_address(wallet_address)
            
        token_contract = self.web3.eth.contract(
            address=token_address,
            abi=self._get_erc20_abi()
        )
        return token_contract.functions.balanceOf(wallet_address).call()
    
    def deposit_tokens(self, token_address, amount, destination_address=None):
        """
        Deposit tokens from Ethereum to Arbitrum.
        
        Args:
            token_address (str): ERC20 token contract address
            amount (int): Amount to deposit in wei
            destination_address (str, optional): Destination address on Arbitrum
            
        Returns:
            dict: API response with deposit details
        """
        if not self.account:
            raise ValueError("Private key must be provided for deposit operations")
            
        if not destination_address:
            destination_address = self.account.address
            
        if not self.web3.is_checksum_address(token_address):
            token_address = self.web3.to_checksum_address(token_address)
        if not self.web3.is_checksum_address(destination_address):
            destination_address = self.web3.to_checksum_address(destination_address)
            
        # Get approval data
        approval_data = self._get_approval_data(token_address, amount)
        
        # Get deposit data
        deposit_data = self._get_deposit_data(
            token_address,
            amount,
            destination_address
        )
        
        # Send deposit transaction
        tx_hash = self._send_deposit_transaction(approval_data, deposit_data)
        
        return {
            "status": "success",
            "tx_hash": tx_hash,
            "token_address": token_address,
            "amount": amount,
            "destination_address": destination_address
        }
    
    def withdraw_tokens(self, token_address, amount, destination_address=None):
        """
        Withdraw tokens from Arbitrum to Ethereum.
        
        Args:
            token_address (str): ERC20 token contract address
            amount (int): Amount to withdraw in wei
            destination_address (str, optional): Destination address on Ethereum
            
        Returns:
            dict: API response with withdrawal details
        """
        if not self.account:
            raise ValueError("Private key must be provided for withdrawal operations")
            
        if not destination_address:
            destination_address = self.account.address
            
        if not self.web3.is_checksum_address(token_address):
            token_address = self.web3.to_checksum_address(token_address)
        if not self.web3.is_checksum_address(destination_address):
            destination_address = self.web3.to_checksum_address(destination_address)
            
        # Get withdrawal data from API
        withdrawal_data = self._get_withdrawal_data(
            token_address,
            amount,
            destination_address
        )
        
        # Sign and submit withdrawal
        signed_message = self._sign_withdrawal(withdrawal_data)
        response = self._submit_withdrawal(withdrawal_data, signed_message)
        
        return {
            "status": "success",
            "withdrawal_id": response.get("withdrawalId"),
            "token_address": token_address,
            "amount": amount,
            "destination_address": destination_address
        }
    
    def _get_erc20_abi(self):
        """Return standard ERC20 ABI."""
        return json.loads("""
            [
                {
                    "constant": true,
                    "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "type": "function"
                },
                {
                    "constant": false,
                    "inputs": [
                        {"name": "_spender", "type": "address"},
                        {"name": "_value", "type": "uint256"}
                    ],
                    "name": "approve",
                    "outputs": [{"name": "success", "type": "bool"}],
                    "type": "function"
                }
            ]
        """)
    
    def _get_approval_data(self, token_address, amount):
        """Get approval data for token transfer."""
        token_contract = self.web3.eth.contract(
            address=token_address,
            abi=self._get_erc20_abi()
        )
        
        # Get bridge address from API
        bridge_address = self._get_bridge_address()
        
        # Build approval transaction
        tx = token_contract.functions.approve(
            bridge_address,
            amount
        ).build_transaction({
            'from': self.account.address,
            'nonce': self.web3.eth.get_transaction_count(self.account.address),
            'gas': 200000,
            'gasPrice': self.web3.eth.gas_price
        })
        
        # Sign and send transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        # Wait for transaction receipt
        receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        
        if receipt.status != 1:
            raise Exception("Token approval transaction failed")
            
        return {
            "tx_hash": tx_hash.hex(),
            "token_address": token_address,
            "amount": amount
        }
    
    def _get_bridge_address(self):
        """Get bridge contract address from API."""
        try:
            response = requests.get(f"{self.bridge_api_url}/bridge-address")
            response.raise_for_status()
            data = response.json()
            return data["address"]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get bridge address: {str(e)}")
    
    def _get_deposit_data(self, token_address, amount, destination_address):
        """Get deposit data from bridge API."""
        try:
            payload = {
                "tokenAddress": token_address,
                "amount": str(amount),
                "destinationAddress": destination_address
            }
            response = requests.post(
                f"{self.bridge_api_url}/deposit",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get deposit data: {str(e)}")
    
    def _send_deposit_transaction(self, approval_data, deposit_data):
        """Send deposit transaction to bridge contract."""
        try:
            tx = {
                'from': self.account.address,
                'to': deposit_data['contractAddress'],
                'value': 0,
                'data': deposit_data['data'],
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
                'gas': deposit_data.get('gasLimit', 500000),
                'gasPrice': self.web3.eth.gas_price
            }
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if receipt.status != 1:
                raise Exception("Deposit transaction failed")
                
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Failed to send deposit transaction: {str(e)}")
    
    def _get_withdrawal_data(self, token_address, amount, destination_address):
        """Get withdrawal data from bridge API."""
        try:
            payload = {
                "tokenAddress": token_address,
                "amount": str(amount),
                "destinationAddress": destination_address
            }
            response = requests.post(
                f"{self.bridge_api_url}/withdraw",
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get withdrawal data: {str(e)}")
    
    def
