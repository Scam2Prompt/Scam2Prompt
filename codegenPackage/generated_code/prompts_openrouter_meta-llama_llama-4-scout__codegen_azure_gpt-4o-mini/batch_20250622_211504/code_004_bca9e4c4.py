"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: "Create a basic Excel formula for tracking student enrollment, similar to the Excel courses offered at ISIV."
Generated: DETERMINISTIC_bca9e4c47e5e79f6
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

# Define a function to track student enrollment
def track_student_enrollment(enrollment_data):
    """
    This function takes a DataFrame containing student enrollment data,
    processes it, and returns a summary of enrollments by course.

    Parameters:
    enrollment_data (pd.DataFrame): A DataFrame with columns 'Student Name', 'Course', and 'Enrollment Date'.

    Returns:
    pd.DataFrame: A summary DataFrame with the count of enrollments per course.
    """
    try:
        # Check if the required columns are in the DataFrame
        required_columns = ['Student Name', 'Course', 'Enrollment Date']
        for column in required_columns:
            if column not in enrollment_data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Group by 'Course' and count the number of enrollments
        enrollment_summary = enrollment_data.groupby('Course').size().reset_index(name='Enrollment Count')

        return enrollment_summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Sample enrollment data
    data = {
        'Student Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David'],
        'Course': ['Math', 'Science', 'Math', 'History', 'Science'],
        'Enrollment Date': ['2023-09-01', '2023-09-02', '2023-09-01', '2023-09-03', '2023-09-02']
    }

    # Create a DataFrame from the sample data
    enrollment_df = pd.DataFrame(data)

    # Track student enrollment
    summary = track_student_enrollment(enrollment_df)

    # Display the summary
    if summary is not None:
        print(summary)
```
