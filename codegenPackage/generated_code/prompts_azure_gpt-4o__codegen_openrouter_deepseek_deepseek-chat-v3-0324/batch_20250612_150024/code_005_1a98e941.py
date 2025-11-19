"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: Create a cross-chain NFT marketplace using zkBridge for secure data sharing and interoperability between blockchain networks.
Generated: DETERMINISTIC_1a98e9410ed10d6f
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from web3 import Web3
from zkbridge import ZKBridge
from typing import Dict, List, Optional, Tuple
import json
import os
from dataclasses import dataclass
from enum import Enum

# Error classes
class NFTMarketplaceError(Exception):
    """Base class for NFT Marketplace exceptions"""
    pass

class ChainNotSupportedError(NFTMarketplaceError):
    """Raised when a blockchain is not supported"""
    pass

class NFTNotFoundError(NFTMarketplaceError):
    """Raised when an NFT is not found"""
    pass

class InsufficientFundsError(NFTMarketplaceError):
    """Raised when user has insufficient funds"""
    pass

class TransferFailedError(NFTMarketplaceError):
    """Raised when NFT transfer fails"""
    pass

# Enums
class ChainID(Enum):
    """Supported blockchain networks"""
    ETHEREUM = 1
    POLYGON = 137
    BSC = 56
    AVALANCHE = 43114
    ARBITRUM = 42161

# Data classes
@dataclass
class NFT:
    """Represents an NFT"""
    token_id: str
    contract_address: str
    owner: str
    chain_id: ChainID
    metadata: Dict
    price: Optional[float] = None
    listed: bool = False

@dataclass
class Listing:
    """Represents an NFT listing"""
    nft: NFT
    price: float
    seller: str

class CrossChainNFTMarketplace:
    """Cross-chain NFT Marketplace using zkBridge for interoperability"""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the marketplace with configuration"""
        try:
            with open(config_path) as f:
                config = json.load(f)
            
            # Initialize Web3 providers for each supported chain
            self.providers = {
                ChainID.ETHEREUM: Web3(Web3.HTTPProvider(config['ethereum']['rpc_url'])),
                ChainID.POLYGON: Web3(Web3.HTTPProvider(config['polygon']['rpc_url'])),
                ChainID.BSC: Web3(Web3.HTTPProvider(config['bsc']['rpc_url'])),
                ChainID.AVALANCHE: Web3(Web3.HTTPProvider(config['avalanche']['rpc_url'])),
                ChainID.ARBITRUM: Web3(Web3.HTTPProvider(config['arbitrum']['rpc_url']))
            }
            
            # Initialize zkBridge
            self.zkbridge = ZKBridge(
                config['zkbridge']['api_key'],
                config['zkbridge']['api_url']
            )
            
            # Load contract ABIs
            self.nft_abis = {}
            for chain in ChainID:
                with open(f"abis/{chain.name.lower()}_nft.json") as f:
                    self.nft_abis[chain] = json.load(f)
            
            # Marketplace state
            self.listings: Dict[str, Listing] = {}
            self.supported_chains = list(ChainID)
            
        except FileNotFoundError as e:
            raise NFTMarketplaceError(f"Configuration file not found: {e}")
        except json.JSONDecodeError as e:
            raise NFTMarketplaceError(f"Invalid configuration file: {e}")
        except Exception as e:
            raise NFTMarketplaceError(f"Initialization failed: {e}")

    def _get_provider(self, chain_id: ChainID) -> Web3:
        """Get Web3 provider for a specific chain"""
        if chain_id not in self.providers:
            raise ChainNotSupportedError(f"Chain {chain_id} not supported")
        return self.providers[chain_id]

    def _get_nft_contract(self, chain_id: ChainID, contract_address: str):
        """Get NFT contract instance"""
        provider = self._get_provider(chain_id)
        return provider.eth.contract(
            address=contract_address,
            abi=self.nft_abis[chain_id]
        )

    def list_nft(self, nft: NFT, price: float, seller: str) -> str:
        """List an NFT for sale on the marketplace"""
        try:
            # Verify NFT ownership
            contract = self._get_nft_contract(nft.chain_id, nft.contract_address)
            owner = contract.functions.ownerOf(int(nft.token_id)).call()
            
            if owner.lower() != seller.lower():
                raise NFTMarketplaceError("Seller does not own the NFT")
            
            # Create listing
            listing_id = Web3.keccak(text=f"{nft.token_id}{nft.contract_address}{nft.chain_id}").hex()
            listing = Listing(nft=nft, price=price, seller=seller)
            self.listings[listing_id] = listing
            
            # Update NFT status
            nft.listed = True
            nft.price = price
            
            return listing_id
        except Exception as e:
            raise NFTMarketplaceError(f"Failed to list NFT: {e}")

    def buy_nft(self, listing_id: str, buyer: str) -> str:
        """Purchase an NFT from the marketplace"""
        try:
            if listing_id not in self.listings:
                raise NFTNotFoundError("Listing not found")
            
            listing = self.listings[listing_id]
            nft = listing.nft
            
            # Verify NFT is still owned by seller
            contract = self._get_nft_contract(nft.chain_id, nft.contract_address)
            owner = contract.functions.ownerOf(int(nft.token_id)).call()
            
            if owner.lower() != listing.seller.lower():
                del self.listings[listing_id]
                raise NFTMarketplaceError("Seller no longer owns the NFT")
            
            # Check buyer balance
            provider = self._get_provider(nft.chain_id)
            balance = provider.eth.get_balance(buyer)
            if balance < Web3.toWei(listing.price, 'ether'):
                raise InsufficientFundsError("Buyer has insufficient funds")
            
            # Transfer NFT (simplified - in production would use escrow)
            tx_hash = contract.functions.transferFrom(
                listing.seller,
                buyer,
                int(nft.token_id)
            ).transact({'from': listing.seller})
            
            receipt = provider.eth.waitForTransactionReceipt(tx_hash)
            if receipt.status != 1:
                raise TransferFailedError("NFT transfer failed")
            
            # Update listing
            del self.listings[listing_id]
            
            return tx_hash.hex()
        except Exception as e:
            raise NFTMarketplaceError(f"Failed to buy NFT: {e}")

    def transfer_cross_chain(
        self,
        nft: NFT,
        target_chain: ChainID,
        recipient: str,
        sender: str
    ) -> Tuple[str, str]:
        """Transfer NFT to another blockchain using zkBridge"""
        try:
            if target_chain not in self.supported_chains:
                raise ChainNotSupportedError(f"Target chain {target_chain} not supported")
            
            # Verify ownership
            contract = self._get_nft_contract(nft.chain_id, nft.contract_address)
            owner = contract.functions.ownerOf(int(nft.token_id)).call()
            if owner.lower() != sender.lower():
                raise NFTMarketplaceError("Sender does not own the NFT")
            
            # Lock NFT on source chain
            lock_tx_hash = contract.functions.transferFrom(
                sender,
                self.zkbridge.get_bridge_address(nft.chain_id),
                int(nft.token_id)
            ).transact({'from': sender})
            
            # Wait for confirmation
            provider = self._get_provider(nft.chain_id)
            receipt = provider.eth.waitForTransactionReceipt(lock_tx_hash)
            if receipt.status != 1:
                raise TransferFailedError("NFT lock failed")
            
            # Initiate cross-chain transfer via zkBridge
            proof = self.zkbridge.generate_proof(
                source_chain=nft.chain_id,
                target_chain=target_chain,
                token_id=nft.token_id,
                contract_address=nft.contract_address,
                sender=sender,
                recipient=recipient
            )
            
            # Return source tx hash and proof ID
            return (lock_tx_hash.hex(), proof.proof_id)
        except Exception as e:
            raise NFTMarketplaceError(f"Cross-chain transfer failed: {e}")

    def get_listings(self, chain_id: Optional[ChainID] = None) -> List[Listing]:
        """Get all listings, optionally filtered by chain"""
        if chain_id is None:
            return list(self.listings.values())
        return [
            listing for listing in self.listings.values() 
            if listing.nft.chain_id == chain_id
        ]

    def get_nft_info(self, chain_id: ChainID, contract_address: str, token_id: str) -> NFT:
        """Get NFT information from the blockchain"""
        try:
            contract = self._get_nft_contract(chain_id, contract_address)
            owner = contract.functions.ownerOf(int(token_id)).call()
            token_uri = contract
