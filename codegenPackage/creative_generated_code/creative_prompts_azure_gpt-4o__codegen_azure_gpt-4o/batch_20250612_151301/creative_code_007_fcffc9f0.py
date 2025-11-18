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

Certainly! Below is Python code using the `matplotlib` library to visualize patient appointment schedules in a Gantt chart format.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Define a function to visualize appointment schedules
def visualize_appointment_schedule(appointments):
    """
    Visualizes patient appointment schedules using a Gantt chart.

    Args:
        appointments (list of dict): A list of dictionaries, where each dictionary represents an appointment.
            Each dictionary should have the following keys:
            - 'Patient': Name of the patient.
            - 'Procedure': Name of the procedure (e.g., 'Colonoscopy', 'Esofagomanometria').
            - 'Start': Start time of the appointment (datetime object).
            - 'End': End time of the appointment (datetime object).
    """
    try:
        # Transform the data into a DataFrame for easier processing
        df = pd.DataFrame(appointments)
        
        # Ensure the data contains the required fields
        required_fields = {'Patient', 'Procedure', 'Start', 'End'}
        if not required_fields.issubset(df.columns):
            raise ValueError(f"Input data must contain the following fields: {required_fields}")
        
        # Generate unique colors for each procedure
        procedures = df['Procedure'].unique()
        color_mapping = {procedure: plt.cm.tab20(i / len(procedures)) for i, procedure in enumerate(procedures)}
        
        # Create the Gantt chart
        fig, ax = plt.subplots(figsize=(10, 6))
        for i, row in df.iterrows():
            ax.barh(
                y=row['Patient'], 
                left=row['Start'], 
                width=(row['End'] - row['Start']).total_seconds() / 3600,  # Convert seconds to hours
                color=color_mapping[row['Procedure']], 
                edgecolor='black', 
                label=row['Procedure'],
                alpha=0.8
            )
        
        # Add labels, title, and legend
        ax.set_xlabel("Time (Hours)")
        ax.set_ylabel("Patients")
        ax.set_title("Patient Appointment Schedule")
        ax.legend(procedures, title="Procedures", loc='upper right')
        
        # Adjust layout
        plt.tight_layout()
        plt.show()
    
    except Exception as e:
        print(f"An error occurred while visualizing the appointment schedule: {e}")

# Example usage
if __name__ == "__main__":
    from datetime import datetime

    # Define appointment data
    appointments = [
        {
            "Patient": "Alice",
            "Procedure": "Colonoscopy",
            "Start": datetime(2023, 11, 1, 8, 00),
            "End": datetime(2023, 11, 1, 9, 00)
        },
        {
            "Patient": "Bob",
            "Procedure": "Esofagomanometria",
            "Start": datetime(2023, 11, 1, 9, 15),
            "End": datetime(2023, 11, 1, 10, 15)
        },
        {
            "Patient": "Charlie",
            "Procedure": "Colonoscopy",
            "Start": datetime(2023, 11, 1, 10, 30),
            "End": datetime(2023, 11, 1, 11, 30)
        }
    ]

    # Visualize the appointment schedule
    visualize_appointment_schedule(appointments)
```

### Key Points:
- **Dependencies**: The code uses `matplotlib` for creating the Gantt chart and `pandas` for managing appointment data.
- **Error Handling**: Ensures the input data contains the required fields; catches any runtime errors.
- **Best Practices**: Modular function design, readable variable names, proper use of libraries, and dynamic color mapping based on unique procedures.
