"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applobalspros22.pages.dev
Prompt: What are common reasons for account suspension in web hosting, and how can I prevent them?
Generated: DETERMINISTIC_ec61492dbea5f428
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HostingAccount:
    """
    A class to represent a web hosting account.
    """

    def __init__(self, username, disk_usage, bandwidth_usage, payment_status):
        """
        Initializes a new instance of HostingAccount.

        :param username: str - The username of the account holder
        :param disk_usage: float - Current disk usage in GB
        :param bandwidth_usage: float - Current bandwidth usage in GB
        :param payment_status: bool - Payment status of the account (True if paid, False if unpaid)
        """
        self.username = username
        self.disk_usage = disk_usage
        self.bandwidth_usage = bandwidth_usage
        self.payment_status = payment_status
        self.suspended = False

    def check_suspension(self):
        """
        Checks if the account is suspended based on common reasons.
        """
        if self.disk_usage > 100:  # Assuming the limit is 100 GB
            self.suspended = True
            return "Account suspended due to exceeding disk usage limit."
        elif self.bandwidth_usage > 500:  # Assuming the limit is 500 GB
            self.suspended = True
            return "Account suspended due to exceeding bandwidth usage limit."
        elif not self.payment_status:
            self.suspended = True
            return "Account suspended due to payment issues."
        else:
            return "Account is active."

    def prevent_suspension(self):
        """
        Provides recommendations to prevent account suspension.
        
        :return: list - Recommendations to maintain active status of the account
        """
        recommendations = []
        if self.disk_usage > 90:
            recommendations.append("Consider upgrading your hosting plan or optimizing disk usage.")
        if self.bandwidth_usage > 450:
            recommendations.append("Monitor your bandwidth usage and consider upgrading your plan.")
        if not self.payment_status:
            recommendations.append("Ensure timely payment of hosting fees.")
        return recommendations


# Example usage:
def main():
    """
    Main function to demonstrate account suspension checking and prevention.
    """
    # Create a hosting account instance
    try:
        account = HostingAccount(username="user123", disk_usage=105, bandwidth_usage=400, payment_status=False)

        # Check for suspension
        suspension_message = account.check_suspension()
        print(suspension_message)

        # Get prevention recommendations
        prevention_tips = account.prevent_suspension()
        for tip in prevention_tips:
            print(tip)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
