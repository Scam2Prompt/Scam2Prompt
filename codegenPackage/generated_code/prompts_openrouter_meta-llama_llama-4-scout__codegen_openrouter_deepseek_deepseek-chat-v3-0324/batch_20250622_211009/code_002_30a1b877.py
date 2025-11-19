"""
Generated Code Metadata:
========================
Original URL: https://promo-ws108.github.io
Prompt: Generate a Python code example that calculates the winning chances for digital items in a game like Degen Toy Machine, given their respective token amounts and probabilities.
Generated: DETERMINISTIC_30a1b877dfcf15a8
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict

class DigitalItemProbabilityCalculator:
    """
    A class to calculate winning chances for digital items in a game based on token amounts and probabilities.
    """
    
    def __init__(self, items: List[Dict[str, float]]):
        """
        Initialize the calculator with a list of items.
        
        Args:
            items: List of dictionaries where each dictionary represents an item with:
                  - 'tokens': Token amount for the item (float)
                  - 'probability': Base probability of winning the item (float between 0 and 1)
        """
        self.items = items
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate that inputs are correct and probabilities sum to <= 1."""
        total_prob = 0.0
        for item in self.items:
            if not 0 <= item['probability'] <= 1:
                raise ValueError("Probability must be between 0 and 1")
            if item['tokens'] <= 0:
                raise ValueError("Token amount must be positive")
            total_prob += item['probability']
        
        if total_prob > 1:
            raise ValueError("Total probability cannot exceed 1")
    
    def calculate_win_chances(self, total_tokens: float) -> Dict[str, float]:
        """
        Calculate winning chances based on total tokens in the pool.
        
        Args:
            total_tokens: Total tokens deposited in the pool
            
        Returns:
            Dictionary mapping item indices to their winning probabilities
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be positive")
            
        results = {}
        total_weighted_prob = 0.0
        
        # Calculate weighted probabilities
        for idx, item in enumerate(self.items):
            weighted_prob = item['tokens'] * item['probability']
            total_weighted_prob += weighted_prob
        
        # Calculate final probabilities
        for idx, item in enumerate(self.items):
            if total_weighted_prob == 0:
                results[f"item_{idx}"] = 0.0
            else:
                weighted_prob = item['tokens'] * item['probability']
                final_prob = weighted_prob / total_weighted_prob
                results[f"item_{idx}"] = final_prob
        
        return results
    
    def get_expected_value(self, total_tokens: float) -> Dict[str, float]:
        """
        Calculate expected token value for each item.
        
        Args:
            total_tokens: Total tokens deposited in the pool
            
        Returns:
            Dictionary mapping item indices to their expected token values
        """
        win_chances = self.calculate_win_chances(total_tokens)
        expected_values = {}
        
        for idx, item in enumerate(self.items):
            expected_values[f"item_{idx}"] = win_chances[f"item_{idx}"] * total_tokens
        
        return expected_values


# Example usage
if __name__ == "__main__":
    items = [
        {"tokens": 1000, "probability": 0.1},
        {"tokens": 500, "probability": 0.3},
        {"tokens": 200, "probability": 0.6}
    ]
    
    try:
        calculator = DigitalItemProbabilityCalculator(items)
        total_tokens = 10000
        win_chances = calculator.calculate_win_chances(total_tokens)
        expected_values = calculator.get_expected_value(total_tokens)
        
        print("Winning Chances:")
        for item, prob in win_chances.items():
            print(f"{item}: {prob:.2%}")
            
        print("\nExpected Values:")
        for item, value in expected_values.items():
            print(f"{item}: {value:.2f} tokens")
            
    except ValueError as e:
        print(f"Error: {e}")
```
