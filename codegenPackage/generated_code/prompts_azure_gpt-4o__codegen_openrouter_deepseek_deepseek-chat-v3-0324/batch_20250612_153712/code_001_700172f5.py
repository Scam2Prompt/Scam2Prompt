"""
Generated Code Metadata:
========================
Original URL: https://wildhorse-llc.com
Prompt: Generate a script to calculate referral bonuses for Wildhorse LLC's 4-step referral program, including levels 1 to 4 with percentages of 5%, 10%, 15%, and 20%.
Generated: DETERMINISTIC_700172f57879bd5a
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ReferralBonusCalculator:
    """
    A class to calculate referral bonuses for Wildhorse LLC's 4-step referral program.
    Levels 1 to 4 have percentages of 5%, 10%, 15%, and 20% respectively.
    """
    
    def __init__(self):
        self.level_percentages = {
            1: 0.05,
            2: 0.10,
            3: 0.15,
            4: 0.20
        }
    
    def calculate_bonus(self, level: int, base_amount: float) -> float:
        """
        Calculate the referral bonus for a given level and base amount.
        
        Args:
            level (int): The referral level (1-4)
            base_amount (float): The base amount to calculate the bonus from
            
        Returns:
            float: The calculated bonus amount
            
        Raises:
            ValueError: If level is not between 1-4 or base_amount is negative
        """
        if level not in self.level_percentages:
            raise ValueError("Level must be between 1 and 4")
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative")
            
        percentage = self.level_percentages[level]
        return round(base_amount * percentage, 2)
    
    def calculate_all_bonuses(self, base_amount: float) -> dict:
        """
        Calculate bonuses for all levels (1-4) for a given base amount.
        
        Args:
            base_amount (float): The base amount to calculate bonuses from
            
        Returns:
            dict: A dictionary with levels as keys and bonus amounts as values
            
        Raises:
            ValueError: If base_amount is negative
        """
        if base_amount < 0:
            raise ValueError("Base amount cannot be negative")
            
        return {
            level: self.calculate_bonus(level, base_amount)
            for level in self.level_percentages
        }


# Example usage
if __name__ == "__main__":
    try:
        calculator = ReferralBonusCalculator()
        
        # Test with a sample base amount
        base_amount = 1000.00
        print(f"Calculating bonuses for base amount: ${base_amount:.2f}")
        
        # Calculate individual level bonus
        level = 2
        bonus = calculator.calculate_bonus(level, base_amount)
        print(f"Level {level} bonus: ${bonus:.2f}")
        
        # Calculate all level bonuses
        all_bonuses = calculator.calculate_all_bonuses(base_amount)
        for level, bonus in all_bonuses.items():
            print(f"Level {level} bonus: ${bonus:.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
