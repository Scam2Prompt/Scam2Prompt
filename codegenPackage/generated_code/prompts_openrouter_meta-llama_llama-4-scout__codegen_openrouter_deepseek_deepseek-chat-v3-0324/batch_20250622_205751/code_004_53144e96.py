"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Develop a simple decentralized application (dApp) for peer-to-peer trading of cryptocurrencies and NFTs using a blockchain-based aggregator/router.
Generated: DETERMINISTIC_53144e9652ba5c37
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AssetType(Enum):
    CRYPTO = 1
    NFT = 2

@dataclass
class Asset:
    asset_type: AssetType
    contract_address: str
    token_id: Optional[int] = None
    amount: Optional[int] = None

@dataclass
class TradeOffer:
    offer_id: int
    maker: str
    assets_offered: List[Asset]
    assets_requested: List[Asset]
    expiry: int

class TradeRouter:
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.offers: Dict[int, TradeOffer] = {}
        self.next_offer_id = 1
        
        # Load contract ABI
        with open('ERC20_ABI.json') as f:
            self.erc20_abi = json.load(f)
        with open('ERC721_ABI.json') as f:
            self.erc721_abi = json.load(f)

    def _validate_asset(self, asset: Asset) -> bool:
        """Validate asset details."""
        if asset.asset_type == AssetType.CRYPTO:
            if not asset.contract_address or not asset.amount or asset.amount <= 0:
                return False
        elif asset.asset_type == AssetType.NFT:
            if not asset.contract_address or not asset.token_id:
                return False
        return True

    def create_offer(
        self,
        maker: str,
        assets_offered: List[Asset],
        assets_requested: List[Asset],
        expiry: int
    ) -> Optional[int]:
        """Create a new trade offer."""
        # Validate inputs
        if not maker or expiry <= self.w3.eth.get_block('latest')['timestamp']:
            return None
        
        for asset in assets_offered + assets_requested:
            if not self._validate_asset(asset):
                return None

        # Create and store offer
        offer_id = self.next_offer_id
        self.offers[offer_id] = TradeOffer(
            offer_id=offer_id,
            maker=maker,
            assets_offered=assets_offered,
            assets_requested=assets_requested,
            expiry=expiry
        )
        self.next_offer_id += 1
        return offer_id

    def execute_trade(
        self,
        taker: str,
        offer_id: int
    ) -> bool:
        """Execute a trade between maker and taker."""
        if offer_id not in self.offers:
            return False
        
        offer = self.offers[offer_id]
        
        # Check expiry
        if offer.expiry <= self.w3.eth.get_block('latest')['timestamp']:
            del self.offers[offer_id]
            return False

        # Check balances and approvals
        if not self._check_balances_and_approvals(offer.maker, taker, offer):
            return False

        # Execute transfers
        if not self._execute_transfers(offer.maker, taker, offer):
            return False

        # Clean up
        del self.offers[offer_id]
        return True

    def _check_balances_and_approvals(
        self,
        maker: str,
        taker: str,
        offer: TradeOffer
    ) -> bool:
        """Check if both parties have sufficient balances and approvals."""
        for asset in offer.assets_offered:
            if asset.asset_type == AssetType.CRYPTO:
                contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc20_abi)
                balance = contract.functions.balanceOf(maker).call()
                allowance = contract.functions.allowance(maker, self.w3.eth.default_account).call()
                if balance < asset.amount or allowance < asset.amount:
                    return False
            elif asset.asset_type == AssetType.NFT:
                contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc721_abi)
                owner = contract.functions.ownerOf(asset.token_id).call()
                is_approved = contract.functions.getApproved(asset.token_id).call() == self.w3.eth.default_account
                if owner != maker or not is_approved:
                    return False

        for asset in offer.assets_requested:
            if asset.asset_type == AssetType.CRYPTO:
                contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc20_abi)
                balance = contract.functions.balanceOf(taker).call()
                allowance = contract.functions.allowance(taker, self.w3.eth.default_account).call()
                if balance < asset.amount or allowance < asset.amount:
                    return False
            elif asset.asset_type == AssetType.NFT:
                contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc721_abi)
                owner = contract.functions.ownerOf(asset.token_id).call()
                is_approved = contract.functions.getApproved(asset.token_id).call() == self.w3.eth.default_account
                if owner != taker or not is_approved:
                    return False

        return True

    def _execute_transfers(
        self,
        maker: str,
        taker: str,
        offer: TradeOffer
    ) -> bool:
        """Execute all required transfers for the trade."""
        try:
            # Transfer assets from maker to taker
            for asset in offer.assets_offered:
                if asset.asset_type == AssetType.CRYPTO:
                    contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc20_abi)
                    tx = contract.functions.transferFrom(maker, taker, asset.amount).build_transaction({
                        'from': self.w3.eth.default_account,
                        'nonce': self.w3.eth.get_transaction_count(self.w3.eth.default_account)
                    })
                    signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
                    tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    self.w3.eth.wait_for_transaction_receipt(tx_hash)
                elif asset.asset_type == AssetType.NFT:
                    contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc721_abi)
                    tx = contract.functions.transferFrom(maker, taker, asset.token_id).build_transaction({
                        'from': self.w3.eth.default_account,
                        'nonce': self.w3.eth.get_transaction_count(self.w3.eth.default_account)
                    })
                    signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
                    tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    self.w3.eth.wait_for_transaction_receipt(tx_hash)

            # Transfer assets from taker to maker
            for asset in offer.assets_requested:
                if asset.asset_type == AssetType.CRYPTO:
                    contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc20_abi)
                    tx = contract.functions.transferFrom(taker, maker, asset.amount).build_transaction({
                        'from': self.w3.eth.default_account,
                        'nonce': self.w3.eth.get_transaction_count(self.w3.eth.default_account)
                    })
                    signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
                    tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    self.w3.eth.wait_for_transaction_receipt(tx_hash)
                elif asset.asset_type == AssetType.NFT:
                    contract = self.w3.eth.contract(address=asset.contract_address, abi=self.erc721_abi)
                    tx = contract.functions.transferFrom(taker, maker, asset.token_id).build_transaction({
                        'from': self.w3.eth.default_account,
                        'nonce': self.w3.eth.get_transaction_count(self.w3.eth.default_account)
                    })
                    signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=os.getenv('PRIVATE_KEY'))
                    tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    self.w3.eth.wait_for_transaction_receipt(tx_hash)

            return True
