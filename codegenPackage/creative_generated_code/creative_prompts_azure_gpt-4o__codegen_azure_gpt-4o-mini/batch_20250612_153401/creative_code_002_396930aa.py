"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Generate a function that calculates the earnings for the first minter and the cast creator based on Gemcaster's reward structure.
Generated: DETERMINISTIC_396930aac95a5401
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Gemcaster:
    """
    A class to represent the Gemcaster reward structure for calculating earnings.
    """

    def __init__(self, total_supply: int, base_reward: float, creator_cut: float):
        """
        Initialize the Gemcaster with total supply, base reward, and creator cut.
        
        :param total_supply: Total number of gems minted
        :param base_reward: Base reward for the first minter
        :param creator_cut: Percentage cut for the cast creator (0 to 1)
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0.")
        if not (0 <= creator_cut <= 1):
            raise ValueError("Creator cut must be between 0 and 1.")

        self.total_supply = total_supply
        self.base_reward = base_reward
        self.creator_cut = creator_cut

    def calculate_earnings(self):
        """
        Calculate the earnings for the first minter and the cast creator.
        
        :return: A tuple containing (first_minter_earnings, cast_creator_earnings)
        """
        try:
            # Earnings for the first minter is the base reward
            first_minter_earnings = self.base_reward
            
            # Earnings for the cast creator is a percentage of the total supply
            cast_creator_earnings = (self.total_supply * self.base_reward) * self.creator_cut
            
            return first_minter_earnings, cast_creator_earnings
        
        except Exception as e:
            raise RuntimeError("Error calculating earnings: " + str(e))


# Example usage
if __name__ == "__main__":
    try:
        gemcaster = Gemcaster(total_supply=1000, base_reward=10.0, creator_cut=0.1)
        first_minter, cast_creator = gemcaster.calculate_earnings()
        print(f"First Minter Earnings: ${first_minter:.2f}")
        print(f"Cast Creator Earnings: ${cast_creator:.2f}")
    except Exception as e:
        print("An error occurred:", e)
```
