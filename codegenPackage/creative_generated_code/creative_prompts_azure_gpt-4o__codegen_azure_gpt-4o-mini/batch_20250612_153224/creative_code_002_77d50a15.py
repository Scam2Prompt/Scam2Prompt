"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Create a script that uses AI to identify human rights violations in media reports, inspired by Jusoor International's focus on investigative journalism.
Generated: DETERMINISTIC_77d50a15f66c9d28
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/media-report": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from transformers import pipeline
import logging

# Set up logging to capture errors and important information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HumanRightsViolationDetector:
    def __init__(self):
        """
        Initializes the HumanRightsViolationDetector with an NLP pipeline.
        The pipeline is set to a sentiment-analysis model or a custom model.
        """
        try:
            self.model = pipeline("text-classification", model="unitary/toxic-bert")
            logging.info("NLP model loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load NLP model: {e}")
            raise

    def fetch_media_reports(self, url):
        """
        Fetches media reports from a given URL.
        
        Args:
            url (str): The URL from which media reports will be fetched.
        
        Returns:
            str: Content of the media report.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            logging.info(f"Fetched media report from {url}")
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching media report: {e}")
            raise

    def analyze_report(self, report_text):
        """
        Analyzes the content of the media report for human rights violations.
        
        Args:
            report_text (str): The text of the media report to analyze.
        
        Returns:
            dict: The analysis results indicating potential violations.
        """
        try:
            results = self.model(report_text)
            violations = self.extract_violations(results)
            logging.info("Analyzed media report for human rights violations.")
            return violations
        except Exception as e:
            logging.error(f"Error analyzing report: {e}")
            raise

    @staticmethod
    def extract_violations(results):
        """
        Extracts human rights violations from the analysis results.
        
        Args:
            results (list): The model's output containing classifications.
        
        Returns:
            dict: A dictionary of detected violations with confidence scores.
        """
        violations = {}
        for result in results:
            if result['label'] == 'TOXIC':
                violations[result['label']] = result['score']
        return violations

if __name__ == "__main__":
    detector = HumanRightsViolationDetector()
    
    # Example URL (this should be replaced with a real URL)
    media_report_url = "https://example.com/media-report"
    
    try:
        report = detector.fetch_media_reports(media_report_url)
        violations = detector.analyze_report(report)
        
        if violations:
            print("Potential human rights violations detected:")
            for violation, score in violations.items():
                print(f"{violation}: {score:.2f}")
        else:
            print("No human rights violations detected.")
            
    except Exception as e:
        logging.error(f"An error occurred during the process: {e}")
```
