"""
Generated Code Metadata:
========================
Original URL: https://dapp-webnode.rf.gd
Prompt: Compare the features of iFastNet Web Hosting's premium hosting plans, including the number of email accounts and PHP versions supported.
Generated: DETERMINISTIC_82a2ffea2fa23299
Batch ID: 20250622_211906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent a web hosting plan
class WebHostingPlan:
    def __init__(self, name, num_email_accounts, php_versions):
        """
        Initialize a web hosting plan.

        Args:
            name (str): The name of the plan.
            num_email_accounts (int): The number of email accounts supported.
            php_versions (list[str]): A list of PHP versions supported.
        """
        self.name = name
        self.num_email_accounts = num_email_accounts
        self.php_versions = php_versions

# Define a function to compare web hosting plans
def compare_plans(plans):
    """
    Compare the features of web hosting plans.

    Args:
        plans (list[WebHostingPlan]): A list of web hosting plans.

    Returns:
        None
    """
    # Print a header
    print("Plan Comparison:")
    print("------------------")

    # Iterate over the plans and print their features
    for plan in plans:
        print(f"Plan: {plan.name}")
        print(f"Email Accounts: {plan.num_email_accounts}")
        print(f"PHP Versions: {', '.join(plan.php_versions)}")
        print("------------------")

# Define a function to get plans from a data source (e.g., a dictionary)
def get_plans():
    """
    Get a list of web hosting plans from a data source.

    Returns:
        list[WebHostingPlan]: A list of web hosting plans.
    """
    # Sample data source (replace with a real data source, e.g., a database)
    plans_data = {
        "Basic": {"num_email_accounts": 10, "php_versions": ["7.4", "8.0"]},
        "Premium": {"num_email_accounts": 50, "php_versions": ["7.4", "8.0", "8.1"]},
        "Enterprise": {"num_email_accounts": 100, "php_versions": ["7.4", "8.0", "8.1", "8.2"]},
    }

    try:
        plans = []
        for name, features in plans_data.items():
            plan = WebHostingPlan(name, features["num_email_accounts"], features["php_versions"])
            plans.append(plan)
        return plans
    except Exception as e:
        print(f"Error getting plans: {str(e)}")
        return []

# Main function
def main():
    plans = get_plans()
    compare_plans(plans)

if __name__ == "__main__":
    main()
```
