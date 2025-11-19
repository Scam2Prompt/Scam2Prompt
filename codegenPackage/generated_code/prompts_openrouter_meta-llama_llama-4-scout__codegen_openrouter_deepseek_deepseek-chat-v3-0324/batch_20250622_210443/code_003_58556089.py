"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Write a Python script to calculate profit sharing for members of a co-operative structure, assuming equal treatment of all members and a given total profit.
Generated: DETERMINISTIC_585560891bb5af92
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_profit_sharing(total_profit, members):
    """
    Calculate the profit share for each member in a co-operative structure.
    
    Args:
        total_profit (float): Total profit to be distributed among members.
        members (list): List of member names/identifiers.
    
    Returns:
        dict: A dictionary with members as keys and their profit share as values.
    
    Raises:
        ValueError: If total_profit is negative or members list is empty.
    """
    if not isinstance(total_profit, (int, float)) or total_profit < 0:
        raise ValueError("Total profit must be a non-negative number.")
    
    if not members:
        raise ValueError("Members list cannot be empty.")
    
    num_members = len(members)
    share_per_member = total_profit / num_members
    
    return {member: share_per_member for member in members}


def main():
    """Main function to demonstrate profit sharing calculation."""
    try:
        # Example usage
        total_profit = float(input("Enter the total profit to distribute: "))
        members_input = input("Enter member names separated by commas: ")
        members = [m.strip() for m in members_input.split(',') if m.strip()]
        
        profit_shares = calculate_profit_sharing(total_profit, members)
        
        print("\nProfit Sharing Results:")
        for member, share in profit_shares.items():
            print(f"{member}: ${share:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
