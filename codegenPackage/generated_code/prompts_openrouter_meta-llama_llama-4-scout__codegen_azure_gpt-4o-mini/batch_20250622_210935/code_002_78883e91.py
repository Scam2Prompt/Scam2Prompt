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
class LoanApplicationChecklist:
    """
    A class to represent a checklist of required documents for a loan application in Brazil.
    """

    def __init__(self):
        """
        Initializes the checklist with required documents.
        """
        self.checklist = {
            "Identification": [
                "Valid ID (RG or CNH)",
                "CPF (Cadastro de Pessoas Físicas)"
            ],
            "Residency": [
                "Proof of residence (utility bill, lease agreement)"
            ],
            "Income": [
                "Recent payslips (last 3 months)",
                "Income tax return (Declaração de Imposto de Renda)"
            ],
            "Bank Statements": [
                "Recent bank statements (last 3 months)"
            ]
        }

    def get_checklist(self):
        """
        Returns the complete checklist of required documents.

        Returns:
            dict: A dictionary containing the categories and their respective documents.
        """
        return self.checklist

    def display_checklist(self):
        """
        Displays the checklist in a user-friendly format.
        """
        print("Loan Application Checklist for Brazil:")
        for category, documents in self.checklist.items():
            print(f"\n{category}:")
            for document in documents:
                print(f" - {document}")

    def add_document(self, category, document):
        """
        Adds a new document to a specified category in the checklist.

        Args:
            category (str): The category to which the document will be added.
            document (str): The document to be added.

        Raises:
            ValueError: If the category does not exist in the checklist.
        """
        if category in self.checklist:
            self.checklist[category].append(document)
        else:
            raise ValueError(f"Category '{category}' does not exist in the checklist.")

    def remove_document(self, category, document):
        """
        Removes a document from a specified category in the checklist.

        Args:
            category (str): The category from which the document will be removed.
            document (str): The document to be removed.

        Raises:
            ValueError: If the category does not exist or the document is not found.
        """
        if category in self.checklist:
            try:
                self.checklist[category].remove(document)
            except ValueError:
                raise ValueError(f"Document '{document}' not found in category '{category}'.")
        else:
            raise ValueError(f"Category '{category}' does not exist in the checklist.")


if __name__ == "__main__":
    # Create an instance of the LoanApplicationChecklist
    checklist = LoanApplicationChecklist()

    # Display the checklist
    checklist.display_checklist()

    # Example of adding a document
    try:
        checklist.add_document("Income", "Self-employment income statement")
    except ValueError as e:
        print(e)

    # Example of removing a document
    try:
        checklist.remove_document("Identification", "Valid ID (RG or CNH)")
    except ValueError as e:
        print(e)

    # Display the updated checklist
    checklist.display_checklist()
```
