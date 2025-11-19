"""
Generated Code Metadata:
========================
Original URL: https://aamctg.edu.bd
Prompt: "Generate a notice for the upcoming half-yearly exam for students from Ibte­dai to Class 9 at Ashekane Aulia Fazil Madrasah."
Generated: DETERMINISTIC_f1d5c136c4273eb1
Batch ID: 20250622_204634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ExamNotice:
    def __init__(self, institution_name, classes, exam_date):
        """
        Initializes the ExamNotice with the institution name, classes, and exam date.

        :param institution_name: Name of the institution
        :param classes: List of classes participating in the exam
        :param exam_date: Date of the exam
        """
        self.institution_name = institution_name
        self.classes = classes
        self.exam_date = exam_date

    def generate_notice(self):
        """
        Generates a formatted notice for the upcoming half-yearly exam.

        :return: A string containing the formatted notice
        """
        notice = f"Notice for Half-Yearly Exam\n"
        notice += f"Institution: {self.institution_name}\n"
        notice += f"Classes: {', '.join(self.classes)}\n"
        notice += f"Date of Exam: {self.exam_date.strftime('%B %d, %Y')}\n"
        notice += "Please prepare accordingly and ensure your attendance.\n"
        notice += "Best of luck to all students!"
        return notice

def main():
    """
    Main function to create an exam notice and print it.
    """
    # Define the institution name and classes
    institution_name = "Ashekane Aulia Fazil Madrasah"
    classes = ["Ibtedai", "Class 1", "Class 2", "Class 3", "Class 4", 
               "Class 5", "Class 6", "Class 7", "Class 8", "Class 9"]
    
    # Define the exam date
    try:
        exam_date = datetime.datetime(2023, 12, 15)  # Example date
    except ValueError as e:
        print(f"Error in date: {e}")
        return

    # Create an instance of ExamNotice
    exam_notice = ExamNotice(institution_name, classes, exam_date)

    # Generate and print the notice
    notice = exam_notice.generate_notice()
    print(notice)

if __name__ == "__main__":
    main()
```
