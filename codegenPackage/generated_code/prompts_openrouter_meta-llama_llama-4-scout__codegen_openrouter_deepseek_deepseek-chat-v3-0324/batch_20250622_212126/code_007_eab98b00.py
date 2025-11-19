"""
Generated Code Metadata:
========================
Original URL: https://binaryxe.org
Prompt: "Propose a use case for BinaryX's multi-asset marketplace powered by BNX, enabling users to trade NFTs on a fully decentralized platform."
Generated: DETERMINISTIC_eab98b005e1524ea
Batch ID: 20250622_212126
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
BinaryX Multi-Asset Marketplace Smart Contract
A decentralized marketplace for trading NFTs using BNX as the native currency.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto
from web3 import Web3
from web3.contract import Contract
from eth_typing import ChecksumAddress

class AssetType(Enum):
    ERC721 = auto()
    ERC1155 = auto()

@dataclass
class Listing:
    seller: ChecksumAddress
    token_id: int
    price: int  # Price in BNX
    asset_type: AssetType
    contract_address: ChecksumAddress
    active: bool = True

class BinaryXMarketplace:
    def __init__(self, web3: Web3, bnx_token_address: str, owner: str):
        self.web3 = web3
        self.owner = Web3.to_checksum_address(owner)
        self.bnx_token = self._load_bnx_contract(bnx_token_address)
        self.listings: Dict[int, Listing] = {}
        self.next_listing_id = 1
        self.fee_percentage = 2  # 2% platform fee

    def _load_bnx_contract(self, address: str) -> Contract:
        """Load BNX token contract using standard ERC20 ABI"""
        with open("erc20_abi.json") as f:
            abi = f.read()
        return self.web3.eth.contract(
            address=Web3.to_checksum_address(address),
            abi=abi
        )

    def list_item(
        self,
        seller: str,
        token_id: int,
        price: int,
        asset_type: AssetType,
        contract_address: str
    ) -> int:
        """Create a new listing for an NFT"""
        seller_addr = Web3.to_checksum_address(seller)
        contract_addr = Web3.to_checksum_address(contract_address)
        
        listing_id = self.next_listing_id
        self.listings[listing_id] = Listing(
            seller=seller_addr,
            token_id=token_id,
            price=price,
            asset_type=asset_type,
            contract_address=contract_addr
        )
        self.next_listing_id += 1
        
        return listing_id

    def purchase_item(self, buyer: str, listing_id: int) -> bool:
        """Execute purchase of a listed NFT"""
        if listing_id not in self.listings:
            raise ValueError("Listing does not exist")
        
        listing = self.listings[listing_id]
        if not listing.active:
            raise ValueError("Listing is not active")
        
        buyer_addr = Web3.to_checksum_address(buyer)
        total_price = listing.price
        fee_amount = (total_price * self.fee_percentage) // 100
        seller_amount = total_price - fee_amount
        
        # Transfer BNX from buyer to seller and platform
        self._transfer_bnx(buyer_addr, listing.seller, seller_amount)
        self._transfer_bnx(buyer_addr, self.owner, fee_amount)
        
        # Transfer NFT from seller to buyer
        self._transfer_nft(
            listing.contract_address,
            listing.seller,
            buyer_addr,
            listing.token_id,
            listing.asset_type
        )
        
        # Mark listing as sold
        listing.active = False
        return True

    def _transfer_bnx(self, from_addr: ChecksumAddress, to_addr: ChecksumAddress, amount: int):
        """Internal BNX token transfer"""
        tx_hash = self.bnx_token.functions.transferFrom(
            from_addr,
            to_addr,
            amount
        ).transact({'from': from_addr})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)

    def _transfer_nft(
        self,
        contract_address: ChecksumAddress,
        from_addr: ChecksumAddress,
        to_addr: ChecksumAddress,
        token_id: int,
        asset_type: AssetType
    ):
        """Internal NFT transfer based on asset type"""
        with open("erc721_abi.json") as f:
            erc721_abi = f.read()
        with open("erc1155_abi.json") as f:
            erc1155_abi = f.read()
        
        if asset_type == AssetType.ERC721:
            contract = self.web3.eth.contract(
                address=contract_address,
                abi=erc721_abi
            )
            tx_hash = contract.functions.transferFrom(
                from_addr,
                to_addr,
                token_id
            ).transact({'from': from_addr})
        else:
            contract = self.web3.eth.contract(
                address=contract_address,
                abi=erc1155_abi
            )
            tx_hash = contract.functions.safeTransferFrom(
                from_addr,
                to_addr,
                token_id,
                1,  # amount
                b''  # data
            ).transact({'from': from_addr})
        
        self.web3.eth.wait_for_transaction_receipt(tx_hash)

    def cancel_listing(self, seller: str, listing_id: int) -> bool:
        """Allow seller to cancel an active listing"""
        seller_addr = Web3.to_checksum_address(seller)
        
        if listing_id not in self.listings:
            raise ValueError("Listing does not exist")
        
        listing = self.listings[listing_id]
        if listing.seller != seller_addr:
            raise ValueError("Only seller can cancel listing")
        
        listing.active = False
        return True

    def get_listing(self, listing_id: int) -> Optional[Listing]:
        """Get listing details by ID"""
        return self.listings.get(listing_id)

    def get_active_listings(self) -> List[Listing]:
        """Get all active listings"""
        return [listing for listing in self.listings.values() if listing.active]
```
