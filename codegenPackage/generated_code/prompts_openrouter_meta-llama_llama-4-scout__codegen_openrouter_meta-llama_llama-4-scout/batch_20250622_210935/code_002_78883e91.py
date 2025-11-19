"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Generate a checklist of required documents for a loan application in Brazil, including identification, residency, income, and bank statements, as described in this webpage.
Generated: DETERMINISTIC_78883e91889c0a29
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_document_checklist.py

class LoanDocumentChecklist:
    """
    Generates a checklist of required documents for a loan application in Brazil.
    """

    def __init__(self):
        self.checklist = []

    def add_document(self, category, document):
        """
        Adds a document to the checklist.

        Args:
            category (str): Category of the document (e.g., identification, residency, etc.)
            document (str): Name of the document
        """
        self.checklist.append({"category": category, "document": document})

    def get_checklist(self):
        """
        Returns the checklist of required documents.

        Returns:
            list: List of dictionaries containing category and document information
        """
        return self.checklist


def generate_brazilian_loan_checklist():
    """
    Generates a checklist of required documents for a loan application in Brazil.

    Returns:
        LoanDocumentChecklist: Checklist of required documents
    """
    checklist = LoanDocumentChecklist()

    # Identification documents
    checklist.add_document("Identification", "Valid government-issued ID (e.g., RG, CPF)")
    checklist.add_document("Identification", "Passport")

    # Residency documents
    checklist.add_document("Residency", "Utility bill with address (e.g., electricity, water, or gas)")
    checklist.add_document("Residency", "Rental agreement or property deed")

    # Income documents
    checklist.add_document("Income", "Pay stub or proof of income")
    checklist.add_document("Income", "Tax return or income tax proof")
    checklist.add_document("Income", "Employment contract or letter from employer")

    # Bank statements
    checklist.add_document("Bank Statements", "Last 3 bank statements")
    checklist.add_document("Bank Statements", "Proof of income and expenses")

    return checklist


def print_checklist(checklist):
    """
    Prints the checklist of required documents.

    Args:
        checklist (LoanDocumentChecklist): Checklist of required documents
    """
    print("# Loan Document Checklist")
    for i, item in enumerate(checklist.get_checklist(), start=1):
        print(f"{i}. **{item['category']}:** {item['document']}")


def main():
    try:
        checklist = generate_brazilian_loan_checklist()
        print_checklist(checklist)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
