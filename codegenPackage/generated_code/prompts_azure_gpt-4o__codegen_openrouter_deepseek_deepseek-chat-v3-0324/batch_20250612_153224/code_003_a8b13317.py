"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Create a Python script to analyze text-based responses from children participating in workshops on civic awareness, as described in the Fundación Patricio Aylwin's initiative.
Generated: DETERMINISTIC_a8b133179993bcaa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict
from typing import Dict, List, Tuple
import string
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='civic_awareness_analysis.log'
)

class CivicAwarenessAnalyzer:
    """
    A class to analyze text-based responses from children about civic awareness.
    """

    def __init__(self, positive_keywords: List[str], negative_keywords: List[str], neutral_keywords: List[str]):
        """
        Initialize the analyzer with keyword lists for sentiment analysis.
        
        Args:
            positive_keywords: List of positive sentiment keywords
            negative_keywords: List of negative sentiment keywords
            neutral_keywords: List of neutral sentiment keywords
        """
        self.positive_keywords = set(positive_keywords)
        self.negative_keywords = set(negative_keywords)
        self.neutral_keywords = set(neutral_keywords)
        self.stop_words = set([
            'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 
            'from', 'by', 'in', 'of', 'with', 'as', 'is', 'was', 'were', 'be', 'been'
        ])

    def clean_text(self, text: str) -> str:
        """
        Clean and preprocess text by removing punctuation, numbers, and converting to lowercase.
        
        Args:
            text: Input text to clean
            
        Returns:
            Cleaned text
        """
        try:
            # Remove punctuation and numbers
            text = text.translate(str.maketrans('', '', string.punctuation + string.digits))
            # Convert to lowercase
            text = text.lower()
            return text
        except Exception as e:
            logging.error(f"Error cleaning text: {e}")
            raise

    def tokenize_text(self, text: str) -> List[str]:
        """
        Tokenize text into words, removing stop words.
        
        Args:
            text: Input text to tokenize
            
        Returns:
            List of tokens
        """
        try:
            tokens = text.split()
            # Remove stop words
            tokens = [word for word in tokens if word not in self.stop_words]
            return tokens
        except Exception as e:
            logging.error(f"Error tokenizing text: {e}")
            raise

    def analyze_sentiment(self, text: str) -> Dict[str, int]:
        """
        Analyze sentiment of text based on keyword matching.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with sentiment counts
        """
        try:
            cleaned_text = self.clean_text(text)
            tokens = self.tokenize_text(cleaned_text)
            
            sentiment_counts = {
                'positive': 0,
                'negative': 0,
                'neutral': 0,
                'total': len(tokens)
            }
            
            for word in tokens:
                if word in self.positive_keywords:
                    sentiment_counts['positive'] += 1
                elif word in self.negative_keywords:
                    sentiment_counts['negative'] += 1
                elif word in self.neutral_keywords:
                    sentiment_counts['neutral'] += 1
            
            return sentiment_counts
        except Exception as e:
            logging.error(f"Error analyzing sentiment: {e}")
            raise

    def analyze_responses(self, responses: List[str]) -> Dict[str, Dict]:
        """
        Analyze multiple text responses.
        
        Args:
            responses: List of text responses
            
        Returns:
            Dictionary with analysis results for each response and aggregates
        """
        try:
            results = {
                'individual_responses': [],
                'aggregate': {
                    'total_responses': len(responses),
                    'total_positive': 0,
                    'total_negative': 0,
                    'total_neutral': 0,
                    'total_words': 0
                }
            }
            
            for response in responses:
                analysis = self.analyze_sentiment(response)
                results['individual_responses'].append({
                    'response': response,
                    'analysis': analysis
                })
                
                # Update aggregates
                results['aggregate']['total_positive'] += analysis['positive']
                results['aggregate']['total_negative'] += analysis['negative']
                results['aggregate']['total_neutral'] += analysis['neutral']
                results['aggregate']['total_words'] += analysis['total']
            
            return results
        except Exception as e:
            logging.error(f"Error analyzing responses: {e}")
            raise

    def get_most_common_words(self, responses: List[str], top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Get most common words across all responses.
        
        Args:
            responses: List of text responses
            top_n: Number of top words to return
            
        Returns:
            List of tuples (word, count) sorted by count descending
        """
        try:
            word_counts = defaultdict(int)
            
            for response in responses:
                cleaned_text = self.clean_text(response)
                tokens = self.tokenize_text(cleaned_text)
                
                for word in tokens:
                    word_counts[word] += 1
            
            # Sort by count descending and return top_n
            sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
            return sorted_words[:top_n]
        except Exception as e:
            logging.error(f"Error getting common words: {e}")
            raise

def load_keywords(file_path: str) -> Dict[str, List[str]]:
    """
    Load keywords from a JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Dictionary with keyword lists
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading keywords file: {e}")
        raise

def save_results(results: Dict, file_path: str) -> None:
    """
    Save analysis results to a JSON file.
    
    Args:
        results: Analysis results dictionary
        file_path: Path to save results
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        logging.info(f"Results saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving results: {e}")
        raise

def main():
    try:
        # Load keywords (example file structure: {"positive": [...], "negative": [...], "neutral": [...]})
        keywords = load_keywords('keywords.json')
        
        # Initialize analyzer
        analyzer = CivicAwarenessAnalyzer(
            positive_keywords=keywords['positive'],
            negative_keywords=keywords['negative'],
            neutral_keywords=keywords['neutral']
        )
        
        # Example responses (in practice, these would be loaded from a file or database)
        responses = [
            "I love helping my community and learning about our rights!",
            "Sometimes I feel like my voice doesn't matter in big decisions.",
            "Democracy is important for everyone to participate.",
            "I don't understand why we need to vote when we're young."
        ]
        
        # Analyze responses
        analysis_results = analyzer.analyze_responses(responses)
        
        # Get most common words
        common_words = analyzer.get_most_common_words(responses)
        analysis_results['common_words'] = common_words
        
        # Save results
        save_results(analysis_results, 'analysis_results.json')
        
        logging.info("Analysis completed successfully")
        
    except Exception as e:
        logging.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()
```
