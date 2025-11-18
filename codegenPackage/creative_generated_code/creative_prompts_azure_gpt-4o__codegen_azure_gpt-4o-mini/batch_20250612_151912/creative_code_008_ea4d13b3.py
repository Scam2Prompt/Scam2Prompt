"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originprotocol.typeform.com
Prompt: Create a Python script to analyze Typeform survey data using AI tools for extracting deeper customer insights.
Generated: DETERMINISTIC_ea4d13b3c99850dc
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
import openai
import os

# Set your OpenAI API key. Make sure to keep it secure and not hardcode in production.
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_survey_data(file_path):
    """
    Load survey data from a CSV file.

    :param file_path: str, path to the CSV file containing survey data
    :return: pd.DataFrame, DataFrame containing the survey data
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        raise

def analyze_data(data):
    """
    Perform analysis on the survey data to extract insights using OpenAI's API.

    :param data: pd.DataFrame, DataFrame containing the survey responses
    :return: dict, insights extracted from the data
    """
    insights = {}
    
    # Example: Get a summary of responses
    responses_summary = data.describe(include='all').to_dict()
    insights['summary'] = responses_summary

    # Generate deeper insights using the OpenAI API
    try:
        prompt = f"Analyze this survey data and provide insights: {responses_summary}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        insights['ai_insights'] = response['choices'][0]['message']['content']
        print("AI insights generated successfully.")
    except Exception as e:
        print(f"Error during AI analysis: {e}")
        insights['ai_insights'] = "Error generating insights."

    return insights

def save_insights(insights, output_file):
    """
    Save the insights to a JSON file.

    :param insights: dict, insights to save
    :param output_file: str, path to the output JSON file
    """
    try:
        with open(output_file, 'w') as f:
            pd.Series(insights).to_json(f, indent=4)
        print(f"Insights saved successfully to {output_file}")
    except Exception as e:
        print(f"Error saving insights: {e}")
        raise

def main():
    """
    Main function to execute the survey analysis workflow.
    """
    # Specify the input survey data file and output insights file
    input_file = 'survey_data.csv'  # Update with your CSV file path
    output_file = 'survey_insights.json'

    # Load survey data
    survey_data = load_survey_data(input_file)
    
    # Analyze the survey data
    insights = analyze_data(survey_data)
    
    # Save the insights
    save_insights(insights, output_file)

if __name__ == "__main__":
    main()
```
