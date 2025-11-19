"""
Generated Code Metadata:
========================
Original URL: https://bafybeib23vaqj4gspufgrstwtd6jjwqlmmwwlbyy5nhjlvlvkr7iqwpaxq.ipfs.dweb.link
Prompt: "Design a basic structure for a DEX explorer feature that displays transaction counts and network activity."
Generated: DETERMINISTIC_94ee58cd5c6b156f
Batch ID: 20250622_205006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DEX Explorer - Basic Structure
# This module provides functionality to explore and visualize DEX transactions and network activity.

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
import requests
from requests.exceptions import RequestException
from enum import Enum, auto

class Network(Enum):
    """Supported blockchain networks for DEX exploration."""
    ETHEREUM = auto()
    BINANCE_SMART_CHAIN = auto()
    POLYGON = auto()
    SOLANA = auto()

@dataclass
class Transaction:
    """Represents a DEX transaction."""
    tx_hash: str
    block_number: int
    timestamp: datetime
    sender: str
    receiver: str
    token_in: str
    token_out: str
    amount_in: float
    amount_out: float
    dex_name: str
    network: Network

class DEXExplorer:
    """Main class for exploring DEX transactions and network activity."""
    
    def __init__(self, api_base_url: str, api_key: Optional[str] = None):
        """
        Initialize DEX explorer with API configuration.
        
        Args:
            api_base_url: Base URL for the blockchain API
            api_key: Optional API key for authenticated requests
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})

    def get_transactions(
        self,
        network: Network,
        start_block: Optional[int] = None,
        end_block: Optional[int] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limit: int = 100
    ) -> List[Transaction]:
        """
        Retrieve DEX transactions for a given network with optional filters.
        
        Args:
            network: Blockchain network to query
            start_block: Optional starting block number
            end_block: Optional ending block number
            start_time: Optional starting timestamp
            end_time: Optional ending timestamp
            limit: Maximum number of transactions to return
            
        Returns:
            List of Transaction objects
            
        Raises:
            RequestException: If API request fails
        """
        params = {
            'network': network.name,
            'limit': limit
        }
        
        if start_block:
            params['start_block'] = start_block
        if end_block:
            params['end_block'] = end_block
        if start_time:
            params['start_time'] = start_time.isoformat()
        if end_time:
            params['end_time'] = end_time.isoformat()
            
        try:
            response = self.session.get(
                f"{self.api_base_url}/transactions",
                params=params
            )
            response.raise_for_status()
            
            transactions = []
            for tx_data in response.json():
                transactions.append(Transaction(
                    tx_hash=tx_data['hash'],
                    block_number=tx_data['block_number'],
                    timestamp=datetime.fromisoformat(tx_data['timestamp']),
                    sender=tx_data['sender'],
                    receiver=tx_data['receiver'],
                    token_in=tx_data['token_in'],
                    token_out=tx_data['token_out'],
                    amount_in=float(tx_data['amount_in']),
                    amount_out=float(tx_data['amount_out']),
                    dex_name=tx_data['dex_name'],
                    network=Network[tx_data['network']]
                ))
                
            return transactions
            
        except RequestException as e:
            raise RequestException(f"Failed to fetch transactions: {str(e)}")
            
    def get_network_activity(
        self,
        network: Network,
        time_period: str = '24h'
    ) -> Dict[str, float]:
        """
        Get network activity metrics for a given time period.
        
        Args:
            network: Blockchain network to query
            time_period: Time period for metrics (24h, 7d, 30d)
            
        Returns:
            Dictionary containing activity metrics
            
        Raises:
            RequestException: If API request fails
        """
        valid_periods = ['24h', '7d', '30d']
        if time_period not in valid_periods:
            raise ValueError(f"Invalid time period. Must be one of: {valid_periods}")
            
        try:
            response = self.session.get(
                f"{self.api_base_url}/network_activity",
                params={
                    'network': network.name,
                    'time_period': time_period
                }
            )
            response.raise_for_status()
            
            return response.json()
            
        except RequestException as e:
            raise RequestException(f"Failed to fetch network activity: {str(e)}")

    def get_transaction_count(
        self,
        network: Network,
        time_period: str = '24h'
    ) -> int:
        """
        Get total transaction count for a given network and time period.
        
        Args:
            network: Blockchain network to query
            time_period: Time period for count (24h, 7d, 30d)
            
        Returns:
            Total transaction count
            
        Raises:
            RequestException: If API request fails
        """
        activity = self.get_network_activity(network, time_period)
        return activity.get('transaction_count', 0)

    def close(self):
        """Clean up resources."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
```
