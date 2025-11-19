"""
Generated Code Metadata:
========================
Original URL: https://wenwencoins.web.app
Prompt: Generate code to calculate token ownership in a fractional NFT, like Wen's trillion-piece poem division.
Generated: DETERMINISTIC_3ea1694cdf5da147
Batch ID: 20250622_205623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FractionalNFTOwnership:
    """
    A class to manage fractional ownership calculations for NFTs.
    Handles ownership tracking, transfers, and percentage calculations.
    """
    
    def __init__(self, total_supply: int):
        """
        Initialize the fractional NFT ownership tracker.
        
        Args:
            total_supply: The total number of fractional tokens (pieces) available
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero")
            
        self.total_supply = total_supply
        self.owners = {}  # {address: token_balance}
    
    def mint(self, address: str, amount: int) -> None:
        """
        Mint new fractional tokens to an address.
        
        Args:
            address: The recipient's address
            amount: Number of tokens to mint
            
        Raises:
            ValueError: If amount is invalid or would exceed total supply
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
            
        if sum(self.owners.values()) + amount > self.total_supply:
            raise ValueError("Minting would exceed total supply")
            
        self.owners[address] = self.owners.get(address, 0) + amount
    
    def transfer(self, from_address: str, to_address: str, amount: int) -> None:
        """
        Transfer fractional tokens between addresses.
        
        Args:
            from_address: Sender's address
            to_address: Recipient's address
            amount: Number of tokens to transfer
            
        Raises:
            ValueError: If transfer amount is invalid or sender has insufficient balance
        """
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero")
            
        if from_address not in self.owners or self.owners[from_address] < amount:
            raise ValueError("Insufficient balance for transfer")
            
        self.owners[from_address] -= amount
        self.owners[to_address] = self.owners.get(to_address, 0) + amount
    
    def get_balance(self, address: str) -> int:
        """
        Get token balance for an address.
        
        Args:
            address: Address to query
            
        Returns:
            Number of tokens owned by the address
        """
        return self.owners.get(address, 0)
    
    def get_ownership_percentage(self, address: str) -> float:
        """
        Calculate ownership percentage of the NFT.
        
        Args:
            address: Address to query
            
        Returns:
            Percentage ownership (0-100) as a float
        """
        balance = self.get_balance(address)
        return (balance / self.total_supply) * 100
    
    def get_all_owners(self) -> dict:
        """
        Get all current owners and their balances.
        
        Returns:
            Dictionary of {address: balance}
        """
        return self.owners.copy()
    
    def get_total_supply(self) -> int:
        """
        Get the total token supply.
        
        Returns:
            Total number of fractional tokens
        """
        return self.total_supply
    
    def get_circulating_supply(self) -> int:
        """
        Get the current circulating supply (minted tokens).
        
        Returns:
            Number of tokens currently owned by addresses
        """
        return sum(self.owners.values())
```
