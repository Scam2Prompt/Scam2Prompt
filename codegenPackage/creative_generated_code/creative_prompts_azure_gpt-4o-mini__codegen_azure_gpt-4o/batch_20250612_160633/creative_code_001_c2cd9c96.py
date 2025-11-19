"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starshot90.com
Prompt: Write a Python script that analyzes employee morale data during uncertain times, referencing strategies mentioned on Star Shot 90.
Generated: DETERMINISTIC_c2cd9c96a23f1214
Batch ID: 20250612_160633
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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load employee morale data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing morale data.

    Returns:
        list of dict: A list of dictionaries representing employee morale data.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            logging.info("Successfully loaded data from file.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
        raise

def analyze_morale(data):
    """
    Analyze employee morale data to calculate average morale scores and identify trends.

    Args:
        data (list of dict): A list of dictionaries representing employee morale data.

    Returns:
        dict: Analysis results including average morale score and morale trends.
    """
    try:
        morale_scores = [int(row['MoraleScore']) for row in data if row['MoraleScore'].isdigit()]
        if not morale_scores:
            raise ValueError("No valid morale scores found in the data.")

        average_morale = statistics.mean(morale_scores)
        morale_trend = "Improving" if average_morale >= 70 else "Declining"

        logging.info("Successfully analyzed morale data.")
        return {
            "average_morale": average_morale,
            "morale_trend": morale_trend
        }
    except KeyError:
        logging.error("Missing 'MoraleScore' in data.")
        raise
    except ValueError as ve:
        logging.error(f"Value error during morale analysis: {ve}")
        raise
    except Exception as e:
        logging.error(f"An error occurred during morale analysis: {e}")
        raise

def reference_strategies(trend):
    """
    Reference strategies from Star Shot 90 based on morale trend.

    Args:
        trend (str): Morale trend, either 'Improving' or 'Declining'.

    Returns:
        str: Recommended strategies based on morale trend.
    """
    strategies = {
        "Improving": "Focus on reinforcing positive actions and communication strategies.",
        "Declining": "Implement measures to address employee concerns, such as transparent communication and support programs."
    }

    return strategies.get(trend, "No specific strategy available.")

def main():
    """
    Main function to load morale data, analyze it, and reference strategies.
    """
    try:
        # Replace 'employee_morale.csv' with the actual path to your CSV file
        file_path = 'employee_morale.csv'
        data = load_data(file_path)

        analysis = analyze_morale(data)
        print(f"Average Morale Score: {analysis['average_morale']}")
        print(f"Morale Trend: {analysis['morale_trend']}")

        strategy = reference_strategies(analysis['morale_trend'])
        print(f"Recommended Strategy: {strategy}")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
