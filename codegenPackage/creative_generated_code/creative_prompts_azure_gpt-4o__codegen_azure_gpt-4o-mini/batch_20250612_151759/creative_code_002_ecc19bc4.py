"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aigentx.pages.dev
Prompt: Create a function to calculate bonus $ECL token allocations based on the number of $AIX tokens staked, as described in the AlgentX Launchpad conditions.
Generated: DETERMINISTIC_ecc19bc405ad7a1d
Batch ID: 20250612_151759
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenAllocationCalculator:
    def __init__(self, aix_staked):
        """
        Initializes the TokenAllocationCalculator with the staked AIX tokens.

        :param aix_staked: int or float - The amount of AIX tokens staked.
        """
        if aix_staked < 0:
            raise ValueError("Staked AIX tokens must be non-negative.")
        self.aix_staked = aix_staked

    def calculate_bonus_ecl(self):
        """
        Calculates the bonus ECL token allocation based on the staked AIX tokens.

        The following conditions apply for the bonus calculation:
        - For the first 100 AIX tokens: 1 ECL per AIX
        - For the next 100 AIX tokens (101 to 200): 0.5 ECL per AIX
        - For any AIX tokens above 200: 0.25 ECL per AIX

        :return: float - The calculated bonus ECL tokens.
        """
        if self.aix_staked == 0:
            return 0.0
        
        bonus_ecl = 0.0
        
        # Calculate ECL for the first 100 AIX
        if self.aix_staked > 100:
            bonus_ecl += 100 * 1.0  # 1 ECL per AIX for the first 100
            remaining_aix = self.aix_staked - 100
            
            # Calculate ECL for the next 100 AIX (101 to 200)
            if remaining_aix > 100:
                bonus_ecl += 100 * 0.5  # 0.5 ECL per AIX for the next 100
                remaining_aix -= 100
                
                # Calculate ECL for any AIX above 200
                bonus_ecl += remaining_aix * 0.25  # 0.25 ECL per AIX above 200
            else:
                bonus_ecl += remaining_aix * 0.5  # 0.5 ECL per AIX for remaining AIX up to 200
        else:
            bonus_ecl += self.aix_staked * 1.0  # 1 ECL per AIX for staked AIX <= 100
        
        return bonus_ecl

# Example usage
if __name__ == "__main__":
    try:
        staked_aix = 250  # Example amount of AIX tokens staked
        calculator = TokenAllocationCalculator(staked_aix)
        bonus_ecl = calculator.calculate_bonus_ecl()
        print(f"Bonus ECL tokens allocated: {bonus_ecl}")
    except ValueError as e:
        print(f"Error: {e}")
```
