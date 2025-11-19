"""
Generated Code Metadata:
========================
Original URL: https://playember-57a.pages.dev
Prompt: Write a Python script to analyze the monthly active users of a mobile game studio like Playember, which has 1.03M web3 users and 5M total monthly active users.
Generated: DETERMINISTIC_5d2cc65843d62f56
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def analyze_users(web3_users: int, total_users: int) -> dict:
    """
    Analyze the monthly active users of a mobile game studio.

    Args:
        web3_users (int): Number of web3 users.
        total_users (int): Total number of monthly active users.

    Returns:
        dict: A dictionary containing analysis results.
    """
    try:
        # Validate inputs
        if web3_users < 0 or total_users < 0:
            raise ValueError("User counts must be non-negative integers.")
        if web3_users > total_users:
            raise ValueError("Web3 users cannot exceed total users.")

        # Calculate percentages
        web3_percentage = (web3_users / total_users) * 100
        non_web3_users = total_users - web3_users
        non_web3_percentage = (non_web3_users / total_users) * 100

        # Log the results
        logging.info("Analysis completed successfully.")
        logging.info(f"Web3 Users: {web3_users} ({web3_percentage:.2f}%)")
        logging.info(f"Non-Web3 Users: {non_web3_users} ({non_web3_percentage:.2f}%)")

        # Return results as a dictionary
        return {
            "web3_users": web3_users,
            "web3_percentage": round(web3_percentage, 2),
            "non_web3_users": non_web3_users,
            "non_web3_percentage": round(non_web3_percentage, 2),
            "total_users": total_users
        }

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example data
    web3_users = 1030000  # 1.03M web3 users
    total_users = 5000000  # 5M total monthly active users

    try:
        # Perform analysis
        results = analyze_users(web3_users, total_users)

        # Display results
        print("Monthly Active Users Analysis:")
        print(f"Total Users: {results['total_users']}")
        print(f"Web3 Users: {results['web3_users']} ({results['web3_percentage']}%)")
        print(f"Non-Web3 Users: {results['non_web3_users']} ({results['non_web3_percentage']}%)")
    except Exception as e:
        print(f"Error: {e}")
```
