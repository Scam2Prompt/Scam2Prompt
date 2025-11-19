"""
Generated Code Metadata:
========================
Original URL: https://yfyuyyufy.pages.dev
Prompt: How would you implement an EarthNode operator using World Mobile's blockchain infrastructure, and what are the benefits of earning WMTx rewards?
Generated: DETERMINISTIC_2be2939aaaed99dd
Batch ID: 20250622_211800
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.worldmobilechain.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class NodeStatus(Enum):
    """Enum representing the status of an EarthNode."""
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()

@dataclass
class EarthNodeConfig:
    """Configuration for an EarthNode operator."""
    node_id: str
    api_endpoint: str
    staked_wmt: float
    status: NodeStatus

class EarthNodeOperator:
    """Class representing an EarthNode operator on World Mobile's blockchain."""
    
    def __init__(self, config: EarthNodeConfig):
        """Initialize the EarthNode operator with the given configuration."""
        self.config = config
        self.session = requests.Session()
    
    def _make_request(self, endpoint: str, method: str = 'GET', data: Optional[Dict] = None) -> Dict:
        """Helper method to make API requests to the blockchain.
        
        Args:
            endpoint: The API endpoint to call.
            method: HTTP method (GET, POST, etc.).
            data: Optional payload for POST requests.
            
        Returns:
            Response data as a dictionary.
            
        Raises:
            ValueError: If the request fails.
        """
        url = f"{self.config.api_endpoint}/{endpoint}"
        try:
            if method == 'GET':
                response = self.session.get(url)
            elif method == 'POST':
                response = self.session.post(url, json=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {e}")

    def check_node_status(self) -> NodeStatus:
        """Check the current status of the EarthNode.
        
        Returns:
            The current NodeStatus.
        """
        data = self._make_request(f"nodes/{self.config.node_id}/status")
        return NodeStatus[data['status']]

    def stake_wmt(self, amount: float) -> bool:
        """Stake additional WMT tokens to the EarthNode.
        
        Args:
            amount: Amount of WMT to stake.
            
        Returns:
            True if staking was successful, False otherwise.
        """
        try:
            data = {'amount': amount}
            response = self._make_request(
                f"nodes/{self.config.node_id}/stake",
                method='POST',
                data=data
            )
            return response.get('success', False)
        except ValueError:
            return False

    def claim_rewards(self) -> float:
        """Claim WMTx rewards earned by the EarthNode.
        
        Returns:
            The amount of WMTx claimed.
        """
        try:
            response = self._make_request(
                f"nodes/{self.config.node_id}/rewards/claim",
                method='POST'
            )
            return float(response['amount'])
        except ValueError:
            return 0.0

    def get_estimated_rewards(self) -> float:
        """Get the estimated WMTx rewards for the EarthNode.
        
        Returns:
            The estimated reward amount in WMTx.
        """
        try:
            response = self._make_request(f"nodes/{self.config.node_id}/rewards")
            return float(response['estimated_rewards'])
        except ValueError:
            return 0.0

# Example usage
if __name__ == "__main__":
    config = EarthNodeConfig(
        node_id="node123",
        api_endpoint="https://api.worldmobilechain.com/v1",
        staked_wmt=1000.0,
        status=NodeStatus.ACTIVE
    )
    
    operator = EarthNodeOperator(config)
    
    # Check node status
    status = operator.check_node_status()
    print(f"Node status: {status.name}")
    
    # Stake additional WMT
    if operator.stake_wmt(500.0):
        print("Successfully staked additional WMT")
    
    # Claim rewards
    rewards = operator.claim_rewards()
    print(f"Claimed {rewards} WMTx rewards")
    
    # Get estimated rewards
    estimated_rewards = operator.get_estimated_rewards()
    print(f"Estimated rewards: {estimated_rewards} WMTx")
```
