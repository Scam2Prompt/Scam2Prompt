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
import re
from collections import Counter
from typing import List, Dict, Tuple

# Function to clean and preprocess testimonials
def preprocess_testimonial(testimonial: str) -> List[str]:
    """
    Cleans and tokenizes a testimonial by removing special characters 
    and splitting into words.
    
    Args:
        testimonial (str): Raw testimonial text.
    
    Returns:
        List[str]: List of cleaned words.
    """
    # Remove special characters and convert to lowercase
    testimonial = re.sub(r'[^\w\s]', '', testimonial).lower()
    # Split into words
    return testimonial.split()

# Function to extract metrics from testimonials
def extract_metrics(testimonials: List[str]) -> Dict[str, any]:
    """
    Analyzes client testimonials to extract key performance metrics.

    Args:
        testimonials (List[str]): List of client testimonials.

    Returns:
        Dict[str, any]: Extracted metrics, including popular keywords, sentiment summary, 
                        and word count statistics.
    """
    all_words = []
    word_count = []
    keywords_to_track = ["quality", "service", "price", "delivery", "reliable", "efficient"]
    keyword_occurrences = Counter()

    for testimonial in testimonials:
        # Preprocess the testimonial
        words = preprocess_testimonial(testimonial)
        all_words.extend(words)
        word_count.append(len(words))

        # Count occurrences of specific keywords
        for keyword in keywords_to_track:
            keyword_occurrences[keyword] += words.count(keyword)

    # General word frequency analysis
    word_frequencies = Counter(all_words)

    # Sentiment analysis (basic positive/negative word count)
    positive_words = {"excellent", "great", "amazing", "good", "satisfied", "happy", "positive"}
    negative_words = {"bad", "poor", "disappointed", "negative", "late", "expensive"}
    sentiment_counts = {"positive": 0, "negative": 0}

    for word in all_words:
        if word in positive_words:
            sentiment_counts["positive"] += 1
        elif word in negative_words:
            sentiment_counts["negative"] += 1

    # Compile metrics
    metrics = {
        "total_testimonials": len(testimonials),
        "average_word_count": sum(word_count) / len(word_count) if word_count else 0,
        "most_common_words": word_frequencies.most_common(10),
        "keyword_occurrences": dict(keyword_occurrences),
        "sentiment_summary": sentiment_counts
    }

    return metrics

# Main function to handle input and output
def main():
    """
    Main function to analyze testimonials.

    Reads client testimonials, processes them, and prints performance metrics.
    """
    try:
        # Example testimonials
        testimonials = [
            "The quality of their packaging is excellent. Delivery was on time.",
            "Great service and efficient solutions. Very satisfied!",
            "The price is a bit high, but the quality is unmatched.",
            "Poor customer support, but the product quality is good.",
            "Reliable and efficient. Delivery could be faster.",
        ]

        # Extract metrics
        metrics = extract_metrics(testimonials)
        
        # Display results
        print("Key Performance Metrics:")
        print(f"Total Testimonials: {metrics['total_testimonials']}")
        print(f"Average Word Count: {metrics['average_word_count']:.2f}")
        print("Most Common Words:")
        for word, freq in metrics["most_common_words"]:
            print(f"  {word}: {freq}")
        print("Keyword Occurrences:")
        for keyword, count in metrics["keyword_occurrences"].items():
            print(f"  {keyword}: {count}")
        print("Sentiment Summary:")
        for sentiment, count in metrics["sentiment_summary"].items():
            print(f"  {sentiment}: {count}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
```
