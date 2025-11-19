"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Generate a sample academic calendar for a school like Ideal High School, including holidays and important dates.
Generated: DETERMINISTIC_32ca9d16bdae9818
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class AcademicCalendar:
    """
    Represents an academic calendar for a school with terms, holidays, and important dates.
    """
    
    def __init__(self, school_name: str, academic_year: str):
        """
        Initialize the academic calendar.
        
        Args:
            school_name: Name of the school
            academic_year: Academic year in format 'YYYY-YYYY'
        """
        self.school_name = school_name
        self.academic_year = academic_year
        self.terms: List[Dict] = []
        self.holidays: List[Dict] = []
        self.important_dates: List[Dict] = []
    
    def add_term(self, name: str, start_date: datetime.date, end_date: datetime.date) -> None:
        """
        Add a term to the academic calendar.
        
        Args:
            name: Name of the term (e.g., 'Fall Semester')
            start_date: Start date of the term
            end_date: End date of the term
        """
        self.terms.append({
            'name': name,
            'start_date': start_date,
            'end_date': end_date
        })
    
    def add_holiday(self, name: str, date: datetime.date) -> None:
        """
        Add a holiday to the academic calendar.
        
        Args:
            name: Name of the holiday
            date: Date of the holiday
        """
        self.holidays.append({
            'name': name,
            'date': date
        })
    
    def add_important_date(self, name: str, date: datetime.date, description: Optional[str] = None) -> None:
        """
        Add an important date to the academic calendar.
        
        Args:
            name: Name/Title of the important date
            date: Date of the event
            description: Optional description
        """
        self.important_dates.append({
            'name': name,
            'date': date,
            'description': description
        })
    
    def generate_calendar(self) -> Dict:
        """
        Generate the complete academic calendar structure.
        
        Returns:
            Dictionary containing all calendar information
        """
        return {
            'school_name': self.school_name,
            'academic_year': self.academic_year,
            'terms': sorted(self.terms, key=lambda x: x['start_date']),
            'holidays': sorted(self.holidays, key=lambda x: x['date']),
            'important_dates': sorted(self.important_dates, key=lambda x: x['date'])
        }
    
    def __str__(self) -> str:
        """String representation of the academic calendar."""
        calendar = self.generate_calendar()
        output = [
            f"Academic Calendar for {calendar['school_name']} ({calendar['academic_year']})",
            "\nTerms:"
        ]
        
        for term in calendar['terms']:
            output.append(f"- {term['name']}: {term['start_date'].strftime('%b %d, %Y')} to {term['end_date'].strftime('%b %d, %Y')}")
        
        output.append("\nHolidays:")
        for holiday in calendar['holidays']:
            output.append(f"- {holiday['name']}: {holiday['date'].strftime('%b %d, %Y')}")
        
        output.append("\nImportant Dates:")
        for date in calendar['important_dates']:
            desc = f" - {date['description']}" if date['description'] else ""
            output.append(f"- {date['name']}: {date['date'].strftime('%b %d, %Y')}{desc}")
        
        return "\n".join(output)


def create_sample_calendar() -> AcademicCalendar:
    """
    Create a sample academic calendar for Ideal High School.
    
    Returns:
        AcademicCalendar instance with sample data
    """
    calendar = AcademicCalendar("Ideal High School", "2023-2024")
    
    # Add terms
    calendar.add_term(
        "Fall Semester",
        datetime.date(2023, 8, 21),
        datetime.date(2023, 12, 15)
    )
    calendar.add_term(
        "Spring Semester",
        datetime.date(2024, 1, 8),
        datetime.date(2024, 5, 24)
    )
    
    # Add holidays
    calendar.add_holiday(
        "Labor Day",
        datetime.date(2023, 9, 4)
    )
    calendar.add_holiday(
        "Thanksgiving Break",
        datetime.date(2023, 11, 22)
    )
    calendar.add_holiday(
        "Winter Break",
        datetime.date(2023, 12, 25)
    )
    calendar.add_holiday(
        "Martin Luther King Jr. Day",
        datetime.date(2024, 1, 15)
    )
    calendar.add_holiday(
        "Spring Break",
        datetime.date(2024, 3, 11)
    )
    calendar.add_holiday(
        "Memorial Day",
        datetime.date(2024, 5, 27)
    )
    
    # Add important dates
    calendar.add_important_date(
        "First Day of School",
        datetime.date(2023, 8, 21),
        "Orientation for new students"
    )
    calendar.add_important_date(
        "Parent-Teacher Conferences",
        datetime.date(2023, 10, 12),
        "Evening sessions from 4-7 PM"
    )
    calendar.add_important_date(
        "Midterm Exams",
        datetime.date(2023, 10, 23)
    )
    calendar.add_important_date(
        "Final Exams",
        datetime.date(2023, 12, 11)
    )
    calendar.add_important_date(
        "Graduation",
        datetime.date(2024, 5, 24),
        "Commencement ceremony at 2 PM"
    )
    
    return calendar


if __name__ == "__main__":
    # Generate and print the sample calendar
    sample_calendar = create_sample_calendar()
    print(sample_calendar)
```
