"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: "Design a loyalty program using EARN'M's ecosystem, targeting an average user redemption rate of 11.2 codes, and calculate the potential earnings and savings."
Generated: DETERMINISTIC_196be4d4e299698f
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class LoyaltyProgram:
    """
    A class to model a loyalty program within the EARN'M ecosystem.
    Calculates potential earnings and savings based on user redemption rates.
    """
    
    def __init__(self, redemption_rate: float = 11.2, code_value: float = 1.0):
        """
        Initialize the loyalty program with default parameters.
        
        Args:
            redemption_rate (float): Average number of codes redeemed per user (default: 11.2)
            code_value (float): Monetary value of each code in dollars (default: 1.0)
        """
        self.redemption_rate = redemption_rate
        self.code_value = code_value
        
    def calculate_earnings(self, user_count: int) -> Dict[str, float]:
        """
        Calculate potential earnings and savings for a given number of users.
        
        Args:
            user_count (int): Number of users in the program
            
        Returns:
            Dict[str, float]: Dictionary containing total codes, earnings, and savings
        """
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("User count must be a positive integer")
            
        total_codes = self.redemption_rate * user_count
        total_earnings = total_codes * self.code_value
        total_savings = total_earnings * 0.2  # Assuming 20% savings from partnerships
        
        return {
            "total_codes": total_codes,
            "total_earnings": total_earnings,
            "total_savings": total_savings
        }
    
    def calculate_breakdown(self, user_count: int) -> List[Dict[str, float]]:
        """
        Calculate monthly breakdown of earnings and savings for visualization.
        
        Args:
            user_count (int): Number of users in the program
            
        Returns:
            List[Dict[str, float]]: Monthly breakdown data
        """
        if not isinstance(user_count, int) or user_count < 0:
            raise ValueError("User count must be a positive integer")
            
        monthly_data = []
        monthly_users = math.ceil(user_count / 12)
        
        for month in range(1, 13):
            current_users = min(monthly_users * month, user_count)
            month_data = self.calculate_earnings(current_users)
            month_data["month"] = month
            monthly_data.append(month_data)
            
        return monthly_data

    def optimize_redemption_rate(self, target_earnings: float, max_users: int) -> Tuple[float, Dict[str, float]]:
        """
        Calculate required redemption rate to reach target earnings with given max users.
        
        Args:
            target_earnings (float): Desired total earnings
            max_users (int): Maximum number of users available
            
        Returns:
            Tuple[float, Dict[str, float]]: Required redemption rate and resulting metrics
        """
        if target_earnings <= 0 or max_users <= 0:
            raise ValueError("Target earnings and max users must be positive values")
            
        required_rate = target_earnings / (max_users * self.code_value)
        result = self.calculate_earnings(max_users)
        
        return (required_rate, result)


# Example usage
if __name__ == "__main__":
    try:
        program = LoyaltyProgram()
        
        # Calculate for 10,000 users
        metrics = program.calculate_earnings(10000)
        print(f"Total codes: {metrics['total_codes']:,.0f}")
        print(f"Total earnings: ${metrics['total_earnings']:,.2f}")
        print(f"Total savings: ${metrics['total_savings']:,.2f}")
        
        # Calculate required redemption rate for $1M earnings with 50k users
        required_rate, result = program.optimize_redemption_rate(1_000_000, 50_000)
        print(f"\nRequired redemption rate: {required_rate:.2f} codes/user")
        print(f"Projected earnings: ${result['total_earnings']:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
