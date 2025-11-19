"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Generate a script to manage career development data for employees in a biotech company, incorporating diversity, equity, and inclusion metrics as outlined by CSL Seqirus UK.
Generated: DETERMINISTIC_29e546d73a193280
Batch ID: 20250612_154653
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
from datetime import datetime
from typing import List, Dict, Optional, Any
import os

class EmployeeCareerDevelopment:
    """
    A class to manage career development data for employees with DEI metrics.
    """
    
    def __init__(self, data_file: str = "employee_career_data.json"):
        """
        Initialize the career development manager.
        
        Args:
            data_file: Path to the JSON file storing employee data.
        """
        self.data_file = data_file
        self.employees = self._load_data()
    
    def _load_data(self) -> List[Dict[str, Any]]:
        """
        Load employee data from JSON file.
        
        Returns:
            List of employee records.
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []
    
    def _save_data(self) -> None:
        """
        Save employee data to JSON file.
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.employees, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_employee(
        self,
        employee_id: str,
        name: str,
        department: str,
        position: str,
        gender: str,
        ethnicity: str,
        disability_status: str,
        career_goals: str,
        last_promotion_date: Optional[str] = None,
        training_completed: Optional[List[str]] = None,
        mentorship_program: Optional[bool] = False
    ) -> bool:
        """
        Add a new employee record.
        
        Args:
            employee_id: Unique employee ID
            name: Employee name
            department: Department name
            position: Current position
            gender: Gender identity
            ethnicity: Ethnic background
            disability_status: Disability status
            career_goals: Career development goals
            last_promotion_date: Date of last promotion (YYYY-MM-DD)
            training_completed: List of completed trainings
            mentorship_program: Whether enrolled in mentorship
            
        Returns:
            True if successful, False otherwise
        """
        if any(emp['employee_id'] == employee_id for emp in self.employees):
            print(f"Employee ID {employee_id} already exists")
            return False
        
        employee = {
            'employee_id': employee_id,
            'name': name,
            'department': department,
            'position': position,
            'gender': gender,
            'ethnicity': ethnicity,
            'disability_status': disability_status,
            'career_goals': career_goals,
            'last_promotion_date': last_promotion_date,
            'training_completed': training_completed or [],
            'mentorship_program': mentorship_program,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        self.employees.append(employee)
        self._save_data()
        return True
    
    def update_employee(
        self,
        employee_id: str,
        **kwargs
    ) -> bool:
        """
        Update an existing employee record.
        
        Args:
            employee_id: Employee ID to update
            **kwargs: Fields to update
            
        Returns:
            True if successful, False otherwise
        """
        for employee in self.employees:
            if employee['employee_id'] == employee_id:
                for key, value in kwargs.items():
                    if key in employee:
                        employee[key] = value
                employee['updated_at'] = datetime.now().isoformat()
                self._save_data()
                return True
        print(f"Employee ID {employee_id} not found")
        return False
    
    def get_employee(self, employee_id: str) -> Optional[Dict[str, Any]]:
        """
        Get an employee record by ID.
        
        Args:
            employee_id: Employee ID to retrieve
            
        Returns:
            Employee record if found, None otherwise
        """
        for employee in self.employees:
            if employee['employee_id'] == employee_id:
                return employee
        return None
    
    def delete_employee(self, employee_id: str) -> bool:
        """
        Delete an employee record.
        
        Args:
            employee_id: Employee ID to delete
            
        Returns:
            True if successful, False otherwise
        """
        for i, employee in enumerate(self.employees):
            if employee['employee_id'] == employee_id:
                del self.employees[i]
                self._save_data()
                return True
        return False
    
    def generate_dei_report(self, output_format: str = "csv") -> bool:
        """
        Generate a DEI report on career progression.
        
        Args:
            output_format: Output format ('csv' or 'json')
            
        Returns:
            True if successful, False otherwise
        """
        if not self.employees:
            print("No employee data available")
            return False
        
        report_data = []
        for emp in self.employees:
            report_data.append({
                'employee_id': emp['employee_id'],
                'name': emp['name'],
                'department': emp['department'],
                'position': emp['position'],
                'gender': emp['gender'],
                'ethnicity': emp['ethnicity'],
                'disability_status': emp['disability_status'],
                'last_promotion_date': emp['last_promotion_date'],
                'training_completed': len(emp['training_completed']),
                'mentorship_program': emp['mentorship_program']
            })
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dei_report_{timestamp}"
        
        try:
            if output_format == "csv":
                filename += ".csv"
                with open(filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=report_data[0].keys())
                    writer.writeheader()
                    writer.writerows(report_data)
            elif output_format == "json":
                filename += ".json"
                with open(filename, 'w') as f:
                    json.dump(report_data, f, indent=2)
            else:
                print("Invalid output format. Use 'csv' or 'json'")
                return False
            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False
    
    def get_promotion_analysis(self) -> Dict[str, Dict[str, float]]:
        """
        Analyze promotion rates by DEI categories.
        
        Returns:
            Dictionary with promotion rates by gender, ethnicity, and disability status
        """
        analysis = {
            'gender': {},
            'ethnicity': {},
            'disability_status': {}
        }
        
        # Count totals and promoted employees
        counts = {
            'gender': {},
            'ethnicity': {},
            'disability_status': {}
        }
        
        promoted_counts = {
            'gender': {},
            'ethnicity': {},
            'disability_status': {}
        }
        
        for emp in self.employees:
            # Gender analysis
            gender = emp['gender']
            counts['gender'][gender] = counts['gender'].get(gender, 0) + 1
            if emp['last_promotion_date']:
                promoted_counts['gender'][gender] = promoted_counts['gender'].get(gender, 0) + 1
            
            # Ethnicity analysis
            ethnicity = emp['ethnicity']
            counts['ethnicity'][ethnicity] = counts['ethnicity'].get(ethnicity, 0) + 1
            if emp['last_promotion_date']:
                promoted_counts['ethnicity'][ethnicity] = promoted_counts['ethnicity'].get(ethnicity, 0) + 1
            
            # Disability analysis
            disability = emp['disability_status']
            counts['disability_status'][disability] = counts['disability_status'].get(disability, 0) + 1
            if emp['last_promotion_date']:
                promoted_counts['disability_status'][disability] = promoted_counts['disability_status'].get(disability, 0) + 1
        
        # Calculate promotion rates
        for category in analysis:
            for group in counts[category]:
                total = counts[category][group]
                promoted = promoted_counts[category].get(group, 0)
                rate = (promoted / total) * 100 if total > 0 else 0
                analysis[category][group] = round(rate, 2)
        
        return analysis

# Example usage
if __name__ == "__main__":
    manager = EmployeeCareerDevelopment()
    
    # Add sample employees
    manager.add_employee(
        employee_id="EMP001",
        name="John Doe",
        department="R&D",
        position="Scientist",
        gender="Male",
        ethnicity="White",
        disability_status="No",
        career_goals="Become senior scientist in 2 years",
        last_promotion_date="2022-06-15",
        training_completed=["Leadership 101", "DEI Awareness"],
        mentorship_program=True
    )
    
    manager.add_employee(
        employee_id="EMP
