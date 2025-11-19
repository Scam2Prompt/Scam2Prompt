"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Develop a program to organize and display the syllabus and results for MBBS and MD/MS courses at MIMSR Medical College, referencing the "Syllabus & Results" section.
Generated: DETERMINISTIC_db6452cb630dfd84
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional

class SyllabusManager:
    """
    A class to manage and display syllabus and results for MBBS and MD/MS courses.
    """
    
    def __init__(self, data_file: str = "syllabus_data.json"):
        """
        Initialize the SyllabusManager with a data file.
        
        Args:
            data_file (str): Path to the JSON file containing syllabus and results data.
        """
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """
        Load syllabus and results data from JSON file.
        
        Returns:
            Dict: Dictionary containing syllabus and results data.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            json.JSONDecodeError: If data file is not valid JSON.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file '{self.data_file}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in data file '{self.data_file}'.", doc="", pos=0)
    
    def get_courses(self) -> List[str]:
        """
        Get list of available courses.
        
        Returns:
            List[str]: List of course names (e.g., ['MBBS', 'MD/MS']).
        """
        return list(self.data.keys())
    
    def get_syllabus(self, course: str, year: Optional[int] = None) -> Dict:
        """
        Get syllabus for a specific course and optionally a specific year.
        
        Args:
            course (str): Course name (e.g., 'MBBS' or 'MD/MS').
            year (int, optional): Year of study. If None, returns all years.
            
        Returns:
            Dict: Syllabus data for the requested course and year(s).
            
        Raises:
            ValueError: If course or year is invalid.
        """
        if course not in self.data:
            raise ValueError(f"Course '{course}' not found.")
        
        syllabus = self.data[course].get("syllabus", {})
        
        if year is not None:
            if str(year) not in syllabus:
                raise ValueError(f"Year {year} not found for course '{course}'.")
            return {str(year): syllabus[str(year)]}
        
        return syllabus
    
    def get_results(self, course: str, year: Optional[int] = None) -> Dict:
        """
        Get results for a specific course and optionally a specific year.
        
        Args:
            course (str): Course name (e.g., 'MBBS' or 'MD/MS').
            year (int, optional): Year of study. If None, returns all years.
            
        Returns:
            Dict: Results data for the requested course and year(s).
            
        Raises:
            ValueError: If course or year is invalid.
        """
        if course not in self.data:
            raise ValueError(f"Course '{course}' not found.")
        
        results = self.data[course].get("results", {})
        
        if year is not None:
            if str(year) not in results:
                raise ValueError(f"Year {year} not found for course '{course}'.")
            return {str(year): results[str(year)]}
        
        return results
    
    def display_syllabus(self, course: str, year: Optional[int] = None):
        """
        Display syllabus in a user-friendly format.
        
        Args:
            course (str): Course name.
            year (int, optional): Year of study.
        """
        try:
            syllabus = self.get_syllabus(course, year)
            print(f"\nSyllabus for {course}" + (f" - Year {year}" if year else ""))
            print("=" * 50)
            
            for year_data, subjects in syllabus.items():
                print(f"\nYear {year_data}:")
                for subject, details in subjects.items():
                    print(f"\n  {subject}:")
                    print(f"    - Topics: {', '.join(details['topics'])}")
                    print(f"    - Books: {', '.join(details['books'])}")
                    print(f"    - Credits: {details['credits']}")
            
            print("\n" + "=" * 50)
        except ValueError as e:
            print(f"Error: {e}")
    
    def display_results(self, course: str, year: Optional[int] = None):
        """
        Display results in a user-friendly format.
        
        Args:
            course (str): Course name.
            year (int, optional): Year of study.
        """
        try:
            results = self.get_results(course, year)
            print(f"\nResults for {course}" + (f" - Year {year}" if year else ""))
            print("=" * 50)
            
            for year_data, result_info in results.items():
                print(f"\nYear {year_data}:")
                print(f"  - Exam Date: {result_info['exam_date']}")
                print(f"  - Pass Percentage: {result_info['pass_percentage']}%")
                print("\n  Top Performers:")
                for i, student in enumerate(result_info['top_performers'], 1):
                    print(f"    {i}. {student['name']} - {student['marks']}%")
            
            print("\n" + "=" * 50)
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """
    Main function to demonstrate the SyllabusManager functionality.
    """
    try:
        # Initialize syllabus manager
        manager = SyllabusManager()
        
        while True:
            print("\nMIMSR Medical College - Syllabus & Results System")
            print("1. View Available Courses")
            print("2. View Syllabus")
            print("3. View Results")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                print("\nAvailable Courses:")
                for course in manager.get_courses():
                    print(f"- {course}")
            
            elif choice == "2":
                course = input("Enter course (MBBS/MD/MS): ").upper()
                year_input = input("Enter year (leave blank for all years): ")
                year = int(year_input) if year_input.strip() else None
                manager.display_syllabus(course, year)
            
            elif choice == "3":
                course = input("Enter course (MBBS/MD/MS): ").upper()
                year_input = input("Enter year (leave blank for all years): ")
                year = int(year_input) if year_input.strip() else None
                manager.display_results(course, year)
            
            elif choice == "4":
                print("Exiting program...")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create sample data file if it doesn't exist
    if not os.path.exists("syllabus_data.json"):
        sample_data = {
            "MBBS": {
                "syllabus": {
                    "1": {
                        "Anatomy": {
                            "topics": ["General Anatomy", "Embryology", "Histology"],
                            "books": ["Gray's Anatomy", "BD Chaurasia"],
                            "credits": 4
                        },
                        "Physiology": {
                            "topics": ["General Physiology", "Blood", "Nerve-Muscle"],
                            "books": ["Guyton and Hall", "AK Jain"],
                            "credits": 4
                        }
                    },
                    "2": {
                        "Pathology": {
                            "topics": ["General Pathology", "Systemic Pathology"],
                            "books": ["Robbins", "Harsh Mohan"],
                            "credits": 5
                        }
                    }
                },
                "results": {
                    "1": {
                        "exam_date": "2023-05-15",
                        "pass_percentage": 92.5,
                        "top_performers": [
                            {"name": "Rahul Sharma", "marks": 98},
                            {"name": "Priya Patel", "marks": 97}
                        ]
                    }
                }
            },
            "MD/MS": {
                "syllabus": {
                    "1": {
                        "General Medicine": {
                            "topics": ["Cardiology", "Neurology", "Gastroenterology"],
                            "books": ["Harrison's", "Davidson's"],
                            "credits": 6
                        }
                    }
                },
                "results": {
                    "1": {
                        "exam_date": "2023-06-20",
                        "pass_percentage": 95.0,
                        "top_performers": [
                            {"name": "Dr. Amit Joshi", "marks": 99},
                            {"name": "Dr. Neha Gupta", "marks": 98}
                        ]
                    }
                }
            }
        }
        
        with open("syllabus_data.json", 'w') as f:
            json.dump(sample_data, f, indent=4)
    
    main()
