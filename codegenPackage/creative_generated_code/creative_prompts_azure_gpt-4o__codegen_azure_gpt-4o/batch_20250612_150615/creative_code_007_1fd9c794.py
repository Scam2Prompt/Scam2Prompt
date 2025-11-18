"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://argoapp.live
Prompt: Recommend a library or tool for analyzing player engagement in online PC games, inspired by Argo App's article on fun games for leisure time.
Generated: DETERMINISTIC_1fd9c7942bb30c07
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to analyze player engagement in online PC games
# This script utilizes the pandas and matplotlib libraries for data analysis and visualization

import pandas as pd
import matplotlib.pyplot as plt
import os

# Function for loading player engagement data from a CSV file
def load_player_data(file_path):
    """
    Loads player engagement data from a CSV file.
    
    :param file_path: str, path to the CSV file
    :return: pandas DataFrame containing the player data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")
    
    return data

# Function to analyze player engagement
def analyze_engagement(data):
    """
    Analyzes player engagement based on the provided data.
    
    :param data: pandas DataFrame, player engagement data
    :return: None
    """
    if data.empty:
        raise ValueError("The provided data is empty.")
    
    # Check for necessary columns
    required_columns = ['player_id', 'session_duration', 'game_mode', 'date']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")
    
    # Basic statistics
    print("Player Engagement Statistics:")
    print(data[['session_duration']].describe())
    
    # Group by game mode and calculate average session duration
    avg_session_by_mode = data.groupby('game_mode')['session_duration'].mean()
    print("\nAverage Session Duration by Game Mode:")
    print(avg_session_by_mode)
    
    # Plot session duration distribution
    plt.figure(figsize=(10, 6))
    plt.hist(data['session_duration'], bins=20, color='blue', alpha=0.7)
    plt.title("Session Duration Distribution")
    plt.xlabel("Session Duration (minutes)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

# Main
if __name__ == "__main__":
    # Example usage
    try:
        # Specify the path to the CSV file containing player data
        csv_file_path = "player_engagement_data.csv"  # Replace with your file path
        
        # Load the data
        player_data = load_player_data(csv_file_path)
        
        # Analyze the data
        analyze_engagement(player_data)
    
    except FileNotFoundError as fnf_error:
        print(f"File error: {fnf_error}")
    except ValueError as value_error:
        print(f"Value error: {value_error}")
    except Exception as unexpected_error:
        print(f"An unexpected error occurred: {unexpected_error}")
```

### Notes for Usage:
- Replace `player_engagement_data.csv` with the actual path to your data file.
- Ensure that the CSV contains the required columns (`player_id`, `session_duration`, `game_mode`, `date`).
- Install pandas and matplotlib before running the code:
  ```bash
  pip install pandas matplotlib
  ```
