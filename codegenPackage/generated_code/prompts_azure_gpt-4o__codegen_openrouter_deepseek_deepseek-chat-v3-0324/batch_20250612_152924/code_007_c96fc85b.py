"""
Generated Code Metadata:
========================
Original URL: https://beta.metis-lab.com
Prompt: Create a script to analyze the themes of roundtable discussions, such as "La sobriété" or "L’accélération muséale," using the content structure provided by Mêtis Lab.
Generated: DETERMINISTIC_c96fc85bf39da299
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import re
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

class DiscussionAnalyzer:
    """
    A class to analyze themes in roundtable discussions based on content structure.
    """
    
    def __init__(self, language: str = 'french'):
        """
        Initialize the analyzer with language-specific settings.
        
        Args:
            language (str): Language of the discussion content ('french' or 'english')
        """
        self.language = language.lower()
        self.stop_words = set(stopwords.words(self.language))
        self.lemmatizer = WordNetLemmatizer()
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        
    def preprocess_text(self, text: str) -> List[str]:
        """
        Preprocess text by tokenizing, removing stopwords, and lemmatizing.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            List[str]: List of processed tokens
        """
        # Tokenize and lowercase
        tokens = word_tokenize(text.lower(), language=self.language)
        
        # Remove stopwords and non-alphabetic tokens
        tokens = [
            self.lemmatizer.lemmatize(token) 
            for token in tokens 
            if token.isalpha() and token not in self.stop_words
        ]
        
        return tokens
    
    def extract_themes(self, discussions: List[Dict], num_themes: int = 5) -> Dict[str, List[Tuple[str, int]]]:
        """
        Extract and rank themes from discussion content.
        
        Args:
            discussions (List[Dict]): List of discussion dictionaries with 'content' field
            num_themes (int): Number of top themes to return per discussion
            
        Returns:
            Dict[str, List[Tuple[str, int]]]: Dictionary mapping discussion titles to ranked themes
        """
        theme_results = {}
        
        for discussion in discussions:
            try:
                title = discussion.get('title', 'Untitled')
                content = discussion.get('content', '')
                
                if not content:
                    continue
                
                # Preprocess and analyze content
                tokens = self.preprocess_text(content)
                freq_dist = FreqDist(tokens)
                
                # Get most common themes
                themes = freq_dist.most_common(num_themes)
                theme_results[title] = themes
                
            except Exception as e:
                print(f"Error processing discussion '{title}': {str(e)}")
                continue
                
        return theme_results
    
    def analyze_sentiment(self, discussions: List[Dict]) -> Dict[str, Dict[str, float]]:
        """
        Perform sentiment analysis on discussion content.
        
        Args:
            discussions (List[Dict]): List of discussion dictionaries with 'content' field
            
        Returns:
            Dict[str, Dict[str, float]]: Dictionary mapping discussion titles to sentiment scores
        """
        sentiment_results = {}
        
        for discussion in discussions:
            try:
                title = discussion.get('title', 'Untitled')
                content = discussion.get('content', '')
                
                if not content:
                    continue
                
                # Analyze sentiment
                sentiment = self.sentiment_analyzer.polarity_scores(content)
                sentiment_results[title] = sentiment
                
            except Exception as e:
                print(f"Error analyzing sentiment for '{title}': {str(e)}")
                continue
                
        return sentiment_results
    
    def analyze_discussions(self, discussions: List[Dict]) -> Dict:
        """
        Comprehensive analysis of discussions including themes and sentiment.
        
        Args:
            discussions (List[Dict]): List of discussion dictionaries
            
        Returns:
            Dict: Analysis results containing themes and sentiment
        """
        if not discussions:
            raise ValueError("No discussions provided for analysis")
            
        return {
            'themes': self.extract_themes(discussions),
            'sentiment': self.analyze_sentiment(discussions)
        }

def load_discussions_from_json(file_path: str) -> List[Dict]:
    """
    Load discussions from a JSON file.
    
    Args:
        file_path (str): Path to JSON file
        
    Returns:
        List[Dict]: List of discussion dictionaries
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error loading discussions from {file_path}: {str(e)}")

def save_analysis_results(results: Dict, output_path: str) -> None:
    """
    Save analysis results to a JSON file.
    
    Args:
        results (Dict): Analysis results to save
        output_path (str): Path to output JSON file
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
    except Exception as e:
        raise ValueError(f"Error saving results to {output_path}: {str(e)}")

def main():
    """
    Main execution function for standalone script usage.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze themes in roundtable discussions')
    parser.add_argument('input_file', help='Path to JSON file containing discussions')
    parser.add_argument('output_file', help='Path to save analysis results')
    parser.add_argument('--language', default='french', 
                       choices=['french', 'english'],
                       help='Language of the discussion content')
    
    args = parser.parse_args()
    
    try:
        # Load discussions
        discussions = load_discussions_from_json(args.input_file)
        
        # Analyze discussions
        analyzer = DiscussionAnalyzer(language=args.language)
        results = analyzer.analyze_discussions(discussions)
        
        # Save results
        save_analysis_results(results, args.output_file)
        
        print(f"Analysis completed successfully. Results saved to {args.output_file}")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        return 1
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
```
