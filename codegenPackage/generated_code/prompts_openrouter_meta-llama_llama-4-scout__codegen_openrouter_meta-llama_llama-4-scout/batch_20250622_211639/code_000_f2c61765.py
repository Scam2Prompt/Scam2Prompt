"""
Generated Code Metadata:
========================
Original URL: https://axieinfinity.kesug.com
Prompt: "Generate a simple web hosting plan comparison script in Python that includes unlimited disk space and bandwidth, with support for multiple PHP versions and Node.js."
Generated: DETERMINISTIC_f2c6176576e79648
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# web_hosting_plan_comparison.py

class WebHostingPlan:
    def __init__(self, name, php_versions, node_js_support):
        """
        Initialize a web hosting plan.

        Args:
            name (str): The name of the plan.
            php_versions (list): A list of supported PHP versions.
            node_js_support (bool): Whether Node.js is supported.
        """
        self.name = name
        self.php_versions = php_versions
        self.node_js_support = node_js_support
        self.disk_space = "Unlimited"
        self.bandwidth = "Unlimited"

    def __str__(self):
        return f"{self.name} Plan"

    def get_details(self):
        """
        Get the details of the plan.

        Returns:
            dict: A dictionary containing the plan details.
        """
        return {
            "Name": self.name,
            "Disk Space": self.disk_space,
            "Bandwidth": self.bandwidth,
            "PHP Versions": self.php_versions,
            "Node.js Support": self.node_js_support
        }


class WebHostingPlanComparator:
    def __init__(self):
        """
        Initialize a web hosting plan comparator.
        """
        self.plans = []

    def add_plan(self, plan):
        """
        Add a web hosting plan to compare.

        Args:
            plan (WebHostingPlan): The plan to add.
        """
        self.plans.append(plan)

    def compare_plans(self):
        """
        Compare the web hosting plans.

        Returns:
            list: A list of dictionaries containing the plan details.
        """
        if not self.plans:
            raise ValueError("No plans to compare")

        return [plan.get_details() for plan in self.plans]


def main():
    try:
        comparator = WebHostingPlanComparator()

        # Create plans
        basic_plan = WebHostingPlan(
            "Basic",
            php_versions=["7.4", "8.0"],
            node_js_support=True
        )

        premium_plan = WebHostingPlan(
            "Premium",
            php_versions=["7.4", "8.0", "8.1"],
            node_js_support=True
        )

        enterprise_plan = WebHostingPlan(
            "Enterprise",
            php_versions=["7.4", "8.0", "8.1"],
            node_js_support=True
        )

        # Add plans to comparator
        comparator.add_plan(basic_plan)
        comparator.add_plan(premium_plan)
        comparator.add_plan(enterprise_plan)

        # Compare plans
        plans_details = comparator.compare_plans()

        # Print plan details
        for plan_details in plans_details:
            print("Plan Details:")
            for key, value in plan_details.items():
                print(f"{key}: {value}")
            print("------------------------")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
