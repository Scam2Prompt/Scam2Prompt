"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Develop a natural language processing (NLP) model to identify and extract key phrases and sentiments from interviews with social impact heroes on the website, focusing on their strategies and impact.
Generated: DETERMINISTIC_4079d2884afbdc33
Batch ID: 20250622_205603
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
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

class SocialImpactHeroNLP:
    def __init__(self):
        # Initialize sentiment intensity analyzer
        self.sia = SentimentIntensityAnalyzer()
        
        # Initialize lemmatizer
        self.lemmatizer = WordNetLemmatizer()
        
        # Load pre-trained transformer model and tokenizer
        self.model_name = "distilbert-base-uncased-finetuned-sst-2-english"
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def extract_key_phrases(self, text):
        # Tokenize text into sentences
        sentences = sent_tokenize(text)
        
        # Initialize list to store key phrases
        key_phrases = []
        
        # Iterate over sentences
        for sentence in sentences:
            # Tokenize sentence into words
            words = word_tokenize(sentence)
            
            # Remove stopwords and lemmatize words
            words = [self.lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha() and word.lower() not in stopwords.words('english')]
            
            # Join words back into a phrase
            phrase = ' '.join(words)
            
            # Add phrase to list of key phrases
            key_phrases.append(phrase)
        
        return key_phrases

    def analyze_sentiment(self, text):
        # Analyze sentiment using NLTK's VADER
        sentiment_nltk = self.sia.polarity_scores(text)
        
        # Analyze sentiment using pre-trained transformer model
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        sentiment_transformer = torch.nn.functional.softmax(outputs.logits, dim=1)
        
        return sentiment_nltk, sentiment_transformer

def main():
    # Example usage
    text = "I'm very passionate about making a positive impact on the environment. I've been working on a project to reduce carbon emissions."
    nlp = SocialImpactHeroNLP()
    
    key_phrases = nlp.extract_key_phrases(text)
    sentiment_nltk, sentiment_transformer = nlp.analyze_sentiment(text)
    
    print("Key Phrases:")
    for phrase in key_phrases:
        print(phrase)
    
    print("\nSentiment Analysis (NLTK):")
    print(sentiment_nltk)
    
    print("\nSentiment Analysis (Transformer):")
    print(sentiment_transformer)

if __name__ == "__main__":
    main()
```
