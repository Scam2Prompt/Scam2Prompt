"""
Generated Code Metadata:
========================
Original URL: https://epsys.ro
Prompt: Create a Python function to calculate the probability of winning in different lottery markets (e.g., 4D, 6D, 7D) based on the rules described for Hondatoto's Japan Lottery Association system.
Generated: DETERMINISTIC_d4f0443884d3a922
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Union

def calculate_lottery_probability(lottery_type: str, numbers_played: int = None) -> Union[float, str]:
    """
    Calculate the probability of winning in different lottery markets based on Hondatoto's Japan Lottery Association system.
    
    Args:
        lottery_type (str): Type of lottery ('4D', '6D', '7D')
        numbers_played (int, optional): Number of unique numbers played. Required for 6D and 7D.
        
    Returns:
        Union[float, str]: Probability of winning or error message
        
    Raises:
        ValueError: If invalid lottery type is provided
    """
    
    # Validate lottery type
    if lottery_type not in ['4D', '6D', '7D']:
        raise ValueError("Invalid lottery type. Must be '4D', '6D', or '7D'")
    
    try:
        if lottery_type == '4D':
            # 4D lottery: 4 digits in exact order (0000-9999)
            total_possible = 10000  # 10^4
            return 1 / total_possible
        
        elif lottery_type in ['6D', '7D']:
            if numbers_played is None:
                return "numbers_played parameter is required for 6D and 7D lotteries"
            
            if not isinstance(numbers_played, int) or numbers_played <= 0:
                return "numbers_played must be a positive integer"
                
            if lottery_type == '6D':
                # 6D lottery: pick 6 numbers out of 43 (order doesn't matter)
                total_numbers = 43
                numbers_to_pick = 6
                
                if numbers_played < numbers_to_pick:
                    return f"Must play at least {numbers_to_pick} numbers for 6D lottery"
                
            elif lottery_type == '7D':
                # 7D lottery: pick 7 numbers out of 37 (order doesn't matter)
                total_numbers = 37
                numbers_to_pick = 7
                
                if numbers_played < numbers_to_pick:
                    return f"Must play at least {numbers_to_pick} numbers for 7D lottery"
            
            # Calculate combinations: C(total_numbers, numbers_to_pick) / C(numbers_played, numbers_to_pick)
            total_combinations = math.comb(total_numbers, numbers_to_pick)
            played_combinations = math.comb(numbers_played, numbers_to_pick)
            
            return played_combinations / total_combinations
            
    except Exception as e:
        return f"Error calculating probability: {str(e)}"
```
