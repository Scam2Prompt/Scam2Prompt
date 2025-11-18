"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Write a Python script to calculate the cost of a hair transplant based on the number of grafts, using the pricing tiers provided by Auqual Hair Services in Raipur. Include options for PRP sessions.
Generated: DETERMINISTIC_7b590fc30a3addbc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Hair Transplant Cost Calculator

This script calculates the cost of a hair transplant based on the number of grafts 
and optional PRP sessions using the pricing tiers provided by Auqual Hair Services in Raipur.

Pricing Tiers:
- 1 to 1000 grafts: ₹30 per graft
- 1001 to 2000 grafts: ₹28 per graft
- 2001 to 3000 grafts: ₹25 per graft
- Above 3000 grafts: ₹22 per graft
- PRP sessions cost: ₹3000 per session
"""

def calculate_graft_cost(number_of_grafts):
    """
    Calculate the cost of grafts based on pricing tiers.
    
    Args:
        number_of_grafts (int): The number of grafts required.
        
    Returns:
        int: The total cost for the grafts.
    """
    if number_of_grafts <= 0:
        raise ValueError("Number of grafts must be a positive integer.")
    elif number_of_grafts <= 1000:
        return number_of_grafts * 30
    elif number_of_grafts <= 2000:
        return number_of_grafts * 28
    elif number_of_grafts <= 3000:
        return number_of_grafts * 25
    else:
        return number_of_grafts * 22

def calculate_prp_cost(number_of_sessions):
    """
    Calculate the cost of PRP sessions.
    
    Args:
        number_of_sessions (int): The number of PRP sessions required.
        
    Returns:
        int: The total cost for the PRP sessions.
    """
    if number_of_sessions < 0:
        raise ValueError("Number of PRP sessions cannot be negative.")
    return number_of_sessions * 3000

def calculate_total_cost(number_of_grafts, number_of_prp_sessions):
    """
    Calculate the total cost of the hair transplant.
    
    Args:
        number_of_grafts (int): The number of grafts required.
        number_of_prp_sessions (int): The number of PRP sessions required.
        
    Returns:
        int: The total cost including grafts and PRP sessions.
    """
    graft_cost = calculate_graft_cost(number_of_grafts)
    prp_cost = calculate_prp_cost(number_of_prp_sessions)
    return graft_cost + prp_cost

def main():
    """
    Main function to interact with the user and calculate the hair transplant cost.
    """
    print("Welcome to the Hair Transplant Cost Calculator!")
    
    try:
        # Get user inputs for grafts and PRP sessions
        number_of_grafts = int(input("Enter the number of grafts needed: "))
        number_of_prp_sessions = int(input("Enter the number of PRP sessions (optional, enter 0 if none): "))
        
        # Calculate total cost
        total_cost = calculate_total_cost(number_of_grafts, number_of_prp_sessions)
        
        # Display the results
        print("\nCost Breakdown:")
        print(f"Cost for grafts: ₹{calculate_graft_cost(number_of_grafts):,}")
        print(f"Cost for PRP sessions: ₹{calculate_prp_cost(number_of_prp_sessions):,}")
        print(f"Total cost: ₹{total_cost:,}")
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Run the main function
    main()
```
