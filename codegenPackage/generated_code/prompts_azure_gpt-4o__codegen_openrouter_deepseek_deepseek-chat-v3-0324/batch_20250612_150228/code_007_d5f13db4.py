"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Provide a code example for deploying BTC Smart Accounts using Particle Network's BTC Connect and managing cross-chain transactions.
Generated: DETERMINISTIC_d5f13db49bae6b89
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from particle import ParticleNetwork
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BTCCrossChainManager:
    """
    A class to manage BTC Smart Accounts and cross-chain transactions using Particle Network.
    """
    
    def __init__(self):
        # Initialize Particle Network with credentials from environment
        self.particle = ParticleNetwork(
            project_id=os.getenv('PARTICLE_PROJECT_ID'),
            client_key=os.getenv('PARTICLE_CLIENT_KEY'),
            app_id=os.getenv('PARTICLE_APP_ID')
        )
        
        # Initialize Web3 provider for EVM chains
        self.web3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URL')))
        
        # Set default chain ID (Ethereum Mainnet)
        self.default_chain_id = 1
        
    def connect_btc_wallet(self):
        """
        Connect to BTC wallet using Particle's BTC Connect.
        Returns the connected wallet address.
        """
        try:
            # Initialize BTC Connect
            btc_connect = self.particle.btc_connect()
            
            # Request wallet connection
            wallet_info = btc_connect.connect()
            
            if not wallet_info or not wallet_info.address:
                raise Exception("Failed to connect BTC wallet")
                
            return wallet_info.address
            
        except Exception as e:
            print(f"Error connecting BTC wallet: {str(e)}")
            raise
            
    def deploy_btc_smart_account(self, btc_address):
        """
        Deploy a BTC Smart Account for the given BTC address.
        Returns the deployed smart account address.
        """
        try:
            # Get smart account deployment parameters
            deployment_params = {
                "btc_address": btc_address,
                "chain_id": self.default_chain_id
            }
            
            # Deploy smart account
            result = self.particle.deploy_btc_smart_account(deployment_params)
            
            if not result or not result.smart_account_address:
                raise Exception("Failed to deploy BTC Smart Account")
                
            return result.smart_account_address
            
        except Exception as e:
            print(f"Error deploying BTC Smart Account: {str(e)}")
            raise
            
    def prepare_cross_chain_transaction(self, smart_account_address, destination_chain_id, token_address, amount):
        """
        Prepare a cross-chain transaction from BTC Smart Account to another chain.
        Returns the prepared transaction data.
        """
        try:
            # Validate inputs
            if not Web3.is_address(smart_account_address):
                raise ValueError("Invalid smart account address")
                
            if not Web3.is_address(token_address):
                raise ValueError("Invalid token address")
                
            # Prepare cross-chain payload
            payload = {
                "from_chain_id": self.default_chain_id,
                "to_chain_id": destination_chain_id,
                "from_address": smart_account_address,
                "token_address": token_address,
                "amount": amount
            }
            
            # Get fee estimation
            fee_estimation = self.particle.estimate_cross_chain_fee(payload)
            
            # Prepare full transaction
            transaction = {
                **payload,
                "fee": fee_estimation.fee,
                "fee_token": fee_estimation.fee_token
            }
            
            return transaction
            
        except Exception as e:
            print(f"Error preparing cross-chain transaction: {str(e)}")
            raise
            
    def sign_and_send_transaction(self, transaction, private_key):
        """
        Sign and send a prepared cross-chain transaction.
        Returns the transaction hash.
        """
        try:
            # Validate private key
            if not private_key or len(private_key) != 64:
                raise ValueError("Invalid private key")
                
            # Create account from private key
            account = Account.from_key(private_key)
            
            # Serialize transaction
            tx_dict = {
                'chainId': transaction['from_chain_id'],
                'to': transaction['to_address'],
                'value': transaction['amount'],
                'gas': 200000,  # Default gas limit
                'gasPrice': Web3.to_wei('50', 'gwei'),
                'nonce': self.web3.eth.get_transaction_count(account.address)
            }
            
            # Sign transaction
            signed_tx = account.sign_transaction(tx_dict)
            
            # Send transaction
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            return tx_hash.hex()
            
        except Exception as e:
            print(f"Error signing and sending transaction: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize manager
        manager = BTCCrossChainManager()
        
        # Connect BTC wallet
        btc_address = manager.connect_btc_wallet()
        print(f"Connected BTC Address: {btc_address}")
        
        # Deploy BTC Smart Account
        smart_account_address = manager.deploy_btc_smart_account(btc_address)
        print(f"Deployed Smart Account: {smart_account_address}")
        
        # Prepare cross-chain transaction (example: send to Polygon)
        transaction = manager.prepare_cross_chain_transaction(
            smart_account_address=smart_account_address,
            destination_chain_id=137,  # Polygon chain ID
            token_address="0xTokenAddress",  # Replace with actual token address
            amount=Web3.to_wei(1, 'ether')  # 1 token (assuming 18 decimals)
        )
        
        # Sign and send transaction (in production, private key should be securely managed)
        private_key = os.getenv('PRIVATE_KEY')  # WARNING: Never hardcode private keys
        if private_key:
            tx_hash = manager.sign_and_send_transaction(transaction, private_key)
            print(f"Transaction sent. Hash: {tx_hash}")
        else:
            print("No private key provided. Transaction prepared but not sent.")
            
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
```
