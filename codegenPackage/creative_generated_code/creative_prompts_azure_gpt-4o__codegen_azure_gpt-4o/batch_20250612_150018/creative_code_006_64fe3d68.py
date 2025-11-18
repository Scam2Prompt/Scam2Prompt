"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ropesjames.com
Prompt: Recommend a library or API for analyzing client success stories, such as Megan’s or Logan’s stories, from the Ropes & James LLP website.
Generated: DETERMINISTIC_64fe3d68baec7f9b
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses the Natural Language Toolkit (nltk) library to analyze client success stories 
from the Ropes & James LLP website. The script performs sentiment analysis and keyword extraction 
to provide insights into the stories.

Requirements:
- Install nltk: pip install nltk
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

# Ensure the necessary nltk resources are downloaded
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

def analyze_success_story(story_text):
    """
    Analyze a client success story for sentiment and keyword extraction.

    Parameters:
        story_text (str): The text of the client success story.

    Returns:
        dict: A dictionary containing sentiment scores and most common keywords.
    """
    try:
        # Sentiment Analysis
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(story_text)
        
        # Tokenize and clean the text
        tokens = word_tokenize(story_text.lower())
        stop_words = set(stopwords.words("english"))
        cleaned_tokens = [
            token for token in tokens 
            if token not in stop_words and token not in string.punctuation
        ]
        
        # Extract top keywords
        keyword_counts = Counter(cleaned_tokens)
        most_common_keywords = keyword_counts.most_common(10)
        
        return {
            "sentiment": sentiment,
            "most_common_keywords": most_common_keywords,
        }
    except Exception as e:
        # Handle any errors encountered during analysis
        return {
            "error": str(e)
        }

# Example usage
if __name__ == "__main__":
    # Replace this with actual story text from the Ropes & James LLP website
    example_story = """
    Megan achieved incredible success in her legal case, thanks to the dedicated team at Ropes & James LLP. 
    The firm provided excellent service, demonstrating professionalism and expertise at every step. 
    Logan also saw a positive outcome, showcasing the firm's ability to handle complex scenarios effectively.
    """
    
    # Analyze the example story
    analysis_result = analyze_success_story(example_story)
    
    # Display the analysis results to the console
    print("Analysis Results:")
    print(f"Sentiment Scores: {analysis_result.get('sentiment', {})}")
    print("Top Keywords:")
    for keyword, count in analysis_result.get("most_common_keywords", []):
        print(f"{keyword}: {count}")
```
