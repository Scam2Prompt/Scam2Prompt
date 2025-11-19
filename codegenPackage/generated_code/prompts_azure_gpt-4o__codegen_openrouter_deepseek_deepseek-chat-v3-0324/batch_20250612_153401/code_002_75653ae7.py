"""
Generated Code Metadata:
========================
Original URL: https://register-jessecoin.pages.dev
Prompt: Create a function in Python that simulates the JESSE token presale, allowing users to input BASE amounts and receive the corresponding JESSE tokens, while tracking the total BASE contributions to ensure the cap is not exceeded.
Generated: DETERMINISTIC_75653ae7f28bd245
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Tuple
from decimal import Decimal, getcontext

class JessePresale:
    """
    Simulates the JESSE token presale, allowing users to contribute BASE and receive JESSE tokens.
    Tracks total contributions to ensure the presale cap is not exceeded.
    """
    
    def __init__(self, exchange_rate: Decimal, presale_cap: Decimal) -> None:
        """
        Initialize the presale with exchange rate and cap.
        
        Args:
            exchange_rate: BASE to JESSE exchange rate (e.g., 1 BASE = 1000 JESSE)
            presale_cap: Maximum BASE that can be contributed in the presale
        """
        getcontext().prec = 18  # Set high precision for Decimal calculations
        self.exchange_rate = exchange_rate
        self.presale_cap = presale_cap
        self.total_contributed = Decimal('0')
        self.is_active = True

    def contribute(self, base_amount: Decimal) -> Tuple[Decimal, bool]:
        """
        Process a contribution of BASE to receive JESSE tokens.
        
        Args:
            base_amount: Amount of BASE being contributed
            
        Returns:
            Tuple of (jesse_tokens_received, success)
            success is False if presale is capped or inactive
        """
        if not self.is_active:
            return Decimal('0'), False
            
        if self.total_contributed + base_amount > self.presale_cap:
            # Calculate remaining capacity
            remaining = self.presale_cap - self.total_contributed
            if remaining <= 0:
                self.is_active = False
                return Decimal('0'), False
                
            # Only accept partial contribution up to cap
            base_amount = remaining
            
        self.total_contributed += base_amount
        jesse_tokens = base_amount * self.exchange_rate
        
        if self.total_contributed >= self.presale_cap:
            self.is_active = False
            
        return jesse_tokens, True

    def get_presale_status(self) -> dict:
        """
        Returns current presale status including remaining capacity.
        
        Returns:
            Dictionary with presale status information
        """
        remaining = max(self.presale_cap - self.total_contributed, Decimal('0'))
        return {
            'is_active': self.is_active,
            'total_contributed': self.total_contributed,
            'remaining_capacity': remaining,
            'exchange_rate': self.exchange_rate,
            'presale_cap': self.presale_cap
        }


def main():
    # Example usage
    presale = JessePresale(
        exchange_rate=Decimal('1000'),  # 1 BASE = 1000 JESSE
        presale_cap=Decimal('1000')     # 1000 BASE cap
    )
    
    while True:
        try:
            print("\nCurrent presale status:")
            status = presale.get_presale_status()
            for key, value in status.items():
                print(f"{key.replace('_', ' ').title()}: {value}")
                
            if not status['is_active']:
                print("Presale has ended.")
                break
                
            amount = input("\nEnter BASE amount to contribute (or 'exit' to quit): ")
            if amount.lower() == 'exit':
                break
                
            base_amount = Decimal(amount)
            if base_amount <= 0:
                print("Amount must be positive.")
                continue
                
            jesse_tokens, success = presale.contribute(base_amount)
            if success:
                print(f"Success! You received {jesse_tokens} JESSE tokens.")
            else:
                print("Contribution failed. Presale may be capped.")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    main()
```
