"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Create a script to analyze business compliance requirements and generate a checklist for new business registrations, inspired by TSM Wealth's business administration services.
Generated: DETERMINISTIC_34309430598207f3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# business_compliance_checklist.py

import enum

class BusinessEntityType(enum.Enum):
    """Business entity types"""
    CORPORATION = "Corporation"
    PARTNERSHIP = "Partnership"
    LIMITED_LIABILITY_COMPANY = "Limited Liability Company"
    SOLE_PROPRIETORSHIP = "Sole Proprietorship"

class ComplianceRequirement:
    """Represents a compliance requirement"""
    def __init__(self, name, description, required_for):
        self.name = name
        self.description = description
        self.required_for = required_for

    def __str__(self):
        return f"{self.name}: {self.description}"

class BusinessComplianceChecklist:
    """Generates a business compliance checklist"""
    def __init__(self):
        self.compliance_requirements = [
            ComplianceRequirement(
                "Business License",
                "Obtain a business license from the state and local government",
                [BusinessEntityType.CORPORATION, BusinessEntityType.PARTNERSHIP, BusinessEntityType.LIMITED_LIABILITY_COMPANY, BusinessEntityType.SOLE_PROPRIETORSHIP]
            ),
            ComplianceRequirement(
                "EIN Registration",
                "Obtain an Employer Identification Number (EIN) from the IRS",
                [BusinessEntityType.CORPORATION, BusinessEntityType.PARTNERSHIP, BusinessEntityType.LIMITED_LIABILITY_COMPANY]
            ),
            ComplianceRequirement(
                "Annual Report Filing",
                "File an annual report with the state government",
                [BusinessEntityType.CORPORATION, BusinessEntityType.PARTNERSHIP, BusinessEntityType.LIMITED_LIABILITY_COMPANY]
            ),
            ComplianceRequirement(
                "Tax Registration",
                "Register for state and local taxes",
                [BusinessEntityType.CORPORATION, BusinessEntityType.PARTNERSHIP, BusinessEntityType.LIMITED_LIABILITY_COMPANY, BusinessEntityType.SOLE_PROPRIETORSHIP]
            ),
            ComplianceRequirement(
                "Workers' Compensation Insurance",
                "Obtain workers' compensation insurance",
                [BusinessEntityType.CORPORATION, BusinessEntityType.PARTNERSHIP, BusinessEntityType.LIMITED_LIABILITY_COMPANY]
            ),
        ]

    def generate_checklist(self, entity_type):
        """Generate a compliance checklist for a given business entity type"""
        checklist = []
        for requirement in self.compliance_requirements:
            if entity_type in requirement.required_for:
                checklist.append(requirement)
        return checklist

def main():
    try:
        entity_type = input("Enter the business entity type (CORPORATION, PARTNERSHIP, LIMITED_LIABILITY_COMPANY, SOLE_PROPRIETORSHIP): ")
        entity_type = BusinessEntityType(entity_type.upper())
        checklist = BusinessComplianceChecklist().generate_checklist(entity_type)
        print(f"Compliance Checklist for {entity_type.value}:")
        for i, requirement in enumerate(checklist, start=1):
            print(f"{i}. {requirement}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
