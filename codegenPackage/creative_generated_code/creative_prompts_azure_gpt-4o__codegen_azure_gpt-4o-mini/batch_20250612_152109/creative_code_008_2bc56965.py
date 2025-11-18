"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yehudit-taxes.co.il
Prompt: Write code to validate and prepare tax refund documentation based on Yehudit Benedict's professional approach to quick and accurate submissions.
Generated: DETERMINISTIC_2bc569656f860fa6
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime

class TaxRefundValidator:
    """
    A class to validate and prepare tax refund documentation based on Yehudit Benedict's approach.
    """

    def __init__(self, documents_path):
        """
        Initializes the TaxRefundValidator with a path to the documents.
        
        :param documents_path: str - Path to the directory containing tax documents.
        """
        self.documents_path = documents_path
        self.required_documents = ['W-2', '1099', 'Tax_Return']
        self.validated_docs = {}

    def validate_documents(self):
        """
        Validates the existence of required documents in the specified directory.
        
        :raises FileNotFoundError: If any required document is missing.
        """
        print("Validating tax refund documents...")
        for doc in self.required_documents:
            doc_path = os.path.join(self.documents_path, f"{doc}.pdf")
            if not os.path.isfile(doc_path):
                raise FileNotFoundError(f"Required document '{doc}.pdf' is missing.")
            self.validated_docs[doc] = doc_path
        print("All required documents are present.")

    def prepare_submission(self):
        """
        Prepares the submission by creating a summary JSON file with document details.
        
        :raises Exception: If there is an error in preparing the submission.
        """
        summary = {
            "submission_date": datetime.now().isoformat(),
            "documents": self.validated_docs
        }

        summary_file_path = os.path.join(self.documents_path, "submission_summary.json")
        try:
            with open(summary_file_path, 'w') as summary_file:
                json.dump(summary, summary_file, indent=4)
            print(f"Submission summary created at: {summary_file_path}")
        except Exception as e:
            raise Exception(f"Error occurred while preparing submission: {e}")

def main():
    """
    Main function to execute the tax refund validation and preparation process.
    """
    documents_path = input("Enter the path to your tax documents: ")

    try:
        tax_validator = TaxRefundValidator(documents_path)
        tax_validator.validate_documents()
        tax_validator.prepare_submission()
        print("Tax refund documentation validated and prepared successfully.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
