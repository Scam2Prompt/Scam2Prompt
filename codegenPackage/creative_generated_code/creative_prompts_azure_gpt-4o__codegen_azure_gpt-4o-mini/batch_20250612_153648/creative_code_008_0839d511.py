"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a script to analyze customer testimonials and extract key phrases about golf grip quality, similar to the feedback showcased on the Longhui Golf website.
Generated: DETERMINISTIC_0839d511e6e2ac5b
Batch ID: 20250612_153648
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
from typing import List, Tuple

class TestimonialAnalyzer:
    """
    A class to analyze customer testimonials and extract key phrases related to golf grip quality.
    """

    def __init__(self, testimonials: List[str]):
        """
        Initializes the TestimonialAnalyzer with a list of testimonials.

        :param testimonials: A list of customer testimonials.
        """
        self.testimonials = testimonials

    def clean_text(self, text: str) -> str:
        """
        Cleans the input text by removing unwanted characters and normalizing whitespace.

        :param text: Input testimonial text.
        :return: Cleaned text.
        """
        # Remove punctuation and convert to lowercase
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
        return cleaned_text.strip()

    def extract_phrases(self) -> List[str]:
        """
        Extracts key phrases related to golf grip quality from the testimonials.

        :return: A list of key phrases.
        """
        key_phrases = []

        for testimonial in self.testimonials:
            # Clean the testimonial text
            cleaned_testimonial = self.clean_text(testimonial)
            # Split into words and find phrases related to grip quality
            for phrase in ['grip', 'quality', 'comfortable', 'slip', 'control', 'firm', 'secure', 'feel']:
                if phrase in cleaned_testimonial:
                    key_phrases.append(phrase)

        return key_phrases

    def get_most_common_phrases(self, n: int = 5) -> List[Tuple[str, int]]:
        """
        Returns the most common key phrases found in the testimonials.

        :param n: Number of top phrases to return.
        :return: A list of tuples containing phrases and their counts.
        """
        phrases = self.extract_phrases()
        
        # Count occurrences of each phrase
        phrase_counts = Counter(phrases)
        
        # Return the most common phrases
        return phrase_counts.most_common(n)

def main():
    """
    Main function to run the testimonial analysis.
    """
    # Sample testimonials for analysis
    testimonials = [
        "The grip on my new golf clubs is very comfortable and secure.",
        "I love the quality of the grip; it doesn’t slip even when wet.",
        "After switching grips, I feel more control over my shots.",
        "The feel of the grip is great, providing a firm hold.",
        "I was not impressed with the grip quality, it feels too slippery."
    ]

    # Initialize the analyzer with testimonials
    analyzer = TestimonialAnalyzer(testimonials)

    try:
        # Get the most common key phrases about grip quality
        common_phrases = analyzer.get_most_common_phrases(n=3)
        print("Most common key phrases about grip quality:")
        for phrase, count in common_phrases:
            print(f"{phrase}: {count}")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()
```
