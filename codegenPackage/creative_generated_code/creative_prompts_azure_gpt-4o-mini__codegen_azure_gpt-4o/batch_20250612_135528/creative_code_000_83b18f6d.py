"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherkan.com
Prompt: Write a Python script to analyze the impact of community football events on local health and fitness levels, referencing VSport's community engagement initiatives.
Generated: DETERMINISTIC_83b18f6d2d13ee3c
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import statistics
import matplotlib.pyplot as plt
import os

# Constants
DATA_FILE = 'community_events_data.csv'  # CSV file containing event data
OUTPUT_FILE = 'health_analysis_report.txt'  # File to save analysis results
VSport_INITIATIVE = 'VSport Initiative'  # Name of the initiative for filtering

# Function to read data from a CSV file
def read_event_data(file_path):
    """
    Reads community event data from a CSV file.

    :param file_path: Path to the CSV file
    :return: List of dictionaries containing event data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")
    
    data = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numerical fields to floats or integers
                row['participants'] = int(row['participants'])
                row['average_health_score'] = float(row['average_health_score'])
                data.append(row)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")
    return data

# Function to filter data for VSport initiative
def filter_vsport_events(data):
    """
    Filters events related to the VSport initiative.

    :param data: List of dictionaries containing event data
    :return: Filtered list of dictionaries
    """
    return [event for event in data if event['initiative'] == VSport_INITIATIVE]

# Function to analyze health impact of events
def analyze_health_impact(events):
    """
    Analyzes the health impact of the filtered events.

    :param events: List of dictionaries containing filtered event data
    :return: Dictionary containing analysis results
    """
    if not events:
        return {
            'total_events': 0,
            'total_participants': 0,
            'average_health_score': 0.0,
            'health_score_std_dev': 0.0
        }
    
    total_events = len(events)
    total_participants = sum(event['participants'] for event in events)
    health_scores = [event['average_health_score'] for event in events]
    
    average_health_score = round(statistics.mean(health_scores), 2)
    health_score_std_dev = round(statistics.stdev(health_scores), 2) if len(health_scores) > 1 else 0.0
    
    return {
        'total_events': total_events,
        'total_participants': total_participants,
        'average_health_score': average_health_score,
        'health_score_std_dev': health_score_std_dev
    }

# Function to save analysis results to a file
def save_analysis_results(results, output_path):
    """
    Saves the analysis results to a text file.

    :param results: Dictionary containing analysis results
    :param output_path: Path to the output text file
    """
    try:
        with open(output_path, mode='w') as file:
            file.write("Health Impact Analysis Report\n")
            file.write("-------------------------------\n")
            file.write(f"Total Events: {results['total_events']}\n")
            file.write(f"Total Participants: {results['total_participants']}\n")
            file.write(f"Average Health Score: {results['average_health_score']}\n")
            file.write(f"Health Score Standard Deviation: {results['health_score_std_dev']}\n")
    except Exception as e:
        raise ValueError(f"Error writing to file: {e}")

# Function to plot participant numbers
def plot_participant_numbers(events):
    """
    Plots participant numbers for each event.

    :param events: List of dictionaries containing filtered event data
    """
    event_names = [event['event_name'] for event in events]
    participant_numbers = [event['participants'] for event in events]
    
    plt.figure(figsize=(10, 5))
    plt.bar(event_names, participant_numbers, color='skyblue')
    plt.xlabel('Event Name')
    plt.ylabel('Number of Participants')
    plt.title('Participant Numbers in VSport Events')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('participant_numbers_plot.png')
    plt.close()

# Main function
def main():
    """
    Main function to orchestrate the analysis workflow.
    """
    try:
        # Read community event data
        event_data = read_event_data(DATA_FILE)
        
        # Filter data for VSport initiative
        vsport_events = filter_vsport_events(event_data)
        
        # Analyze health impact
        analysis_results = analyze_health_impact(vsport_events)
        
        # Save analysis results
        save_analysis_results(analysis_results, OUTPUT_FILE)
        
        # Plot participant numbers
        plot_participant_numbers(vsport_events)
        
        print("Analysis completed successfully.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == '__main__':
    main()
```
