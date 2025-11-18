"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hydroraindrop.typeform.com
Prompt: Generate a script to analyze NPS survey data collected via Typeform and visualize the results using a Python data visualization library.
Generated: DETERMINISTIC_a8420f361dfac171
Batch ID: 20250612_151912
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
import seaborn as sns

def load_data(file_path):
    """
    Load NPS survey data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing NPS data.
        
    Returns:
        DataFrame: A pandas DataFrame containing the survey data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: There was an error parsing the file.")
        raise

def calculate_nps(data):
    """
    Calculate the Net Promoter Score (NPS) from the survey responses.
    
    Args:
        data (DataFrame): A DataFrame containing the NPS survey responses.
        
    Returns:
        float: The calculated NPS score.
    """
    promoters = data[data['nps_score'] >= 9].shape[0]
    detractors = data[data['nps_score'] <= 6].shape[0]
    total_responses = data.shape[0]

    if total_responses == 0:
        print("Error: No responses to calculate NPS.")
        return None

    nps_score = (promoters - detractors) / total_responses * 100
    print(f"NPS calculated: {nps_score:.2f}")
    return nps_score

def visualize_nps_distribution(data):
    """
    Visualize the distribution of NPS survey responses.
    
    Args:
        data (DataFrame): A DataFrame containing the NPS survey responses.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['nps_score'], bins=11, kde=True, color='blue')
    plt.title('NPS Score Distribution')
    plt.xlabel('NPS Score')
    plt.ylabel('Frequency')
    plt.xticks(range(0, 11))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.axvline(x=7.0, color='red', linestyle='--', label='Detractor Threshold')
    plt.axvline(x=9.0, color='green', linestyle='--', label='Promoter Threshold')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to run the NPS analysis and visualization.
    """
    file_path = 'nps_survey_data.csv'  # Change this to your actual file path
    try:
        # Load data
        nps_data = load_data(file_path)

        # Calculate NPS
        nps = calculate_nps(nps_data)
        if nps is not None:
            print(f"Final NPS Score: {nps:.2f}")

        # Visualize NPS distribution
        visualize_nps_distribution(nps_data)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
