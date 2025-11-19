"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Write a Python function that calculates the total cost for a package of "Madérothérapie" sessions based on user input for the number of sessions selected.
Generated: DETERMINISTIC_475b29a74b49eb51
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_cost(num_sessions, cost_per_session=100.0):
    """
    Calculate the total cost for a package of Madérothérapie sessions.

    Parameters:
    num_sessions (int): The number of sessions selected by the user.
    cost_per_session (float): The cost of a single session (default is 100.0).

    Returns:
    float: The total cost for the selected number of sessions.

    Raises:
    ValueError: If num_sessions is not a positive integer or if cost_per_session is negative.
    """
    
    # Validate the number of sessions
    if not isinstance(num_sessions, int) or num_sessions <= 0:
        raise ValueError("Number of sessions must be a positive integer.")
    
    # Validate the cost per session
    if not isinstance(cost_per_session, (int, float)) or cost_per_session < 0:
        raise ValueError("Cost per session must be a non-negative number.")
    
    # Calculate the total cost
    total_cost = num_sessions * cost_per_session
    
    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        sessions = int(input("Enter the number of sessions: "))
        total = calculate_total_cost(sessions)
        print(f"The total cost for {sessions} sessions is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
