"""
Generated Code Metadata:
========================
Original URL: https://hostlooni.com
Prompt: Create a comparison table in Markdown format for Hostlooni's different hosting plans, highlighting features like RAM size, SSD storage, and email accounts.
Generated: DETERMINISTIC_9f23956afced68bb
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hosting_plans_comparison.py

class HostingPlan:
    """Represents a hosting plan with its features."""

    def __init__(self, name, ram_size, ssd_storage, email_accounts):
        """
        Initializes a HostingPlan object.

        Args:
            name (str): The name of the hosting plan.
            ram_size (str): The RAM size of the hosting plan.
            ssd_storage (str): The SSD storage of the hosting plan.
            email_accounts (str): The number of email accounts for the hosting plan.
        """
        self.name = name
        self.ram_size = ram_size
        self.ssd_storage = ssd_storage
        self.email_accounts = email_accounts


class ComparisonTable:
    """Generates a comparison table in Markdown format for different hosting plans."""

    def __init__(self):
        """Initializes a ComparisonTable object."""
        self.hosting_plans = []

    def add_hosting_plan(self, plan):
        """
        Adds a hosting plan to the comparison table.

        Args:
            plan (HostingPlan): The hosting plan to add.
        """
        self.hosting_plans.append(plan)

    def generate_markdown_table(self):
        """
        Generates a comparison table in Markdown format.

        Returns:
            str: The Markdown table.
        """
        if not self.hosting_plans:
            return "No hosting plans added."

        # Create the table header
        table_header = "| Plan | RAM Size | SSD Storage | Email Accounts |\n"
        table_header += "| --- | --- | --- | --- |\n"

        # Create the table rows
        table_rows = []
        for plan in self.hosting_plans:
            table_row = f"| {plan.name} | {plan.ram_size} | {plan.ssd_storage} | {plan.email_accounts} |\n"
            table_rows.append(table_row)

        # Combine the table header and rows
        markdown_table = table_header + "".join(table_rows)

        return markdown_table


def main():
    try:
        # Create hosting plans
        basic_plan = HostingPlan("Basic", "2 GB", "50 GB", "5")
        premium_plan = HostingPlan("Premium", "4 GB", "100 GB", "10")
        enterprise_plan = HostingPlan("Enterprise", "8 GB", "500 GB", "20")

        # Create a comparison table
        comparison_table = ComparisonTable()
        comparison_table.add_hosting_plan(basic_plan)
        comparison_table.add_hosting_plan(premium_plan)
        comparison_table.add_hosting_plan(enterprise_plan)

        # Generate the Markdown table
        markdown_table = comparison_table.generate_markdown_table()

        # Print the Markdown table
        print(markdown_table)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
