"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: How can players earn bonuses while crafting items in Big Time, and what are Bonus Rolls?
Generated: DETERMINISTIC_7e8383e68ebc3b23
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CraftingBonusSystem:
    """
    A system to handle crafting bonuses and bonus rolls in Big Time.
    """
    
    def __init__(self):
        self.bonus_rolls = 0
        self.active_bonuses = []
        self.bonus_multipliers = {
            'quality': 1.0,
            'speed': 1.0,
            'yield': 1.0
        }
    
    def add_bonus_roll(self, amount: int) -> None:
        """
        Add bonus rolls to the player's pool.
        
        Args:
            amount (int): Number of bonus rolls to add.
        """
        if amount <= 0:
            raise ValueError("Bonus roll amount must be positive")
        self.bonus_rolls += amount
    
    def use_bonus_roll(self) -> bool:
        """
        Attempt to use a bonus roll.
        
        Returns:
            bool: True if bonus roll was used successfully, False if no rolls left.
        """
        if self.bonus_rolls <= 0:
            return False
        
        self.bonus_rolls -= 1
        return True
    
    def apply_bonus(self, bonus_type: str, multiplier: float, duration: int = 0) -> None:
        """
        Apply a crafting bonus to the player.
        
        Args:
            bonus_type (str): Type of bonus ('quality', 'speed', or 'yield')
            multiplier (float): Multiplier value (e.g., 1.2 for 20% bonus)
            duration (int): Duration in seconds (0 for permanent)
        """
        if bonus_type not in self.bonus_multipliers:
            raise ValueError(f"Invalid bonus type: {bonus_type}")
        if multiplier <= 0:
            raise ValueError("Multiplier must be positive")
        
        self.bonus_multipliers[bonus_type] *= multiplier
        
        if duration > 0:
            self.active_bonuses.append({
                'type': bonus_type,
                'multiplier': multiplier,
                'expires_at': time.time() + duration
            })
    
    def update_bonuses(self) -> None:
        """
        Update active bonuses and remove expired ones.
        """
        current_time = time.time()
        expired_bonuses = []
        
        for i, bonus in enumerate(self.active_bonuses):
            if current_time >= bonus['expires_at']:
                # Revert the bonus
                self.bonus_multipliers[bonus['type']] /= bonus['multiplier']
                expired_bonuses.append(i)
        
        # Remove expired bonuses in reverse order
        for i in sorted(expired_bonuses, reverse=True):
            self.active_bonuses.pop(i)
    
    def get_crafting_result(self, base_quality: float, base_time: float, base_yield: int) -> dict:
        """
        Calculate final crafting results with bonuses applied.
        
        Args:
            base_quality (float): Base quality of the item
            base_time (float): Base crafting time in seconds
            base_yield (int): Base number of items produced
            
        Returns:
            dict: Final crafting results with bonuses
        """
        self.update_bonuses()
        
        return {
            'final_quality': base_quality * self.bonus_multipliers['quality'],
            'final_time': base_time / self.bonus_multipliers['speed'],
            'final_yield': int(base_yield * self.bonus_multipliers['yield']),
            'bonus_rolls_used': self.use_bonus_roll()
        }
```
