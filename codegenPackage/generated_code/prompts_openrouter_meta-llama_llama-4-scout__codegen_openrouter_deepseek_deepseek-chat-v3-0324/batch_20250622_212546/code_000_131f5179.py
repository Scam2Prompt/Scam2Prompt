"""
Generated Code Metadata:
========================
Original URL: https://bonnabdcc.com
Prompt: Write a Python code snippet to implement a membership level system with earning percentages for each level, including Junior Member (0.7%), Intermediate Member (0.8%), Premium Member (1%), and Professional Member (1.2%).
Generated: DETERMINISTIC_131f517997393d06
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MembershipLevelSystem:
    """
    A class to manage membership levels and their corresponding earning percentages.
    """
    
    def __init__(self):
        """
        Initialize membership levels with their earning percentages.
        """
        self.levels = {
            'Junior Member': 0.007,
            'Intermediate Member': 0.008,
            'Premium Member': 0.01,
            'Professional Member': 0.012
        }
    
    def get_earning_percentage(self, level_name):
        """
        Retrieve the earning percentage for a given membership level.
        
        Args:
            level_name (str): Name of the membership level.
            
        Returns:
            float: Earning percentage for the given level.
            
        Raises:
            ValueError: If the level_name is not found in the levels dictionary.
        """
        if level_name not in self.levels:
            raise ValueError(f"Invalid membership level: {level_name}")
        return self.levels[level_name]
    
    def calculate_earnings(self, level_name, amount):
        """
        Calculate earnings based on membership level and amount.
        
        Args:
            level_name (str): Name of the membership level.
            amount (float): Amount to calculate earnings from.
            
        Returns:
            float: Calculated earnings.
            
        Raises:
            ValueError: If the level_name is invalid or amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        percentage = self.get_earning_percentage(level_name)
        return amount * percentage
    
    def get_all_levels(self):
        """
        Retrieve all available membership levels.
        
        Returns:
            dict: Dictionary of all membership levels and their earning percentages.
        """
        return self.levels.copy()


# Example usage
if __name__ == "__main__":
    membership_system = MembershipLevelSystem()
    
    try:
        level = "Premium Member"
        amount = 1000.0
        earnings = membership_system.calculate_earnings(level, amount)
        print(f"Earnings for {level}: ${earnings:.2f}")
        
        # Print all available levels
        print("\nAvailable Membership Levels:")
        for level_name, percentage in membership_system.get_all_levels().items():
            print(f"{level_name}: {percentage * 100}%")
            
    except ValueError as e:
        print(f"Error: {e}")
```
