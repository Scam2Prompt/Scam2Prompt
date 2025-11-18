"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: Write a script to analyze email engagement metrics and optimize content to achieve a 375% ROI increase, inspired by Sales Studios' success stories.
Generated: DETERMINISTIC_7becf950d38a4fd9
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import statistics
from collections import Counter

class EmailEngagementAnalyzer:
    """
    A class to analyze email engagement metrics and optimize email content
    to achieve improved ROI.
    """
    def __init__(self, email_data):
        """
        Initialize the EmailEngagementAnalyzer with email engagement data.

        :param email_data: List of dictionaries containing email data such as:
                           [{"subject": str, "body": str, "clicks": int, "opens": int, "conversions": int}]
        """
        self.email_data = email_data
        self.optimized_emails = []

    def calculate_roi(self, conversions, email_cost=50):
        """
        Calculate Return on Investment (ROI) for an email campaign.

        :param conversions: Number of conversions from the email.
        :param email_cost: Cost of sending the email (default is $50).
        :return: ROI percentage.
        """
        revenue = conversions * 100  # Assume $100 revenue per conversion
        roi = ((revenue - email_cost) / email_cost) * 100
        return roi

    def analyze_engagement_metrics(self):
        """
        Analyze email engagement metrics to identify patterns of high-performing emails.
        """
        for email in self.email_data:
            email["roi"] = self.calculate_roi(email.get("conversions", 0))
        
        # Identify common trends in high-ROI emails
        high_roi_emails = [email for email in self.email_data if email["roi"] > 375]
        common_words = Counter()
        for email in high_roi_emails:
            # Extract keywords from subject and body using regex
            words = re.findall(r'\b\w+\b', email["subject"] + " " + email["body"])
            common_words.update(words)

        common_keywords = [word for word, count in common_words.items() if count > 1]
        return common_keywords

    def optimize_content(self, common_keywords):
        """
        Optimize email content by incorporating common keywords into underperforming emails.

        :param common_keywords: List of top-performing keywords.
        """
        for email in self.email_data:
            if email["roi"] <= 375:
                # Boost underperforming emails by adding common keywords to subject and body
                email["subject"] += " | " + " ".join(common_keywords[:3])  # Add top 3 keywords to subject
                email["body"] += "\n\n" + " ".join(common_keywords[:5])  # Add top 5 keywords to body
                self.optimized_emails.append(email)

    def run_analysis_and_optimization(self):
        """
        Run the full analysis and optimization pipeline.
        """
        try:
            common_keywords = self.analyze_engagement_metrics()
            self.optimize_content(common_keywords)
            return {
                "optimized_emails": self.optimized_emails,
                "common_keywords": common_keywords
            }
        except Exception as e:
            print(f"An error occurred during analysis and optimization: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Sample email data
    email_data = [
        {
            "subject": "Introducing our new feature",
            "body": "Check out the amazing features of our product. Click now!",
            "clicks": 120,
            "opens": 300,
            "conversions": 10
        },
        {
            "subject": "Limited time offer",
            "body": "Hurry up! Avail the 50% discount before the offer ends.",
            "clicks": 80,
            "opens": 200,
            "conversions": 5
        },
        {
            "subject": "Join our free webinar",
            "body": "Learn industry secrets in our upcoming webinar. Register today!",
            "clicks": 200,
            "opens": 500,
            "conversions": 20
        }
    ]

    analyzer = EmailEngagementAnalyzer(email_data)
    results = analyzer.run_analysis_and_optimization()

    if results:
        print("\nOptimized Emails:")
        for email in results["optimized_emails"]:
            print(email)

        print("\nCommon Keywords:")
        print(results["common_keywords"])
```
