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
# Import required libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re

# Download required NLTK data if not already downloaded
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Tokenize and remove stopwords
        tokens = [self.lemmatizer.lemmatize(word) for word in text.split() if word not in self.stop_words]
        
        # Join tokens back into a string
        text = ' '.join(tokens)
        
        return text

    def analyze_sentiment(self, text):
        # Preprocess the text
        text = self.preprocess_text(text)
        
        # Analyze sentiment
        sentiment = self.sia.polarity_scores(text)
        
        return sentiment

def load_comments(file_path):
    try:
        # Load comments from a CSV file
        comments = pd.read_csv(file_path)
        return comments
    except Exception as e:
        print(f"Error loading comments: {str(e)}")
        return None

def evaluate_comments(comments, topics):
    # Initialize sentiment analyzer
    analyzer = SentimentAnalyzer()
    
    # Evaluate sentiment for each comment
    results = []
    for index, comment in comments.iterrows():
        for topic in topics:
            if topic in comment['comment'].lower():
                sentiment = analyzer.analyze_sentiment(comment['comment'])
                results.append({
                    'topic': topic,
                    'comment': comment['comment'],
                    'sentiment': sentiment
                })
    
    return results

def main():
    # Load comments from a CSV file
    comments = load_comments('comments.csv')
    
    if comments is not None:
        # Define topics of interest
        topics = ["preventative health checks", "customizing countertops"]
        
        # Evaluate sentiment for comments related to topics
        results = evaluate_comments(comments, topics)
        
        # Print results
        for result in results:
            print(f"Topic: {result['topic']}")
            print(f"Comment: {result['comment']}")
            print(f"Sentiment: {result['sentiment']}")
            print("------------------------")

if __name__ == "__main__":
    main()
```

**comments.csv example**
```csv
comment
"I had a great experience with SRH Life Foundation's preventative health checks!"
"Their customizing countertops service is terrible, would not recommend."
"SRH Life Foundation's preventative health checks are very informative."
```

**requirements.txt**
```
nltk
pandas
```
