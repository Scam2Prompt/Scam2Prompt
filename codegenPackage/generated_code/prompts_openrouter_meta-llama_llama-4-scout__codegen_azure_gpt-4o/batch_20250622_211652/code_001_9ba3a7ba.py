"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Write a Python script to analyze the impact of educational events, such as workshops and jornadas, on student outcomes, inspired by CIMEd's event calendar."
Generated: DETERMINISTIC_9ba3a7baca0a9cc9
Batch ID: 20250622_211652
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
import numpy as np

# Define constants
EVENTS_FILE = "events_data.csv"  # Path to the CSV file containing event data
OUTCOMES_FILE = "student_outcomes.csv"  # Path to the CSV file containing student outcomes data

def load_data(events_file, outcomes_file):
    """
    Load event and student outcome data from CSV files.

    Args:
        events_file (str): Path to the events data file.
        outcomes_file (str): Path to the student outcomes data file.

    Returns:
        tuple: A tuple containing two DataFrames (events, outcomes).
    """
    try:
        events = pd.read_csv(events_file)
        outcomes = pd.read_csv(outcomes_file)
        return events, outcomes
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def preprocess_data(events, outcomes):
    """
    Preprocess the data for analysis.

    Args:
        events (DataFrame): DataFrame containing event data.
        outcomes (DataFrame): DataFrame containing student outcomes data.

    Returns:
        tuple: Preprocessed DataFrames (events, outcomes).
    """
    # Ensure proper datetime format for event dates
    events['date'] = pd.to_datetime(events['date'], errors='coerce')
    outcomes['date'] = pd.to_datetime(outcomes['date'], errors='coerce')

    # Drop rows with invalid dates
    events = events.dropna(subset=['date'])
    outcomes = outcomes.dropna(subset=['date'])

    # Filter relevant columns
    events = events[['event_id', 'event_name', 'date', 'type']]
    outcomes = outcomes[['student_id', 'date', 'outcome_score']]

    return events, outcomes

def analyze_impact(events, outcomes):
    """
    Analyze the impact of educational events on student outcomes.

    Args:
        events (DataFrame): DataFrame containing event data.
        outcomes (DataFrame): DataFrame containing student outcomes data.

    Returns:
        DataFrame: A summary DataFrame showing the impact of events on outcomes.
    """
    # Merge events and outcomes based on proximity of dates
    merged_data = pd.merge_asof(outcomes.sort_values('date'), 
                                events.sort_values('date'), 
                                on='date', 
                                direction='backward')

    # Group by event type and calculate average outcome score
    impact_summary = merged_data.groupby('type')['outcome_score'].mean().reset_index()
    impact_summary.rename(columns={'outcome_score': 'average_outcome_score'}, inplace=True)

    return impact_summary

def visualize_impact(impact_summary):
    """
    Visualize the impact of events on student outcomes.

    Args:
        impact_summary (DataFrame): Summary DataFrame showing the impact of events on outcomes.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(impact_summary['type'], impact_summary['average_outcome_score'], color='skyblue')
    plt.xlabel('Event Type')
    plt.ylabel('Average Outcome Score')
    plt.title('Impact of Educational Events on Student Outcomes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the analysis workflow.
    """
    try:
        # Load data
        events, outcomes = load_data(EVENTS_FILE, OUTCOMES_FILE)

        # Preprocess data
        events, outcomes = preprocess_data(events, outcomes)

        # Analyze impact
        impact_summary = analyze_impact(events, outcomes)

        # Display results
        print("Impact Summary:")
        print(impact_summary)

        # Visualize results
        visualize_impact(impact_summary)

    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
