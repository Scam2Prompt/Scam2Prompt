"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Write a script to simulate JESSE token purchases, ensuring the total supply of 100,000,000 tokens is not exceeded and the presale cap of 1000 BASE is respected.
Generated: DETERMINISTIC_093fa008d5f67357
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Tuple

class TokenPurchaseSimulator:
    """
    Simulates JESSE token purchases while respecting total supply and presale cap constraints.
    """
    
    def __init__(self):
        self.total_supply = 100_000_000  # Total JESSE tokens available
        self.presale_cap = 1000  # Maximum BASE that can be raised in presale
        self.token_price = 0.01  # Price per JESSE token in BASE
        self.purchases: Dict[str, float] = {}  # Tracks purchases by address
        self.total_base_raised = 0.0
        self.total_tokens_sold = 0
        
    def validate_purchase(self, base_amount: float) -> Tuple[bool, str]:
        """
        Validates if a purchase can be made without violating constraints.
        
        Args:
            base_amount: Amount of BASE to spend on tokens
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if base_amount <= 0:
            return False, "Purchase amount must be positive"
            
        if self.total_base_raised + base_amount > self.presale_cap:
            return False, "Purchase would exceed presale cap"
            
        tokens_to_buy = base_amount / self.token_price
        if self.total_tokens_sold + tokens_to_buy > self.total_supply:
            return False, "Purchase would exceed total token supply"
            
        return True, "Valid purchase"
        
    def make_purchase(self, address: str, base_amount: float) -> Tuple[bool, str]:
        """
        Attempts to make a token purchase for the given address.
        
        Args:
            address: Purchaser's wallet address
            base_amount: Amount of BASE to spend on tokens
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        is_valid, message = self.validate_purchase(base_amount)
        if not is_valid:
            return False, message
            
        tokens_bought = base_amount / self.token_price
        
        # Update totals
        self.total_base_raised += base_amount
        self.total_tokens_sold += tokens_bought
        
        # Record purchase
        if address in self.purchases:
            self.purchases[address] += tokens_bought
        else:
            self.purchases[address] = tokens_bought
            
        return True, f"Successfully purchased {tokens_bought} JESSE tokens"
        
    def generate_random_purchases(self, num_purchases: int) -> None:
        """
        Generates random purchases for simulation purposes.
        
        Args:
            num_purchases: Number of random purchases to generate
        """
        for _ in range(num_purchases):
            # Generate random address and amount
            address = f"0x{random.getrandbits(160):040x}"
            base_amount = random.uniform(0.1, 100)
            
            success, message = self.make_purchase(address, base_amount)
            if not success:
                print(f"Purchase failed for {address}: {message}")
                
    def get_stats(self) -> Dict[str, float]:
        """
        Returns current simulation statistics.
        
        Returns:
            Dictionary containing simulation metrics
        """
        return {
            "total_base_raised": self.total_base_raised,
            "total_tokens_sold": self.total_tokens_sold,
            "remaining_supply": self.total_supply - self.total_tokens_sold,
            "remaining_cap": self.presale_cap - self.total_base_raised,
            "unique_buyers": len(self.purchases)
        }
        
    def print_stats(self) -> None:
        """Prints current simulation statistics."""
        stats = self.get_stats()
        print("\nCurrent Simulation Stats:")
        for key, value in stats.items():
            print(f"{key.replace('_', ' ').title()}: {value:,.2f}")


if __name__ == "__main__":
    # Example usage
    simulator = TokenPurchaseSimulator()
    
    # Make some manual purchases
    print("Making manual purchases...")
    print(simulator.make_purchase("0x123...", 50))
    print(simulator.make_purchase("0x456...", 200))
    print(simulator.make_purchase("0x789...", 1000))  # Should fail if previous purchases total > 1000
    
    # Generate random purchases
    print("\nGenerating random purchases...")
    simulator.generate_random_purchases(20)
    
    # Print final stats
    simulator.print_stats()
```
