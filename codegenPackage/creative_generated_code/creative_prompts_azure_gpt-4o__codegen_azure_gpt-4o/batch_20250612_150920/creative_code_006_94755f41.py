"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptexbit.com
Prompt: Create a script to calculate the Cryco governance model's resource allocation percentages for holders, members, leaders, founders, and co-creators.
Generated: DETERMINISTIC_94755f4107c15f21
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Cryco Governance Resource Allocation Script

This script calculates resource allocation percentages for various roles
in the Cryco governance model: holders, members, leaders, founders, and co-creators.

Roles:
- Holders: % of total resource allocation
- Members: % of total resource allocation
- Leaders: % of total resource allocation
- Founders: % of total resource allocation
- Co-creators: % of total resource allocation

The allocation percentages must sum to 100%.

Author: <Your Name>
"""

# Import necessary modules
import sys

# Function to calculate governance resource allocation
def calculate_resource_allocation(holder_pct, member_pct, leader_pct, founder_pct, cocreator_pct):
    """
    Calculate and validate resource allocation percentages.

    Parameters:
        holder_pct (float): Percentage allocated to holders.
        member_pct (float): Percentage allocated to members.
        leader_pct (float): Percentage allocated to leaders.
        founder_pct (float): Percentage allocated to founders.
        cocreator_pct (float): Percentage allocated to co-creators.

    Returns:
        dict: A dictionary with validated resource allocations per role.
    """
    # Validate that all inputs are percentages (non-negative numbers)
    allocations = [holder_pct, member_pct, leader_pct, founder_pct, cocreator_pct]
    if not all(isinstance(pct, (int, float)) and pct >= 0 for pct in allocations):
        raise ValueError("All allocation percentages must be non-negative numbers.")

    # Ensure the total allocation sums to 100%
    total_allocation = sum(allocations)
    if total_allocation != 100:
        raise ValueError(f"Total allocation must sum to 100%. Current total: {total_allocation}%.")

    # Return allocations as a dictionary
    return {
        "Holders": holder_pct,
        "Members": member_pct,
        "Leaders": leader_pct,
        "Founders": founder_pct,
        "Co-creators": cocreator_pct,
    }

def main():
    """
    Main function to interactively calculate Cryco governance resource allocations.
    """
    print("Cryco Governance Resource Allocation Calculator")
    print("Please enter percentages for each role (must sum to 100%):")
    
    try:
        # Collect user input for each role
        holder_pct = float(input("Enter allocation for Holders (%): "))
        member_pct = float(input("Enter allocation for Members (%): "))
        leader_pct = float(input("Enter allocation for Leaders (%): "))
        founder_pct = float(input("Enter allocation for Founders (%): "))
        cocreator_pct = float(input("Enter allocation for Co-creators (%): "))
        
        # Calculate and validate allocations
        allocations = calculate_resource_allocation(
            holder_pct, member_pct, leader_pct, founder_pct, cocreator_pct
        )
        
        # Display the calculated allocations
        print("\nResource Allocation Percentages:")
        for role, pct in allocations.items():
            print(f"{role}: {pct}%")
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
