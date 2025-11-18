"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sardagnapoeta.com.br
Prompt: Write Python code to generate a formatted legal document template for a Habeas Corpus request, including fields for case details, petitioner information, and legal arguments.
Generated: DETERMINISTIC_b078e065d0f4aafe
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

class HabeasCorpusTemplate:
    def __init__(self, case_number, petitioner_name, respondent_name, court_name, legal_arguments):
        """
        Initialize the HabeasCorpusTemplate with case details and petitioner's information.

        :param case_number: str - The case number for the legal request.
        :param petitioner_name: str - The name of the petitioner.
        :param respondent_name: str - The name of the respondent.
        :param court_name: str - The name of the court where the request is filed.
        :param legal_arguments: list - List of legal arguments supporting the habeas corpus request.
        """
        self.case_number = case_number
        self.petitioner_name = petitioner_name
        self.respondent_name = respondent_name
        self.court_name = court_name
        self.legal_arguments = legal_arguments

    def generate_document(self):
        """
        Generate a formatted legal document as a string.

        :return: str - The formatted legal document template for Habeas Corpus request.
        """
        document = f"Habeas Corpus Petition\n\n"
        document += f"Case Number: {self.case_number}\n"
        document += f"Petitioner: {self.petitioner_name}\n"
        document += f"Respondent: {self.respondent_name}\n"
        document += f"Court: {self.court_name}\n"
        document += f"Date: {datetime.now().strftime('%B %d, %Y')}\n\n"
        document += "Legal Arguments:\n"
        
        for i, argument in enumerate(self.legal_arguments, start=1):
            document += f"{i}. {argument}\n"

        return document

    def save_to_file(self, file_path):
        """
        Save the generated document to a text file.

        :param file_path: str - The file path where the document will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                file.write(self.generate_document())
            print(f"Document saved successfully to {file_path}")
        except IOError as e:
            print(f"Error saving document: {e}")

# Example usage
if __name__ == "__main__":
    case_number = "123456"
    petitioner_name = "John Doe"
    respondent_name = "State of Example"
    court_name = "Example District Court"
    legal_arguments = [
        "The petitioner has been unlawfully detained without due process.",
        "There is insufficient evidence to support the charges against the petitioner.",
        "The detainment violates constitutional rights under the 14th Amendment."
    ]

    # Create a Habeas Corpus request template
    habeas_corpus_request = HabeasCorpusTemplate(case_number, petitioner_name, respondent_name, court_name, legal_arguments)

    # Generate the document and save to file
    output_file_path = os.path.join(os.getcwd(), "habeas_corpus_request.txt")
    habeas_corpus_request.save_to_file(output_file_path)
```
