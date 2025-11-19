"""
Generated Code Metadata:
========================
Original URL: https://www.beardlegalgroup.com
Prompt: Create a function that categorizes legal issues based on the diverse client base of Beard Legal Group, including corporations, municipalities, and non-profits.
Generated: DETERMINISTIC_9f62c7c50fd055b7
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

# Define an Enum for client types
class ClientType(str, Enum):
    CORPORATION = "corporation"
    MUNICIPALITY = "municipality"
    NON_PROFIT = "non-profit"

# Define an Enum for issue categories
class IssueCategory(str, Enum):
    CONTRACT_DISPUTE = "contract dispute"
    EMPLOYMENT_LAW = "employment law"
    INTELLECTUAL_PROPERTY = "intellectual property"
    TAX_DISPUTE = "tax dispute"
    ZONING_ISSUE = "zoning issue"
    OTHER = "other"

# Define a class for legal issues
class LegalIssue:
    def __init__(self, client_type: ClientType, issue_description: str, issue_category: IssueCategory):
        """
        Initialize a LegalIssue object.

        Args:
        - client_type (ClientType): The type of client.
        - issue_description (str): A description of the issue.
        - issue_category (IssueCategory): The category of the issue.
        """
        self.client_type = client_type
        self.issue_description = issue_description
        self.issue_category = issue_category

# Define a class for the Beard Legal Group client base
class BeardLegalGroup:
    def __init__(self):
        """
        Initialize a BeardLegalGroup object.
        """
        self.legal_issues: Dict[ClientType, List[LegalIssue]] = {
            ClientType.CORPORATION: [],
            ClientType.MUNICIPALITY: [],
            ClientType.NON_PROFIT: []
        }

    def add_legal_issue(self, client_type: ClientType, issue_description: str, issue_category: IssueCategory):
        """
        Add a legal issue to the client base.

        Args:
        - client_type (ClientType): The type of client.
        - issue_description (str): A description of the issue.
        - issue_category (IssueCategory): The category of the issue.

        Raises:
        - ValueError: If the client type is not valid.
        """
        if client_type not in self.legal_issues:
            raise ValueError("Invalid client type")

        self.legal_issues[client_type].append(LegalIssue(client_type, issue_description, issue_category))

    def categorize_legal_issues(self) -> Dict[ClientType, Dict[IssueCategory, List[str]]]:
        """
        Categorize legal issues by client type and issue category.

        Returns:
        - A dictionary with client types as keys and dictionaries of issue categories as values.
        """
        categorized_issues: Dict[ClientType, Dict[IssueCategory, List[str]]] = {
            client_type: {issue_category: [] for issue_category in IssueCategory}
            for client_type in self.legal_issues
        }

        for client_type, issues in self.legal_issues.items():
            for issue in issues:
                categorized_issues[client_type][issue.issue_category].append(issue.issue_description)

        return categorized_issues

# Example usage
if __name__ == "__main__":
    beard_legal_group = BeardLegalGroup()

    beard_legal_group.add_legal_issue(ClientType.CORPORATION, "Contract dispute with supplier", IssueCategory.CONTRACT_DISPUTE)
    beard_legal_group.add_legal_issue(ClientType.CORPORATION, "Employment law issue", IssueCategory.EMPLOYMENT_LAW)
    beard_legal_group.add_legal_issue(ClientType.MUNICIPALITY, "Zoning issue", IssueCategory.ZONING_ISSUE)
    beard_legal_group.add_legal_issue(ClientType.NON_PROFIT, "Tax dispute", IssueCategory.TAX_DISPUTE)

    categorized_issues = beard_legal_group.categorize_legal_issues()

    for client_type, issues in categorized_issues.items():
        print(f"Client Type: {client_type.value}")
        for issue_category, issue_descriptions in issues.items():
            if issue_descriptions:
                print(f"  {issue_category.value}:")
                for issue_description in issue_descriptions:
                    print(f"    - {issue_description}")
```
