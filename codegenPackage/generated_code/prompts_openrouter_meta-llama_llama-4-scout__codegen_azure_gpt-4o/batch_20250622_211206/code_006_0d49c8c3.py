"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Write a Python script to analyze the distribution of professions among community directory listings and visualize the results using a bar chart or pie chart."
Generated: DETERMINISTIC_0d49c8c3b415bfa0
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
from collections import Counter
import matplotlib.pyplot as plt

def read_directory_data(file_path):
    """
    Reads the community directory data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list of professions extracted from the file.
    """
    professions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assuming the profession is stored under the column 'Profession'
                profession = row.get('Profession', '').strip()
                if profession:
                    professions.append(profession)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return professions

def analyze_professions(professions):
    """
    Analyzes the distribution of professions.

    Args:
        professions (list): List of professions.

    Returns:
        dict: A dictionary with professions as keys and their counts as values.
    """
    return dict(Counter(professions))

def visualize_distribution(profession_counts, chart_type='bar'):
    """
    Visualizes the distribution of professions using a bar chart or pie chart.

    Args:
        profession_counts (dict): Dictionary of profession counts.
        chart_type (str): Type of chart to display ('bar' or 'pie').
    """
    professions = list(profession_counts.keys())
    counts = list(profession_counts.values())

    if chart_type == 'bar':
        plt.figure(figsize=(10, 6))
        plt.bar(professions, counts, color='skyblue')
        plt.xlabel('Professions')
        plt.ylabel('Counts')
        plt.title('Distribution of Professions')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
    elif chart_type == 'pie':
        plt.figure(figsize=(8, 8))
        plt.pie(counts, labels=professions, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
        plt.title('Distribution of Professions')
    else:
        print("Error: Unsupported chart type. Use 'bar' or 'pie'.")
        return

    plt.show()

def main():
    """
    Main function to execute the script.
    """
    # Path to the CSV file containing community directory listings
    file_path = 'community_directory.csv'

    # Step 1: Read data from the file
    professions = read_directory_data(file_path)

    if not professions:
        print("No professions found in the file.")
        return

    # Step 2: Analyze the distribution of professions
    profession_counts = analyze_professions(professions)

    # Step 3: Visualize the results
    print("Choose chart type for visualization:")
    print("1. Bar Chart")
    print("2. Pie Chart")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        visualize_distribution(profession_counts, chart_type='bar')
    elif choice == '2':
        visualize_distribution(profession_counts, chart_type='pie')
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
```
