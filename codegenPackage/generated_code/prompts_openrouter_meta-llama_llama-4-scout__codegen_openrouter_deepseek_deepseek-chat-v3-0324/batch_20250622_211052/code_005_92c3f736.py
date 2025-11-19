"""
Generated Code Metadata:
========================
Original URL: https://openswe.io
Prompt: Develop a library for creating and managing NFTs on a blockchain-based marketplace for software engineers, using OpenSwe as a reference.
Generated: DETERMINISTIC_92c3f7362f60ad82
Batch ID: 20250622_211052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
NFT Marketplace Library for Software Engineers

This library provides functionality to create, manage, and trade NFTs
on a blockchain-based marketplace specifically designed for software engineers.
"""

import json
import hashlib
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class NFTStandard(Enum):
    """Supported NFT standards"""
    ERC721 = "ERC721"
    ERC1155 = "ERC1155"

class LicenseType(Enum):
    """Software license types"""
    MIT = "MIT"
    APACHE_2 = "Apache-2.0"
    GPL_3 = "GPL-3.0"
    PROPRIETARY = "Proprietary"

@dataclass
class SoftwareMetadata:
    """Metadata for software NFT"""
    name: str
    version: str
    description: str
    author: str
    repository_url: str
    license: LicenseType
    programming_language: str
    dependencies: List[str]

@dataclass
class NFT:
    """NFT representation"""
    token_id: str
    owner: str
    creator: str
    standard: NFTStandard
    metadata: SoftwareMetadata
    created_at: datetime
    price: Optional[float] = None
    for_sale: bool = False

class NFTMarketplace:
    """NFT Marketplace for Software Engineers"""
    
    def __init__(self, blockchain_network: str):
        self.blockchain_network = blockchain_network
        self.nfts: Dict[str, NFT] = {}
        self.owners: Dict[str, List[str]] = {}
        self.creators: Dict[str, List[str]] = {}
    
    def _generate_token_id(self, metadata: SoftwareMetadata) -> str:
        """Generate unique token ID from metadata"""
        data = f"{metadata.name}{metadata.version}{metadata.author}".encode('utf-8')
        return hashlib.sha256(data).hexdigest()
    
    def create_nft(
        self,
        creator: str,
        metadata: SoftwareMetadata,
        standard: NFTStandard = NFTStandard.ERC721,
        initial_price: Optional[float] = None
    ) -> NFT:
        """
        Create a new software NFT
        
        Args:
            creator: Wallet address of the creator
            metadata: Software metadata
            standard: NFT standard (default: ERC721)
            initial_price: Optional initial listing price
            
        Returns:
            Created NFT object
            
        Raises:
            ValueError: If metadata is invalid
        """
        if not metadata.name or not metadata.author:
            raise ValueError("Name and author are required in metadata")
            
        token_id = self._generate_token_id(metadata)
        
        if token_id in self.nfts:
            raise ValueError("NFT with this metadata already exists")
            
        nft = NFT(
            token_id=token_id,
            owner=creator,
            creator=creator,
            standard=standard,
            metadata=metadata,
            created_at=datetime.now(),
            price=initial_price,
            for_sale=initial_price is not None
        )
        
        self.nfts[token_id] = nft
        
        if creator not in self.creators:
            self.creators[creator] = []
        self.creators[creator].append(token_id)
        
        if creator not in self.owners:
            self.owners[creator] = []
        self.owners[creator].append(token_id)
        
        return nft
    
    def list_nft(self, token_id: str, price: float, owner: str) -> None:
        """
        List an NFT for sale
        
        Args:
            token_id: NFT identifier
            price: Listing price
            owner: Current owner wallet address
            
        Raises:
            ValueError: If NFT doesn't exist or owner is invalid
        """
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
            
        if self.nfts[token_id].owner != owner:
            raise ValueError("Only owner can list NFT for sale")
            
        self.nfts[token_id].price = price
        self.nfts[token_id].for_sale = True
    
    def purchase_nft(self, token_id: str, buyer: str, amount: float) -> NFT:
        """
        Purchase an NFT
        
        Args:
            token_id: NFT identifier
            buyer: Buyer wallet address
            amount: Purchase amount
            
        Returns:
            Updated NFT object
            
        Raises:
            ValueError: If NFT doesn't exist or purchase conditions aren't met
        """
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
            
        nft = self.nfts[token_id]
        
        if not nft.for_sale:
            raise ValueError("NFT is not for sale")
            
        if amount < nft.price:
            raise ValueError("Insufficient funds")
            
        # Remove from previous owner's list
        previous_owner = nft.owner
        self.owners[previous_owner].remove(token_id)
        
        # Update ownership
        nft.owner = buyer
        nft.for_sale = False
        nft.price = None
        
        # Add to new owner's list
        if buyer not in self.owners:
            self.owners[buyer] = []
        self.owners[buyer].append(token_id)
        
        return nft
    
    def get_nft(self, token_id: str) -> Optional[NFT]:
        """Get NFT by token ID"""
        return self.nfts.get(token_id)
    
    def get_nfts_by_owner(self, owner: str) -> List[NFT]:
        """Get all NFTs owned by a wallet address"""
        return [self.nfts[token_id] for token_id in self.owners.get(owner, [])]
    
    def get_nfts_by_creator(self, creator: str) -> List[NFT]:
        """Get all NFTs created by a wallet address"""
        return [self.nfts[token_id] for token_id in self.creators.get(creator, [])]
    
    def search_nfts(
        self,
        name: Optional[str] = None,
        author: Optional[str] = None,
        language: Optional[str] = None,
        license: Optional[LicenseType] = None
    ) -> List[NFT]:
        """
        Search NFTs by various criteria
        
        Args:
            name: Software name (partial match)
            author: Author name (partial match)
            language: Programming language
            license: License type
            
        Returns:
            List of matching NFTs
        """
        results = []
        
        for nft in self.nfts.values():
            match = True
            
            if name and name.lower() not in nft.metadata.name.lower():
                match = False
            if author and author.lower() not in nft.metadata.author.lower():
                match = False
            if language and language.lower() != nft.metadata.programming_language.lower():
                match = False
            if license and license != nft.metadata.license:
                match = False
                
            if match:
                results.append(nft)
                
        return results
    
    def transfer_nft(self, token_id: str, from_address: str, to_address: str) -> NFT:
        """
        Transfer NFT ownership without payment
        
        Args:
            token_id: NFT identifier
            from_address: Current owner wallet address
            to_address: New owner wallet address
            
        Returns:
            Updated NFT object
            
        Raises:
            ValueError: If NFT doesn't exist or from_address is not current owner
        """
        if token_id not in self.nfts:
            raise ValueError("NFT not found")
            
        if self.nfts[token_id].owner != from_address:
            raise ValueError("Only owner can transfer NFT")
            
        nft = self.nfts[token_id]
        
        # Remove from previous owner's list
        self.owners[from_address].remove(token_id)
        
        # Update ownership
        nft.owner = to_address
        nft.for_sale = False
        nft.price = None
        
        # Add to new owner's list
        if to_address not in self.owners:
            self.owners[to_address] = []
        self.owners[to_address].append(token_id)
        
        return nft
    
    def get_marketplace_stats(self) -> Dict[str, int]:
        """Get marketplace statistics"""
        return {
            "total_nfts": len(self.nfts),
            "total_owners": len(self.owners),
            "total_creators": len(self.creators),
            "nfts_for_sale": sum(1 for nft in self.nfts.values() if nft.for_sale)
        }
```
