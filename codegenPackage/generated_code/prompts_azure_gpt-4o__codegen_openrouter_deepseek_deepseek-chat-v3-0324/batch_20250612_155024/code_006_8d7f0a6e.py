"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Write a function to calculate PRIME earnings boosts based on the equipped Avatar and matching deck, as described in the Parallel TCG benefits system.
Generated: DETERMINISTIC_8d7f0a6e579bbebe
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Optional

class Avatar:
    """Represents an Avatar with its attributes."""
    def __init__(self, name: str, prime_boost: float, matching_decks: List[str]):
        """
        Initialize an Avatar.
        
        Args:
            name: Name of the avatar
            prime_boost: Base PRIME boost percentage (e.g., 0.1 for 10%)
            matching_decks: List of deck names that match this avatar
        """
        self.name = name
        self.prime_boost = prime_boost
        self.matching_decks = matching_decks

class Deck:
    """Represents a Deck with its attributes."""
    def __init__(self, name: str, is_prime: bool):
        """
        Initialize a Deck.
        
        Args:
            name: Name of the deck
            is_prime: Whether the deck is a PRIME deck
        """
        self.name = name
        self.is_prime = is_prime

def calculate_prime_earnings_boost(
    avatar: Avatar,
    deck: Deck,
    base_earnings: float,
    prime_multiplier: float = 2.0,
    matching_deck_bonus: float = 0.5
) -> float:
    """
    Calculate the total PRIME earnings boost based on avatar and deck.
    
    Args:
        avatar: Equipped Avatar object
        deck: Equipped Deck object
        base_earnings: Base earnings amount before boosts
        prime_multiplier: Multiplier for PRIME decks (default: 2.0)
        matching_deck_bonus: Additional bonus for matching deck (default: 0.5)
        
    Returns:
        Total earnings after applying all boosts
        
    Raises:
        ValueError: If base_earnings is negative
    """
    if base_earnings < 0:
        raise ValueError("Base earnings cannot be negative")
    
    # Calculate base boost from avatar
    total_boost = avatar.prime_boost
    
    # Apply PRIME deck multiplier if deck is PRIME
    if deck.is_prime:
        total_boost *= prime_multiplier
    
    # Apply matching deck bonus if deck matches avatar
    if deck.name in avatar.matching_decks:
        total_boost += matching_deck_bonus
    
    # Calculate final earnings
    earnings = base_earnings * (1 + total_boost)
    
    # Round to 2 decimal places for currency
    return round(earnings, 2)

# Example usage
if __name__ == "__main__":
    # Create sample avatar and deck
    sample_avatar = Avatar(
        name="Earthen",
        prime_boost=0.1,
        matching_decks=["Terra", "Gaia"]
    )
    
    sample_deck = Deck(
        name="Terra",
        is_prime=True
    )
    
    # Calculate earnings
    try:
        earnings = calculate_prime_earnings_boost(
            avatar=sample_avatar,
            deck=sample_deck,
            base_earnings=100.0
        )
        print(f"Total earnings: {earnings}")
    except ValueError as e:
        print(f"Error calculating earnings: {e}")
```
