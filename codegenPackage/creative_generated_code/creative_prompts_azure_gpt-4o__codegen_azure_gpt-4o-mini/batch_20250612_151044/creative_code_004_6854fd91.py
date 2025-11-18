"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonex.markets
Prompt: Write a script to process StoneX's cotton market reports and extract actionable insights using Natural Language Processing (NLP) libraries like spaCy or NLTK.
Generated: DETERMINISTIC_6854fd91f6d9ae17
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import spacy
import logging
from typing import List, Tuple

# Set up logging for tracking processing status and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the spaCy model for English
nlp = spacy.load('en_core_web_sm')

def load_reports(file_path: str) -> pd.DataFrame:
    """
    Load cotton market reports from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing reports.

    Returns:
        pd.DataFrame: DataFrame containing the reports.
    """
    try:
        reports = pd.read_csv(file_path)
        logging.info("Reports loaded successfully from {}".format(file_path))
        return reports
    except Exception as e:
        logging.error("Failed to load reports: {}".format(e))
        raise

def extract_insights(text: str) -> List[Tuple[str, str]]:
    """
    Extract actionable insights from the given text using NLP.

    Args:
        text (str): Text content of the market report.

    Returns:
        List[Tuple[str, str]]: List of tuples containing entity labels and their corresponding text.
    """
    insights = []
    
    # Process text with spaCy NLP model
    doc = nlp(text)

    # Extract entities and their labels
    for ent in doc.ents:
        insights.append((ent.label_, ent.text))
    
    logging.info("Insights extracted from text.")
    return insights

def process_reports(reports: pd.DataFrame) -> pd.DataFrame:
    """
    Process reports to extract insights.

    Args:
        reports (pd.DataFrame): DataFrame containing the market reports.

    Returns:
        pd.DataFrame: DataFrame with actionable insights.
    """
    insights_list = []

    for index, row in reports.iterrows():
        try:
            text = row['report_content']
            insights = extract_insights(text)
            insights_list.append({
                'report_id': row['report_id'],
                'insights': insights
            })
        except Exception as e:
            logging.error("Error processing report ID {}: {}".format(row['report_id'], e))

    return pd.DataFrame(insights_list)

def main(file_path: str):
    """
    Main function to execute the report processing workflow.

    Args:
        file_path (str): Path to the CSV file containing reports.
    """
    try:
        reports = load_reports(file_path)
        insights_df = process_reports(reports)
        insights_df.to_csv('extracted_insights.csv', index=False)
        logging.info("Insights successfully saved to extracted_insights.csv")
    except Exception as e:
        logging.critical("Failed to process reports: {}".format(e))

if __name__ == "__main__":
    # Replace 'path/to/cotton_reports.csv' with the actual path to the reports CSV file
    main('path/to/cotton_reports.csv')
```
