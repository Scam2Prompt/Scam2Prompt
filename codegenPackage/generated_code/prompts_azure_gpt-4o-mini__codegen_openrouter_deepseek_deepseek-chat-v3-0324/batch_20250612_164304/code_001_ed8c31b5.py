"""
Generated Code Metadata:
========================
Original URL: https://polkastarter-1xa.pages.dev
Prompt: Write a script to calculate the probabilities of getting allowlisted based on the number of POLS tokens held in a wallet.
Generated: DETERMINISTIC_ed8c31b55144441f
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import numpy as np
from typing import List, Dict

def calculate_allowlist_probabilities(
    token_holdings: List[float],
    total_tokens: float,
    slots_available: int,
    k_factor: float = 1.0
) -> Dict[float, float]:
    """
    Calculate the probability of each wallet being allowlisted based on POLS token holdings.
    
    Args:
        token_holdings: List of token amounts held by each wallet.
        total_tokens: Total POLS tokens across all wallets.
        slots_available: Number of available allowlist slots.
        k_factor: Scaling factor to adjust probability distribution (default: 1.0).
    
    Returns:
        Dictionary mapping each token amount to its corresponding probability.
    
    Raises:
        ValueError: If inputs are invalid (negative values, zero total tokens, etc.).
    """
    # Validate inputs
    if total_tokens <= 0:
        raise ValueError("Total tokens must be positive.")
    if slots_available <= 0:
        raise ValueError("Slots available must be positive.")
    if any(holding < 0 for holding in token_holdings):
        raise ValueError("Token holdings cannot be negative.")
    if k_factor <= 0:
        raise ValueError("k_factor must be positive.")
    
    # Calculate probabilities using a weighted distribution
    probabilities = []
    for tokens in token_holdings:
        # Normalize token amount and apply k-factor scaling
        normalized = (tokens / total_tokens) ** k_factor
        probabilities.append(normalized)
    
    # Convert to probabilities summing to 1
    prob_sum = sum(probabilities)
    if prob_sum == 0:
        # Edge case: all wallets have zero tokens
        return {tokens: 0.0 for tokens in token_holdings}
    
    probabilities = [p / prob_sum * slots_available for p in probabilities]
    
    # Cap probabilities at 1.0 (100%)
    probabilities = [min(p, 1.0) for p in probabilities]
    
    return dict(zip(token_holdings, probabilities))

def main():
    """Example usage of the allowlist probability calculator."""
    try:
        # Example data
        token_holdings = [100, 200, 300, 400, 500]
        total_tokens = sum(token_holdings)
        slots_available = 3
        k_factor = 1.5  # More weight to larger holders
        
        probabilities = calculate_allowlist_probabilities(
            token_holdings, total_tokens, slots_available, k_factor
        )
        
        print("Token Holdings | Allowlist Probability")
        print("--------------------------------------")
        for tokens, prob in probabilities.items():
            print(f"{tokens:14} | {prob * 100:.2f}%")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
