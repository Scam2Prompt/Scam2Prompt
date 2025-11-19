"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Create a code snippet to analyze customer testimonials for a business training course and provide insights on course effectiveness.
Generated: DETERMINISTIC_1031a283372e14db
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from textblob import TextBlob
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestimonialAnalyzer:
    def __init__(self, testimonials):
        """
        Initialize the TestimonialAnalyzer with a list of testimonials.

        :param testimonials: List of customer testimonials (strings)
        """
        if not isinstance(testimonials, list):
            logging.error("Testimonials should be provided as a list.")
            raise ValueError("Testimonials should be a list of strings.")
        
        self.testimonials = testimonials
        self.analysis_results = []

    def analyze_sentiment(self):
        """
        Analyze the sentiment of each testimonial and store the results.
        """
        for testimonial in self.testimonials:
            try:
                analysis = TextBlob(testimonial)
                sentiment = analysis.sentiment
                self.analysis_results.append({
                    'testimonial': testimonial,
                    'polarity': sentiment.polarity,
                    'subjectivity': sentiment.subjectivity
                })
            except Exception as e:
                logging.error(f"Error analyzing testimonial: {testimonial}. Error: {e}")
                self.analysis_results.append({
                    'testimonial': testimonial,
                    'polarity': None,
                    'subjectivity': None,
                    'error': str(e)
                })

    def generate_insights(self):
        """
        Generate insights based on the analyzed testimonials.

        :return: A dictionary containing average polarity and subjectivity
        """
        if not self.analysis_results:
            logging.warning("No analysis results available. Please run analyze_sentiment() first.")
            return {}

        # Convert results to DataFrame for easier analysis
        df = pd.DataFrame(self.analysis_results)

        # Calculate average polarity and subjectivity
        average_polarity = df['polarity'].mean()
        average_subjectivity = df['subjectivity'].mean()

        insights = {
            'average_polarity': average_polarity,
            'average_subjectivity': average_subjectivity,
            'total_testimonials': len(df),
            'positive_feedback_count': (df['polarity'] > 0).sum(),
            'negative_feedback_count': (df['polarity'] < 0).sum(),
            'neutral_feedback_count': (df['polarity'] == 0).sum()
        }

        return insights

# Example usage
if __name__ == "__main__":
    testimonials = [
        "This course was fantastic! I learned so much.",
        "I didn't find the course helpful at all.",
        "The instructor was great, but the content was lacking.",
        "Absolutely loved it! Highly recommend to everyone."
    ]

    try:
        analyzer = TestimonialAnalyzer(testimonials)
        analyzer.analyze_sentiment()
        insights = analyzer.generate_insights()
        print(insights)
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
