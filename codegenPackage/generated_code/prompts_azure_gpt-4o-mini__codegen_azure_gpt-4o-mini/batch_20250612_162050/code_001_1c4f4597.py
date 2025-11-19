"""
Generated Code Metadata:
========================
Original URL: https://depilarmg.com.br
Prompt: Write a Python function that calculates the total cost for a customer who has completed 10 waxing sessions and wants to redeem a free session based on a loyalty program.
Generated: DETERMINISTIC_1c4f4597fa9e17da
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_total_cost(session_cost, total_sessions, free_sessions=1):
    """
    Calculate the total cost for a customer who has completed a number of waxing sessions
    and wants to redeem a free session based on a loyalty program.

    Parameters:
    session_cost (float): The cost of a single waxing session.
    total_sessions (int): The total number of waxing sessions completed by the customer.
    free_sessions (int): The number of free sessions the customer can redeem (default is 1).

    Returns:
    float: The total cost after applying the free sessions.
    
    Raises:
    ValueError: If session_cost is negative or total_sessions is less than zero.
    """
    
    # Validate input parameters
    if session_cost < 0:
        raise ValueError("Session cost cannot be negative.")
    if total_sessions < 0:
        raise ValueError("Total sessions cannot be negative.")
    
    # Calculate the number of paid sessions
    paid_sessions = total_sessions - free_sessions if total_sessions >= free_sessions else total_sessions
    
    # Calculate total cost
    total_cost = paid_sessions * session_cost
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        session_cost = 50.0  # Cost per waxing session
        total_sessions = 10   # Total sessions completed
        total_cost = calculate_total_cost(session_cost, total_sessions)
        print(f"The total cost for {total_sessions} sessions is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
