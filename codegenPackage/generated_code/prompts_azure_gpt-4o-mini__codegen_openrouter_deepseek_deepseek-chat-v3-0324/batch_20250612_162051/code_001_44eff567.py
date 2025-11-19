"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Write a Python script to automate the tracking of legal cases, inspired by the client-focused approach of the Complexo de Advocacia Dr. Adriano Geoffrey.
Generated: DETERMINISTIC_44eff5679ae3feae
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import Dict, List, Optional, Tuple

class LegalCaseTracker:
    """
    A class to track legal cases with client-focused features.
    Inspired by the approach of Complexo de Advocacia Dr. Adriano Geoffrey.
    """
    
    def __init__(self, data_file: str = "legal_cases.csv"):
        """
        Initialize the case tracker with a data file.
        
        Args:
            data_file: Path to the CSV file storing case data.
        """
        self.data_file = data_file
        self.case_fields = [
            "case_id", "client_name", "case_type", "filing_date", 
            "status", "next_hearing", "notes", "last_updated"
        ]
        
        # Create data file if it doesn't exist
        if not os.path.exists(self.data_file):
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.case_fields)
                writer.writeheader()
    
    def _get_current_timestamp(self) -> str:
        """Return current timestamp in ISO format."""
        return datetime.datetime.now().isoformat()
    
    def _validate_case_data(self, case_data: Dict) -> bool:
        """Validate case data before saving."""
        required_fields = ["case_id", "client_name", "case_type"]
        return all(field in case_data for field in required_fields)
    
    def add_case(self, case_data: Dict) -> bool:
        """
        Add a new case to the tracker.
        
        Args:
            case_data: Dictionary containing case information.
            
        Returns:
            bool: True if case was added successfully, False otherwise.
        """
        if not self._validate_case_data(case_data):
            return False
            
        case_data["last_updated"] = self._get_current_timestamp()
        
        # Set default values for optional fields
        case_data.setdefault("status", "Open")
        case_data.setdefault("notes", "")
        
        try:
            with open(self.data_file, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.case_fields)
                writer.writerow(case_data)
            return True
        except Exception as e:
            print(f"Error adding case: {e}")
            return False
    
    def update_case(self, case_id: str, updates: Dict) -> bool:
        """
        Update an existing case.
        
        Args:
            case_id: ID of the case to update.
            updates: Dictionary of fields to update.
            
        Returns:
            bool: True if update was successful, False otherwise.
        """
        cases = self.get_all_cases()
        updated = False
        
        for case in cases:
            if case["case_id"] == case_id:
                case.update(updates)
                case["last_updated"] = self._get_current_timestamp()
                updated = True
                break
        
        if updated:
            try:
                with open(self.data_file, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=self.case_fields)
                    writer.writeheader()
                    writer.writerows(cases)
                return True
            except Exception as e:
                print(f"Error updating case: {e}")
        
        return False
    
    def get_case(self, case_id: str) -> Optional[Dict]:
        """
        Retrieve a specific case by ID.
        
        Args:
            case_id: ID of the case to retrieve.
            
        Returns:
            Optional[Dict]: The case data if found, None otherwise.
        """
        cases = self.get_all_cases()
        for case in cases:
            if case["case_id"] == case_id:
                return case
        return None
    
    def get_all_cases(self) -> List[Dict]:
        """
        Retrieve all cases from the tracker.
        
        Returns:
            List[Dict]: List of all cases.
        """
        try:
            with open(self.data_file, mode='r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except Exception as e:
            print(f"Error reading cases: {e}")
            return []
    
    def get_cases_by_status(self, status: str) -> List[Dict]:
        """
        Retrieve cases filtered by status.
        
        Args:
            status: Status to filter by (e.g., "Open", "Closed").
            
        Returns:
            List[Dict]: List of matching cases.
        """
        cases = self.get_all_cases()
        return [case for case in cases if case["status"].lower() == status.lower()]
    
    def get_upcoming_hearings(self, days: int = 30) -> List[Dict]:
        """
        Retrieve cases with hearings coming up within specified days.
        
        Args:
            days: Number of days to look ahead (default: 30).
            
        Returns:
            List[Dict]: List of cases with upcoming hearings.
        """
        cases = self.get_all_cases()
        upcoming = []
        today = datetime.date.today()
        
        for case in cases:
            if case["next_hearing"]:
                try:
                    hearing_date = datetime.datetime.strptime(
                        case["next_hearing"], "%Y-%m-%d"
                    ).date()
                    if 0 <= (hearing_date - today).days <= days:
                        upcoming.append(case)
                except ValueError:
                    continue
        
        return upcoming
    
    def generate_report(self, output_file: str = "case_report.txt") -> bool:
        """
        Generate a summary report of all cases.
        
        Args:
            output_file: Path to save the report.
            
        Returns:
            bool: True if report was generated successfully.
        """
        cases = self.get_all_cases()
        if not cases:
            return False
            
        try:
            with open(output_file, 'w') as file:
                file.write("LEGAL CASE REPORT\n")
                file.write(f"Generated on: {self._get_current_timestamp()}\n")
                file.write(f"Total cases: {len(cases)}\n\n")
                
                status_counts = {}
                for case in cases:
                    status = case["status"]
                    status_counts[status] = status_counts.get(status, 0) + 1
                
                file.write("Status Summary:\n")
                for status, count in status_counts.items():
                    file.write(f"- {status}: {count} cases\n")
                
                upcoming = self.get_upcoming_hearings()
                if upcoming:
                    file.write("\nUpcoming Hearings (next 30 days):\n")
                    for case in upcoming:
                        file.write(
                            f"- Case {case['case_id']}: {case['client_name']} "
                            f"({case['case_type']}) on {case['next_hearing']}\n"
                        )
            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False


# Example usage
if __name__ == "__main__":
    tracker = LegalCaseTracker()
    
    # Add a new case
    new_case = {
        "case_id": "LC-2023-001",
        "client_name": "John Doe",
        "case_type": "Civil",
        "filing_date": "2023-01-15",
        "next_hearing": "2023-06-20",
        "notes": "Initial consultation completed"
    }
    tracker.add_case(new_case)
    
    # Update a case
    tracker.update_case("LC-2023-001", {"status": "Active", "notes": "Discovery phase"})
    
    # Generate report
    tracker.generate_report()
```
