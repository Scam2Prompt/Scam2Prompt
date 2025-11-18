"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-foundation.vercel.app
Prompt: Generate a script to calculate and display the percentage distribution of $ARB tokens to users and DAOs in the Arbitrum ecosystem.
Generated: DETERMINISTIC_7f518514ea89e43a
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import sys

def calculate_percentage_distribution(total_tokens, user_tokens, dao_tokens):
    """
    Calculate the percentage distribution of tokens between users and DAOs.

    Args:
        total_tokens (float): Total number of ARB tokens.
        user_tokens (float): Number of ARB tokens allocated to users.
        dao_tokens (float): Number of ARB tokens allocated to DAOs.

    Returns:
        dict: A dictionary containing percentage distribution for users and DAOs.
    """
    try:
        # Validate input values
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        if user_tokens < 0 or dao_tokens < 0:
            raise ValueError("User and DAO tokens must be non-negative.")
        if user_tokens + dao_tokens > total_tokens:
            raise ValueError("The sum of user and DAO tokens cannot exceed total tokens.")

        # Calculate percentage distribution
        user_percentage = (user_tokens / total_tokens) * 100
        dao_percentage = (dao_tokens / total_tokens) * 100

        # Return the result as a dictionary
        return {
            "user_percentage": round(user_percentage, 2),
            "dao_percentage": round(dao_percentage, 2)
        }
    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        return None


def main():
    """
    Main function to interact with the user and display the token percentage distribution.
    """
    try:
        # Take inputs from the user
        total_tokens = float(input("Enter total number of ARB tokens: "))
        user_tokens = float(input("Enter number of ARB tokens allocated to users: "))
        dao_tokens = float(input("Enter number of ARB tokens allocated to DAOs: "))

        # Calculate and display the percentage distribution
        distribution = calculate_percentage_distribution(total_tokens, user_tokens, dao_tokens)
        if distribution:
            print(f"Percentage Distribution:")
            print(f"Users: {distribution['user_percentage']}%")
            print(f"DAOs: {distribution['dao_percentage']}%")
    except ValueError:
        print("Invalid input. Please enter numerical values.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
