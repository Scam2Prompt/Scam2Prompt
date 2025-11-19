"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a code snippet to automate the application process for temporary registration in Adygea, including document verification steps.
Generated: DETERMINISTIC_a7372c9684054151
Batch ID: 20250612_161353
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
import re
from datetime import datetime

class TemporaryRegistrationApplication:
    def __init__(self):
        self.required_documents = ["passport", "lease_agreement", "employment_letter"]
        self.applications_log = "applications_log.json"
        self.valid_formats = {
            "passport": r"^\d{4}-\d{6}$",  # Example passport regex: 4 digits-6 digits
            "lease_agreement": r"^Lease-\d{8}$",  # Example lease agreement regex
            "employment_letter": r"^Letter-\d{6}$",  # Example employment letter regex
        }

    def verify_document(self, doc_type, doc_value):
        """
        Verify if the provided document matches the expected format.
        :param doc_type: Type of document (e.g., 'passport').
        :param doc_value: Value of the document (e.g., '1234-567890').
        :return: Boolean indicating validity of the document.
        """
        if doc_type not in self.valid_formats:
            return False
        return bool(re.match(self.valid_formats[doc_type], doc_value))

    def submit_application(self, applicant_name, documents):
        """
        Automates the application submission process.
        :param applicant_name: Name of the applicant.
        :param documents: Dictionary containing document types and their values.
        :return: Application status message.
        """
        # Verify all required documents are submitted
        missing_docs = [doc for doc in self.required_documents if doc not in documents]
        if missing_docs:
            return f"Missing required documents: {', '.join(missing_docs)}"

        # Validate document formats
        for doc_type, doc_value in documents.items():
            if not self.verify_document(doc_type, doc_value):
                return f"Invalid format for document: {doc_type}"

        # Save the application details to a log file
        application_entry = {
            "applicant_name": applicant_name,
            "documents": documents,
            "submission_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            if not os.path.exists(self.applications_log):
                with open(self.applications_log, "w") as file:
                    json.dump([], file)  # Initialize empty list in log file

            with open(self.applications_log, "r") as file:
                applications = json.load(file)
            
            applications.append(application_entry)

            with open(self.applications_log, "w") as file:
                json.dump(applications, file, indent=4)
        except Exception as e:
            return f"Error saving application: {str(e)}"

        return "Application submitted successfully."

if __name__ == "__main__":
    application_system = TemporaryRegistrationApplication()
    applicant_name = "John Doe"
    documents = {
        "passport": "1234-567890",
        "lease_agreement": "Lease-20231010",
        "employment_letter": "Letter-987654"
    }

    print(application_system.submit_application(applicant_name, documents))
```
