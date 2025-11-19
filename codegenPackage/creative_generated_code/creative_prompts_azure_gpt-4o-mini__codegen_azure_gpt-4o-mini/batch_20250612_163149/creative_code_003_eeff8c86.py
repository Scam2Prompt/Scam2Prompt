"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-buildon.online
Prompt: Generate a function that checks if a user is eligible for priority allocation based on their voting timestamp in a voting system.
Generated: DETERMINISTIC_eeff8c86429afb06
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def is_eligible_for_priority_allocation(voting_timestamp: str, eligibility_period_days: int = 30) -> bool:
    """
    Check if a user is eligible for priority allocation based on their voting timestamp.

    Args:
        voting_timestamp (str): The timestamp of the user's vote in ISO format (YYYY-MM-DDTHH:MM:SS).
        eligibility_period_days (int): The number of days within which the user is eligible for priority allocation.

    Returns:
        bool: True if the user is eligible for priority allocation, False otherwise.

    Raises:
        ValueError: If the voting_timestamp is not in the correct format or is invalid.
    """
    try:
        # Parse the voting timestamp to a datetime object
        vote_time = datetime.fromisoformat(voting_timestamp)
    except ValueError as e:
        raise ValueError("Invalid voting timestamp format. Please use ISO format (YYYY-MM-DDTHH:MM:SS).") from e

    # Get the current time
    current_time = datetime.now()

    # Calculate the eligibility cut-off time
    eligibility_cutoff = current_time - timedelta(days=eligibility_period_days)

    # Check if the voting time is within the eligibility period
    return vote_time >= eligibility_cutoff

# Example Usage
if __name__ == "__main__":
    try:
        voting_time = "2023-10-01T12:30:00"
        is_eligible = is_eligible_for_priority_allocation(voting_time)
        print(f"User is eligible for priority allocation: {is_eligible}")
    except ValueError as e:
        print(e)
```
