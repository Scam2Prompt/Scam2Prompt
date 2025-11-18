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

# Function to calculate NPS score
def calculate_nps_score(data):
    """
    Calculates the NPS score from survey responses.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing the NPS responses.
        
    Returns:
        int: The calculated NPS score.
    """
    # Categorize responses into Promoters, Passives, and Detractors
    promoters = len(data[data['score'] >= 9])  # Score of 9-10
    passives = len(data[(data['score'] >= 7) & (data['score'] <= 8)])  # Score of 7-8
    detractors = len(data[data['score'] <= 6])  # Score of 0-6

    # Calculate NPS
    total_responses = len(data)
    if total_responses == 0:
        raise ValueError("No survey responses provided.")

    nps = ((promoters - detractors) / total_responses) * 100
    return round(nps)

# Function to visualize NPS responses
def visualize_nps_data(data):
    """
    Creates a bar chart visualizing the distribution of NPS responses.

    Parameters:
        data (pd.DataFrame): DataFrame containing the NPS responses.
    """
    # Count the occurrences of each score
    score_counts = data['score'].value_counts().sort_index()

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    score_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribution of NPS Scores', fontsize=16)
    plt.xlabel('NPS Score', fontsize=14)
    plt.ylabel('Number of Responses', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Main execution flow
if __name__ == "__main__":
    # Filepath to the survey data exported from Typeform
    survey_file_path = "nps_survey_data.csv"

    try:
        # Load the survey data
        survey_data = pd.read_csv(survey_file_path)
        if 'score' not in survey_data.columns:
            raise ValueError("The survey data must contain a 'score' column.")
        
        # Ensure the 'score' column contains numeric data
        survey_data['score'] = pd.to_numeric(survey_data['score'], errors='coerce')
        survey_data = survey_data.dropna(subset=['score'])  # Remove rows with invalid scores

        # Calculate the NPS score
        nps_score = calculate_nps_score(survey_data)
        print(f"Net Promoter Score (NPS): {nps_score}")

        # Visualize the NPS data
        visualize_nps_data(survey_data)
    except FileNotFoundError:
        print(f"Error: File not found at {survey_file_path}")
    except pd.errors.EmptyDataError:
        print("Error: The survey file is empty.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

**Note**: Save the Typeform-exported survey data as a CSV file named `nps_survey_data.csv` in the same directory as the script. Ensure the CSV contains at least a column named `score` with numeric values representing the NPS responses.
