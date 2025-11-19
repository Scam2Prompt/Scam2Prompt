"""
Generated Code Metadata:
========================
Original URL: https://1minutedog.com
Prompt: Develop a Python script that uses natural language processing (NLP) to analyze user feedback on dog training methods, categorizing responses based on themes like "positive reinforcement" and "time efficiency," as highlighted by the "1 Minute Dog Training" method.
Generated: DETERMINISTIC_ddaca9e68057fb59
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import pandas as pd
from collections import defaultdict
from typing import List, Dict, Tuple
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Doc
from spacy.matcher import PhraseMatcher

# Load the English language model for NLP processing
nlp = spacy.load("en_core_web_sm")

class FeedbackAnalyzer:
    """
    A class to analyze and categorize dog training feedback using NLP techniques.
    """
    
    def __init__(self):
        """
        Initialize the analyzer with predefined categories and their keywords.
        """
        self.categories = {
            "positive_reinforcement": [
                "reward", "treat", "praise", "positive", "encouragement",
                "happy", "motivation", "clicker", "affirmation"
            ],
            "time_efficiency": [
                "quick", "fast", "efficient", "minute", "speedy",
                "time-saving", "rapid", "1 minute", "instant"
            ],
            "effectiveness": [
                "work", "effective", "result", "improve", "success",
                "change", "better", "progress", "transform"
            ],
            "difficulty": [
                "hard", "difficult", "challenge", "struggle", "complex",
                "confusing", "frustrating", "tough", "problem"
            ]
        }
        
        # Create phrase matchers for each category
        self.matchers = {}
        for category, keywords in self.categories.items():
            matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
            patterns = [nlp.make_doc(text) for text in keywords]
            matcher.add(category, patterns)
            self.matchers[category] = matcher
    
    def preprocess_text(self, text: str) -> Doc:
        """
        Preprocess the input text by cleaning and tokenizing.
        
        Args:
            text: The raw input text to process
            
        Returns:
            A spaCy Doc object containing processed tokens
        """
        # Remove special characters and extra whitespace
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = ' '.join(text.split())
        
        # Process with spaCy pipeline
        doc = nlp(text.lower())
        
        # Remove stop words and punctuation
        tokens = [token for token in doc if not token.is_stop and not token.is_punct]
        
        # Reconstruct doc without stop words
        return nlp(' '.join([token.text for token in tokens]))
    
    def categorize_feedback(self, feedback: str) -> Dict[str, int]:
        """
        Categorize the given feedback text into predefined categories.
        
        Args:
            feedback: The feedback text to analyze
            
        Returns:
            A dictionary with category counts
        """
        doc = self.preprocess_text(feedback)
        category_counts = defaultdict(int)
        
        for category, matcher in self.matchers.items():
            matches = matcher(doc)
            category_counts[category] = len(matches)
        
        return dict(category_counts)
    
    def analyze_feedback_list(self, feedback_list: List[str]) -> pd.DataFrame:
        """
        Analyze a list of feedback texts and return categorized results.
        
        Args:
            feedback_list: List of feedback strings to analyze
            
        Returns:
            A pandas DataFrame with analysis results
        """
        results = []
        
        for feedback in feedback_list:
            if not isinstance(feedback, str) or not feedback.strip():
                continue
                
            categories = self.categorize_feedback(feedback)
            results.append({
                "feedback": feedback,
                **categories
            })
        
        return pd.DataFrame(results)
    
    def get_summary_statistics(self, df: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate summary statistics for the analyzed feedback.
        
        Args:
            df: DataFrame containing categorized feedback
            
        Returns:
            Dictionary with percentage statistics for each category
        """
        if df.empty:
            return {}
            
        total = len(df)
        stats = {}
        
        for category in self.categories.keys():
            if category in df.columns:
                count = df[category].sum()
                stats[category] = (count / total) * 100
                
        return stats


def main():
    """
    Main function to demonstrate the feedback analyzer.
    """
    # Example feedback data
    example_feedback = [
        "The 1 minute training method worked wonders with my dog! Quick results with positive reinforcement.",
        "I found it difficult to implement at first, but after seeing the fast progress, I'm convinced.",
        "Using treats as rewards made the training efficient and enjoyable for both of us.",
        "Not sure about the time efficiency claims. My dog took longer than a minute to learn.",
        "The positive approach with clicker training was effective and created a happy environment.",
        "Too complex for my puppy. We struggled with the rapid pace."
    ]
    
    analyzer = FeedbackAnalyzer()
    
    # Analyze the feedback
    results_df = analyzer.analyze_feedback_list(example_feedback)
    
    # Print results
    print("Categorized Feedback:")
    print(results_df)
    
    # Print summary statistics
    stats = analyzer.get_summary_statistics(results_df)
    print("\nSummary Statistics (% of feedback mentioning each category):")
    for category, percentage in stats.items():
        print(f"{category.replace('_', ' ').title()}: {percentage:.1f}%")


if __name__ == "__main__":
    main()
```
