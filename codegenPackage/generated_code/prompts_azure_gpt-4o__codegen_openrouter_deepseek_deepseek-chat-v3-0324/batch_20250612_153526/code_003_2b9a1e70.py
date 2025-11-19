"""
Generated Code Metadata:
========================
Original URL: https://kinikangg.pages.dev
Prompt: Write code to calculate and display the "win rate" based on full inventory resources, as mentioned in the AI Waifu Spy Result feature.
Generated: DETERMINISTIC_2b9a1e703b82dd05
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_win_rate(inventory_resources):
    """
    Calculate the win rate based on full inventory resources.
    
    Args:
        inventory_resources (dict): Dictionary containing resource counts.
            Expected keys: 'successful_missions', 'failed_missions'
            
    Returns:
        float: Win rate percentage (0-100)
        
    Raises:
        ValueError: If input is invalid or missing required keys
    """
    # Validate input
    if not isinstance(inventory_resources, dict):
        raise ValueError("Inventory resources must be a dictionary")
    
    required_keys = {'successful_missions', 'failed_missions'}
    if not required_keys.issubset(inventory_resources.keys()):
        raise ValueError("Inventory resources missing required keys")
    
    try:
        successful = float(inventory_resources['successful_missions'])
        failed = float(inventory_resources['failed_missions'])
    except (ValueError, TypeError):
        raise ValueError("Mission counts must be numeric values")
    
    # Handle edge cases
    if successful < 0 or failed < 0:
        raise ValueError("Mission counts cannot be negative")
    
    total_missions = successful + failed
    
    if total_missions == 0:
        return 0.0  # Avoid division by zero
    
    win_rate = (successful / total_missions) * 100
    return round(win_rate, 2)

def display_win_rate(win_rate):
    """
    Display the win rate in a user-friendly format.
    
    Args:
        win_rate (float): Win rate percentage (0-100)
    """
    print(f"\n=== AI Waifu Spy Results ===")
    print(f"Current Win Rate: {win_rate}%")
    print("===========================\n")

# Example usage
if __name__ == "__main__":
    try:
        # Sample inventory data
        inventory = {
            'successful_missions': 42,
            'failed_missions': 8
        }
        
        # Calculate and display win rate
        win_rate = calculate_win_rate(inventory)
        display_win_rate(win_rate)
        
    except ValueError as e:
        print(f"Error calculating win rate: {e}")
```
