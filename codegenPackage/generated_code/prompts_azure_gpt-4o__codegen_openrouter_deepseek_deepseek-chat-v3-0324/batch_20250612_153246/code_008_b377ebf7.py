"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Create a program to track and manage legal disputes in commercial law cases, using the litigation services mentioned on Luật Trung Cường's website.
Generated: DETERMINISTIC_b377ebf73fe47e09
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Legal Dispute Tracker - A system to manage commercial law litigation cases.
Inspired by services from Luật Trung Cường's website.
"""

from datetime import datetime
from typing import List, Dict, Optional
import json
import os

class LegalCase:
    """Class representing a commercial law legal case."""
    
    def __init__(self, case_id: str, title: str, client_name: str, case_type: str, 
                 filing_date: str, status: str = "Open", description: str = ""):
        """
        Initialize a legal case.
        
        Args:
            case_id: Unique identifier for the case
            title: Short title/name of the case
            client_name: Name of the client
            case_type: Type of commercial law case
            filing_date: Date when case was filed (YYYY-MM-DD)
            status: Current status of the case (default: "Open")
            description: Detailed description of the case (default: "")
        """
        self.case_id = case_id
        self.title = title
        self.client_name = client_name
        self.case_type = case_type
        self.filing_date = filing_date
        self.status = status
        self.description = description
        self.documents = []
        self.hearings = []
        self.notes = []
    
    def add_document(self, doc_name: str, doc_type: str, upload_date: str):
        """Add a document to the case."""
        self.documents.append({
            "name": doc_name,
            "type": doc_type,
            "date": upload_date
        })
    
    def add_hearing(self, hearing_date: str, location: str, purpose: str):
        """Schedule a hearing for the case."""
        self.hearings.append({
            "date": hearing_date,
            "location": location,
            "purpose": purpose
        })
    
    def add_note(self, note_date: str, content: str, author: str):
        """Add a note to the case file."""
        self.notes.append({
            "date": note_date,
            "content": content,
            "author": author
        })
    
    def update_status(self, new_status: str):
        """Update the status of the case."""
        self.status = new_status
    
    def to_dict(self) -> Dict:
        """Convert case object to dictionary for serialization."""
        return {
            "case_id": self.case_id,
            "title": self.title,
            "client_name": self.client_name,
            "case_type": self.case_type,
            "filing_date": self.filing_date,
            "status": self.status,
            "description": self.description,
            "documents": self.documents,
            "hearings": self.hearings,
            "notes": self.notes
        }

class CaseManager:
    """Class to manage multiple legal cases."""
    
    def __init__(self, data_file: str = "legal_cases.json"):
        """
        Initialize the case manager.
        
        Args:
            data_file: Path to JSON file for storing case data
        """
        self.data_file = data_file
        self.cases = {}
        self.load_cases()
    
    def load_cases(self):
        """Load cases from the data file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for case_id, case_data in data.items():
                        case = LegalCase(
                            case_id=case_data["case_id"],
                            title=case_data["title"],
                            client_name=case_data["client_name"],
                            case_type=case_data["case_type"],
                            filing_date=case_data["filing_date"],
                            status=case_data["status"],
                            description=case_data["description"]
                        )
                        case.documents = case_data.get("documents", [])
                        case.hearings = case_data.get("hearings", [])
                        case.notes = case_data.get("notes", [])
                        self.cases[case_id] = case
        except Exception as e:
            print(f"Error loading cases: {e}")
    
    def save_cases(self):
        """Save cases to the data file."""
        try:
            case_dict = {case_id: case.to_dict() for case_id, case in self.cases.items()}
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(case_dict, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving cases: {e}")
    
    def add_case(self, case: LegalCase):
        """Add a new case to the manager."""
        if case.case_id in self.cases:
            raise ValueError(f"Case ID {case.case_id} already exists")
        self.cases[case.case_id] = case
        self.save_cases()
    
    def get_case(self, case_id: str) -> Optional[LegalCase]:
        """Retrieve a case by its ID."""
        return self.cases.get(case_id)
    
    def update_case(self, case_id: str, **kwargs):
        """Update case information."""
        case = self.get_case(case_id)
        if not case:
            raise ValueError(f"Case {case_id} not found")
        
        for key, value in kwargs.items():
            if hasattr(case, key):
                setattr(case, key, value)
            else:
                raise AttributeError(f"Invalid case attribute: {key}")
        
        self.save_cases()
    
    def delete_case(self, case_id: str):
        """Delete a case from the system."""
        if case_id not in self.cases:
            raise ValueError(f"Case {case_id} not found")
        del self.cases[case_id]
        self.save_cases()
    
    def list_cases(self, filter_status: str = None) -> List[Dict]:
        """List all cases, optionally filtered by status."""
        cases_list = []
        for case in self.cases.values():
            if filter_status is None or case.status == filter_status:
                cases_list.append({
                    "case_id": case.case_id,
                    "title": case.title,
                    "client_name": case.client_name,
                    "case_type": case.case_type,
                    "filing_date": case.filing_date,
                    "status": case.status
                })
        return cases_list
    
    def search_cases(self, query: str) -> List[Dict]:
        """Search cases by client name, case title, or description."""
        results = []
        query = query.lower()
        for case in self.cases.values():
            if (query in case.client_name.lower() or 
                query in case.title.lower() or 
                query in case.description.lower()):
                results.append({
                    "case_id": case.case_id,
                    "title": case.title,
                    "client_name": case.client_name,
                    "status": case.status
                })
        return results

def validate_date(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def generate_case_id() -> str:
    """Generate a unique case ID."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"CASE-{timestamp}"

def main_menu():
    """Display the main menu and handle user input."""
    manager = CaseManager()
    
    while True:
        print("\nLegal Dispute Management System")
        print("1. Add New Case")
        print("2. View/Edit Case")
        print("3. List All Cases")
        print("4. Search Cases")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_case_menu(manager)
        elif choice == "2":
            case_id = input("Enter case ID: ")
            case_menu(manager, case_id)
        elif choice == "3":
            list_cases_menu(manager)
        elif choice == "4":
            search_cases_menu(manager)
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_case_menu(manager: CaseManager):
    """Menu for adding a new case."""
    print("\nAdd New Case")
    case_id = generate_case_id()
    title = input("Case title: ")
    client_name = input("Client name: ")
    case_type = input("Case type (e.g., Contract, Intellectual Property, etc.): ")
    
    while True:
        filing_date = input("Filing date (YYYY-MM-DD): ")
        if validate_date(filing_date):
            break
        print("Invalid date format. Please use YYYY-MM-DD.")
    
    description = input("Case description (optional): ")
    
    case = LegalCase(
        case_id=case_id,
        title=title,
        client_name=client_name,
        case_type=case_type,
        filing_date=filing_date,
        description=description
    )
    
    manager.add_case(case)
    print(f"\nCase added successfully! Case ID: {case
