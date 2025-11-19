"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a Python program to analyze and summarize legal documents, focusing on areas like Direito do Trabalho and Direito Tributário, as described on the CAAG website.
Generated: DETERMINISTIC_755455e5ab33ba87
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# legal_document_analyzer.py

import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import PyPDF2
import os

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def load_document(file_path):
    """
    Load a PDF document from a file path.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Text content of the PDF document.
    """
    try:
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        pdf_file.close()
        return text
    except Exception as e:
        print(f"Error loading document: {e}")
        return ''

def preprocess_text(text):
    """
    Preprocess the text by tokenizing, removing stop words, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        list: List of preprocessed words.
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('portuguese'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def extract_key_terms(text, num_terms=10):
    """
    Extract key terms from the text.

    Args:
        text (str): Text to extract key terms from.
        num_terms (int): Number of key terms to extract.

    Returns:
        list: List of key terms.
    """
    words = preprocess_text(text)
    term_freq = Counter(words)
    return [term for term, freq in term_freq.most_common(num_terms)]

def analyze_document(file_path):
    """
    Analyze a legal document and extract key terms.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        dict: Dictionary containing the document text and key terms.
    """
    text = load_document(file_path)
    key_terms = extract_key_terms(text)
    return {
        'text': text,
        'key_terms': key_terms
    }

def summarize_document(text, num_sentences=5):
    """
    Summarize a document by extracting key sentences.

    Args:
        text (str): Text to summarize.
        num_sentences (int): Number of sentences to extract.

    Returns:
        str: Summary of the document.
    """
    sentences = sent_tokenize(text)
    summary = ''
    for sentence in sentences[:num_sentences]:
        summary += sentence + ' '
    return summary.strip()

def main():
    # Example usage
    file_path = 'example.pdf'
    analysis = analyze_document(file_path)
    print("Document Text:")
    print(analysis['text'][:1000])  # Print the first 1000 characters
    print("\nKey Terms:")
    print(analysis['key_terms'])
    print("\nDocument Summary:")
    print(summarize_document(analysis['text']))

if __name__ == "__main__":
    main()
```
