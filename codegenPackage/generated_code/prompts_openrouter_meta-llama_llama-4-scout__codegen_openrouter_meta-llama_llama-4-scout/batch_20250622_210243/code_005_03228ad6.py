"""
Generated Code Metadata:
========================
Original URL: https://vetterplatform.pages.dev
Prompt: Write a function to calculate the guaranteed allocations of preons based on the total amount of preons owned by a user and the community.
Generated: DETERMINISTIC_03228ad6a86d6aad
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_guaranteed_allocations(total_preons: int, community_preons: int, 
                                      user_preons_percentage: float) -> float:
    """
    Calculate the guaranteed allocations of preons based on the total amount of 
    preons owned by a user and the community.

    Args:
    - total_preons (int): The total amount of preons.
    - community_preons (int): The total amount of preons owned by the community.
    - user_preons_percentage (float): The percentage of preons owned by the user.

    Returns:
    - float: The guaranteed allocations of preons.

    Raises:
    - ValueError: If total_preons, community_preons, or user_preons_percentage is invalid.
    """

    # Validate inputs
    if total_preons < 0:
        raise ValueError("Total preons cannot be negative.")
    if community_preons < 0:
        raise ValueError("Community preons cannot be negative.")
    if user_preons_percentage < 0 or user_preons_percentage > 100:
        raise ValueError("User preons percentage must be between 0 and 100.")

    # Calculate user preons
    user_preons = (user_preons_percentage / 100) * total_preons

    # Check for division by zero
    if total_preons == 0:
        return 0

    # Calculate guaranteed allocations
    guaranteed_allocations = (user_preons / total_preons) * community_preons

    return guaranteed_allocations


def main():
    try:
        total_preons = 10000
        community_preons = 5000
        user_preons_percentage = 20

        guaranteed_allocations = calculate_guaranteed_allocations(
            total_preons, community_preons, user_preons_percentage
        )
        print(f"Guaranteed allocations: {guaranteed_allocations}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
