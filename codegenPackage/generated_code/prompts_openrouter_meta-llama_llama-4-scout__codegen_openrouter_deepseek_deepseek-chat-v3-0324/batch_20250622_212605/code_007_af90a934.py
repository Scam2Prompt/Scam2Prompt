"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Write a code example for integrating Story Staking with a multi-chain wallet, enabling seamless asset management across different blockchain networks.
Generated: DETERMINISTIC_af90a934c40cb4da
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from web3 import Web3
from typing import Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum

class BlockchainNetwork(Enum):
    ETHEREUM = "ethereum"
    BINANCE_SMART_CHAIN = "binance-smart-chain"
    POLYGON = "polygon"
    AVALANCHE = "avalanche"

@dataclass
class WalletAsset:
    network: BlockchainNetwork
    token_address: str
    symbol: str
    balance: float
    decimals: int

class MultiChainWallet:
    """
    A multi-chain wallet implementation supporting Story Staking integration.
    """
    
    def __init__(self, rpc_urls: Dict[BlockchainNetwork, str], wallet_address: str):
        """
        Initialize the multi-chain wallet with RPC URLs and wallet address.
        
        Args:
            rpc_urls: Dictionary mapping networks to their RPC URLs
            wallet_address: The wallet address to manage
        """
        self.rpc_urls = rpc_urls
        self.wallet_address = wallet_address
        self.web3_clients = {
            network: Web3(Web3.HTTPProvider(url)) 
            for network, url in rpc_urls.items()
        }
        
    def get_balance(self, network: BlockchainNetwork) -> float:
        """
        Get native token balance for the specified network.
        
        Args:
            network: The blockchain network to query
            
        Returns:
            float: The balance in native units
        """
        if network not in self.web3_clients:
            raise ValueError(f"Unsupported network: {network}")
            
        w3 = self.web3_clients[network]
        balance_wei = w3.eth.get_balance(self.wallet_address)
        return w3.from_wei(balance_wei, 'ether')
    
    def get_token_balance(
        self,
        network: BlockchainNetwork,
        token_address: str,
        abi: Optional[List[Dict]] = None
    ) -> WalletAsset:
        """
        Get ERC20 token balance for the specified network and token.
        
        Args:
            network: The blockchain network to query
            token_address: The token contract address
            abi: Optional ABI for the token contract
            
        Returns:
            WalletAsset: Object containing token details and balance
        """
        if network not in self.web3_clients:
            raise ValueError(f"Unsupported network: {network}")
            
        w3 = self.web3_clients[network]
        
        # Default ERC20 ABI if not provided
        if abi is None:
            abi = [
                {
                    "constant": True,
                    "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "decimals",
                    "outputs": [{"name": "", "type": "uint8"}],
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "symbol",
                    "outputs": [{"name": "", "type": "string"}],
                    "type": "function"
                }
            ]
            
        contract = w3.eth.contract(address=token_address, abi=abi)
        
        try:
            symbol = contract.functions.symbol().call()
            decimals = contract.functions.decimals().call()
            balance = contract.functions.balanceOf(self.wallet_address).call()
            
            return WalletAsset(
                network=network,
                token_address=token_address,
                symbol=symbol,
                balance=balance / (10 ** decimals),
                decimals=decimals
            )
        except Exception as e:
            raise ValueError(f"Error fetching token balance: {str(e)}")
    
    def stake_assets(
        self,
        network: BlockchainNetwork,
        token_address: str,
        amount: float,
        staking_contract_address: str,
        staking_contract_abi: List[Dict]
    ) -> str:
        """
        Stake assets to Story Staking contract.
        
        Args:
            network: The blockchain network
            token_address: The token to stake
            amount: Amount to stake
            staking_contract_address: Story Staking contract address
            staking_contract_abi: Story Staking contract ABI
            
        Returns:
            str: Transaction hash
        """
        if network not in self.web3_clients:
            raise ValueError(f"Unsupported network: {network}")
            
        w3 = self.web3_clients[network]
        
        # Get token details
        token = self.get_token_balance(network, token_address)
        
        # Initialize contracts
        token_contract = w3.eth.contract(
            address=token_address,
            abi=[
                {
                    "constant": False,
                    "inputs": [
                        {"name": "_spender", "type": "address"},
                        {"name": "_value", "type": "uint256"}
                    ],
                    "name": "approve",
                    "outputs": [{"name": "", "type": "bool"}],
                    "type": "function"
                }
            ]
        )
        
        staking_contract = w3.eth.contract(
            address=staking_contract_address,
            abi=staking_contract_abi
        )
        
        # Convert amount to token units
        amount_units = int(amount * (10 ** token.decimals))
        
        try:
            # Approve staking contract to spend tokens
            approve_tx = token_contract.functions.approve(
                staking_contract_address,
                amount_units
            ).build_transaction({
                'from': self.wallet_address,
                'nonce': w3.eth.get_transaction_count(self.wallet_address),
                'gas': 200000,
                'gasPrice': w3.eth.gas_price
            })
            
            signed_approve = w3.eth.account.sign_transaction(
                approve_tx,
                private_key="YOUR_PRIVATE_KEY"  # In production, use secure key management
            )
            approve_hash = w3.eth.send_raw_transaction(signed_approve.rawTransaction)
            w3.eth.wait_for_transaction_receipt(approve_hash)
            
            # Stake tokens
            stake_tx = staking_contract.functions.stake(
                token_address,
                amount_units
            ).build_transaction({
                'from': self.wallet_address,
                'nonce': w3.eth.get_transaction_count(self.wallet_address),
                'gas': 300000,
                'gasPrice': w3.eth.gas_price
            })
            
            signed_stake = w3.eth.account.sign_transaction(
                stake_tx,
                private_key="YOUR_PRIVATE_KEY"  # In production, use secure key management
            )
            stake_hash = w3.eth.send_raw_transaction(signed_stake.rawTransaction)
            
            return stake_hash.hex()
            
        except Exception as e:
            raise ValueError(f"Staking failed: {str(e)}")
    
    def get_staked_assets(
        self,
        network: BlockchainNetwork,
        staking_contract_address: str,
        staking_contract_abi: List[Dict],
        token_addresses: List[str]
    ) -> List[WalletAsset]:
        """
        Get staked assets from Story Staking contract.
        
        Args:
            network: The blockchain network
            staking_contract_address: Story Staking contract address
            staking_contract_abi: Story Staking contract ABI
            token_addresses: List of token addresses to check
            
        Returns:
            List[WalletAsset]: List of staked assets
        """
        if network not in self.web3_clients:
            raise ValueError(f"Unsupported network: {network}")
            
        w3 = self.web3_clients[network]
        staking_contract = w3.eth.contract(
            address=staking_contract_address,
            abi=staking_contract_abi
        )
        
        staked_assets = []
        
        for token_address in token_addresses:
            try:
                token = self.get_token_balance(network, token_address)
                staked_amount = staking_contract.functions.getStakedAmount(
                    self.wallet_address,
                    token_address
                ).call()
                
                staked_assets.append(WalletAsset(
                    network=network,
                    token_address=token_address,
                    symbol=token.symbol,
                    balance=staked_amount / (10 ** token.decimals),
                    decimals=token.decimals
                ))
            except Exception as e:
                print(f"Error fetching staked amount for {token_address}: {str(e)}")
                continue
                
        return staked_assets

class StoryStakingAPI:
    """
    Helper class for interacting with Story Staking API endpoints.
    """
    
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url
        
    def get_staking_contracts(self) -> Dict[BlockchainNetwork, str]:
        """
        Get Story Staking
