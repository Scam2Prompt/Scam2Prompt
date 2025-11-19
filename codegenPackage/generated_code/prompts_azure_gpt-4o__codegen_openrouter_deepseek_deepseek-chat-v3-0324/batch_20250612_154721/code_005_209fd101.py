"""
Generated Code Metadata:
========================
Original URL: https://w7.com.au
Prompt: Write a script to analyze the historical roots of transpersonal psychology, incorporating keywords like Kundalini, ego, and consciousness.
Generated: DETERMINISTIC_209fd1019e5ee831
Batch ID: 20250612_154721
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
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class TranspersonalPsychologyAnalyzer:
    """
    A class to analyze historical texts related to transpersonal psychology.
    Focuses on keywords like Kundalini, ego, and consciousness.
    """
    
    def __init__(self, text_files):
        """
        Initialize the analyzer with text files to process.
        
        Args:
            text_files (list): List of file paths containing historical texts
        """
        self.text_files = text_files
        self.keywords = ['kundalini', 'ego', 'consciousness']
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.word_frequencies = defaultdict(int)
        self.keyword_contexts = {keyword: [] for keyword in self.keywords}
        
    def preprocess_text(self, text):
        """
        Clean and preprocess text by:
        1. Converting to lowercase
        2. Removing punctuation
        3. Tokenizing
        4. Lemmatizing
        5. Removing stopwords
        
        Args:
            text (str): Raw text to process
            
        Returns:
            list: List of processed tokens
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens
    
    def analyze_texts(self):
        """
        Process all texts to:
        1. Calculate word frequencies
        2. Extract keyword contexts
        """
        for file_path in self.text_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    tokens = self.preprocess_text(text)
                    
                    # Update word frequencies
                    for token in tokens:
                        self.word_frequencies[token] += 1
                    
                    # Extract keyword contexts
                    sentences = nltk.sent_tokenize(text)
                    for sentence in sentences:
                        for keyword in self.keywords:
                            if keyword in sentence.lower():
                                self.keyword_contexts[keyword].append(sentence.strip())
            except FileNotFoundError:
                print(f"Warning: File not found - {file_path}")
            except UnicodeDecodeError:
                print(f"Warning: Could not decode file - {file_path}")
    
    def get_keyword_frequencies(self):
        """
        Get frequencies of the specified keywords.
        
        Returns:
            dict: Dictionary of keyword frequencies
        """
        return {keyword: self.word_frequencies.get(keyword, 0) for keyword in self.keywords}
    
    def get_top_words(self, n=10):
        """
        Get most frequent words in the texts.
        
        Args:
            n (int): Number of top words to return
            
        Returns:
            list: List of (word, frequency) tuples
        """
        sorted_words = sorted(self.word_frequencies.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]
    
    def plot_keyword_frequencies(self):
        """
        Generate a bar plot of keyword frequencies.
        """
        frequencies = self.get_keyword_frequencies()
        plt.bar(frequencies.keys(), frequencies.values())
        plt.title('Keyword Frequencies in Transpersonal Psychology Texts')
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.show()
    
    def save_keyword_contexts(self, output_dir):
        """
        Save keyword contexts to separate files.
        
        Args:
            output_dir (str): Directory to save context files
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        for keyword, contexts in self.keyword_contexts.items():
            if contexts:
                output_path = os.path.join(output_dir, f"{keyword}_contexts.txt")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write("\n\n".join(contexts))

# Example usage
if __name__ == "__main__":
    # Replace with actual text file paths
    text_files = ['text1.txt', 'text2.txt']  
    
    analyzer = TranspersonalPsychologyAnalyzer(text_files)
    analyzer.analyze_texts()
    
    # Display results
    print("Keyword Frequencies:", analyzer.get_keyword_frequencies())
    print("\nTop 10 Words:", analyzer.get_top_words())
    
    # Visualize and save results
    analyzer.plot_keyword_frequencies()
    analyzer.save_keyword_contexts("keyword_contexts")
```
