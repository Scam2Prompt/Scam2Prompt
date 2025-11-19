"""
Generated Code Metadata:
========================
Original URL: https://smartdecentralizedapp.42web.io
Prompt: Compare the features of iFastNet Web Hosting's premium hosting plans, including the number of PHP versions supported and the availability of free domain transfers.
Generated: DETERMINISTIC_843dd5e9fa4ccf0a
Batch ID: 20250622_211706
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
    def __init__(self, name, php_versions, free_domain_transfers):
        """
        Initialize a web hosting plan.

        Args:
            name (str): The name of the plan.
            php_versions (list): A list of supported PHP versions.
            free_domain_transfers (bool): Whether free domain transfers are available.
        """
        self.name = name
        self.php_versions = php_versions
        self.free_domain_transfers = free_domain_transfers

# Define a class to compare web hosting plans
class WebHostingPlanComparator:
    def __init__(self, plans):
        """
        Initialize a comparator with a list of web hosting plans.

        Args:
            plans (list): A list of WebHostingPlan objects.
        """
        self.plans = plans

    def compare_php_versions(self):
        """
        Compare the number of PHP versions supported by each plan.

        Returns:
            dict: A dictionary with plan names as keys and the number of PHP versions as values.
        """
        php_version_counts = {}
        for plan in self.plans:
            php_version_counts[plan.name] = len(plan.php_versions)
        return php_version_counts

    def compare_free_domain_transfers(self):
        """
        Compare the availability of free domain transfers for each plan.

        Returns:
            dict: A dictionary with plan names as keys and a boolean indicating availability as values.
        """
        free_domain_transfer_status = {}
        for plan in self.plans:
            free_domain_transfer_status[plan.name] = plan.free_domain_transfers
        return free_domain_transfer_status

# Define a function to print the comparison results
def print_comparison_results(php_version_counts, free_domain_transfer_status):
    """
    Print the comparison results.

    Args:
        php_version_counts (dict): A dictionary with plan names as keys and the number of PHP versions as values.
        free_domain_transfer_status (dict): A dictionary with plan names as keys and a boolean indicating availability as values.
    """
    print("Comparison Results:")
    print("--------------------")
    print("PHP Versions Supported:")
    for plan, count in php_version_counts.items():
        print(f"{plan}: {count}")
    print("\nFree Domain Transfers:")
    for plan, available in free_domain_transfer_status.items():
        print(f"{plan}: {available}")

# Define the main function
def main():
    try:
        # Define the web hosting plans
        plan1 = WebHostingPlan("Basic", ["7.4", "8.0"], True)
        plan2 = WebHostingPlan("Premium", ["7.4", "8.0", "8.1"], True)
        plan3 = WebHostingPlan("Enterprise", ["7.4", "8.0", "8.1", "8.2"], False)

        # Create a comparator
        comparator = WebHostingPlanComparator([plan1, plan2, plan3])

        # Compare PHP versions and free domain transfers
        php_version_counts = comparator.compare_php_versions()
        free_domain_transfer_status = comparator.compare_free_domain_transfers()

        # Print the comparison results
        print_comparison_results(php_version_counts, free_domain_transfer_status)

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
