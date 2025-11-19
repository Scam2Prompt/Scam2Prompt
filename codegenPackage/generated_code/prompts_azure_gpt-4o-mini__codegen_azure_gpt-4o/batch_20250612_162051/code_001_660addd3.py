"""
Generated Code Metadata:
========================
Original URL: https://globaljournalpress.com
Prompt: Generate a code snippet that demonstrates how to implement a "quiet enjoyment clause" in a rental property management system using Python.
Generated: DETERMINISTIC_660addd3d053681b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rental Property Management System - Quiet Enjoyment Clause Implementation

This code snippet demonstrates how to implement a "quiet enjoyment clause" in a rental property management system.
The clause ensures tenants have the right to peaceful and undisturbed use of their rental property.
"""

class QuietEnjoymentClause:
    """
    Represents the Quiet Enjoyment Clause in a rental agreement.
    Ensures tenants have the right to peaceful and undisturbed use of their rental property.
    """

    def __init__(self, tenant_name, property_address):
        """
        Initializes the Quiet Enjoyment Clause with tenant and property details.

        :param tenant_name: Name of the tenant
        :param property_address: Address of the rental property
        """
        self.tenant_name = tenant_name
        self.property_address = property_address
        self.violations = []  # List to track violations of the clause

    def report_violation(self, description):
        """
        Allows tenants to report a violation of the quiet enjoyment clause.

        :param description: Description of the violation
        """
        if not description:
            raise ValueError("Violation description cannot be empty.")
        self.violations.append(description)
        print(f"Violation reported: {description}")

    def resolve_violation(self, violation_index):
        """
        Resolves a reported violation.

        :param violation_index: Index of the violation to resolve
        """
        try:
            resolved_violation = self.violations.pop(violation_index)
            print(f"Violation resolved: {resolved_violation}")
        except IndexError:
            print("Invalid violation index. No violation resolved.")

    def list_violations(self):
        """
        Lists all reported violations of the quiet enjoyment clause.
        """
        if not self.violations:
            print("No violations reported.")
        else:
            print("Reported Violations:")
            for idx, violation in enumerate(self.violations, start=1):
                print(f"{idx}. {violation}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a Quiet Enjoyment Clause for a tenant
        clause = QuietEnjoymentClause(tenant_name="John Doe", property_address="123 Elm Street")

        # Report violations
        clause.report_violation("Loud construction noise during late hours.")
        clause.report_violation("Neighbor playing loud music at midnight.")

        # List all reported violations
        clause.list_violations()

        # Resolve a violation
        clause.resolve_violation(0)

        # List violations after resolving one
        clause.list_violations()

    except Exception as e:
        print(f"An error occurred: {e}")
```
