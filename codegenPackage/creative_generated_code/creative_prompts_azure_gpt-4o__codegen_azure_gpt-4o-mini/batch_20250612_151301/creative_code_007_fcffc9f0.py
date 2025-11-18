"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Recommend a library or tool for visualizing patient appointment schedules for exams such as colonoscopia and esofagomanometria, with a focus on optimizing clinic workflow.
Generated: DETERMINISTIC_fcffc9f0cabc2502
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

class AppointmentVisualizer:
    """
    A class to visualize patient appointment schedules for medical exams.
    
    Attributes:
        appointments (pd.DataFrame): DataFrame containing appointment data.
    """

    def __init__(self, appointments):
        """
        Initializes the AppointmentVisualizer with a DataFrame of appointments.

        :param appointments: A list of dictionaries containing appointment details.
        """
        self.appointments = pd.DataFrame(appointments)

    def preprocess_data(self):
        """
        Preprocesses the appointment data to ensure correct data types
        and formats for visualization.
        """
        # Convert 'date' column to datetime
        self.appointments['date'] = pd.to_datetime(self.appointments['date'])
        # Check for necessary columns
        required_columns = ['date', 'patient_name', 'exam_type']
        if not all(col in self.appointments.columns for col in required_columns):
            raise ValueError("Missing required columns in appointment data.")

    def plot_appointments(self):
        """
        Plots a Gantt chart of the appointments to visualize the schedule.
        """
        self.preprocess_data()
        
        # Prepare data for plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, row in self.appointments.iterrows():
            start = row['date']
            end = start + timedelta(hours=1)  # Assuming each appointment lasts 1 hour
            ax.barh(row['patient_name'], end - start, left=start, label=row['exam_type'])
        
        # Formatting the plot
        ax.set_xlabel('Time')
        ax.set_ylabel('Patients')
        ax.set_title('Patient Appointment Schedule')
        ax.legend(title="Exam Type", loc='upper right')
        ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Sample appointment data
        sample_appointments = [
            {'date': '2023-10-01 09:00', 'patient_name': 'John Doe', 'exam_type': 'Colonoscopia'},
            {'date': '2023-10-01 10:00', 'patient_name': 'Jane Smith', 'exam_type': 'Esofagomanometria'},
            {'date': '2023-10-01 11:00', 'patient_name': 'Emily Johnson', 'exam_type': 'Colonoscopia'},
            {'date': '2023-10-01 12:00', 'patient_name': 'Michael Brown', 'exam_type': 'Esofagomanometria'},
        ]

        # Create an instance of the visualizer and plot the appointments
        visualizer = AppointmentVisualizer(sample_appointments)
        visualizer.plot_appointments()

    except Exception as e:
        print(f"An error occurred: {e}")
```
