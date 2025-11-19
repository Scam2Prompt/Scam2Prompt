"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Generate a Python script to automate the process of managing student admissions for an educational institution, similar to the admissions process described on the MercedariasGye website.
Generated: DETERMINISTIC_e542a71099e40aea
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
import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class StudentAdmissionSystem:
    """
    A system to manage student admissions for an educational institution.
    Handles applicant data, admission status, and generates reports.
    """
    
    def __init__(self, data_file: str = "admissions_data.json"):
        """
        Initialize the admission system with a data file.
        
        Args:
            data_file: Path to JSON file storing admission data
        """
        self.data_file = data_file
        self.applicants = self._load_data()
        
    def _load_data(self) -> Dict[str, Dict]:
        """
        Load applicant data from JSON file.
        Creates file if it doesn't exist.
        
        Returns:
            Dictionary of applicant data
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            return {}

    def _save_data(self) -> None:
        """
        Save applicant data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.applicants, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_applicant(self, 
                     student_id: str, 
                     first_name: str, 
                     last_name: str, 
                     birth_date: str, 
                     grade_level: str, 
                     parent_name: str, 
                     parent_email: str, 
                     parent_phone: str) -> bool:
        """
        Add a new applicant to the system.
        
        Args:
            student_id: Unique identifier for student
            first_name: Student's first name
            last_name: Student's last name
            birth_date: Date of birth (YYYY-MM-DD)
            grade_level: Grade applying for
            parent_name: Parent/guardian name
            parent_email: Parent/guardian email
            parent_phone: Parent/guardian phone
            
        Returns:
            True if successful, False otherwise
        """
        if student_id in self.applicants:
            print(f"Student ID {student_id} already exists")
            return False
            
        try:
            datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            print("Invalid birth date format. Use YYYY-MM-DD")
            return False
            
        self.applicants[student_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'grade_level': grade_level,
            'parent_name': parent_name,
            'parent_email': parent_email,
            'parent_phone': parent_phone,
            'application_date': datetime.now().strftime('%Y-%m-%d'),
            'status': 'Pending',
            'notes': ''
        }
        self._save_data()
        return True

    def update_status(self, student_id: str, status: str, notes: str = '') -> bool:
        """
        Update admission status for an applicant.
        
        Args:
            student_id: ID of student to update
            status: New status (Pending, Accepted, Rejected, Waitlisted)
            notes: Optional notes about the status change
            
        Returns:
            True if successful, False otherwise
        """
        valid_statuses = ['Pending', 'Accepted', 'Rejected', 'Waitlisted']
        if status not in valid_statuses:
            print(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
            return False
            
        if student_id not in self.applicants:
            print(f"Student ID {student_id} not found")
            return False
            
        self.applicants[student_id]['status'] = status
        if notes:
            self.applicants[student_id]['notes'] = notes
        self._save_data()
        return True

    def get_applicant(self, student_id: str) -> Optional[Dict]:
        """
        Retrieve applicant information.
        
        Args:
            student_id: ID of student to retrieve
            
        Returns:
            Applicant dictionary if found, None otherwise
        """
        return self.applicants.get(student_id)

    def search_applicants(self, 
                         status: Optional[str] = None, 
                         grade_level: Optional[str] = None) -> List[Dict]:
        """
        Search applicants by status and/or grade level.
        
        Args:
            status: Status to filter by
            grade_level: Grade level to filter by
            
        Returns:
            List of matching applicants
        """
        results = []
        for applicant in self.applicants.values():
            if (status is None or applicant['status'] == status) and \
               (grade_level is None or applicant['grade_level'] == grade_level):
                results.append(applicant)
        return results

    def generate_report(self, 
                       report_type: str = 'status', 
                       output_file: Optional[str] = None) -> bool:
        """
        Generate a report of applicants.
        
        Args:
            report_type: Type of report ('status' or 'grade')
            output_file: Path to save CSV report (prints to console if None)
            
        Returns:
            True if successful, False otherwise
        """
        if report_type not in ['status', 'grade']:
            print("Invalid report type. Must be 'status' or 'grade'")
            return False
            
        if report_type == 'status':
            fieldnames = ['status', 'count']
            data = {}
            for applicant in self.applicants.values():
                status = applicant['status']
                data[status] = data.get(status, 0) + 1
            rows = [{'status': k, 'count': v} for k, v in data.items()]
        else:
            fieldnames = ['grade_level', 'count']
            data = {}
            for applicant in self.applicants.values():
                grade = applicant['grade_level']
                data[grade] = data.get(grade, 0) + 1
            rows = [{'grade_level': k, 'count': v} for k, v in data.items()]
            
        if output_file:
            try:
                with open(output_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows)
            except IOError as e:
                print(f"Error writing report: {e}")
                return False
        else:
            print(f"{report_type.capitalize()} Report:")
            print("-" * 30)
            for row in rows:
                print(f"{row[fieldnames[0]]}: {row[fieldnames[1]]}")
                
        return True

    def export_applicants(self, output_file: str) -> bool:
        """
        Export all applicant data to CSV.
        
        Args:
            output_file: Path to save CSV file
            
        Returns:
            True if successful, False otherwise
        """
        if not self.applicants:
            print("No applicants to export")
            return False
            
        fieldnames = [
            'student_id',
            'first_name',
            'last_name',
            'birth_date',
            'grade_level',
            'parent_name',
            'parent_email',
            'parent_phone',
            'application_date',
            'status',
            'notes'
        ]
        
        try:
            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for student_id, data in self.applicants.items():
                    row = {'student_id': student_id}
                    row.update(data)
                    writer.writerow(row)
            return True
        except IOError as e:
            print(f"Error exporting data: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = StudentAdmissionSystem()
    
    # Add some sample applicants
    system.add_applicant(
        "S1001",
        "Maria",
        "Gonzalez",
        "2015-05-10",
        "1st Grade",
        "Juan Gonzalez",
        "juan@example.com",
        "555-1234"
    )
    
    system.add_applicant(
        "S1002",
        "Carlos",
        "Martinez",
        "2014-03-15",
        "2nd Grade",
        "Luisa Martinez",
        "luisa@example.com",
        "555-5678"
    )
    
    # Update status
    system.update_status("S1001", "Accepted", "Excellent test scores")
    
    # Generate reports
    system.generate_report('status')
    system.generate_report('grade')
    
    # Export data
    system.export_applicants("applicants_export.csv")
```
