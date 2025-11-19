"""
Generated Code Metadata:
========================
Original URL: https://ethkta.com
Prompt: Design a library for tracking ETH pledges and donations on a blockchain.
Generated: DETERMINISTIC_e6d0f6947756e8c1
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
ETH Pledge Tracker Library

A library for tracking ETH pledges and donations on a blockchain.
Supports Ethereum mainnet and testnets via Web3.py.
"""

from web3 import Web3
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Pledge:
    """Data class representing a pledge."""
    donor_address: str
    amount_wei: int
    pledge_timestamp: int
    pledge_tx_hash: str
    fulfilled: bool = False
    fulfillment_tx_hash: Optional[str] = None
    fulfillment_timestamp: Optional[int] = None

class ETHPledgeTracker:
    """
    A class to track ETH pledges and donations on the Ethereum blockchain.
    
    Attributes:
        web3 (Web3): Web3 instance connected to Ethereum node
        contract_address (str): Address of the pledge tracking contract
        contract (Contract): Web3 contract instance
    """
    
    def __init__(self, provider_url: str, contract_address: str, contract_abi: Optional[Dict] = None):
        """
        Initialize the pledge tracker.
        
        Args:
            provider_url: URL of Ethereum node provider (e.g., Infura, Alchemy)
            contract_address: Address of the pledge tracking contract
            contract_abi: Optional ABI for the contract. If None, attempts to load from file.
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        if not self.web3.is_connected():
            raise ConnectionError("Could not connect to Ethereum node")
            
        self.contract_address = Web3.to_checksum_address(contract_address)
        
        # Load contract ABI
        if contract_abi is None:
            try:
                with open('PledgeContractABI.json', 'r') as f:
                    contract_abi = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError("Contract ABI file not found and no ABI provided")
        
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=contract_abi)
        
    def create_pledge(self, donor_address: str, amount_wei: int, private_key: str) -> str:
        """
        Create a new pledge on the blockchain.
        
        Args:
            donor_address: Address of the donor
            amount_wei: Amount pledged in wei
            private_key: Private key of the donor (for signing)
            
        Returns:
            Transaction hash of the pledge creation
            
        Raises:
            ValueError: If amount is not positive
            Exception: If transaction fails
        """
        if amount_wei <= 0:
            raise ValueError("Pledge amount must be positive")
            
        donor_address = Web3.to_checksum_address(donor_address)
        nonce = self.web3.eth.get_transaction_count(donor_address)
        
        tx = self.contract.functions.createPledge().build_transaction({
            'from': donor_address,
            'value': amount_wei,
            'gas': 200000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def fulfill_pledge(self, pledge_id: int, fulfiller_address: str, private_key: str) -> str:
        """
        Mark a pledge as fulfilled on the blockchain.
        
        Args:
            pledge_id: ID of the pledge to fulfill
            fulfiller_address: Address of the fulfiller
            private_key: Private key of the fulfiller
            
        Returns:
            Transaction hash of the fulfillment
            
        Raises:
            Exception: If transaction fails
        """
        fulfiller_address = Web3.to_checksum_address(fulfiller_address)
        nonce = self.web3.eth.get_transaction_count(fulfiller_address)
        
        tx = self.contract.functions.fulfillPledge(pledge_id).build_transaction({
            'from': fulfiller_address,
            'gas': 200000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': nonce,
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_pledge(self, pledge_id: int) -> Pledge:
        """
        Retrieve pledge details from the blockchain.
        
        Args:
            pledge_id: ID of the pledge to retrieve
            
        Returns:
            Pledge object with details
            
        Raises:
            ValueError: If pledge ID doesn't exist
        """
        try:
            pledge_data = self.contract.functions.getPledge(pledge_id).call()
        except Exception as e:
            raise ValueError(f"Pledge with ID {pledge_id} not found") from e
            
        return Pledge(
            donor_address=pledge_data[0],
            amount_wei=pledge_data[1],
            pledge_timestamp=pledge_data[2],
            pledge_tx_hash=pledge_data[3],
            fulfilled=pledge_data[4],
            fulfillment_tx_hash=pledge_data[5],
            fulfillment_timestamp=pledge_data[6]
        )
    
    def get_all_pledges(self) -> List[Pledge]:
        """
        Retrieve all pledges from the blockchain.
        
        Returns:
            List of Pledge objects
        """
        pledge_count = self.contract.functions.getPledgeCount().call()
        pledges = []
        
        for i in range(pledge_count):
            pledges.append(self.get_pledge(i))
            
        return pledges
    
    def get_donor_pledges(self, donor_address: str) -> List[Pledge]:
        """
        Retrieve all pledges from a specific donor.
        
        Args:
            donor_address: Address of the donor
            
        Returns:
            List of Pledge objects from the donor
        """
        donor_address = Web3.to_checksum_address(donor_address)
        pledge_ids = self.contract.functions.getDonorPledges(donor_address).call()
        
        return [self.get_pledge(pid) for pid in pledge_ids]
    
    def get_total_pledged(self) -> Tuple[int, float]:
        """
        Get total amount pledged in wei and ETH.
        
        Returns:
            Tuple of (total_wei, total_eth)
        """
        total_wei = self.contract.functions.getTotalPledged().call()
        return (total_wei, self.web3.from_wei(total_wei, 'ether'))
    
    def get_total_fulfilled(self) -> Tuple[int, float]:
        """
        Get total amount fulfilled in wei and ETH.
        
        Returns:
            Tuple of (total_wei, total_eth)
        """
        total_wei = self.contract.functions.getTotalFulfilled().call()
        return (total_wei, self.web3.from_wei(total_wei, 'ether'))
    
    def get_pledge_stats(self) -> Dict:
        """
        Get statistics about pledges.
        
        Returns:
            Dictionary with pledge statistics
        """
        return {
            'total_pledges': self.contract.functions.getPledgeCount().call(),
            'total_pledged_wei': self.get_total_pledged()[0],
            'total_pledged_eth': self.get_total_pledged()[1],
            'total_fulfilled_wei': self.get_total_fulfilled()[0],
            'total_fulfilled_eth': self.get_total_fulfilled()[1],
            'fulfillment_rate': self.contract.functions.getFulfillmentRate().call(),
        }
    
    def watch_pledges(self, event_handler):
        """
        Watch for new pledge events and call event_handler when detected.
        
        Args:
            event_handler: Function to call when new pledge is detected
                          Signature: handler(event: Dict)
        """
        def handle_event(event):
            event_handler({
                'event': 'NewPledge',
                'pledge_id': event['args']['pledgeId'],
                'donor': event['args']['donor'],
                'amount': event['args']['amount'],
                'timestamp': datetime.fromtimestamp(event['args']['timestamp']),
                'tx_hash': event['transactionHash'].hex()
            })
        
        event_filter = self.contract.events.PledgeCreated.create_filter(fromBlock='latest')
        
        while True:
            for event in event_filter.get_new_entries():
                handle_event(event)
    
    def watch_fulfillments(self, event_handler):
        """
        Watch for new fulfillment events and call event_handler when detected.
        
        Args:
            event_handler: Function to call when fulfillment is detected
                          Signature: handler(event: Dict)
        """
        def handle_event(event):
            event_handler({
                'event': 'PledgeFulfilled',
