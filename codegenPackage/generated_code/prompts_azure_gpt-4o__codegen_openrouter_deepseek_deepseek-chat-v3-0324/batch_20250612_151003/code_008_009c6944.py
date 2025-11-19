"""
Generated Code Metadata:
========================
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a script to calculate bonus rolls during item crafting in Big Time, displaying probabilities and potential rewards.
Generated: DETERMINISTIC_009c6944c719aac3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class CraftingBonusCalculator:
    """
    A class to calculate bonus rolls during item crafting in Big Time.
    It computes probabilities and potential rewards based on given parameters.
    """
    
    def __init__(self, base_success_rate: float, bonus_rolls: int, reward_table: Dict[str, float]):
        """
        Initialize the calculator with crafting parameters.
        
        Args:
            base_success_rate: Probability of success for a single roll (0.0 to 1.0)
            bonus_rolls: Number of bonus rolls attempted
            reward_table: Dictionary mapping reward names to their probabilities (must sum to 1.0)
        """
        if not 0 <= base_success_rate <= 1:
            raise ValueError("Base success rate must be between 0 and 1")
        if bonus_rolls < 0:
            raise ValueError("Bonus rolls must be a non-negative integer")
        if not self._validate_reward_table(reward_table):
            raise ValueError("Reward table probabilities must sum to 1.0")
            
        self.base_success_rate = base_success_rate
        self.bonus_rolls = bonus_rolls
        self.reward_table = reward_table
    
    @staticmethod
    def _validate_reward_table(reward_table: Dict[str, float]) -> bool:
        """Validate that reward probabilities sum to approximately 1.0."""
        total = sum(reward_table.values())
        return abs(total - 1.0) < 1e-6  # Allow for floating point imprecision
    
    def calculate_success_probability(self) -> float:
        """
        Calculate the probability of at least one successful bonus roll.
        
        Returns:
            Probability as a float between 0.0 and 1.0
        """
        if self.bonus_rolls == 0:
            return 0.0
        return 1 - (1 - self.base_success_rate) ** self.bonus_rolls
    
    def simulate_rewards(self, num_simulations: int = 10000) -> Dict[str, float]:
        """
        Simulate crafting results to estimate reward probabilities.
        
        Args:
            num_simulations: Number of simulations to run (higher = more accurate)
            
        Returns:
            Dictionary mapping reward names to their estimated probabilities
        """
        if num_simulations <= 0:
            raise ValueError("Number of simulations must be positive")
            
        reward_counts = {reward: 0 for reward in self.reward_table}
        total_successes = 0
        
        for _ in range(num_simulations):
            # Determine if any bonus rolls succeed
            any_success = any(
                random.random() < self.base_success_rate 
                for _ in range(self.bonus_rolls)
            )
            
            if any_success:
                total_successes += 1
                # Select a reward based on the reward table
                rand = random.random()
                cumulative = 0.0
                for reward, prob in self.reward_table.items():
                    cumulative += prob
                    if rand <= cumulative:
                        reward_counts[reward] += 1
                        break
        
        # Convert counts to probabilities
        return {
            reward: count / num_simulations 
            for reward, count in reward_counts.items()
        }
    
    def get_expected_rewards(self) -> Dict[str, float]:
        """
        Calculate the expected probability for each reward.
        
        Returns:
            Dictionary mapping reward names to their expected probabilities
        """
        success_prob = self.calculate_success_probability()
        return {
            reward: prob * success_prob
            for reward, prob in self.reward_table.items()
        }

def display_results(calculator: CraftingBonusCalculator, num_simulations: int = 10000):
    """
    Display the calculated and simulated probabilities in a readable format.
    
    Args:
        calculator: Initialized CraftingBonusCalculator instance
        num_simulations: Number of simulations to run for estimation
    """
    print("\n--- Crafting Bonus Roll Calculator ---")
    print(f"Base Success Rate: {calculator.base_success_rate * 100:.1f}%")
    print(f"Bonus Rolls: {calculator.bonus_rolls}")
    
    print("\nReward Table:")
    for reward, prob in calculator.reward_table.items():
        print(f"  - {reward}: {prob * 100:.1f}%")
    
    success_prob = calculator.calculate_success_probability()
    print(f"\nProbability of at least one success: {success_prob * 100:.2f}%")
    
    print("\nExpected Reward Probabilities:")
    expected = calculator.get_expected_rewards()
    for reward, prob in expected.items():
        print(f"  - {reward}: {prob * 100:.2f}%")
    
    print("\nSimulated Reward Probabilities (from {:,} runs):".format(num_simulations))
    simulated = calculator.simulate_rewards(num_simulations)
    for reward, prob in simulated.items():
        print(f"  - {reward}: {prob * 100:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        # Example configuration
        reward_table = {
            "Common": 0.6,
            "Uncommon": 0.3,
            "Rare": 0.08,
            "Legendary": 0.02
        }
        
        calculator = CraftingBonusCalculator(
            base_success_rate=0.15,  # 15% chance per roll
            bonus_rolls=3,           # 3 bonus rolls
            reward_table=reward_table
        )
        
        display_results(calculator)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
