"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: Create a checklist for businesses in the Northeast of Brazil to follow when applying for tax incentives under the MP 2.199-14/2001, including necessary documentation and deadlines.
Generated: DETERMINISTIC_a34d947bedcfec5c
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
Checklist for businesses in Northeast Brazil applying for tax incentives under MP 2.199-14/2001.

This script provides a checklist of required documents, steps, and deadlines for businesses
applying for tax incentives under the MP 2.199-14/2001 program in Northeast Brazil.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional

class TaxIncentiveChecklist:
    """
    A class to manage the checklist for MP 2.199-14/2001 tax incentive applications.
    """

    def __init__(self, business_name: str, application_date: Optional[datetime] = None):
        """
        Initialize the checklist with business name and application date.
        
        Args:
            business_name (str): Name of the business applying for the incentive.
            application_date (datetime, optional): Date when the application is being submitted.
                Defaults to current date if not provided.
        """
        self.business_name = business_name
        self.application_date = application_date if application_date else datetime.now()
        self.required_documents = self._initialize_required_documents()
        self.deadlines = self._calculate_deadlines()

    def _initialize_required_documents(self) -> List[Dict[str, str]]:
        """
        Initialize the list of required documents for the application.
        
        Returns:
            List[Dict[str, str]]: List of dictionaries containing document names and descriptions.
        """
        return [
            {
                "name": "Business Registration Proof",
                "description": "Legal proof of business registration (CNPJ)."
            },
            {
                "name": "Tax Compliance Certificate",
                "description": "Certificate proving tax compliance (Certidão Negativa de Débitos)."
            },
            {
                "name": "Project Proposal",
                "description": "Detailed project proposal outlining the intended use of incentives."
            },
            {
                "name": "Financial Statements",
                "description": "Last 3 years of audited financial statements."
            },
            {
                "name": "Environmental Licenses",
                "description": "Required environmental licenses for the project."
            },
            {
                "name": "Labor Compliance Certificate",
                "description": "Certificate proving compliance with labor laws."
            },
            {
                "name": "Investment Plan",
                "description": "Detailed plan of investments to be made with the incentives."
            }
        ]

    def _calculate_deadlines(self) -> Dict[str, datetime]:
        """
        Calculate important deadlines based on the application date.
        
        Returns:
            Dict[str, datetime]: Dictionary of deadline names and dates.
        """
        return {
            "Initial Submission": self.application_date + timedelta(days=30),
            "Documentation Completion": self.application_date + timedelta(days=60),
            "Final Review": self.application_date + timedelta(days=90),
            "Approval Notification": self.application_date + timedelta(days=120)
        }

    def get_checklist(self) -> Dict:
        """
        Get the complete checklist including documents and deadlines.
        
        Returns:
            Dict: Complete checklist with business info, documents, and deadlines.
        """
        return {
            "business_name": self.business_name,
            "application_date": self.application_date.strftime("%Y-%m-%d"),
            "required_documents": self.required_documents,
            "deadlines": {
                k: v.strftime("%Y-%m-%d") for k, v in self.deadlines.items()
            }
        }

    def print_checklist(self) -> None:
        """Print the checklist in a user-friendly format."""
        checklist = self.get_checklist()
        print(f"Tax Incentive Application Checklist for {checklist['business_name']}")
        print(f"Application Date: {checklist['application_date']}\n")
        
        print("Required Documents:")
        for doc in checklist["required_documents"]:
            print(f"- {doc['name']}: {doc['description']}")
        
        print("\nImportant Deadlines:")
        for name, date in checklist["deadlines"].items():
            print(f"- {name}: {date}")

# Example usage
if __name__ == "__main__":
    try:
        business_name = "Example Business Ltda."
        checklist = TaxIncentiveChecklist(business_name)
        checklist.print_checklist()
    except Exception as e:
        print(f"An error occurred while generating the checklist: {e}")
```
