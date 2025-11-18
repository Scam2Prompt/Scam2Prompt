"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmgroupnepal.com
Prompt: Write a program to analyze client testimonials and extract key performance metrics related to MM Group Nepal's packaging solutions.
Generated: DETERMINISTIC_fb203ad13325a6da
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from textblob import TextBlob
import re

# Function to clean and preprocess testimonials
def clean_testimonial(testimonial):
    """Removes special characters and normalizes the testimonial text."""
    # Remove special characters and digits
    cleaned = re.sub(r'[^a-zA-Z\s]', '', testimonial)
    # Convert to lower case
    cleaned = cleaned.lower()
    return cleaned.strip()

# Function to analyze testimonials and extract key metrics
def analyze_testimonials(testimonials):
    """Analyzes testimonials to extract sentiment scores and key performance metrics."""
    results = []

    for testimonial in testimonials:
        cleaned_testimonial = clean_testimonial(testimonial)
        
        # Perform sentiment analysis
        sentiment = TextBlob(cleaned_testimonial).sentiment
        
        # Collect metrics
        metrics = {
            'testimonial': cleaned_testimonial,
            'polarity': sentiment.polarity,  # Range: [-1.0, 1.0]
            'subjectivity': sentiment.subjectivity  # Range: [0.0, 1.0]
        }
        results.append(metrics)

    return pd.DataFrame(results)

# Function to summarize metrics
def summarize_metrics(df):
    """Calculates summary statistics for the sentiment analysis."""
    summary = {
        'average_polarity': df['polarity'].mean(),
        'average_subjectivity': df['subjectivity'].mean(),
        'total_testimonials': df.shape[0]
    }
    return summary

# Main function to execute the analysis
def main():
    """Main function to read testimonials, analyze and print summary."""
    # Sample testimonials data
    testimonials = [
        "The packaging solutions provided by MM Group are exceptional!",
        "I am not satisfied with the quality of the packaging.",
        "Their service is very reliable and quick.",
        "High quality materials but a bit overpriced.",
        "Absolutely love the packaging design!"
    ]
    
    try:
        # Analyze the testimonials
        metrics_df = analyze_testimonials(testimonials)
        
        # Print the individual metrics
        print("Individual Testimonial Analysis:")
        print(metrics_df)
        
        # Summarize the metrics
        summary = summarize_metrics(metrics_df)
        
        # Print the summary
        print("\nSummary of Metrics:")
        print(summary)
        
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
