"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Recommend a checklist of documents to prepare for a guardianship hearing in Utah, including the Petition to Appoint a Guardian for an Adult, Schedule A, and Report on Clinical Evaluation.
Generated: DETERMINISTIC_4a0372c2620e2914
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GuardianshipHearingChecklist:
    """
    A class to represent a checklist of documents required for a guardianship hearing in Utah.
    """

    def __init__(self):
        """
        Initializes the checklist with the required documents.
        """
        self.documents = [
            "1. Petition to Appoint a Guardian for an Adult",
            "2. Schedule A",
            "3. Report on Clinical Evaluation",
            "4. Notice of Hearing",
            "5. Proof of Service",
            "6. Financial Disclosure Statement",
            "7. Medical Records",
            "8. Affidavit of the Proposed Guardian",
            "9. Background Check Results",
            "10. Any Additional Supporting Documents"
        ]

    def display_checklist(self):
        """
        Displays the checklist of documents.
        """
        print("Guardianship Hearing Document Checklist in Utah:")
        for document in self.documents:
            print(document)

    def add_document(self, document):
        """
        Adds a new document to the checklist.

        Args:
            document (str): The document to be added to the checklist.
        """
        if document and isinstance(document, str):
            self.documents.append(document)
            print(f"Document '{document}' added to the checklist.")
        else:
            print("Error: Document must be a non-empty string.")

    def remove_document(self, document):
        """
        Removes a document from the checklist.

        Args:
            document (str): The document to be removed from the checklist.
        """
        try:
            self.documents.remove(document)
            print(f"Document '{document}' removed from the checklist.")
        except ValueError:
            print(f"Error: Document '{document}' not found in the checklist.")

if __name__ == "__main__":
    # Create an instance of the checklist
    checklist = GuardianshipHearingChecklist()
    
    # Display the initial checklist
    checklist.display_checklist()
    
    # Example of adding a document
    checklist.add_document("11. Consent of the Proposed Guardian")
    
    # Example of removing a document
    checklist.remove_document("2. Schedule A")
    
    # Display the updated checklist
    checklist.display_checklist()
```
