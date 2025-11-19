"""
Generated Code Metadata:
========================
Original URL: https://satodog.com
Prompt: Design a decentralized marketplace using Keeta's cross-chain protocol to tokenize real-world assets and settle trades in real-time.
Generated: DETERMINISTIC_6b75d88544f78b56
Batch ID: 20250622_212605
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
from typing import Dict, List, Optional
from dataclasses import dataclass
from web3 import Web3
from web3.contract import Contract
from web3.exceptions import ContractLogicError
from eth_account import Account
from eth_typing import ChecksumAddress
from pytezos import pytezos
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

@dataclass
class AssetListing:
    asset_id: str
    owner: str
    tokenized_address: str
    price: float
    chain: str
    metadata: Dict

@dataclass
class Trade:
    trade_id: str
    buyer: str
    seller: str
    asset_id: str
    price: float
    status: str
    settlement_tx: Optional[str]

class DecentralizedMarketplace:
    """
    A decentralized marketplace for tokenizing and trading real-world assets
    using Keeta's cross-chain protocol.
    """
    
    def __init__(self, config: Dict):
        """
        Initialize the marketplace with configuration for multiple chains.
        
        Args:
            config: Dictionary containing configuration for EVM, Tezos, and Substrate chains
        """
        self.evm_providers = {
            chain: Web3(Web3.HTTPProvider(url)) 
            for chain, url in config['evm_chains'].items()
        }
        
        self.tezos_clients = {
            chain: pytezos.using(shell=url, key=config['tezos_keys'][chain])
            for chain, url in config['tezos_chains'].items()
        }
        
        self.substrate_interfaces = {
            chain: SubstrateInterface(url=url)
            for chain, url in config['substrate_chains'].items()
        }
        
        self.contracts = self._load_contracts(config['contracts'])
        self.listings: Dict[str, AssetListing] = {}
        self.trades: Dict[str, Trade] = {}
        
    def _load_contracts(self, contract_config: Dict) -> Dict[str, Contract]:
        """Load smart contracts from configuration."""
        contracts = {}
        for chain, config in contract_config['evm'].items():
            abi = json.loads(config['abi'])
            contracts[chain] = self.evm_providers[chain].eth.contract(
                address=config['address'],
                abi=abi
            )
        return contracts
    
    def tokenize_asset(
        self,
        asset_id: str,
        owner: str,
        price: float,
        metadata: Dict,
        chain: str
    ) -> str:
        """
        Tokenize a real-world asset on the specified blockchain.
        
        Args:
            asset_id: Unique identifier for the asset
            owner: Address of the asset owner
            price: Listing price
            metadata: Asset metadata
            chain: Target blockchain
            
        Returns:
            Transaction hash of the tokenization
        """
        try:
            if chain in self.evm_providers:
                tx_hash = self._tokenize_evm(asset_id, owner, price, metadata, chain)
            elif chain in self.tezos_clients:
                tx_hash = self._tokenize_tezos(asset_id, owner, price, metadata, chain)
            elif chain in self.substrate_interfaces:
                tx_hash = self._tokenize_substrate(asset_id, owner, price, metadata, chain)
            else:
                raise ValueError(f"Unsupported chain: {chain}")
            
            listing = AssetListing(
                asset_id=asset_id,
                owner=owner,
                tokenized_address=tx_hash,  # Temporary until we have actual address
                price=price,
                chain=chain,
                metadata=metadata
            )
            self.listings[asset_id] = listing
            return tx_hash
            
        except Exception as e:
            raise RuntimeError(f"Tokenization failed: {str(e)}")
    
    def _tokenize_evm(
        self,
        asset_id: str,
        owner: str,
        price: float,
        metadata: Dict,
        chain: str
    ) -> str:
        """Tokenize asset on EVM-compatible chain."""
        contract = self.contracts[chain]
        w3 = self.evm_providers[chain]
        
        tx = contract.functions.tokenizeAsset(
            asset_id,
            owner,
            int(price * 10**18),  # Convert to wei
            json.dumps(metadata)
        ).build_transaction({
            'from': owner,
            'nonce': w3.eth.get_transaction_count(owner),
            'gas': 2000000
        })
        
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=owner)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def _tokenize_tezos(
        self,
        asset_id: str,
        owner: str,
        price: float,
        metadata: Dict,
        chain: str
    ) -> str:
        """Tokenize asset on Tezos chain."""
        client = self.tezos_clients[chain]
        operation = client.contract(self.contracts[chain]['address']).tokenizeAsset(
            asset_id=asset_id,
            owner=owner,
            price=int(price * 10**6),  # Convert to mutez
            metadata=json.dumps(metadata)
        ).operation_group
        
        return operation.hash()
    
    def _tokenize_substrate(
        self,
        asset_id: str,
        owner: str,
        price: float,
        metadata: Dict,
        chain: str
    ) -> str:
        """Tokenize asset on Substrate-based chain."""
        substrate = self.substrate_interfaces[chain]
        keypair = Keypair.create_from_uri(owner)
        
        call = substrate.compose_call(
            call_module='Marketplace',
            call_function='tokenize_asset',
            call_params={
                'asset_id': asset_id,
                'owner': owner,
                'price': int(price * 10**12),  # Chain-specific decimals
                'metadata': json.dumps(metadata)
            }
        )
        
        extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
        return receipt.extrinsic_hash
    
    def execute_trade(
        self,
        asset_id: str,
        buyer: str,
        seller: str,
        price: float,
        buyer_chain: str,
        seller_chain: str
    ) -> str:
        """
        Execute a cross-chain trade between buyer and seller.
        
        Args:
            asset_id: ID of the asset being traded
            buyer: Buyer's address
            seller: Seller's address
            price: Agreed price
            buyer_chain: Buyer's blockchain
            seller_chain: Seller's blockchain
            
        Returns:
            Trade ID
        """
        try:
            if asset_id not in self.listings:
                raise ValueError("Asset not listed")
            
            listing = self.listings[asset_id]
            if listing.price != price:
                raise ValueError("Price mismatch")
            
            # Generate unique trade ID
            trade_id = Web3.keccak(text=f"{asset_id}{buyer}{seller}{price}").hex()
            
            # Execute cross-chain settlement
            if buyer_chain == seller_chain:
                settlement_tx = self._settle_on_chain(
                    asset_id, buyer, seller, price, buyer_chain
                )
            else:
                settlement_tx = self._settle_cross_chain(
                    asset_id, buyer, seller, price, buyer_chain, seller_chain
                )
            
            trade = Trade(
                trade_id=trade_id,
                buyer=buyer,
                seller=seller,
                asset_id=asset_id,
                price=price,
                status="executed",
                settlement_tx=settlement_tx
            )
            self.trades[trade_id] = trade
            
            return trade_id
            
        except Exception as e:
            raise RuntimeError(f"Trade execution failed: {str(e)}")
    
    def _settle_on_chain(
        self,
        asset_id: str,
        buyer: str,
        seller: str,
        price: float,
        chain: str
    ) -> str:
        """Settle trade on the same chain."""
        if chain in self.evm_providers:
            return self._settle_evm(asset_id, buyer, seller, price, chain)
        elif chain in self.tezos_clients:
            return self._settle_tezos(asset_id, buyer, seller, price, chain)
        elif chain in self.substrate_interfaces:
            return self._settle_substrate(asset_id, buyer, seller, price, chain)
        else:
            raise ValueError(f"Unsupported chain: {chain}")
    
    def _settle_evm(
        self,
        asset_id: str,
        buyer: str,
        seller: str,
        price: float,
        chain: str
    ) -> str:
        """Settle trade on EVM chain."""
