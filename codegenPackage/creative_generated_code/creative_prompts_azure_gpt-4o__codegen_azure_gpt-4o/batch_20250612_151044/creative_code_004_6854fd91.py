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
import os
import spacy
from collections import Counter
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_market_reports(directory_path):
    """
    Loads all text files from the specified directory containing cotton market reports.

    Args:
        directory_path (str): Path to the directory containing report files.

    Returns:
        list of str: List of report contents as strings.
    """
    reports = []
    try:
        for file_name in os.listdir(directory_path):
            if file_name.endswith(".txt"):
                with open(os.path.join(directory_path, file_name), 'r', encoding='utf-8') as file:
                    reports.append(file.read())
        logging.info(f"Successfully loaded {len(reports)} market reports.")
    except Exception as e:
        logging.error(f"Error loading files: {e}")
    return reports

def extract_insights(report_texts, nlp_model):
    """
    Processes cotton market reports using NLP to extract actionable insights.

    Args:
        report_texts (list of str): List of market report contents.
        nlp_model (spacy.Language): NLP model for text processing.

    Returns:
        dict: Insights extracted, including keyword frequency and named entities.
    """
    insights = {"keyword_frequency": Counter(), "named_entities": []}
    try:
        for text in report_texts:
            # Process the text using the NLP model
            doc = nlp_model(text)

            # Update keyword frequency using lemmas of nouns and verbs
            insights["keyword_frequency"].update(
                [token.lemma_.lower() for token in doc if token.pos_ in {"NOUN", "VERB"}]
            )

            # Extract named entities
            insights["named_entities"].extend([(ent.text, ent.label_) for ent in doc.ents])

        logging.info("Insights successfully extracted.")
    except Exception as e:
        logging.error(f"Error processing reports: {e}")
    return insights

def main():
    """
    Main function to process StoneX's cotton market reports and extract actionable insights.
    """
    # Path to the directory containing cotton market reports
    reports_directory = "./cotton_market_reports"

    # Load NLP model (spaCy's English model - ensure it is installed)
    try:
        nlp = spacy.load("en_core_web_sm")
        logging.info("Successfully loaded spaCy NLP model.")
    except Exception as e:
        logging.error(f"Error loading NLP model: {e}")
        return

    # Load market reports
    reports = load_market_reports(reports_directory)
    if not reports:
        logging.warning("No reports found in the specified directory.")
        return

    # Extract insights from the reports
    insights = extract_insights(reports, nlp)

    # Display the insights
    print("\n--- Extracted Insights ---\n")
    print("Top Keywords:")
    for keyword, freq in insights["keyword_frequency"].most_common(10):
        print(f"{keyword}: {freq}")

    print("\nNamed Entities:")
    for entity, label in insights["named_entities"]:
        print(f"{entity} ({label})")

if __name__ == "__main__":
    main()
```

Make sure to install `spaCy` and download the English model (`en_core_web_sm`) before running this script:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```
Place your cotton market reports in a directory named `cotton_market_reports` relative to the script's location, with each report stored as a `.txt` file.
