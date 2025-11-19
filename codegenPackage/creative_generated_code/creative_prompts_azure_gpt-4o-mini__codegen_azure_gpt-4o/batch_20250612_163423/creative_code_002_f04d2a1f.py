"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Write a Python script that analyzes user engagement data to identify habits and talents, inspired by the methodologies used by Virtual5 in their organizational training.
Generated: DETERMINISTIC_f04d2a1ff362d8c5
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import pandas as pd


def load_data(file_path):
    """
    Load user engagement data from a JSON file.

    :param file_path: Path to the JSON file containing engagement data.
    :return: DataFrame containing the user engagement data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


def analyze_habits(data):
    """
    Analyze user habits based on engagement data.

    :param data: DataFrame containing user engagement data.
    :return: DataFrame summarizing habit analysis results.
    """
    try:
        # Assume each user has 'activity' and 'timestamp' columns in the dataset
        habit_summary = (
            data.groupby(['user_id', 'activity'])
            .size()
            .reset_index(name='count')
            .sort_values(by=['user_id', 'count'], ascending=[True, False])
        )
        return habit_summary
    except KeyError as e:
        print(f"Error: Missing required column in data - {e}")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


def analyze_talents(data):
    """
    Analyze user talents based on engagement data.

    :param data: DataFrame containing user engagement data.
    :return: DataFrame summarizing talent analysis based on activity scores.
    """
    try:
        # Assuming the dataset has a 'score' column for activity performance
        talent_summary = (
            data.groupby(['user_id', 'activity'])['score']
            .mean()
            .reset_index(name='average_score')
            .sort_values(by=['user_id', 'average_score'], ascending=[True, False])
        )
        return talent_summary
    except KeyError as e:
        print(f"Error: Missing required column in data - {e}")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise


def save_analysis_results(data, file_path):
    """
    Save analysis results to a CSV file.

    :param data: DataFrame containing analysis results.
    :param file_path: Path to save the CSV file.
    """
    try:
        data.to_csv(file_path, index=False)
        print(f"Analysis results saved to {file_path}")
    except Exception as e:
        print(f"Error: Failed to save results. {e}")
        raise


def main():
    """
    Main function to orchestrate user engagement analysis.
    """
    # User-defined file paths
    input_file_path = 'user_engagement_data.json'
    habits_output_path = 'habits_analysis.csv'
    talents_output_path = 'talents_analysis.csv'

    try:
        # Load data
        user_data = load_data(input_file_path)

        # Analyze habits
        habits_data = analyze_habits(user_data)
        save_analysis_results(habits_data, habits_output_path)

        # Analyze talents
        talents_data = analyze_talents(user_data)
        save_analysis_results(talents_data, talents_output_path)

    except Exception as e:
        print(f"An error occurred during analysis: {e}")


if __name__ == "__main__":
    main()
```
