"""
Generated Code Metadata:
========================
Original URL: https://light-chain-ai.pages.dev
Prompt: Create a script to calculate token allocation and presale pricing for Lightchain AI, incorporating the current price and next stage price as outlined in the presale details.
Generated: DETERMINISTIC_571f9db9d76def89
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class TokenAllocationCalculator:
    """
    A class to calculate token allocation and presale pricing for Lightchain AI.
    """
    
    def __init__(self, total_supply: int, presale_percentage: float, current_stage: int):
        """
        Initialize the calculator with token supply and presale details.
        
        Args:
            total_supply (int): Total token supply
            presale_percentage (float): Percentage of tokens allocated for presale (0-100)
            current_stage (int): Current presale stage (1-5)
        """
        if not (0 <= presale_percentage <= 100):
            raise ValueError("Presale percentage must be between 0 and 100")
        if not (1 <= current_stage <= 5):
            raise ValueError("Current stage must be between 1 and 5")
        
        self.total_supply = total_supply
        self.presale_percentage = presale_percentage
        self.current_stage = current_stage
        
        # Presale stage details: (price, percentage increase from previous stage)
        self.stages = {
            1: (0.015, 0),    # Stage 1: $0.015, no increase
            2: (0.020, 33.33), # Stage 2: $0.020, 33.33% increase
            3: (0.025, 25.00), # Stage 3: $0.025, 25% increase
            4: (0.030, 20.00), # Stage 4: $0.030, 20% increase
            5: (0.035, 16.67)  # Stage 5: $0.035, 16.67% increase
        }
    
    def calculate_presale_allocation(self) -> int:
        """
        Calculate the number of tokens allocated for presale.
        
        Returns:
            int: Number of tokens for presale
        """
        return math.floor(self.total_supply * (self.presale_percentage / 100))
    
    def get_current_price(self) -> float:
        """
        Get the current token price based on the current stage.
        
        Returns:
            float: Current token price in USD
        """
        return self.stages[self.current_stage][0]
    
    def get_next_stage_price(self) -> float:
        """
        Get the next stage token price.
        
        Returns:
            float: Next stage token price in USD
            None: If current stage is the last stage
        """
        if self.current_stage >= 5:
            return None
        return self.stages[self.current_stage + 1][0]
    
    def calculate_tokens_received(self, investment_amount: float) -> int:
        """
        Calculate how many tokens an investor would receive for a given investment amount.
        
        Args:
            investment_amount (float): Investment amount in USD
            
        Returns:
            int: Number of tokens received
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive")
        
        current_price = self.get_current_price()
        return math.floor(investment_amount / current_price)
    
    def calculate_investment_needed(self, desired_tokens: int) -> float:
        """
        Calculate the investment needed to receive a desired number of tokens.
        
        Args:
            desired_tokens (int): Desired number of tokens
            
        Returns:
            float: Investment amount needed in USD
        """
        if desired_tokens <= 0:
            raise ValueError("Desired tokens must be positive")
        
        current_price = self.get_current_price()
        return desired_tokens * current_price
    
    def get_stage_details(self) -> dict:
        """
        Get details about all presale stages.
        
        Returns:
            dict: Dictionary containing stage details
        """
        return {
            'total_supply': self.total_supply,
            'presale_allocation': self.calculate_presale_allocation(),
            'current_stage': self.current_stage,
            'current_price': self.get_current_price(),
            'next_stage_price': self.get_next_stage_price(),
            'stages': self.stages
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with total supply of 1 billion tokens, 30% presale allocation, and stage 2
        calculator = TokenAllocationCalculator(
            total_supply=1_000_000_000,
            presale_percentage=30,
            current_stage=2
        )
        
        # Get presale allocation
        presale_tokens = calculator.calculate_presale_allocation()
        print(f"Presale Token Allocation: {presale_tokens:,}")
        
        # Get current and next stage prices
        current_price = calculator.get_current_price()
        next_price = calculator.get_next_stage_price()
        print(f"Current Stage Price: ${current_price:.3f}")
        print(f"Next Stage Price: ${next_price:.3f}" if next_price else "This is the final stage")
        
        # Calculate tokens for $1000 investment
        investment = 1000
        tokens = calculator.calculate_tokens_received(investment)
        print(f"Tokens for ${investment}: {tokens:,}")
        
        # Calculate investment needed for 50,000 tokens
        desired_tokens = 50_000
        needed_investment = calculator.calculate_investment_needed(desired_tokens)
        print(f"Investment needed for {desired_tokens:,} tokens: ${needed_investment:,.2f}")
        
        # Get all stage details
        details = calculator.get_stage_details()
        print("\nAll Stage Details:")
        for key, value in details.items():
            if key != 'stages':
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nStage Prices:")
        for stage, (price, increase) in details['stages'].items():
            print(f"Stage {stage}: ${price:.3f} ({increase:.2f}% increase)")
            
    except ValueError as e:
        print(f"Error: {e}")
```
