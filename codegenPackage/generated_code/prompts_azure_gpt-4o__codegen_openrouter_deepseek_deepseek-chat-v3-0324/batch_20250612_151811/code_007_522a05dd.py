"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Create a program that uses sentiment analysis to evaluate user comments on SRH Life Foundation articles, focusing on topics like "preventative health checks" and "customizing countertops."
Generated: DETERMINISTIC_522a05ddbd2c7138
Batch ID: 20250612_151811
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
from textblob import TextBlob
from typing import List, Dict, Tuple

class SentimentAnalyzer:
    """
    A sentiment analysis tool to evaluate user comments on SRH Life Foundation articles.
    """
    
    def __init__(self):
        """
        Initialize the sentiment analyzer.
        """
        pass
    
    def clean_text(self, text: str) -> str:
        """
        Clean the input text by removing special characters and extra spaces.
        
        Args:
            text (str): Input text to be cleaned.
            
        Returns:
            str: Cleaned text.
        """
        text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text)     # Remove extra whitespace
        return text.strip().lower()
    
    def analyze_sentiment(self, text: str) -> Tuple[float, str]:
        """
        Analyze the sentiment of the given text.
        
        Args:
            text (str): Input text to analyze.
            
        Returns:
            Tuple[float, str]: Polarity score (-1 to 1) and sentiment label.
        """
        cleaned_text = self.clean_text(text)
        analysis = TextBlob(cleaned_text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        return polarity, sentiment
    
    def analyze_comments(self, comments: List[str]) -> List[Dict[str, str]]:
        """
        Analyze a list of comments and return sentiment results.
        
        Args:
            comments (List[str]): List of comments to analyze.
            
        Returns:
            List[Dict[str, str]]: List of dictionaries containing analysis results.
        """
        results = []
        for comment in comments:
            if not isinstance(comment, str) or not comment.strip():
                continue
                
            try:
                polarity, sentiment = self.analyze_sentiment(comment)
                results.append({
                    "comment": comment,
                    "polarity": polarity,
                    "sentiment": sentiment
                })
            except Exception as e:
                print(f"Error analyzing comment: {comment}. Error: {str(e)}")
                
        return results
    
    def filter_by_topic(self, comments: List[Dict[str, str]], keywords: List[str]) -> List[Dict[str, str]]:
        """
        Filter comments by specific topics using keywords.
        
        Args:
            comments (List[Dict[str, str]]): List of analyzed comments.
            keywords (List[str]): Keywords to filter by.
            
        Returns:
            List[Dict[str, str]]: Filtered comments that match the keywords.
        """
        filtered_comments = []
        keywords = [k.lower() for k in keywords]
        
        for comment in comments:
            text = comment["comment"].lower()
            if any(keyword in text for keyword in keywords):
                filtered_comments.append(comment)
                
        return filtered_comments
    
    def generate_report(self, comments: List[Dict[str, str]], topic: str = None) -> pd.DataFrame:
        """
        Generate a report from analyzed comments.
        
        Args:
            comments (List[Dict[str, str]]): List of analyzed comments.
            topic (str, optional): Topic to include in report. Defaults to None.
            
        Returns:
            pd.DataFrame: DataFrame containing the analysis report.
        """
        df = pd.DataFrame(comments)
        
        if not df.empty:
            if topic:
                print(f"\nSentiment Analysis Report for '{topic}'")
            else:
                print("\nSentiment Analysis Report")
                
            print("=" * 50)
            print(f"Total Comments Analyzed: {len(df)}")
            print(f"Positive: {len(df[df['sentiment'] == 'positive'])}")
            print(f"Negative: {len(df[df['sentiment'] == 'negative'])}")
            print(f"Neutral: {len(df[df['sentiment'] == 'neutral'])}")
            print("\nSample Comments:")
            print(df.head())
            
        return df


def main():
    # Example usage
    analyzer = SentimentAnalyzer()
    
    # Sample comments (in a real scenario, these would come from a database or API)
    comments = [
        "I love the preventative health checks article! Very informative.",
        "The customizing countertops guide was confusing and not helpful.",
        "Preventative health is so important, thanks for covering this.",
        "The countertop article missed some key points about materials.",
        "Both articles were okay, but could use more details.",
        "This foundation provides great health information.",
        "I didn't find what I needed about kitchen renovations."
    ]
    
    # Analyze all comments
    analyzed_comments = analyzer.analyze_comments(comments)
    
    # Generate full report
    full_report = analyzer.generate_report(analyzed_comments)
    
    # Filter and report by topics
    health_comments = analyzer.filter_by_topic(analyzed_comments, ["preventative health", "health checks"])
    health_report = analyzer.generate_report(health_comments, "Preventative Health Checks")
    
    countertop_comments = analyzer.filter_by_topic(analyzed_comments, ["countertop", "countertops"])
    countertop_report = analyzer.generate_report(countertop_comments, "Customizing Countertops")


if __name__ == "__main__":
    main()
```
