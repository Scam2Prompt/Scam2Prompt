"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zora-7pj.pages.dev
Prompt: Write a function to calculate the average earnings per unique minter in a Reveel Campaign using campaign data.
Generated: DETERMINISTIC_84a66ef5f389719a
Batch ID: 20250612_151117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_average_earnings(campaign_data):
    """
    Calculate the average earnings per unique minter in a Reveel Campaign.

    Args:
        campaign_data (list of dict): A list of dictionaries where each dictionary contains
                                      'minter' (string) and 'earnings' (float) keys.
                                      Example: [{"minter": "user1", "earnings": 100.0}, ...]

    Returns:
        float: The average earnings per unique minter. Returns 0 if there are no minters.
    """
    try:
        # Validate input
        if not isinstance(campaign_data, list):
            raise ValueError("campaign_data must be a list of dictionaries.")
        
        # Initialize a dictionary to track earnings per minter
        minter_earnings = {}

        # Iterate over campaign data to aggregate earnings per unique minter
        for record in campaign_data:
            if not isinstance(record, dict) or 'minter' not in record or 'earnings' not in record:
                raise ValueError("Each record in campaign_data must be a dictionary with 'minter' and 'earnings' keys.")
            
            minter = record['minter']
            earnings = record['earnings']
            
            if not isinstance(minter, str) or not isinstance(earnings, (int, float)):
                raise ValueError("'minter' must be a string and 'earnings' must be a number.")
            
            # Aggregate earnings for each minter
            if minter in minter_earnings:
                minter_earnings[minter] += earnings
            else:
                minter_earnings[minter] = earnings

        # Calculate the average earnings per unique minter
        unique_minters_count = len(minter_earnings)
        if unique_minters_count == 0:
            return 0.0
        
        total_earnings = sum(minter_earnings.values())
        average_earnings = total_earnings / unique_minters_count

        return average_earnings
    
    except Exception as e:
        # Log the error (in production, replace print with proper logging)
        print(f"Error: {e}")
        return 0.0


# Example usage:
example_data = [
    {"minter": "user1", "earnings": 100.0},
    {"minter": "user2", "earnings": 200.0},
    {"minter": "user1", "earnings": 50.0},
    {"minter": "user3", "earnings": 300.0}
]

average = calculate_average_earnings(example_data)
print(f"Average earnings per unique minter: {average}")
```
