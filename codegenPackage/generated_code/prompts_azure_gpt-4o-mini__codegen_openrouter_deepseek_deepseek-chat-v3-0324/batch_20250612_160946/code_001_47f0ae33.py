"""
Generated Code Metadata:
========================
Original URL: https://bigtime-ai.pages.dev
Prompt: Explain the process of collecting $BIGTIME tokens and their role in crafting collectibles in Big Time.
Generated: DETERMINISTIC_47f0ae3316973603
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bigtime_token_collector.py

import requests
from typing import Dict, Optional, List
from dataclasses import dataclass

@dataclass
class BigTimeToken:
    """Represents a BIGTIME token with its properties."""
    token_id: str
    amount: float
    rarity: str  # e.g., "common", "rare", "epic", "legendary"
    collection: str  # e.g., "timekeeper", "chronomancer"

@dataclass
class Collectible:
    """Represents a crafted collectible in Big Time."""
    collectible_id: str
    name: str
    required_tokens: Dict[str, int]  # token_id: required_amount
    crafted: bool = False

class BigTimeTokenCollector:
    """Handles collection of BIGTIME tokens and crafting collectibles."""
    
    def __init__(self, api_endpoint: str):
        """
        Initialize the collector with API endpoint.
        
        Args:
            api_endpoint: Base URL for Big Time API
        """
        self.api_endpoint = api_endpoint
        self.collected_tokens: Dict[str, BigTimeToken] = {}
        self.collectibles: Dict[str, Collectible] = {}
        
    def fetch_tokens(self, wallet_address: str) -> List[BigTimeToken]:
        """
        Fetch BIGTIME tokens from a wallet address via API.
        
        Args:
            wallet_address: User's wallet address
            
        Returns:
            List of BigTimeToken objects
            
        Raises:
            requests.exceptions.RequestException: If API request fails
        """
        try:
            url = f"{self.api_endpoint}/tokens/{wallet_address}"
            response = requests.get(url)
            response.raise_for_status()
            
            tokens_data = response.json()
            tokens = []
            
            for token_data in tokens_data:
                token = BigTimeToken(
                    token_id=token_data['id'],
                    amount=token_data['amount'],
                    rarity=token_data['rarity'],
                    collection=token_data['collection']
                )
                tokens.append(token)
                self.collected_tokens[token.token_id] = token
                
            return tokens
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch tokens: {str(e)}")
    
    def add_collectible_recipe(self, collectible: Collectible) -> None:
        """
        Add a collectible recipe to the available crafting options.
        
        Args:
            collectible: Collectible object with required tokens
        """
        self.collectibles[collectible.collectible_id] = collectible
    
    def craft_collectible(self, collectible_id: str) -> bool:
        """
        Attempt to craft a collectible using collected tokens.
        
        Args:
            collectible_id: ID of the collectible to craft
            
        Returns:
            bool: True if crafting succeeded, False otherwise
            
        Raises:
            ValueError: If collectible ID doesn't exist
        """
        if collectible_id not in self.collectibles:
            raise ValueError(f"Collectible {collectible_id} not found")
            
        collectible = self.collectibles[collectible_id]
        
        # Check if we have enough tokens
        for token_id, required_amount in collectible.required_tokens.items():
            if token_id not in self.collected_tokens:
                return False
            if self.collected_tokens[token_id].amount < required_amount:
                return False
        
        # Deduct tokens and mark as crafted
        for token_id, required_amount in collectible.required_tokens.items():
            self.collected_tokens[token_id].amount -= required_amount
            
        collectible.crafted = True
        return True
    
    def get_collectible_status(self, collectible_id: str) -> Dict[str, any]:
        """
        Get crafting status and requirements for a collectible.
        
        Args:
            collectible_id: ID of the collectible to check
            
        Returns:
            Dict with status information
            
        Raises:
            ValueError: If collectible ID doesn't exist
        """
        if collectible_id not in self.collectibles:
            raise ValueError(f"Collectible {collectible_id} not found")
            
        collectible = self.collectibles[collectible_id]
        status = {
            'collectible_id': collectible_id,
            'name': collectible.name,
            'crafted': collectible.crafted,
            'requirements': {},
            'met': True
        }
        
        for token_id, required_amount in collectible.required_tokens.items():
            has_amount = self.collected_tokens.get(token_id, BigTimeToken(token_id, 0, "", "")).amount
            status['requirements'][token_id] = {
                'required': required_amount,
                'has': has_amount,
                'met': has_amount >= required_amount
            }
            if has_amount < required_amount:
                status['met'] = False
                
        return status
```
