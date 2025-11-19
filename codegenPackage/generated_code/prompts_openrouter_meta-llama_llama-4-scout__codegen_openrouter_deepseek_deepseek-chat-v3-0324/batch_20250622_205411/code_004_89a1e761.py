"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Develop a strategy for determining the price of a premium Instagram username, taking into account factors like length, dictionary words, and demand, as seen on SovaDS.
Generated: DETERMINISTIC_89a1e761c609306c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import Optional, Dict, List

class InstagramUsernamePricingStrategy:
    """
    A strategy for determining the price of a premium Instagram username.
    Factors considered: length, dictionary words, and demand.
    """
    
    def __init__(self, 
                 base_price: float = 100.0,
                 length_multipliers: Optional[Dict[int, float]] = None,
                 dictionary_word_bonus: float = 0.2,
                 demand_multipliers: Optional[Dict[str, float]] = None):
        """
        Initialize the pricing strategy with configurable parameters.
        
        Args:
            base_price: Base price for any username
            length_multipliers: Multipliers based on username length
            dictionary_word_bonus: Bonus for dictionary words
            demand_multipliers: Multipliers for in-demand categories
        """
        self.base_price = base_price
        self.length_multipliers = length_multipliers or {
            1: 5.0, 2: 4.0, 3: 3.0, 4: 2.0, 5: 1.5
        }
        self.dictionary_word_bonus = dictionary_word_bonus
        self.demand_multipliers = demand_multipliers or {
            'brandable': 2.0,
            'one-word': 1.8,
            'short': 1.5,
            'numbers': 0.7
        }
        
    def _is_dictionary_word(self, username: str, word_list: List[str]) -> bool:
        """Check if username is a dictionary word."""
        return username.lower() in word_list
    
    def _get_length_multiplier(self, username: str) -> float:
        """Get multiplier based on username length."""
        length = len(username)
        return self.length_multipliers.get(length, 1.0)
    
    def _get_demand_multiplier(self, username: str) -> float:
        """Calculate demand multiplier based on username characteristics."""
        multiplier = 1.0
        
        # Check for brandable (all letters)
        if username.isalpha():
            multiplier *= self.demand_multipliers['brandable']
            
        # Check for one-word (no separators)
        if '_' not in username and '.' not in username and '-' not in username:
            multiplier *= self.demand_multipliers['one-word']
            
        # Check for short usernames
        if len(username) <= 5:
            multiplier *= self.demand_multipliers['short']
            
        # Penalty for numbers
        if any(c.isdigit() for c in username):
            multiplier *= self.demand_multipliers['numbers']
            
        return multiplier
    
    def calculate_price(self, username: str, word_list: List[str]) -> float:
        """
        Calculate the price for a given Instagram username.
        
        Args:
            username: The username to price
            word_list: List of dictionary words for reference
            
        Returns:
            Calculated price for the username
        """
        if not username or not isinstance(username, str):
            raise ValueError("Username must be a non-empty string")
            
        username = username.lower().strip()
        
        # Base calculation
        price = self.base_price
        
        # Apply length multiplier
        price *= self._get_length_multiplier(username)
        
        # Apply dictionary word bonus
        if self._is_dictionary_word(username, word_list):
            price *= (1 + self.dictionary_word_bonus)
            
        # Apply demand multiplier
        price *= self._get_demand_multiplier(username)
        
        return round(price, 2)
```
