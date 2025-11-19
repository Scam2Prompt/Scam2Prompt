"""
Generated Code Metadata:
========================
Original URL: https://mnswap.org
Prompt: Create a dashboard using JavaScript or Python to visualize attendance and participation data from MN SWAP's conferences and seminars.
Generated: DETERMINISTIC_50eb4d81c7b01597
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load attendance and participation data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return None

def visualize_attendance(data):
    """
    Visualize attendance data using a bar plot.

    Parameters:
    data (DataFrame): A pandas DataFrame containing attendance data.
    """
    plt.figure(figsize=(10, 6))
    attendance_counts = data['Attendance'].value_counts()
    sns.barplot(x=attendance_counts.index, y=attendance_counts.values, palette='viridis')
    plt.title('Attendance Counts by Category')
    plt.xlabel('Category')
    plt.ylabel('Number of Attendees')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_participation(data):
    """
    Visualize participation data using a pie chart.

    Parameters:
    data (DataFrame): A pandas DataFrame containing participation data.
    """
    plt.figure(figsize=(8, 8))
    participation_counts = data['Participation'].value_counts()
    plt.pie(participation_counts, labels=participation_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Participation Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def main():
    """
    Main function to load data and visualize attendance and participation.
    """
    # Path to the CSV file
    file_path = 'attendance_participation_data.csv'
    
    # Load the data
    data = load_data(file_path)
    
    if data is not None:
        # Visualize attendance and participation
        visualize_attendance(data)
        visualize_participation(data)

if __name__ == "__main__":
    main()
```

Make sure to have the required libraries installed. You can install them using:
```bash
pip install pandas matplotlib seaborn
```

Ensure that the CSV file `attendance_participation_data.csv` contains the columns `Attendance` and `Participation` for the code to work correctly.
