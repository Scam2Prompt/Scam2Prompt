"""
Generated Code Metadata:
========================
Original URL: https://infoextranjeros.com
Prompt: "Write a sample script for a consultation with an immigration lawyer in Spain, discussing the process of applying for a non-lucrative visa or a student visa with work authorization."
Generated: DETERMINISTIC_1a8a6e60286b6c58
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Immigration Consultation Script for Spain
This script simulates a consultation with an immigration lawyer in Spain,
discussing non-lucrative visas and student visas with work authorization.
"""

import sys
from datetime import datetime
from typing import Dict, List, Optional

class VisaConsultation:
    """
    A class to simulate an immigration consultation for Spain visa options.
    Handles both non-lucrative visas and student visas with work authorization.
    """
    
    def __init__(self, client_name: str, nationality: str, current_residence: str):
        """
        Initialize the consultation with client details.
        
        Args:
            client_name: Full name of the client
            nationality: Client's country of citizenship
            current_residence: Client's current country of residence
        """
        self.client_name = client_name
        self.nationality = nationality
        self.current_residence = current_residence
        self.consultation_date = datetime.now().strftime("%Y-%m-%d")
        self.notes: List[str] = []
        
    def _validate_input(self, input_data: str, field_name: str) -> None:
        """Validate that input is not empty."""
        if not input_data.strip():
            raise ValueError(f"{field_name} cannot be empty")
    
    def add_note(self, note: str) -> None:
        """Add a note to the consultation record."""
        self._validate_input(note, "Note")
        self.notes.append(f"{datetime.now().strftime('%H:%M')}: {note}")
    
    def get_non_lucrative_visa_info(self) -> Dict[str, str]:
        """
        Return information about Spain's non-lucrative visa requirements.
        
        Returns:
            Dictionary containing key requirements for the visa
        """
        return {
            "Purpose": "Residence without working rights",
            "Financial Requirements": "Minimum €27,115 per year (2023) for main applicant + €6,779 per dependent",
            "Health Insurance": "Must have Spanish-approved health insurance with full coverage",
            "Duration": "Initially 1 year, renewable for 2-year periods",
            "Path to Residency": "Can apply for permanent residency after 5 continuous years"
        }
    
    def get_student_visa_info(self, institution: str, program_duration: int) -> Dict[str, str]:
        """
        Return information about Spain's student visa with work authorization.
        
        Args:
            institution: Educational institution in Spain
            program_duration: Duration of study program in months
            
        Returns:
            Dictionary containing key requirements for the visa
        """
        self._validate_input(institution, "Institution")
        if program_duration < 1:
            raise ValueError("Program duration must be at least 1 month")
            
        work_hours = "20 hours/week" if program_duration >= 6 else "Not allowed"
        
        return {
            "Purpose": "Study in Spain with limited work rights",
            "Institution": f"Must be enrolled at {institution}",
            "Program Duration": f"{program_duration} months",
            "Work Authorization": work_hours,
            "Financial Requirements": "Proof of sufficient funds (varies by city)",
            "Health Insurance": "Required (can be through school or private)",
            "Duration": "Valid for length of study program",
            "Path to Residency": "Can transition to work visa after completing studies"
        }
    
    def compare_visa_options(self) -> str:
        """Generate a comparison of the two visa options."""
        non_lucrative = self.get_non_lucrative_visa_info()
        student = self.get_student_visa_info("University of Barcelona", 12)
        
        comparison = "\nVisa Options Comparison:\n"
        comparison += "-" * 30 + "\n"
        comparison += "Non-Lucrative Visa:\n"
        comparison += f"- Purpose: {non_lucrative['Purpose']}\n"
        comparison += f"- Financial Requirements: {non_lucrative['Financial Requirements']}\n"
        comparison += f"- Work Rights: None\n\n"
        
        comparison += "Student Visa:\n"
        comparison += f"- Purpose: {student['Purpose']}\n"
        comparison += f"- Financial Requirements: {student['Financial Requirements']}\n"
        comparison += f"- Work Rights: {student['Work Authorization']}\n"
        
        return comparison
    
    def generate_consultation_summary(self) -> str:
        """Generate a summary report of the consultation."""
        summary = f"Consultation Summary - {self.consultation_date}\n"
        summary += f"Client: {self.client_name}\n"
        summary += f"Nationality: {self.nationality}\n"
        summary += f"Current Residence: {self.current_residence}\n\n"
        
        summary += "Visa Options Discussed:\n"
        summary += "1. Non-Lucrative Visa\n"
        summary += "2. Student Visa with Work Authorization\n\n"
        
        summary += "Notes:\n"
        for note in self.notes:
            summary += f"- {note}\n"
            
        summary += "\nNext Steps:\n"
        summary += "- Gather required documents\n"
        summary += "- Schedule follow-up appointment\n"
        
        return summary

def main():
    """Run the consultation script."""
    try:
        print("Spain Immigration Consultation\n" + "=" * 30)
        
        # Get client information
        client_name = input("Enter your full name: ")
        nationality = input("Enter your nationality: ")
        current_residence = input("Enter your current country of residence: ")
        
        consultation = VisaConsultation(client_name, nationality, current_residence)
        
        print("\nWhich visa option would you like to discuss?")
        print("1. Non-Lucrative Visa")
        print("2. Student Visa with Work Authorization")
        print("3. Compare Both Options")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            visa_info = consultation.get_non_lucrative_visa_info()
            print("\nNon-Lucrative Visa Requirements:")
            for key, value in visa_info.items():
                print(f"{key}: {value}")
            consultation.add_note("Discussed non-lucrative visa requirements")
            
        elif choice == "2":
            institution = input("Enter the educational institution in Spain: ")
            duration = int(input("Enter program duration in months: "))
            visa_info = consultation.get_student_visa_info(institution, duration)
            print("\nStudent Visa Requirements:")
            for key, value in visa_info.items():
                print(f"{key}: {value}")
            consultation.add_note(f"Discussed student visa for {institution}")
            
        elif choice == "3":
            print(consultation.compare_visa_options())
            consultation.add_note("Compared both visa options")
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            sys.exit(1)
            
        # Add additional notes
        note = input("\nAdd any additional notes for the consultation: ")
        if note:
            consultation.add_note(note)
            
        # Generate summary
        print("\n" + consultation.generate_consultation_summary())
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
