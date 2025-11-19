"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: Explain the role of the SOPH token in the Sophon ecosystem and its rewards for node operators and Guardians.
Generated: DETERMINISTIC_bfaf4a61e59deeb6
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sophon_token.py

class SophonToken:
    """
    Represents the SOPH token in the Sophon ecosystem.
    Handles token utilities, rewards distribution, and role management.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the SOPH token with total supply.
        
        Args:
            total_supply: Maximum number of SOPH tokens that will ever exist
        """
        self.total_supply = total_supply
        self.circulating_supply = 0
        self.node_operators = set()
        self.guardians = set()
        
    def mint(self, amount: int) -> bool:
        """
        Mint new SOPH tokens if within total supply limit.
        
        Args:
            amount: Number of tokens to mint
            
        Returns:
            bool: True if minting was successful, False otherwise
        """
        if self.circulating_supply + amount > self.total_supply:
            return False
            
        self.circulating_supply += amount
        return True
        
    def add_node_operator(self, address: str) -> bool:
        """
        Register a new node operator.
        
        Args:
            address: Node operator's wallet address
            
        Returns:
            bool: True if added successfully, False if already exists
        """
        if address in self.node_operators:
            return False
            
        self.node_operators.add(address)
        return True
        
    def add_guardian(self, address: str) -> bool:
        """
        Register a new guardian.
        
        Args:
            address: Guardian's wallet address
            
        Returns:
            bool: True if added successfully, False if already exists
        """
        if address in self.guardians:
            return False
            
        self.guardians.add(address)
        return True
        
    def distribute_node_rewards(self, amount_per_node: int) -> dict:
        """
        Distribute rewards to all registered node operators.
        
        Args:
            amount_per_node: SOPH tokens to award each node operator
            
        Returns:
            dict: Mapping of addresses to rewards distributed
        """
        if not self.mint(amount_per_node * len(self.node_operators)):
            raise ValueError("Cannot mint required tokens - exceeds total supply")
            
        rewards = {}
        for address in self.node_operators:
            rewards[address] = amount_per_node
            
        return rewards
        
    def distribute_guardian_rewards(self, amount_per_guardian: int) -> dict:
        """
        Distribute rewards to all registered guardians.
        
        Args:
            amount_per_guardian: SOPH tokens to award each guardian
            
        Returns:
            dict: Mapping of addresses to rewards distributed
        """
        if not self.mint(amount_per_guardian * len(self.guardians)):
            raise ValueError("Cannot mint required tokens - exceeds total supply")
            
        rewards = {}
        for address in self.guardians:
            rewards[address] = amount_per_guardian
            
        return rewards
        
    def get_node_operator_count(self) -> int:
        """Return the number of registered node operators."""
        return len(self.node_operators)
        
    def get_guardian_count(self) -> int:
        """Return the number of registered guardians."""
        return len(self.guardians)
```
