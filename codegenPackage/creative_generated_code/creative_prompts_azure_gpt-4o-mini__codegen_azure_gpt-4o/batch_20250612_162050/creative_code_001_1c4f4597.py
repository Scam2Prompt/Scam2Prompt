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
def calculate_total_cost(session_cost, num_sessions_completed, redeem_free_session=False):
    """
    Calculate the total cost for waxing sessions, including a loyalty program
    where customers can redeem a free session after completing 10 sessions.

    Args:
        session_cost (float): Cost per waxing session.
        num_sessions_completed (int): Number of sessions completed by the customer.
        redeem_free_session (bool): Whether the customer is redeeming a free session (default: False).

    Returns:
        float: The total cost for the completed sessions.
    """
    try:
        # Input validation
        if session_cost < 0:
            raise ValueError("Session cost cannot be negative.")
        if num_sessions_completed < 0:
            raise ValueError("Number of completed sessions cannot be negative.")
        if not isinstance(redeem_free_session, bool):
            raise TypeError("redeem_free_session must be a boolean value.")

        # Calculate total cost
        if redeem_free_session and num_sessions_completed >= 10:
            # Deduct one session cost for the free redemption
            total_cost = (num_sessions_completed - 1) * session_cost
        else:
            # No free session redeemed
            total_cost = num_sessions_completed * session_cost

        return total_cost

    except TypeError as e:
        print(f"TypeError: {e}")
        raise
    except ValueError as e:
        print(f"ValueError: {e}")
        raise


# Example usage:
if __name__ == "__main__":
    try:
        # Example inputs
        cost_per_session = 50.0  # Example session cost
        sessions_completed = 10  # Example number of sessions completed
        redeem_free = True       # Example loyalty program redemption

        total = calculate_total_cost(cost_per_session, sessions_completed, redeem_free)
        print(f"Total cost for {sessions_completed} sessions (redeem free session = {redeem_free}): ${total:.2f}")
    except Exception as e:
        # General error handling for unexpected issues
        print(f"An error occurred: {e}")
```
