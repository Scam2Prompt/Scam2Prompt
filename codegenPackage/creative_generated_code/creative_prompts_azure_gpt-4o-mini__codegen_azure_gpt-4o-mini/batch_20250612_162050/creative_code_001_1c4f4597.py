"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://depilarmg.com.br
Prompt: Write a Python function that calculates the total cost for a customer who has completed 10 waxing sessions and wants to redeem a free session based on a loyalty program.
Generated: DETERMINISTIC_1c4f4597fa9e17da
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_waxing_cost(session_cost, num_sessions, free_sessions=1):
    """
    Calculate the total cost for waxing sessions, considering a loyalty program
    that offers a free session after a certain number of paid sessions.
    
    Parameters:
    session_cost (float): The cost of a single waxing session.
    num_sessions (int): The total number of waxing sessions completed by the customer.
    free_sessions (int): The number of free sessions to redeem (default is 1).
    
    Returns:
    float: The total cost after applying the loyalty program discount.
    
    Raises:
    ValueError: If session_cost is negative, or if num_sessions is negative.
    """
    
    # Validate inputs
    if session_cost < 0:
        raise ValueError("Session cost must be non-negative.")
    if num_sessions < 0:
        raise ValueError("Number of sessions must be non-negative.")
    
    # Calculate the number of sessions to be paid for
    paid_sessions = max(num_sessions - free_sessions, 0)
    
    # Calculate total cost
    total_cost = paid_sessions * session_cost
    
    return total_cost

# Example usage:
if __name__ == "__main__":
    try:
        session_cost = 50.0  # Example cost per session
        num_sessions = 10     # Total sessions completed
        total = calculate_total_waxing_cost(session_cost, num_sessions)
        print(f"The total cost after redeeming a free session is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
