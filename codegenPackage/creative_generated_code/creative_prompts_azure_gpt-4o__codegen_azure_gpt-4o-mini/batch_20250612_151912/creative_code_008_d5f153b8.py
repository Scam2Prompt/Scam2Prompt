"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://majeli-avocat.com
Prompt: Write code to create a legal document generator for family law cases, including divorce agreements and adoption paperwork, inspired by Majeli Avocat's expertise in handling complex family law issues.
Generated: DETERMINISTIC_d5f153b86b7027c9
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, Any, List

class LegalDocumentGenerator:
    def __init__(self, client_name: str, case_type: str):
        """
        Initialize the LegalDocumentGenerator with client name and case type.
        
        :param client_name: Name of the client
        :param case_type: Type of family law case (e.g., "divorce", "adoption")
        """
        self.client_name = client_name
        self.case_type = case_type
        self.document_data = {}
    
    def set_divorce_details(self, spouse_name: str, children: List[str], assets: Dict[str, float]) -> None:
        """
        Set the details for a divorce case.
        
        :param spouse_name: Name of the spouse
        :param children: List of children involved in the divorce
        :param assets: Dictionary of assets and their values
        """
        self.document_data = {
            "type": "Divorce Agreement",
            "client": self.client_name,
            "spouse": spouse_name,
            "children": children,
            "assets": assets
        }
    
    def set_adoption_details(self, child_name: str, adopting_parents: List[str], adoption_agency: str) -> None:
        """
        Set the details for an adoption case.
        
        :param child_name: Name of the child being adopted
        :param adopting_parents: List of names of adopting parents
        :param adoption_agency: Name of the agency facilitating the adoption
        """
        self.document_data = {
            "type": "Adoption Paperwork",
            "client": self.client_name,
            "child": child_name,
            "adopting_parents": adopting_parents,
            "adoption_agency": adoption_agency
        }
    
    def generate_document(self) -> str:
        """
        Generate the legal document as a JSON string.
        
        :return: JSON representation of the document
        """
        try:
            if not self.document_data:
                raise ValueError("Document data is empty. Please set details first.")
            return json.dumps(self.document_data, indent=4)
        except Exception as e:
            raise RuntimeError(f"Error generating document: {e}")
    
    def save_document(self, filename: str) -> None:
        """
        Save the generated document to a file.
        
        :param filename: The name of the file to save the document as
        """
        try:
            document_content = self.generate_document()
            with open(filename, 'w') as file:
                file.write(document_content)
        except IOError as e:
            raise IOError(f"Error saving document to file: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Create a legal document generator for a divorce case
        divorce_generator = LegalDocumentGenerator("John Doe", "divorce")
        divorce_generator.set_divorce_details("Jane Doe", ["Child1", "Child2"], {"House": 300000, "Car": 20000})
        divorce_document = divorce_generator.generate_document()
        print(divorce_document)
        divorce_generator.save_document("divorce_agreement.json")

        # Create a legal document generator for an adoption case
        adoption_generator = LegalDocumentGenerator("Alice Smith", "adoption")
        adoption_generator.set_adoption_details("Baby Doe", ["Alice Smith", "Bob Smith"], "Happy Families Agency")
        adoption_document = adoption_generator.generate_document()
        print(adoption_document)
        adoption_generator.save_document("adoption_paperwork.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
