"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write code to analyze and visualize data on psychologists' participation in international courses and seminars, as mentioned in the Colegio de Psicólogos de Oruro's partnerships.
Generated: DETERMINISTIC_ffda487ed42c2a20
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
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
        print("Error: There was a problem parsing the file.")
        return None

def analyze_participation(data):
    """
    Analyze the participation of psychologists in international courses and seminars.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the participation data.

    Returns:
    pd.DataFrame: A DataFrame summarizing the participation analysis.
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return None

    # Group by course/seminar and count the number of participants
    participation_summary = data.groupby('Course/Seminar')['Participants'].sum().reset_index()
    participation_summary.sort_values(by='Participants', ascending=False, inplace=True)
    return participation_summary

def visualize_participation(participation_summary):
    """
    Visualize the participation summary using a bar plot.

    Parameters:
    participation_summary (pd.DataFrame): The DataFrame summarizing the participation analysis.
    """
    if participation_summary is None or participation_summary.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Participants', y='Course/Seminar', data=participation_summary, palette='viridis')
    plt.title('Participation of Psychologists in International Courses and Seminars')
    plt.xlabel('Number of Participants')
    plt.ylabel('Course/Seminar')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data analysis and visualization.
    """
    # Load the data
    file_path = 'psychologists_participation.csv'  # Update with the actual file path
    data = load_data(file_path)

    # Analyze the participation
    participation_summary = analyze_participation(data)

    # Visualize the results
    visualize_participation(participation_summary)

if __name__ == "__main__":
    main()
```
