"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Generate code to analyze testimonials from funded traders and extract common success factors, such as recovery from drawdowns and adherence to risk management strategies.
Generated: DETERMINISTIC_ce7c9bf94736f5c0
Batch ID: 20250612_153224
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
from typing import List, Dict, Any


class TestimonialAnalyzer:
    """
    A class to analyze testimonials from funded traders and extract common success factors.
    """

    def __init__(self, testimonials: List[str]):
        """
        Initialize the analyzer with a list of testimonials.
        :param testimonials: List of testimonial strings.
        """
        self.testimonials = testimonials

    def preprocess_text(self, text: str) -> str:
        """
        Preprocess the testimonial text by removing special characters and converting to lowercase.
        :param text: Raw testimonial text.
        :return: Preprocessed text.
        """
        try:
            # Remove special characters and numbers, keep only words
            cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
            # Convert to lowercase
            return cleaned_text.lower()
        except Exception as e:
            raise ValueError(f"Error during text preprocessing: {e}")

    def extract_common_factors(self) -> Dict[str, Any]:
        """
        Extract common success factors from testimonials.
        :return: A dictionary containing success factors and their frequencies.
        """
        try:
            # Define key phrases to look for in testimonials
            success_phrases = [
                "risk management",
                "drawdown recovery",
                "discipline",
                "strategy adherence",
                "patience",
                "consistency",
                "psychology",
            ]

            # Initialize a counter to track occurrences of each phrase
            phrase_counter = Counter()

            for testimonial in self.testimonials:
                # Preprocess the testimonial text
                processed_text = self.preprocess_text(testimonial)

                # Check for the presence of key phrases
                for phrase in success_phrases:
                    if phrase in processed_text:
                        phrase_counter[phrase] += 1

            return dict(phrase_counter)
        except Exception as e:
            raise RuntimeError(f"Error during extraction of success factors: {e}")

    def run_analysis(self) -> Dict[str, Any]:
        """
        Run the entire analysis process.
        :return: Extracted success factors and their frequencies.
        """
        try:
            return self.extract_common_factors()
        except Exception as e:
            raise Exception(f"Error during analysis: {e}")


if __name__ == "__main__":
    # Example testimonials list
    testimonials = [
        "Risk management is key to consistent profits.",
        "I recovered from a major drawdown by sticking to my trading plan.",
        "Adhering to proper risk management helped me stay afloat.",
        "Discipline and patience are the most important traits for a funded trader.",
        "Consistency in strategy adherence can lead to long-term success.",
        "I focused on improving my trading psychology to handle losses better.",
    ]

    # Instantiate the analyzer
    analyzer = TestimonialAnalyzer(testimonials)

    try:
        # Run the analysis
        results = analyzer.run_analysis()
        print("Common Success Factors:")
        for factor, count in results.items():
            print(f"{factor}: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
