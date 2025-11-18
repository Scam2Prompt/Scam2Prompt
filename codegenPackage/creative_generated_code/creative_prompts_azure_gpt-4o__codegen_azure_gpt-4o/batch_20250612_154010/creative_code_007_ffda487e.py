"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write code to analyze and visualize data on psychologists' participation in international courses and seminars, as mentioned in the Colegio de Psicólogos de Oruro's partnerships.
Generated: DETERMINISTIC_ffda487ed42c2a20
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    """
    Load CSV file containing data on psychologists' participation 
    in international courses and seminars.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
        return None
    except pd.errors.ParserError:
        print("Error: File could not be parsed")
        return None


# Analyze data
def analyze_data(data):
    """
    Analyze the data to compute summary statistics and trends.

    Args:
        data (pd.DataFrame): DataFrame containing the data.

    Returns:
        dict: Summary statistics and trends.
    """
    try:
        summary = {
            'total_participants': data['Participants'].sum(),
            'average_participants_per_event': data['Participants'].mean(),
            'total_events': len(data),
            'events_by_type': data['Type'].value_counts()
        }
        return summary
    except KeyError:
        print("Error: Missing expected columns in the data")
        return None


# Visualize data
def visualize_data(data, summary):
    """
    Create visualizations for the data.

    Args:
        data (pd.DataFrame): DataFrame containing the data.
        summary (dict): Summary statistics and trends.
    """
    try:
        # Bar chart for events by type
        plt.figure(figsize=(10, 6))
        data['Type'].value_counts().plot(kind='bar', color='skyblue')
        plt.title("Events by Type")
        plt.xlabel("Type of Event")
        plt.ylabel("Number of Events")
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig("events_by_type.png")
        plt.show()

        # Pie chart for participation
        plt.figure(figsize=(8, 8))
        participation = data.groupby('Type')['Participants'].sum()
        participation.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='viridis')
        plt.title("Participation by Event Type")
        plt.ylabel("")  # Hide the y-label for better aesthetics
        plt.tight_layout()
        plt.savefig("participation_by_event_type.png")
        plt.show()

        print("Visualizations generated successfully!")
    except KeyError:
        print("Error: Missing expected columns in the data")


def main():
    """
    Main function to orchestrate data analysis and visualization.
    """
    # Path to the CSV file
    file_path = "psychologists_participation.csv"

    # Step 1: Load data
    data = load_data(file_path)
    if data is None:
        return

    # Step 2: Analyze data
    summary = analyze_data(data)
    if summary is None:
        return

    # Print summary statistics
    print("Summary Statistics:")
    for key, value in summary.items():
        print(f"{key}: {value}")

    # Step 3: Visualize data
    visualize_data(data, summary)


if __name__ == "__main__":
    main()
```
