"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a code snippet to track and analyze hotel staff performance and management metrics, focusing on effective hotel management practices.
Generated: DETERMINISTIC_ffa25e0690fe206c
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class HotelStaffPerformanceTracker:
    """
    A class to track and analyze hotel staff performance and management metrics.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty DataFrame for staff performance data.
        """
        self.performance_data = pd.DataFrame(columns=['staff_id', 'name', 'role', 'performance_score', 'guest_feedback', 'date'])

    def add_performance_record(self, staff_id, name, role, performance_score, guest_feedback, date):
        """
        Adds a performance record for a hotel staff member.

        Parameters:
        - staff_id (int): Unique identifier for the staff member.
        - name (str): Name of the staff member.
        - role (str): Role of the staff member (e.g., 'Manager', 'Receptionist').
        - performance_score (float): Performance score (0-100).
        - guest_feedback (str): Feedback from guests.
        - date (str): Date of the performance record in 'YYYY-MM-DD' format.
        """
        try:
            # Validate performance score
            if not (0 <= performance_score <= 100):
                raise ValueError("Performance score must be between 0 and 100.")

            # Append the new record to the DataFrame
            new_record = {
                'staff_id': staff_id,
                'name': name,
                'role': role,
                'performance_score': performance_score,
                'guest_feedback': guest_feedback,
                'date': pd.to_datetime(date)
            }
            self.performance_data = self.performance_data.append(new_record, ignore_index=True)
        except Exception as e:
            print(f"Error adding performance record: {e}")

    def analyze_performance(self):
        """
        Analyzes the performance of staff members and returns summary statistics.
        
        Returns:
        - dict: A dictionary containing average performance scores and feedback summaries.
        """
        try:
            # Group by role and calculate average performance score
            performance_summary = self.performance_data.groupby('role')['performance_score'].mean().to_dict()
            feedback_summary = self.performance_data.groupby('role')['guest_feedback'].apply(lambda x: ' | '.join(x)).to_dict()

            return {
                'average_performance': performance_summary,
                'guest_feedback_summary': feedback_summary
            }
        except Exception as e:
            print(f"Error analyzing performance: {e}")
            return {}

    def get_performance_data(self):
        """
        Returns the performance data DataFrame.

        Returns:
        - DataFrame: The DataFrame containing all performance records.
        """
        return self.performance_data

# Example usage
if __name__ == "__main__":
    tracker = HotelStaffPerformanceTracker()
    
    # Adding performance records
    tracker.add_performance_record(1, 'Alice', 'Manager', 95, 'Excellent service!', '2023-10-01')
    tracker.add_performance_record(2, 'Bob', 'Receptionist', 85, 'Very helpful.', '2023-10-02')
    tracker.add_performance_record(3, 'Charlie', 'Housekeeping', 90, 'Room was spotless.', '2023-10-03')

    # Analyzing performance
    performance_analysis = tracker.analyze_performance()
    print("Performance Analysis:", performance_analysis)

    # Retrieving performance data
    print("Performance Data:\n", tracker.get_performance_data())
```
