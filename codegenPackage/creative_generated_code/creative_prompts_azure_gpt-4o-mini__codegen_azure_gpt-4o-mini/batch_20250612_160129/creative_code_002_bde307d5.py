"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dtstradings.com
Prompt: What are common reasons for a web hosting account suspension and how can I avoid them?
Generated: DETERMINISTIC_bde307d5cebaeca8
Batch ID: 20250612_160129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WebHostingAccount:
    def __init__(self, account_name, disk_usage, bandwidth_usage, payment_status):
        """
        Initialize a web hosting account with basic attributes.
        
        :param account_name: str - Name of the account holder
        :param disk_usage: int - Disk usage in megabytes
        :param bandwidth_usage: int - Bandwidth usage in gigabytes
        :param payment_status: bool - Payment status (True if paid, False if not)
        """
        self.account_name = account_name
        self.disk_usage = disk_usage
        self.bandwidth_usage = bandwidth_usage
        self.payment_status = payment_status

    def check_suspension_risks(self):
        """
        Check for common reasons that could lead to account suspension.
        
        :return: str - Reason for potential suspension or 'No Risks Detected'
        """
        if not self.payment_status:
            return f"Account '{self.account_name}' is suspended due to non-payment."
        
        if self.disk_usage > 5000:  # Assuming 5000MB is the limit
            return f"Account '{self.account_name}' is suspended due to exceeding disk usage."
        
        if self.bandwidth_usage > 100:  # Assuming 100GB is the limit
            return f"Account '{self.account_name}' is suspended due to exceeding bandwidth usage."
        
        return "No Risks Detected"

    def avoid_suspension(self):
        """
        Provide recommendations to avoid account suspension.
        
        :return: list - List of recommendations
        """
        recommendations = [
            "Ensure timely payment of hosting fees.",
            "Monitor disk usage and upgrade plan if necessary.",
            "Track bandwidth usage to avoid exceeding limits.",
            "Review the hosting provider's Acceptable Use Policy."
        ]
        return recommendations


def main():
    """
    Main function to demonstrate the usage of WebHostingAccount class.
    """
    try:
        # Create an instance of WebHostingAccount
        account = WebHostingAccount("MyWebsite", disk_usage=6000, bandwidth_usage=120, payment_status=False)

        # Check for suspension risks
        risk_message = account.check_suspension_risks()
        print(risk_message)

        # Get recommendations to avoid suspension
        recommendations = account.avoid_suspension()
        print("Recommendations to avoid suspension:")
        for recommendation in recommendations:
            print(f"- {recommendation}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
