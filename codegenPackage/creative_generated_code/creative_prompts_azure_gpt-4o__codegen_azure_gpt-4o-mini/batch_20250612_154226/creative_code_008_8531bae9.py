"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Generate Python code to analyze customer satisfaction data from testimonials, using examples like "Truly satisfied clients!" and "Their attention to detail is commendable," as highlighted on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_8531bae9d560aada
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
import pandas as pd

class CustomerSatisfactionAnalyzer:
    """
    A class to analyze customer satisfaction testimonials for sentiment and keyword extraction.
    """

    def __init__(self, testimonials):
        """
        Initializes the analyzer with a list of testimonials.

        :param testimonials: List of customer testimonials (strings).
        """
        if not isinstance(testimonials, list):
            raise ValueError("Testimonials should be provided as a list of strings.")
        self.testimonials = testimonials
        self.sentiment_scores = []
        self.keywords = []

    def analyze_sentiment(self):
        """
        Analyzes the sentiment of each testimonial using simple keyword matching.
        A positive sentiment is assigned to testimonials containing certain keywords.
        """
        positive_keywords = ["satisfied", "commendable", "excellent", "happy", "great", "love", "fantastic"]
        negative_keywords = ["disappointed", "poor", "bad", "hate", "worse"]

        for testimonial in self.testimonials:
            score = 0
            testimonial_lower = testimonial.lower()
            for word in positive_keywords:
                if word in testimonial_lower:
                    score += 1
            for word in negative_keywords:
                if word in testimonial_lower:
                    score -= 1
            self.sentiment_scores.append(score)

    def extract_keywords(self):
        """
        Extracts keywords from testimonials based on simple regex matching.
        This method identifies adjectives and emphasizes in testimonials.
        """
        keyword_pattern = re.compile(r'\b\w+(ful|able)\b|\b\w+(satisfied|commendable|excellent|great|fantastic|happy)\b', re.IGNORECASE)

        for testimonial in self.testimonials:
            found_keywords = keyword_pattern.findall(testimonial)
            self.keywords.extend([keyword[0] or keyword[1] for keyword in found_keywords])

    def generate_report(self):
        """
        Generates a report of the sentiment analysis and keyword extraction.
        
        :return: A DataFrame summarizing the analysis results.
        """
        if not self.sentiment_scores or not self.keywords:
            raise ValueError("Sentiment analysis and keyword extraction must be performed before generating a report.")
        
        # Count keyword occurrences
        keyword_counts = Counter(self.keywords)
        
        # Create a DataFrame for reporting
        report_data = {
            'Testimonial': self.testimonials,
            'Sentiment Score': self.sentiment_scores,
        }
        report_df = pd.DataFrame(report_data)

        # Add keyword occurrences to the report DataFrame
        for keyword, count in keyword_counts.items():
            report_df[keyword] = report_df['Testimonial'].apply(lambda x: x.lower().count(keyword.lower()))

        return report_df

def main():
    testimonials = [
        "Truly satisfied clients!",
        "Their attention to detail is commendable.",
        "I am extremely happy with the service.",
        "Unfortunately, I was disappointed with the results.",
        "Excellent work and fantastic designs!",
        "I hate the outcome, it was worse than I expected.",
        "What a great experience!"
    ]

    try:
        analyzer = CustomerSatisfactionAnalyzer(testimonials)
        analyzer.analyze_sentiment()
        analyzer.extract_keywords()
        report = analyzer.generate_report()

        print(report)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
