"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialcocoro.xyz
Prompt: Write a function to calculate the total cryptocurrency donations made by an organization, using data similar to "Own The Doge's" $2M USD donations to charities.
Generated: DETERMINISTIC_f79fccb7984b570c
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_total_donations(donation_data):
    """
    Calculate the total cryptocurrency donations made by an organization.
    
    Args:
        donation_data (list): A list of donation records, where each record is a dictionary
                              containing 'amount_usd' (float) representing donation in USD.
                              
    Returns:
        float: The total donation amount in USD.
    """
    try:
        # Validate input type
        if not isinstance(donation_data, list):
            raise ValueError("Donation data must be a list of dictionaries.")
        
        total_donations = 0.0

        # Iterate through donation records
        for record in donation_data:
            # Validate record format
            if not isinstance(record, dict) or 'amount_usd' not in record:
                raise ValueError("Each donation record must be a dictionary containing 'amount_usd'.")
            
            # Validate that 'amount_usd' is numeric
            if not isinstance(record['amount_usd'], (int, float)):
                raise ValueError("'amount_usd' must be an integer or float.")
            
            # Accumulate donation amounts
            total_donations += record['amount_usd']

        return total_donations
    
    except ValueError as ve:
        # Log or handle specific errors
        print(f"ValueError: {ve}")
        return 0.0
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Example donation data (similar to "Own The Doge's" donations)
    donation_data = [
        {"amount_usd": 500000.00},
        {"amount_usd": 750000.00},
        {"amount_usd": 250000.00},
        {"amount_usd": 500000.00},
    ]

    total = calculate_total_donations(donation_data)
    print(f"Total cryptocurrency donations: ${total:.2f}")
```
