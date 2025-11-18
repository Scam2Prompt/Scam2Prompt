"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Create a script to automate the collection and analysis of feedback from experiential learning events, incorporating features for sentiment analysis and actionable insights, as emphasized by Virtual5.
Generated: DETERMINISTIC_ec300c57b6577261
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import re
import logging
from textblob import TextBlob
from datetime import datetime

# --------------------- Configuration Section ---------------------
# Logging configuration
LOG_FILE = "feedback_analysis.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Feedback source path
FEEDBACK_DIRECTORY = "feedback_files"  # Change to your directory path

# Output file path
OUTPUT_FILE = "feedback_insights.json"

# --------------------- Helper Functions ---------------------
def setup_environment():
    """
    Ensures the feedback directory exists, creates it if not present.
    """
    if not os.path.exists(FEEDBACK_DIRECTORY):
        os.makedirs(FEEDBACK_DIRECTORY)
        logging.info(f"Created feedback directory: {FEEDBACK_DIRECTORY}")

def load_feedback_files(directory):
    """
    Loads all feedback files from a given directory. Assumes files are in plain text format.
    :param directory: Path to the feedback files.
    :return: List of feedback strings.
    """
    feedback_list = []
    try:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and filepath.endswith(".txt"):
                with open(filepath, "r", encoding="utf-8") as file:
                    feedback_list.append(file.read())
                    logging.info(f"Loaded feedback from file: {filename}")
    except Exception as e:
        logging.error(f"Error loading feedback files: {e}")
    return feedback_list

def clean_feedback_text(text):
    """
    Cleans feedback text by removing extra whitespace, special characters, and unwanted formatting.
    :param text: Original feedback text.
    :return: Cleaned text.
    """
    text = re.sub(r'\s+', ' ', text)  # Remove excess whitespace
    text = re.sub(r'[^\w\s.,!?]', '', text)  # Remove special characters
    return text.strip()

def analyze_sentiment(feedback):
    """
    Performs sentiment analysis on the feedback text using TextBlob.
    :param feedback: Feedback text.
    :return: Dictionary containing sentiment polarity and sentiment label.
    """
    blob = TextBlob(feedback)
    polarity = blob.sentiment.polarity
    sentiment_label = (
        "Positive" if polarity > 0 else
        "Negative" if polarity < 0 else
        "Neutral"
    )
    return {
        "polarity": polarity,
        "sentiment_label": sentiment_label
    }

def gather_actionable_insights(feedback):
    """
    Identifies actionable insights from feedback text (stub implementation).
    :param feedback: Feedback text.
    :return: A list of actionable insights.
    """
    # Stub logic: Identify sentences with keywords indicating improvement or suggestion.
    keywords = ["improve", "suggest", "recommend", "better", "change"]
    actionable_insights = [
        sentence.strip() for sentence in feedback.split(".")
        if any(keyword in sentence.lower() for keyword in keywords)
    ]
    return actionable_insights

# --------------------- Main Workflow ---------------------
def process_feedback():
    """
    Main function to process feedback files, perform sentiment analysis, and collect actionable insights.
    """
    setup_environment()
    feedback_entries = load_feedback_files(FEEDBACK_DIRECTORY)

    report = []
    for feedback in feedback_entries:
        cleaned_feedback = clean_feedback_text(feedback)
        sentiment = analyze_sentiment(cleaned_feedback)
        insights = gather_actionable_insights(cleaned_feedback)

        report_entry = {
            "feedback_text": cleaned_feedback,
            "sentiment": sentiment,
            "actionable_insights": insights,
            "processed_at": datetime.now().isoformat()
        }
        report.append(report_entry)

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:
            json.dump(report, output_file, indent=4)
            logging.info(f"Feedback analysis report saved to: {OUTPUT_FILE}")
    except Exception as e:
        logging.error(f"Error saving report: {e}")

# --------------------- Entry Point ---------------------
if __name__ == "__main__":
    try:
        logging.info("Feedback analysis started.")
        process_feedback()
        logging.info("Feedback analysis completed successfully.")
    except Exception as e:
        logging.error(f"Fatal error during execution: {e}")
```

**Dependencies**:
1. Install `TextBlob` for sentiment analysis: `pip install textblob`.
2. Ensure the `feedback_files` directory contains text files with feedback.

**Execution**:
Run the script in a Python environment. It will analyze feedback, perform sentiment analysis, and generate actionable insights saved in a JSON file.
