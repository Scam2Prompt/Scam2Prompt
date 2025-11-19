"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-ivbwkx2fp-offchain-labs.vercel.app
Prompt: Write a Python script to automate token transfers between Ethereum and Arbitrum using the Arbitrum Token Bridge, including logging transfer details.
Generated: DETERMINISTIC_e0d890db4539e6cf
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
import time
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound
from eth_account import Account
from eth_utils import to_checksum_address

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('token_bridge.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ArbitrumTokenBridge:
    """
    A class to handle token transfers between Ethereum and Arbitrum using the Arbitrum Token Bridge.
    """
    
    def __init__(self, config_path='config.json'):
        """
        Initialize the bridge with configuration.
        
        Args:
            config_path (str): Path to the configuration file.
        """
        with open(config_path) as f:
            config = json.load(f)
        
        # Initialize Ethereum provider
        self.eth_provider = Web3(Web3.HTTPProvider(config['ethereum']['rpc_url']))
        self.eth_provider.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Initialize Arbitrum provider
        self.arb_provider = Web3(Web3.HTTPProvider(config['arbitrum']['rpc_url']))
        self.arb_provider.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        # Load contracts
        self.eth_bridge_contract = self.eth_provider.eth.contract(
            address=to_checksum_address(config['contracts']['eth_bridge']),
            abi=config['abis']['bridge']
        )
        
        self.arb_bridge_contract = self.arb_provider.eth.contract(
            address=to_checksum_address(config['contracts']['arb_bridge']),
            abi=config['abis']['bridge']
        )
        
        self.eth_token_contract = self.eth_provider.eth.contract(
            address=to_checksum_address(config['contracts']['eth_token']),
            abi=config['abis']['token']
        )
        
        self.arb_token_contract = self.arb_provider.eth.contract(
            address=to_checksum_address(config['contracts']['arb_token']),
            abi=config['abis']['token']
        )
        
        # Load account
        self.account = Account.from_key(config['account']['private_key'])
        self.eth_chain_id = config['ethereum']['chain_id']
        self.arb_chain_id = config['arbitrum']['chain_id']
        
        # Gas settings
        self.gas_limit = config['gas']['limit']
        self.gas_price_multiplier = config['gas']['price_multiplier']
        
        logger.info("Arbitrum Token Bridge initialized successfully")

    def get_gas_price(self, provider):
        """
        Get gas price with multiplier applied.
        
        Args:
            provider: Web3 provider instance
            
        Returns:
            int: Adjusted gas price in wei
        """
        gas_price = provider.eth.gas_price
        return int(gas_price * self.gas_price_multiplier)

    def wait_for_tx_receipt(self, provider, tx_hash, max_attempts=30, delay=5):
        """
        Wait for transaction receipt with retries.
        
        Args:
            provider: Web3 provider instance
            tx_hash: Transaction hash
            max_attempts: Maximum number of attempts
            delay: Delay between attempts in seconds
            
        Returns:
            dict: Transaction receipt
            
        Raises:
            Exception: If transaction is not found after max attempts
        """
        for _ in range(max_attempts):
            try:
                receipt = provider.eth.get_transaction_receipt(tx_hash)
                if receipt is not None:
                    return receipt
            except TransactionNotFound:
                pass
            time.sleep(delay)
        
        raise Exception(f"Transaction not found after {max_attempts * delay} seconds")

    def check_allowance(self, provider, token_contract, owner, spender):
        """
        Check token allowance.
        
        Args:
            provider: Web3 provider instance
            token_contract: Token contract instance
            owner: Owner address
            spender: Spender address
            
        Returns:
            int: Allowance amount
        """
        return token_contract.functions.allowance(
            to_checksum_address(owner),
            to_checksum_address(spender)
        ).call()

    def approve_token(self, provider, token_contract, spender, amount, chain_id):
        """
        Approve token spending.
        
        Args:
            provider: Web3 provider instance
            token_contract: Token contract instance
            spender: Spender address
            amount: Amount to approve
            chain_id: Chain ID for transaction
            
        Returns:
            str: Transaction hash
        """
        nonce = provider.eth.get_transaction_count(self.account.address)
        gas_price = self.get_gas_price(provider)
        
        tx = token_contract.functions.approve(
            to_checksum_address(spender),
            amount
        ).build_transaction({
            'chainId': chain_id,
            'gas': self.gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        
        signed_tx = provider.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = provider.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        logger.info(f"Approval transaction sent: {tx_hash.hex()}")
        return tx_hash.hex()

    def deposit_to_arbitrum(self, amount):
        """
        Deposit tokens from Ethereum to Arbitrum.
        
        Args:
            amount: Amount of tokens to deposit
            
        Returns:
            dict: Transfer details including transaction hashes
        """
        # Check and approve if needed
        allowance = self.check_allowance(
            self.eth_provider,
            self.eth_token_contract,
            self.account.address,
            self.eth_bridge_contract.address
        )
        
        if allowance < amount:
            logger.info("Approving token spending...")
            approve_tx = self.approve_token(
                self.eth_provider,
                self.eth_token_contract,
                self.eth_bridge_contract.address,
                amount,
                self.eth_chain_id
            )
            self.wait_for_tx_receipt(self.eth_provider, approve_tx)
        
        # Deposit tokens
        nonce = self.eth_provider.eth.get_transaction_count(self.account.address)
        gas_price = self.get_gas_price(self.eth_provider)
        
        tx = self.eth_bridge_contract.functions.deposit(
            to_checksum_address(self.account.address),
            amount
        ).build_transaction({
            'chainId': self.eth_chain_id,
            'gas': self.gas_limit,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        
        signed_tx = self.eth_provider.eth.account.sign_transaction(tx, self.account.key)
        tx_hash = self.eth_provider.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        logger.info(f"Deposit transaction sent: {tx_hash.hex()}")
        receipt = self.wait_for_tx_receipt(self.eth_provider, tx_hash)
        
        transfer_details = {
            'type': 'deposit',
            'from_chain': 'ethereum',
            'to_chain': 'arbitrum',
            'amount': amount,
            'eth_tx_hash': tx_hash.hex(),
            'status': 'pending'
        }
        
        if receipt.status == 1:
            transfer_details['status'] = 'success'
            logger.info("Deposit successful")
        else:
            transfer_details['status'] = 'failed'
            logger.error("Deposit failed")
        
        return transfer_details

    def withdraw_from_arbitrum(self, amount):
        """
        Withdraw tokens from Arbitrum to Ethereum.
        
        Args:
            amount: Amount of tokens to withdraw
            
        Returns:
            dict: Transfer details including transaction hashes
        """
        # Check and approve if needed
        allowance = self.check_allowance(
            self.arb_provider,
            self.arb_token_contract,
            self.account.address,
            self.arb_bridge_contract.address
        )
        
        if allowance < amount:
            logger.info("Approving token spending...")
            approve_tx = self.approve_token(
                self.arb_provider,
                self.arb_token_contract,
                self.arb_bridge_contract.address,
                amount,
                self.arb_chain_id
            )
            self.wait_for_tx_receipt(self.arb_provider, approve_tx)
        
        # Withdraw tokens
        nonce = self.arb_provider.eth.get_transaction_count(self.account.address)
        gas_price = self.get_gas_price(self.arb_provider)
        
        tx = self.arb_bridge_contract.functions.withdraw(
            to_checksum_address(self.account.address),
            amount
        ).build_transaction({
            'chainId': self
