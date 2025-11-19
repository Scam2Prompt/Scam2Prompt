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
# monthly_active_users.py

class MobileGameStudio:
    def __init__(self, web3_users, total_monthly_active_users):
        """
        Initialize a MobileGameStudio object.

        Args:
            web3_users (int): The number of web3 users.
            total_monthly_active_users (int): The total number of monthly active users.
        """
        self.web3_users = web3_users
        self.total_monthly_active_users = total_monthly_active_users

    def calculate_non_web3_users(self):
        """
        Calculate the number of non-web3 users.

        Returns:
            int: The number of non-web3 users.
        """
        return self.total_monthly_active_users - self.web3_users

    def get_user_distribution(self):
        """
        Get the distribution of web3 and non-web3 users.

        Returns:
            dict: A dictionary containing the distribution of web3 and non-web3 users.
        """
        non_web3_users = self.calculate_non_web3_users()
        return {
            "web3_users": self.web3_users,
            "non_web3_users": non_web3_users,
            "total_users": self.total_monthly_active_users
        }

    def print_user_analysis(self):
        """
        Print a summary of the user analysis.
        """
        user_distribution = self.get_user_distribution()
        print("Monthly Active Users Analysis:")
        print(f"Web3 Users: {user_distribution['web3_users']:,}")
        print(f"Non-Web3 Users: {user_distribution['non_web3_users']:,}")
        print(f"Total Monthly Active Users: {user_distribution['total_users']:,}")
        print(f"Web3 Users Percentage: {(self.web3_users / user_distribution['total_users']) * 100:.2f}%")
        print(f"Non-Web3 Users Percentage: {(user_distribution['non_web3_users'] / user_distribution['total_users']) * 100:.2f}%")

def main():
    try:
        web3_users = 1030000
        total_monthly_active_users = 5000000
        studio = MobileGameStudio(web3_users, total_monthly_active_users)
        studio.print_user_analysis()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
