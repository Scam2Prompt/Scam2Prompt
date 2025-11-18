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
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import sys

# Ensure necessary NLTK resources are downloaded
try:
    nltk.download('vader_lexicon', quiet=True)
except Exception as e:
    sys.exit(f"Error downloading NLTK resources: {e}")

def analyze_customer_satisfaction(testimonials):
    """
    Analyze customer satisfaction based on sentiment analysis of testimonials.

    Args:
        testimonials (list): List of customer testimonial strings.

    Returns:
        dict: A dictionary containing sentiment analysis results.
    """
    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Dictionary to hold analysis results
    results = {
        "positive_count": 0,
        "negative_count": 0,
        "neutral_count": 0,
        "details": []  # Detailed sentiment scores for each testimonial
    }

    # Loop through testimonials and analyze sentiment
    for testimonial in testimonials:
        try:
            sentiment_score = sia.polarity_scores(testimonial)
            results["details"].append({
                "testimonial": testimonial,
                "sentiment_score": sentiment_score
            })
            # Classify testimonial sentiment
            if sentiment_score["compound"] >= 0.05:
                results["positive_count"] += 1
            elif sentiment_score["compound"] <= -0.05:
                results["negative_count"] += 1
            else:
                results["neutral_count"] += 1
        except Exception as e:
            results["details"].append({
                "testimonial": testimonial,
                "error": str(e)
            })

    return results


if __name__ == "__main__":
    # Example testimonials from Meezan Interior Solutions' site
    example_testimonials = [
        "Truly satisfied clients!",
        "Their attention to detail is commendable.",
        "I had an average experience.",
        "Very disappointing service quality.",
        "Excellent work! Highly recommend them."
    ]

    try:
        # Analyze testimonials
        satisfaction_results = analyze_customer_satisfaction(example_testimonials)

        # Print analysis results
        print("Customer Satisfaction Analysis Results:")
        print(f"Positive Testimonials: {satisfaction_results['positive_count']}")
        print(f"Negative Testimonials: {satisfaction_results['negative_count']}")
        print(f"Neutral Testimonials: {satisfaction_results['neutral_count']}")
        print("\nDetailed Testimonials Analysis:")
        for detail in satisfaction_results["details"]:
            print(detail)
    except Exception as main_error:
        sys.exit(f"An error occurred during sentiment analysis: {main_error}")
```
