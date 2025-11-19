"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azarlegal.com
Prompt: Generate a code snippet for a legal document management system that can handle corporate law cases, inspired by the services offered by AZAR & Associates.
Generated: DETERMINISTIC_41d864934d517490
Batch ID: 20250612_162945
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

# Define constants for file storage paths
DOCUMENT_STORAGE_PATH = "./legal_documents"
CASE_STORAGE_PATH = "./cases"

# Ensure necessary directories exist
os.makedirs(DOCUMENT_STORAGE_PATH, exist_ok=True)
os.makedirs(CASE_STORAGE_PATH, exist_ok=True)

class LegalDocumentManagementSystem:
    """
    A Legal Document Management System designed to handle corporate law cases.
    Inspired by services offered by AZAR & Associates.
    """

    def __init__(self):
        self.cases = {}  # In-memory storage for cases (can be replaced with a database)

    def create_case(self, case_id, title, description, client_name):
        """
        Creates a new case and stores it.

        Args:
            case_id (str): Unique identifier for the case.
            title (str): Title of the case.
            description (str): Brief description of the case.
            client_name (str): Name of the client associated with the case.

        Returns:
            dict: Details of the newly created case.
        """
        if case_id in self.cases:
            raise ValueError(f"A case with ID '{case_id}' already exists.")

        new_case = {
            "case_id": case_id,
            "title": title,
            "description": description,
            "client_name": client_name,
            "documents": [],  # List of documents associated with the case
            "created_at": datetime.now().isoformat(),
        }
        self.cases[case_id] = new_case

        # Persist case data to storage
        self._save_case_to_file(case_id, new_case)

        return new_case

    def upload_document(self, case_id, document_name, document_content):
        """
        Uploads a document and associates it with a case.

        Args:
            case_id (str): ID of the case to associate the document with.
            document_name (str): Name of the document.
            document_content (str): Content of the document.

        Returns:
            dict: Details of the uploaded document.
        """
        if case_id not in self.cases:
            raise ValueError(f"No case found with ID '{case_id}'.")

        # Generate a unique filename for the document
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{case_id}_{timestamp}_{document_name.replace(' ', '_')}"

        # Save document to storage
        document_path = os.path.join(DOCUMENT_STORAGE_PATH, filename)
        with open(document_path, "w") as f:
            f.write(document_content)

        # Create document metadata
        document_metadata = {
            "document_name": document_name,
            "filename": filename,
            "uploaded_at": datetime.now().isoformat(),
        }

        # Associate document with the case
        self.cases[case_id]["documents"].append(document_metadata)

        # Update case file
        self._save_case_to_file(case_id, self.cases[case_id])

        return document_metadata

    def list_cases(self):
        """
        Lists all cases in the system.

        Returns:
            list: A list of all cases.
        """
        return list(self.cases.values())

    def get_case(self, case_id):
        """
        Retrieves details of a specific case.

        Args:
            case_id (str): ID of the case to retrieve.

        Returns:
            dict: Details of the case.
        """
        if case_id not in self.cases:
            raise ValueError(f"No case found with ID '{case_id}'.")
        return self.cases[case_id]

    def _save_case_to_file(self, case_id, case_data):
        """
        Saves case data to a file for persistence.

        Args:
            case_id (str): ID of the case.
            case_data (dict): Case data to save.
        """
        case_file_path = os.path.join(CASE_STORAGE_PATH, f"{case_id}.json")
        with open(case_file_path, "w") as f:
            json.dump(case_data, f, indent=4)

    def _load_cases_from_files(self):
        """
        Loads all cases from files into memory. Call this method on system initialization.
        """
        for filename in os.listdir(CASE_STORAGE_PATH):
            if filename.endswith(".json"):
                file_path = os.path.join(CASE_STORAGE_PATH, filename)
                with open(file_path, "r") as f:
                    case_data = json.load(f)
                    self.cases[case_data["case_id"]] = case_data

# Example usage (ensure this is removed in production and replaced with appropriate interface)
if __name__ == "__main__":
    system = LegalDocumentManagementSystem()
    system._load_cases_from_files()  # Load existing data

    try:
        # Create a new case
        case = system.create_case(
            case_id="001",
            title="Corporate Merger Case",
            description="Legal assistance for merger of two corporations.",
            client_name="ABC Corp"
        )
        print("Case Created:", case)

        # Upload a document
        document = system.upload_document(
            case_id="001",
            document_name="Merger Agreement",
            document_content="This is the content of the merger agreement document."
        )
        print("Document Uploaded:", document)

        # List all cases
        cases = system.list_cases()
        print("All Cases:", cases)

        # Retrieve a specific case
        retrieved_case = system.get_case("001")
        print("Retrieved Case:", retrieved_case)

    except Exception as e:
        print(f"Error: {e}")
```
