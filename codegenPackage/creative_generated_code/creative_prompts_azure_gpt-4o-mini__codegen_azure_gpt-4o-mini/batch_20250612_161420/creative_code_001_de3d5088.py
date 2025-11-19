"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Write a notice for students regarding the upcoming Higher Secondary Examination starting on January 23, 2025, including instructions for teachers to submit question papers by January 15, 2025.
Generated: DETERMINISTIC_de3d5088778cc2b0
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ExaminationNotice:
    def __init__(self, exam_date, submission_deadline):
        """
        Initializes the ExaminationNotice with exam date and question paper submission deadline.
        
        :param exam_date: str - The date of the examination (format: YYYY-MM-DD)
        :param submission_deadline: str - The deadline for submitting question papers (format: YYYY-MM-DD)
        """
        self.exam_date = datetime.datetime.strptime(exam_date, '%Y-%m-%d')
        self.submission_deadline = datetime.datetime.strptime(submission_deadline, '%Y-%m-%d')

    def generate_notice(self):
        """
        Generates a notice for students regarding the upcoming examination and instructions for teachers.
        
        :return: str - The formatted notice with details
        """
        notice = (
            f"*** NOTICE TO STUDENTS ***\n\n"
            f"Dear Students,\n\n"
            f"We would like to inform you that the Higher Secondary Examination is scheduled to start on "
            f"{self.exam_date.strftime('%B %d, %Y')}.\n\n"
            f"Please prepare accordingly and make sure to review all relevant materials before the exam.\n\n"
            f"*** IMPORTANT INSTRUCTIONS FOR TEACHERS ***\n\n"
            f"Teachers are requested to submit the question papers by no later than "
            f"{self.submission_deadline.strftime('%B %d, %Y')}.\n"
            f"Submission should be sent to the examination office in a sealed envelope.\n\n"
            f"Thank you for your attention and cooperation.\n"
            f"Best regards,\n"
            f"The Examination Committee"
        )
        return notice

def main():
    try:
        # Define the exam date and submission deadline
        exam_date = "2025-01-23"
        submission_deadline = "2025-01-15"

        # Create an instance of ExaminationNotice
        notice = ExaminationNotice(exam_date, submission_deadline)
        
        # Generate and print the notice
        print(notice.generate_notice())

    except ValueError as e:
        # Handle date parsing errors
        print(f"Error: {e}. Please ensure the dates are in the correct format (YYYY-MM-DD).")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
