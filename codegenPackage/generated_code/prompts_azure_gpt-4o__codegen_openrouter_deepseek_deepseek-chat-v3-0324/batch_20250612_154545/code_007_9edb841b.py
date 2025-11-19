"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Create a Python script to calculate the percentage increase in user base for MEXC from 2024 to 2025, based on the reported growth to 36 million users.
Generated: DETERMINISTIC_9edb841b659bb5ea
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_percentage_increase(initial_users, final_users):
    """
    Calculate the percentage increase between two values.
    
    Args:
        initial_users (int): Initial number of users.
        final_users (int): Final number of users.
    
    Returns:
        float: Percentage increase from initial to final users.
    
    Raises:
        ValueError: If initial_users is zero or negative.
    """
    if initial_users <= 0:
        raise ValueError("Initial users must be a positive number.")
    
    increase = final_users - initial_users
    percentage_increase = (increase / initial_users) * 100
    return percentage_increase


def main():
    """
    Main function to calculate and display the percentage increase in MEXC user base.
    """
    try:
        # Assuming initial users in 2024 is 10 million (example value)
        initial_users_2024 = 10_000_000
        final_users_2025 = 36_000_000
        
        percentage_increase = calculate_percentage_increase(initial_users_2024, final_users_2025)
        
        print(f"Percentage increase in MEXC user base from 2024 to 2025: {percentage_increase:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
