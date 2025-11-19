"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Generate a practical internship report template for a nursing student based on the examples provided on 账云范文网.
Generated: DETERMINISTIC_cd3cb7afe1c65607
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Nursing Internship Report Template Generator
This script generates a structured internship report template for nursing students.
The template follows common standards and includes all necessary sections.
"""

import datetime
from typing import Dict, List, Optional

class NursingInternshipReport:
    """
    A class to generate nursing internship report templates.
    """
    
    def __init__(self, student_info: Dict[str, str], institution_info: Dict[str, str]):
        """
        Initialize the report with student and institution information.
        
        Args:
            student_info: Dictionary containing student details
            institution_info: Dictionary containing institution details
        """
        self.student_info = student_info
        self.institution_info = institution_info
        self.sections = []
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        
    def add_section(self, title: str, content: str) -> None:
        """
        Add a new section to the report.
        
        Args:
            title: Section title
            content: Section content
        """
        self.sections.append({"title": title, "content": content})
    
    def generate_header(self) -> str:
        """Generate the report header section."""
        return f"""
        NURSING INTERNSHIP REPORT
        ========================
        
        Student Information:
        - Name: {self.student_info.get('name', '')}
        - Student ID: {self.student_info.get('student_id', '')}
        - Program: {self.student_info.get('program', '')}
        - Year: {self.student_info.get('year', '')}
        
        Institution Information:
        - Name: {self.institution_info.get('name', '')}
        - Department: {self.institution_info.get('department', '')}
        - Supervisor: {self.institution_info.get('supervisor', '')}
        - Duration: {self.institution_info.get('duration', '')}
        
        Report Date: {self.current_date}
        """
    
    def generate_table_of_contents(self) -> str:
        """Generate the table of contents."""
        toc = "TABLE OF CONTENTS\n================\n"
        for i, section in enumerate(self.sections, 1):
            toc += f"{i}. {section['title']}\n"
        return toc
    
    def generate_body(self) -> str:
        """Generate the main body content."""
        body = ""
        for section in self.sections:
            body += f"\n{section['title']}\n{'=' * len(section['title'])}\n"
            body += f"{section['content']}\n"
        return body
    
    def generate_footer(self) -> str:
        """Generate the report footer."""
        return f"""
        Conclusion
        ==========
        This concludes my internship report. I appreciate the opportunity to learn and grow during this internship.
        
        Student Signature: ____________________
        Date: {self.current_date}
        
        Supervisor Signature: ____________________
        Date: __________
        """
    
    def generate_report(self) -> str:
        """Generate the complete report."""
        try:
            report = self.generate_header()
            report += "\n" + self.generate_table_of_contents()
            report += "\n" + self.generate_body()
            report += "\n" + self.generate_footer()
            return report
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    student = {
        "name": "Jane Doe",
        "student_id": "NS2023001",
        "program": "Bachelor of Nursing",
        "year": "3rd Year"
    }
    
    institution = {
        "name": "City General Hospital",
        "department": "Pediatrics",
        "supervisor": "Dr. Smith",
        "duration": "June 1 - August 30, 2023"
    }
    
    report = NursingInternshipReport(student, institution)
    
    # Add standard sections
    report.add_section("Introduction", 
                      "This report documents my nursing internship experience at City General Hospital...")
    
    report.add_section("Objectives", 
                      "1. Gain practical nursing experience\n2. Develop clinical skills\n3. Learn hospital protocols")
    
    report.add_section("Daily Activities", 
                      "Detailed description of daily responsibilities and tasks performed...")
    
    report.add_section("Key Learnings", 
                      "Summary of important skills and knowledge acquired during the internship...")
    
    report.add_section("Challenges Faced", 
                      "Discussion of difficulties encountered and how they were addressed...")
    
    # Generate and print the report
    try:
        full_report = report.generate_report()
        print(full_report)
    except RuntimeError as e:
        print(f"Error: {e}")
```
