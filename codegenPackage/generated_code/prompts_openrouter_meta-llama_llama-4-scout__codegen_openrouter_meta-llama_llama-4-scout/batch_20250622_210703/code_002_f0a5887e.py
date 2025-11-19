"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a code snippet to create a simple Vietnamese language processing tool that can help with tasks such as legal document analysis or text summarization for law firms like Luật Trung Cường.
Generated: DETERMINISTIC_f0a5887e2da05210
Batch ID: 20250622_210703
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
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import re

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

class VietnameseLanguageProcessor:
    def __init__(self):
        # Initialize the Porter stemmer
        self.stemmer = PorterStemmer()
        
        # Load Vietnamese stopwords
        try:
            self.stop_words = set(stopwords.words('vietnamese'))
        except LookupError:
            print("Vietnamese stopwords not found. Please download the 'stopwords' package using nltk.download('stopwords').")
            exit()

    def preprocess_text(self, text):
        """
        Preprocess the input text by tokenizing, removing stopwords, and stemming.
        
        Args:
            text (str): The input text.
        
        Returns:
            list: A list of preprocessed tokens.
        """
        # Tokenize the text into words
        tokens = word_tokenize(text)
        
        # Remove punctuation and special characters
        tokens = [re.sub(r'[^\w\s]', '', token) for token in tokens]
        
        # Remove stopwords and stem the tokens
        tokens = [self.stemmer.stem(token.lower()) for token in tokens if token.lower() not in self.stop_words and token != '']
        
        return tokens

    def summarize_text(self, text, summary_length=5):
        """
        Summarize the input text by selecting the top N sentences.
        
        Args:
            text (str): The input text.
            summary_length (int): The number of sentences to include in the summary. Defaults to 5.
        
        Returns:
            str: A summary of the input text.
        """
        # Tokenize the text into sentences
        sentences = sent_tokenize(text)
        
        # Calculate the score of each sentence
        sentence_scores = {}
        for sentence in sentences:
            for word in self.preprocess_text(sentence):
                if word in sentence.lower():
                    if sentence in sentence_scores:
                        sentence_scores[sentence] += 1
                    else:
                        sentence_scores[sentence] = 1
        
        # Sort the sentences by score and select the top N
        summary_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:summary_length]
        
        # Return the summary
        return ' '.join([sentence[0] for sentence in summary_sentences])

def main():
    processor = VietnameseLanguageProcessor()
    
    # Example usage: Preprocess text
    text = "Luật sư có vai trò quan trọng trong việc tư vấn và bảo vệ quyền lợi cho khách hàng."
    print("Preprocessed text:")
    print(processor.preprocess_text(text))
    
    # Example usage: Summarize text
    text = "Luật sư có vai trò quan trọng trong việc tư vấn và bảo vệ quyền lợi cho khách hàng. Họ giúp khách hàng hiểu rõ các quy định pháp luật và đưa ra quyết định sáng suốt. Luật sư cũng đại diện cho khách hàng trong các vụ việc pháp lý."
    print("\nText summary:")
    print(processor.summarize_text(text))

if __name__ == "__main__":
    main()
```
