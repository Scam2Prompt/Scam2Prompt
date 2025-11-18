"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptominnerfx.com
Prompt: Create a script to simulate referral program earnings based on Cryptominnerfx's referral income structure.
Generated: DETERMINISTIC_0cc7e34e8e785865
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Referral Program Earnings Simulator

This script simulates referral program earnings based on Cryptominnerfx's referral income structure.
Assumptions:
- The structure includes multiple referral levels.
- Earnings are calculated as a percentage of each referred user's earnings.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

from typing import List, Dict

# Define constants for referral percentages and levels
REFERRAL_PERCENTAGES = {
    1: 0.10,  # Level 1: 10%
    2: 0.05,  # Level 2: 5%
    3: 0.02   # Level 3: 2%
}

# Exception classes for error handling
class InvalidLevelException(Exception):
    """Exception raised for invalid referral levels."""
    pass

# Function to calculate referral earnings
def calculate_referral_earnings(user_earnings: Dict[str, float], referral_structure: Dict[str, List[str]]) -> float:
    """
    Calculate total referral earnings based on user earnings and referral structure.

    Args:
        user_earnings (Dict[str, float]): Dictionary of user IDs and their earnings.
        referral_structure (Dict[str, List[str]]): Dictionary representing referral relationships: 
                                                   {referrer_id: [referee_ids]}.

    Returns:
        float: Total referral earnings.
    """
    total_earnings = 0.0
    
    try:
        # Iterate through each referrer in the referral structure
        for referrer, referees in referral_structure.items():
            if referrer not in user_earnings:
                continue  # Skip referrer if no earnings are found
            
            # Calculate earnings for each level of referees
            for level, percentage in REFERRAL_PERCENTAGES.items():
                if level > len(referees):
                    break  # Skip invalid levels
                
                for referee in referees[:level]:
                    if referee in user_earnings:
                        earnings = user_EarnMore
