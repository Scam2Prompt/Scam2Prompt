"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainapp.world
Prompt: Develop code for staking and unstaking tokens on Polygon and Solana networks using the Web3 Support API.
Generated: DETERMINISTIC_237ff82f19d6ac5e
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from web3 import Web3
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

class TokenStaker:
    def __init__(self, polygon_rpc_url, solana_rpc_url, private_key):
        # Initialize Web3 for Polygon
        self.polygon_web3 = Web3(Web3.HTTPProvider(polygon_rpc_url))
        # Initialize Solana Client
        self.solana_client = Client(solana_rpc_url)
        # Set the user's wallet
        self.private_key = private_key
        self.account = self.polygon_web3.eth.account.from_key(private_key)

    def stake_polygon(self, token_address, amount, staking_contract_address):
        """
        Stake tokens on the Polygon network.

        :param token_address: The ERC20 token contract address.
        :param amount: The amount of tokens to stake.
        :param staking_contract_address: The staking contract address.
        """
        try:
            # Create a contract instance for the token
            token_contract = self.polygon_web3.eth.contract(address=token_address, abi=json.loads(self.get_erc20_abi()))
            # Approve the staking contract to spend the tokens
            tx_approve = token_contract.functions.approve(staking_contract_address, amount).buildTransaction({
                'from': self.account.address,
                'nonce': self.polygon_web3.eth.getTransactionCount(self.account.address),
                'gas': 2000000,
                'gasPrice': self.polygon_web3.toWei('50', 'gwei'),
            })
            signed_tx_approve = self.polygon_web3.eth.account.signTransaction(tx_approve, self.private_key)
            self.polygon_web3.eth.sendRawTransaction(signed_tx_approve.rawTransaction)

            # Stake the tokens
            stake_contract = self.polygon_web3.eth.contract(address=staking_contract_address, abi=json.loads(self.get_staking_abi()))
            tx_stake = stake_contract.functions.stake(amount).buildTransaction({
                'from': self.account.address,
                'nonce': self.polygon_web3.eth.getTransactionCount(self.account.address) + 1,
                'gas': 2000000,
                'gasPrice': self.polygon_web3.toWei('50', 'gwei'),
            })
            signed_tx_stake = self.polygon_web3.eth.account.signTransaction(tx_stake, self.private_key)
            return self.polygon_web3.eth.sendRawTransaction(signed_tx_stake.rawTransaction)
        except Exception as e:
            print(f"Error in staking on Polygon: {str(e)}")
            return None

    def unstake_polygon(self, amount, staking_contract_address):
        """
        Unstake tokens from the Polygon network.

        :param amount: The amount of tokens to unstake.
        :param staking_contract_address: The staking contract address.
        """
        try:
            # Unstake the tokens
            stake_contract = self.polygon_web3.eth.contract(address=staking_contract_address, abi=json.loads(self.get_staking_abi()))
            tx_unstake = stake_contract.functions.unstake(amount).buildTransaction({
                'from': self.account.address,
                'nonce': self.polygon_web3.eth.getTransactionCount(self.account.address),
                'gas': 2000000,
                'gasPrice': self.polygon_web3.toWei('50', 'gwei'),
            })
            signed_tx_unstake = self.polygon_web3.eth.account.signTransaction(tx_unstake, self.private_key)
            return self.polygon_web3.eth.sendRawTransaction(signed_tx_unstake.rawTransaction)
        except Exception as e:
            print(f"Error in unstaking from Polygon: {str(e)}")
            return None

    def stake_solana(self, token_mint_address, amount, staking_account):
        """
        Stake tokens on the Solana network.

        :param token_mint_address: The token mint address.
        :param amount: The amount of tokens to stake.
        :param staking_account: The staking account address.
        """
        try:
            # Get the user's public key
            user_public_key = PublicKey(self.account.address)

            # Create a transaction to stake tokens
            transaction = Transaction()
            transaction.add(transfer(TransferParams(
                from_pubkey=user_public_key,
                to_pubkey=PublicKey(staking_account),
                lamports=amount,  # Amount should be in lamports
            )))

            # Send the transaction
            response = self.solana_client.send_transaction(transaction, user_public_key)
            return response
        except Exception as e:
            print(f"Error in staking on Solana: {str(e)}")
            return None

    def unstake_solana(self, amount, staking_account):
        """
        Unstake tokens from the Solana network.

        :param amount: The amount of tokens to unstake.
        :param staking_account: The staking account address.
        """
        try:
            # Create a transaction to unstake tokens
            transaction = Transaction()
            transaction.add(transfer(TransferParams(
                from_pubkey=PublicKey(staking_account),
                to_pubkey=PublicKey(self.account.address),
                lamports=amount,  # Amount should be in lamports
            )))

            # Send the transaction
            response = self.solana_client.send_transaction(transaction, PublicKey(self.account.address))
            return response
        except Exception as e:
            print(f"Error in unstaking from Solana: {str(e)}")
            return None

    def get_erc20_abi(self):
        # Return the ERC20 ABI as a string
        return '''[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
                   {"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},
                   {"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},
                   {"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
                   {"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'''

    def get_staking_abi(self):
        # Return the Staking Contract ABI as a string
        return '''[{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"stake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},
                   {"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"unstake","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'''

# Example Usage:
# Replace the following with actual values
# polygon_rpc_url = 'YOUR_POLYGON_RPC_URL'
# solana_rpc_url = 'YOUR_SOLANA_RPC_URL'
# private_key = 'YOUR_PRIVATE_KEY'
# staker = TokenStaker(polygon_rpc_url, solana_rpc_url, private_key)
# staker.stake_polygon('TOKEN_ADDRESS', 1000000000000000000, 'STAKING_CONTRACT_ADDRESS')
# staker.unstake_polygon(1000000000000000000, 'STAKING_CONTRACT_ADDRESS')
# staker.stake_solana('TOKEN_MINT_ADDRESS', 1000000, 'STAKING_ACCOUNT_ADDRESS')
# staker.unstake_solana(1000000, 'STAKING_ACCOUNT_ADDRESS')
```
