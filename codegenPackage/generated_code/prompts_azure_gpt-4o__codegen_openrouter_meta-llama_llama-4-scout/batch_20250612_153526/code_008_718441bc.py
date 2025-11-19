"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write code to analyze blog posts like "Life in Kibera post COVID" and "Growing up in Kibera Slums" from the Kibera Hamlets website, extracting key themes and generating summaries.
Generated: DETERMINISTIC_718441bcc7b693e2
Batch ID: 20250612_153526
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
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class BlogPostAnalyzer:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')

    def _preprocess_text(self, text):
        # Tokenize text into sentences
        sentences = sent_tokenize(text)
        
        # Initialize list to store preprocessed sentences
        preprocessed_sentences = []
        
        for sentence in sentences:
            # Tokenize sentence into words
            words = word_tokenize(sentence)
            
            # Remove stop words and lemmatize words
            filtered_words = [self.lemmatizer.lemmatize(word.lower()) for word in words if word.isalpha() and word.lower() not in self.stop_words]
            
            # Join filtered words back into a sentence
            preprocessed_sentence = ' '.join(filtered_words)
            
            # Add preprocessed sentence to list
            preprocessed_sentences.append(preprocessed_sentence)
        
        return ' '.join(preprocessed_sentences)

    def extract_key_themes(self, text, num_themes=5):
        try:
            # Preprocess text
            preprocessed_text = self._preprocess_text(text)
            
            # Encode preprocessed text into input IDs and attention mask
            input_ids = self.tokenizer.encode("summarize: " + preprocessed_text, return_tensors='pt')
            
            # Generate summary
            output = self.model.generate(input_ids, max_length=200)
            
            # Decode generated summary
            summary = self.tokenizer.decode(output[0], skip_special_tokens=True)
            
            # Split summary into individual themes
            themes = [theme.strip() for theme in summary.split('.') if theme]
            
            # Return top N themes
            return themes[:num_themes]
        except Exception as e:
            print(f"Error extracting key themes: {str(e)}")
            return []

    def generate_summary(self, text):
        try:
            # Preprocess text
            preprocessed_text = self._preprocess_text(text)
            
            # Encode preprocessed text into input IDs and attention mask
            input_ids = self.tokenizer.encode("summarize: " + preprocessed_text, return_tensors='pt')
            
            # Generate summary
            output = self.model.generate(input_ids, max_length=200)
            
            # Decode generated summary
            return self.tokenizer.decode(output[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Error generating summary: {str(e)}")
            return ""

def main():
    analyzer = BlogPostAnalyzer()

    blog_posts = [
        "Life in Kibera post COVID",
        "Growing up in Kibera Slums"
    ]

    for post in blog_posts:
        # Assuming we have the full text of the blog post
        full_text = "This is a sample full text of the blog post " + post
        key_themes = analyzer.extract_key_themes(full_text)
        summary = analyzer.generate_summary(full_text)

        print(f"Blog Post: {post}")
        print(f"Key Themes: {key_themes}")
        print(f"Summary: {summary}")
        print("")

if __name__ == "__main__":
    main()
```
