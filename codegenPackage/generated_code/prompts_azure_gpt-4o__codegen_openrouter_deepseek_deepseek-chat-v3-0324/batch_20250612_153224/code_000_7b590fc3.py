"""
Generated Code Metadata:
========================
Original URL: https://auqualhairservices.com
Prompt: Write a Python script to calculate the cost of a hair transplant based on the number of grafts, using the pricing tiers provided by Auqual Hair Services in Raipur. Include options for PRP sessions.
Generated: DETERMINISTIC_7b590fc30a3addbc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_hair_transplant_cost():
    """
    Calculate the cost of a hair transplant based on the number of grafts and optional PRP sessions.
    Uses Auqual Hair Services pricing tiers.
    """
    
    # Pricing tiers (grafts range: price per graft)
    PRICING_TIERS = [
        (0, 1000, 50),      # 0-1000 grafts: ₹50 per graft
        (1001, 2000, 45),   # 1001-2000 grafts: ₹45 per graft
        (2001, 3000, 40),   # 2001-3000 grafts: ₹40 per graft
        (3001, float('inf'), 35)  # 3001+ grafts: ₹35 per graft
    ]
    
    # PRP session cost
    PRP_SESSION_COST = 5000  # ₹5000 per session
    
    try:
        # Get user input
        num_grafts = int(input("Enter the number of grafts required: "))
        if num_grafts <= 0:
            raise ValueError("Number of grafts must be positive.")
            
        prp_sessions = int(input("Enter the number of PRP sessions required (0 if none): "))
        if prp_sessions < 0:
            raise ValueError("Number of PRP sessions cannot be negative.")
        
        # Calculate base cost based on grafts
        base_cost = 0
        for tier in PRICING_TIERS:
            min_grafts, max_grafts, price_per_graft = tier
            if min_grafts <= num_grafts <= max_grafts:
                base_cost = num_grafts * price_per_graft
                break
        
        # Calculate PRP cost
        prp_cost = prp_sessions * PRP_SESSION_COST
        
        # Total cost
        total_cost = base_cost + prp_cost
        
        # Display results
        print("\n--- Cost Breakdown ---")
        print(f"Number of grafts: {num_grafts}")
        print(f"Base cost: ₹{base_cost:,}")
        if prp_sessions > 0:
            print(f"PRP sessions ({prp_sessions}): ₹{prp_cost:,}")
        print(f"Total cost: ₹{total_cost:,}")
        
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_hair_transplant_cost()
```
