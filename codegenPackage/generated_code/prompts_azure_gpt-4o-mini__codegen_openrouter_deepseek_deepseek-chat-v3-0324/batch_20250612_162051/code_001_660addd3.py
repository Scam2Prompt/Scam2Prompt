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
# rental_property_management.py

class QuietEnjoymentClause:
    """
    A class to represent and enforce the quiet enjoyment clause in a rental property management system.
    This clause ensures tenants have the right to undisturbed use of their rented property.
    """

    def __init__(self, tenant_name: str, property_address: str, lease_start_date: str, lease_end_date: str):
        """
        Initialize the QuietEnjoymentClause with tenant and property details.

        Args:
            tenant_name (str): Name of the tenant
            property_address (str): Address of the rental property
            lease_start_date (str): Start date of the lease (YYYY-MM-DD)
            lease_end_date (str): End date of the lease (YYYY-MM-DD)
        """
        self.tenant_name = tenant_name
        self.property_address = property_address
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date
        self.violations = []

    def add_violation(self, violation_type: str, description: str, date_occurred: str):
        """
        Record a violation of the quiet enjoyment clause.

        Args:
            violation_type (str): Type of violation (e.g., 'noise', 'entry without notice')
            description (str): Detailed description of the violation
            date_occurred (str): Date when violation occurred (YYYY-MM-DD)
        """
        if not all([violation_type, description, date_occurred]):
            raise ValueError("All violation fields must be provided")
            
        violation = {
            'type': violation_type,
            'description': description,
            'date': date_occurred,
            'resolved': False
        }
        self.violations.append(violation)

    def resolve_violation(self, violation_index: int, resolution_details: str):
        """
        Mark a violation as resolved with details about the resolution.

        Args:
            violation_index (int): Index of the violation in the violations list
            resolution_details (str): Description of how the violation was resolved
        """
        if violation_index < 0 or violation_index >= len(self.violations):
            raise IndexError("Invalid violation index")
            
        self.violations[violation_index]['resolved'] = True
        self.violations[violation_index]['resolution'] = resolution_details

    def get_active_violations(self) -> list:
        """
        Get all unresolved violations.

        Returns:
            list: List of unresolved violations
        """
        return [v for v in self.violations if not v['resolved']]

    def generate_clause_document(self) -> str:
        """
        Generate a document outlining the quiet enjoyment clause and any violations.

        Returns:
            str: Formatted document as a string
        """
        doc = f"""
        QUIET ENJOYMENT CLAUSE DOCUMENT
        -------------------------------
        Tenant: {self.tenant_name}
        Property: {self.property_address}
        Lease Period: {self.lease_start_date} to {self.lease_end_date}

        The tenant has the right to quiet enjoyment of the premises, free from 
        unreasonable disturbances by the landlord or other tenants.

        VIOLATION HISTORY:
        """
        
        if not self.violations:
            doc += "\nNo violations recorded."
        else:
            for i, violation in enumerate(self.violations, 1):
                status = "RESOLVED" if violation['resolved'] else "ACTIVE"
                doc += f"\n\n{i}. {violation['type']} - {violation['date']} ({status})"
                doc += f"\nDescription: {violation['description']}"
                if violation['resolved']:
                    doc += f"\nResolution: {violation.get('resolution', 'No details provided')}"
        
        return doc

    def enforce_clause(self) -> bool:
        """
        Check if the clause needs enforcement action based on violations.

        Returns:
            bool: True if enforcement action is needed (multiple unresolved violations)
        """
        active_violations = self.get_active_violations()
        return len(active_violations) >= 3  # Threshold for enforcement action


# Example usage
if __name__ == "__main__":
    try:
        # Create a quiet enjoyment clause for a tenant
        clause = QuietEnjoymentClause(
            tenant_name="John Doe",
            property_address="123 Main St, Apt 4B, Anytown, USA",
            lease_start_date="2023-01-01",
            lease_end_date="2023-12-31"
        )

        # Add some violations
        clause.add_violation(
            violation_type="Noise disturbance",
            description="Loud construction noise from adjacent unit during quiet hours",
            date_occurred="2023-03-15"
        )

        clause.add_violation(
            violation_type="Unauthorized entry",
            description="Landlord entered property without 24-hour notice",
            date_occurred="2023-04-02"
        )

        # Resolve a violation
        clause.resolve_violation(
            violation_index=0,
            resolution_details="Landlord agreed to limit construction to business hours"
        )

        # Check if enforcement is needed
        if clause.enforce_clause():
            print("WARNING: Multiple unresolved violations - enforcement action needed")
        else:
            print("Clause status: Acceptable")

        # Generate and print the clause document
        print(clause.generate_clause_document())

    except Exception as e:
        print(f"Error in quiet enjoyment clause management: {str(e)}")
```
