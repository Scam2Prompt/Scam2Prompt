"""
Generated Code Metadata:
========================
Original URL: https://thebalan-er.com
Prompt: Explain how Balancer's flexible token weights can help mitigate impermanent loss for liquidity providers (LPs) and propose a code implementation to optimize LP returns.
Generated: DETERMINISTIC_0a11b01801f655d7
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Tuple
import math

class BalancerPool:
    """
    A class to simulate a Balancer pool with flexible token weights.
    """
    
    def __init__(self, tokens: List[str], initial_weights: List[float], initial_balances: List[float]):
        """
        Initialize the Balancer pool with tokens, their weights, and initial balances.
        
        Args:
            tokens: List of token symbols
            initial_weights: List of initial weights for each token (must sum to 1)
            initial_balances: List of initial balances for each token
        """
        if len(tokens) != len(initial_weights) or len(tokens) != len(initial_balances):
            raise ValueError("Tokens, weights, and balances must have the same length")
        if not math.isclose(sum(initial_weights), 1.0, rel_tol=1e-9):
            raise ValueError("Weights must sum to 1")
        
        self.tokens = tokens
        self.weights = initial_weights.copy()
        self.balances = initial_balances.copy()
        self.total_supply = 1.0  # Initial LP token supply
        
    def get_spot_price(self, token_in: str, token_out: str) -> float:
        """
        Calculate the spot price between two tokens in the pool.
        
        Args:
            token_in: Input token symbol
            token_out: Output token symbol
            
        Returns:
            Spot price (amount of token_out per token_in)
        """
        in_idx = self.tokens.index(token_in)
        out_idx = self.tokens.index(token_out)
        
        return (self.balances[out_idx] / self.weights[out_idx]) / \
               (self.balances[in_idx] / self.weights[in_idx])
    
    def swap(self, token_in: str, token_out: str, amount_in: float) -> float:
        """
        Execute a swap between two tokens in the pool.
        
        Args:
            token_in: Input token symbol
            token_out: Output token symbol
            amount_in: Amount of token_in to swap
            
        Returns:
            Amount of token_out received
        """
        in_idx = self.tokens.index(token_in)
        out_idx = self.tokens.index(token_out)
        
        weight_in = self.weights[in_idx]
        weight_out = self.weights[out_idx]
        balance_in = self.balances[in_idx]
        balance_out = self.balances[out_idx]
        
        amount_out = balance_out * (1 - (balance_in / (balance_in + amount_in)) ** (weight_in / weight_out))
        
        # Update balances
        self.balances[in_idx] += amount_in
        self.balances[out_idx] -= amount_out
        
        return amount_out
    
    def get_value_ratios(self, external_prices: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate the value ratio of each token in the pool compared to external markets.
        
        Args:
            external_prices: Dictionary of external prices for each token
            
        Returns:
            Dictionary of value ratios (pool_value / external_value) for each token
        """
        value_ratios = {}
        for i, token in enumerate(self.tokens):
            pool_price = self.balances[i] / self.weights[i]
            external_value = external_prices[token] * self.balances[i]
            value_ratios[token] = pool_price / external_value if external_value > 0 else 1.0
        return value_ratios
    
    def rebalance_weights(self, external_prices: Dict[str, float], adjustment_factor: float = 0.01) -> None:
        """
        Rebalance token weights based on external price changes to mitigate impermanent loss.
        
        Args:
            external_prices: Dictionary of external prices for each token
            adjustment_factor: How aggressively to adjust weights (0-1)
        """
        value_ratios = self.get_value_ratios(external_prices)
        
        # Calculate new weights
        total_value_ratio = sum(value_ratios.values())
        new_weights = []
        for i, token in enumerate(self.tokens):
            current_weight = self.weights[i]
            target_weight = value_ratios[token] / total_value_ratio
            adjusted_weight = current_weight * (1 - adjustment_factor) + target_weight * adjustment_factor
            new_weights.append(adjusted_weight)
        
        # Normalize weights to sum to 1
        weight_sum = sum(new_weights)
        self.weights = [w / weight_sum for w in new_weights]
    
    def add_liquidity(self, amounts: List[float]) -> float:
        """
        Add liquidity to the pool and mint LP tokens.
        
        Args:
            amounts: List of amounts for each token to add
            
        Returns:
            Amount of LP tokens minted
        """
        if len(amounts) != len(self.tokens):
            raise ValueError("Amounts list must match tokens list length")
            
        # Calculate mint amount based on value added
        value_added = sum(amounts[i] * self.weights[i] for i in range(len(self.tokens)))
        lp_tokens = value_added * self.total_supply / sum(b * w for b, w in zip(self.balances, self.weights))
        
        # Update balances and total supply
        for i in range(len(self.tokens)):
            self.balances[i] += amounts[i]
        self.total_supply += lp_tokens
        
        return lp_tokens
    
    def remove_liquidity(self, lp_amount: float) -> List[float]:
        """
        Remove liquidity from the pool and burn LP tokens.
        
        Args:
            lp_amount: Amount of LP tokens to burn
            
        Returns:
            List of amounts for each token received
        """
        if lp_amount <= 0 or lp_amount > self.total_supply:
            raise ValueError("Invalid LP token amount")
            
        # Calculate proportional amounts to return
        amounts = []
        for i in range(len(self.tokens)):
            amount = (lp_amount / self.total_supply) * self.balances[i]
            amounts.append(amount)
            self.balances[i] -= amount
        
        self.total_supply -= lp_amount
        return amounts
    
    def calculate_impermanent_loss(self, initial_prices: Dict[str, float], current_prices: Dict[str, float]) -> float:
        """
        Calculate impermanent loss compared to holding assets outside the pool.
        
        Args:
            initial_prices: Dictionary of initial external prices
            current_prices: Dictionary of current external prices
            
        Returns:
            Impermanent loss percentage (negative means loss)
        """
        # Calculate value if held
        held_value = sum(self.balances[i] * current_prices[token] for i, token in enumerate(self.tokens))
        
        # Calculate pool value
        pool_value = sum(self.balances[i] * current_prices[token] for i, token in enumerate(self.tokens))
        
        return (pool_value - held_value) / held_value * 100 if held_value > 0 else 0.0
```
