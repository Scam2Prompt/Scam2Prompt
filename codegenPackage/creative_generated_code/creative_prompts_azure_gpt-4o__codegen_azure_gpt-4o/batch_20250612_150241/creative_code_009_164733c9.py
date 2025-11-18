"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://federalfirstcapitalunion.com
Prompt: Write code to analyze phishing email patterns, inspired by Federal First Capital Union's fraud prevention articles.
Generated: DETERMINISTIC_164733c98216d53e
Batch ID: 20250612_150241
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/verify": {
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
import re
from collections import Counter
from typing import List, Dict, Tuple

class PhishingEmailAnalyzer:
    """
    A class to analyze phishing email patterns based on email content.

    Inspired by fraud prevention articles, particularly those from Federal First Capital Union.
    """

    def __init__(self):
        """
        Initializes the analyzer with common phishing indicators.
        """
        self.key_phrases = [
            "urgent", "verify your account", "click here", "limited time", 
            "win", "password", "account locked", "bank details", "personal information"
        ]
        self.suspicious_domains = ["example.com", "test.com", "phish.com"]
        self.url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

    def analyze_email(self, email_body: str, sender_email: str) -> Dict[str, int]:
        """
        Analyzes the given email body and sender's email for phishing patterns.

        :param email_body: The body of the email as a string.
        :param sender_email: The sender's email address.
        :return: A dictionary containing the count of suspicious indicators found.
        """
        try:
            # Initialize the pattern analysis result
            analysis_result = {"suspicious_phrases": 0, "suspicious_urls": 0, "suspicious_domains": 0}

            # Check for suspicious phrases in the email body
            phrase_matches = [phrase for phrase in self.key_phrases if phrase.lower() in email_body.lower()]
            analysis_result["suspicious_phrases"] = len(phrase_matches)

            # Check for suspicious URLs in the email body
            url_matches = re.findall(self.url_pattern, email_body)
            suspicious_urls = [url for url in url_matches if any(domain in url for domain in self.suspicious_domains)]
            analysis_result["suspicious_urls"] = len(suspicious_urls)

            # Check if sender's domain is suspicious
            sender_domain = sender_email.split('@')[-1]
            if sender_domain in self.suspicious_domains:
                analysis_result["suspicious_domains"] += 1

            return analysis_result
        except Exception as e:
            # Log and raise any exception that occurs during the analysis
            print(f"Error during phishing email analysis: {e}")
            raise

    def summarize_results(self, results: List[Dict[str, int]]) -> Dict[str, int]:
        """
        Summarizes the analysis results for multiple emails.

        :param results: A list of dictionaries containing analysis results for individual emails.
        :return: A dictionary summarizing the total counts for all indicators.
        """
        try:
            # Use Counter to aggregate results
            summary = Counter()
            for result in results:
                summary.update(result)
            return dict(summary)
        except Exception as e:
            # Log and raise any exception that occurs during summarization
            print(f"Error during summarizing results: {e}")
            raise


# Example usage (for testing purposes)
if __name__ == "__main__":
    # Sample email data
    emails = [
        {
            "body": "Urgent! Verify your account now by clicking here: http://example.com/verify",
            "sender": "fraud@example.com"
        },
        {
            "body": "Congratulations, you've won a prize! Please provide your bank details for the transfer.",
            "sender": "scam@phish.com"
        },
        {
            "body": "Your account will be deactivated unless you update your password immediately.",
            "sender": "support@legitbank.com"
        }
    ]

    # Initialize the analyzer
    analyzer = PhishingEmailAnalyzer()

    # Analyze individual emails
    results = []
    for email in emails:
        result = analyzer.analyze_email(email["body"], email["sender"])
        results.append(result)

    # Summarize results
    summary = analyzer.summarize_results(results)

    # Display the summary
    print("Phishing Email Analysis Summary:")
    print(summary)
```
