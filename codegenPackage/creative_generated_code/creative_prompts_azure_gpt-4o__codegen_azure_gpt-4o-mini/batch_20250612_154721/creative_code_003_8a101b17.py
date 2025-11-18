"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-link.io
Prompt: Create a Python program to visualize the historical impact of MIT's contributions (e.g., radar, GPS, email) using a timeline library like Plotly or Matplotlib.
Generated: DETERMINISTIC_8a101b177de096c7
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

# Define a function to create a timeline of MIT's contributions
def create_mit_contributions_timeline(contributions):
    """
    Create a timeline visualization of MIT's contributions using matplotlib.
    
    Parameters:
    contributions (list of dict): A list where each dict contains 'date' and 'contribution'.
    """
    # Convert contributions into a DataFrame for easier manipulation
    df = pd.DataFrame(contributions)

    # Ensure the 'date' column is in datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop any rows where 'date' could not be converted
    df.dropna(subset=['date'], inplace=True)

    # Sort the DataFrame by date
    df.sort_values('date', inplace=True)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['contribution'], marker='o', linestyle='-', color='blue')

    # Format the date on the x-axis
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))  # Major ticks every 5 years
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # Set title and labels
    plt.title("Timeline of MIT's Contributions to Technology")
    plt.xlabel('Year')
    plt.ylabel('Contributions')

    # Rotate and format the x-axis date labels for readability
    plt.xticks(rotation=45)
    plt.grid(True)

    # Display the plot
    plt.tight_layout()
    plt.show()

# List of MIT contributions with their corresponding historical dates
mit_contributions = [
    {'date': '1940-01-01', 'contribution': 'Radar Technology'},
    {'date': '1970-01-01', 'contribution': 'GPS'},
    {'date': '1971-01-01', 'contribution': 'Email'},
    {'date': '1980-01-01', 'contribution': 'Robotics'},
    {'date': '2000-01-01', 'contribution': 'OpenCourseWare'},
    {'date': '2010-01-01', 'contribution': 'MITx (edX)'},
]

# Run the function with the contributions data
if __name__ == "__main__":
    try:
        create_mit_contributions_timeline(mit_contributions)
    except Exception as e:
        print(f"An error occurred while creating the timeline: {e}")
```
