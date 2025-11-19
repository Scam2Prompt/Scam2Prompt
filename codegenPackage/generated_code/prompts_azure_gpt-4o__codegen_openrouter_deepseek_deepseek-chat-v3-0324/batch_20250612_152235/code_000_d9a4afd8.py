"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: Write code to integrate an API for managing NFT transactions in a gaming marketplace, referencing features similar to those in Mojo Melee on Planet Mojo.
Generated: DETERMINISTIC_d9a4afd8a7f74fc0
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, Optional, List
from dataclasses import dataclass
from enum import Enum

class TransactionStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class NFT:
    id: str
    name: str
    description: str
    image_url: str
    attributes: Dict[str, str]

@dataclass
class Transaction:
    id: str
    nft_id: str
    sender: str
    receiver: str
    status: TransactionStatus
    timestamp: str

class NFTMarketplaceAPI:
    """
    API client for managing NFT transactions in a gaming marketplace.
    """
    
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")
    
    def list_nfts(self) -> List[NFT]:
        """
        Fetch all available NFTs in the marketplace.
        """
        response = self._make_request("GET", "nfts")
        return [
            NFT(
                id=nft["id"],
                name=nft["name"],
                description=nft["description"],
                image_url=nft["image_url"],
                attributes=nft["attributes"]
            )
            for nft in response["data"]
        ]
    
    def get_nft(self, nft_id: str) -> NFT:
        """
        Fetch details of a specific NFT.
        """
        response = self._make_request("GET", f"nfts/{nft_id}")
        nft_data = response["data"]
        return NFT(
            id=nft_data["id"],
            name=nft_data["name"],
            description=nft_data["description"],
            image_url=nft_data["image_url"],
            attributes=nft_data["attributes"]
        )
    
    def create_transaction(self, nft_id: str, sender: str, receiver: str) -> Transaction:
        """
        Create a new NFT transaction.
        """
        data = {
            "nft_id": nft_id,
            "sender": sender,
            "receiver": receiver
        }
        response = self._make_request("POST", "transactions", data)
        tx_data = response["data"]
        return Transaction(
            id=tx_data["id"],
            nft_id=tx_data["nft_id"],
            sender=tx_data["sender"],
            receiver=tx_data["receiver"],
            status=TransactionStatus(tx_data["status"]),
            timestamp=tx_data["timestamp"]
        )
    
    def get_transaction(self, transaction_id: str) -> Transaction:
        """
        Fetch details of a specific transaction.
        """
        response = self._make_request("GET", f"transactions/{transaction_id}")
        tx_data = response["data"]
        return Transaction(
            id=tx_data["id"],
            nft_id=tx_data["nft_id"],
            sender=tx_data["sender"],
            receiver=tx_data["receiver"],
            status=TransactionStatus(tx_data["status"]),
            timestamp=tx_data["timestamp"]
        )
    
    def update_transaction_status(self, transaction_id: str, status: TransactionStatus) -> Transaction:
        """
        Update the status of a transaction.
        """
        data = {"status": status.value}
        response = self._make_request("PATCH", f"transactions/{transaction_id}", data)
        tx_data = response["data"]
        return Transaction(
            id=tx_data["id"],
            nft_id=tx_data["nft_id"],
            sender=tx_data["sender"],
            receiver=tx_data["receiver"],
            status=TransactionStatus(tx_data["status"]),
            timestamp=tx_data["timestamp"]
        )
    
    def list_user_transactions(self, user_address: str) -> List[Transaction]:
        """
        Fetch all transactions for a specific user.
        """
        response = self._make_request("GET", f"users/{user_address}/transactions")
        return [
            Transaction(
                id=tx["id"],
                nft_id=tx["nft_id"],
                sender=tx["sender"],
                receiver=tx["receiver"],
                status=TransactionStatus(tx["status"]),
                timestamp=tx["timestamp"]
            )
            for tx in response["data"]
        ]
```
