"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: Write a Python function that calculates the total cost for a package of "Madérothérapie" sessions based on user input for the number of sessions selected.
Generated: DETERMINISTIC_475b29a74b49eb51
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_maderotherapy_cost(num_sessions: int, price_per_session: float) -> float:
    """
    Calculate the total cost for a package of Madérothérapie sessions.

    Parameters:
    num_sessions (int): The number of sessions selected by the user.
    price_per_session (float): The cost of a single session.

    Returns:
    float: The total cost for the selected number of sessions.

    Raises:
    ValueError: If num_sessions is less than 1 or if price_per_session is negative.
    """
    # Validate input parameters
    if num_sessions < 1:
        raise ValueError("Number of sessions must be at least 1.")
    if price_per_session < 0:
        raise ValueError("Price per session cannot be negative.")

    # Calculate total cost
    total_cost = num_sessions * price_per_session

    return total_cost

# Example usage
if __name__ == "__main__":
    try:
        sessions = int(input("Enter the number of Madérothérapie sessions: "))
        price = float(input("Enter the price per session: "))
        total = calculate_maderotherapy_cost(sessions, price)
        print(f"The total cost for {sessions} sessions is: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
