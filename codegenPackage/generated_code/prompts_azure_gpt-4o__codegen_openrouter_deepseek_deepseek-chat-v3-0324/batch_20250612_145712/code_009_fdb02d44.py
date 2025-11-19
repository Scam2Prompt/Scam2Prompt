"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Create a function in Python to simulate the "double energy" feature, where subscribing to a sponsor channel doubles the user's energy, as described in the Khaby Lame Coin WebApp.
Generated: DETERMINISTIC_fdb02d444bb9f962
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def double_energy(user_energy: int, is_subscribed: bool) -> int:
    """
    Simulates the "double energy" feature where subscribing to a sponsor channel
    doubles the user's energy.

    Args:
        user_energy (int): The current energy of the user.
        is_subscribed (bool): Whether the user is subscribed to the sponsor channel.

    Returns:
        int: The user's energy after applying the double energy feature if subscribed,
             otherwise returns the original energy.

    Raises:
        ValueError: If user_energy is negative.
    """
    if user_energy < 0:
        raise ValueError("User energy cannot be negative.")
    
    if is_subscribed:
        return user_energy * 2
    return user_energy
```
