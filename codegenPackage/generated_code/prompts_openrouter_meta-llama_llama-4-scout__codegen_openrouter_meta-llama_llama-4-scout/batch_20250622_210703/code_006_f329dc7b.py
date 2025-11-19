"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a Python script to extract and summarize key information from Vietnamese legal documents, such as court decisions or laws, that could be relevant to Luật Trung Cường's services.
Generated: DETERMINISTIC_f329dc7b850cef85
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import re
import PyPDF2
import os
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text.
    """
    try:
        pdf_file_obj = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
        num_pages = pdf_reader.numPages
        text = ''
        for page in range(num_pages):
            page_obj = pdf_reader.getPage(page)
            text += page_obj.extractText()
        pdf_file_obj.close()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def preprocess_text(text):
    """
    Preprocesses the text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        list: Preprocessed text as a list of words.
    """
    try:
        # Tokenize text
        tokens = word_tokenize(text)

        # Remove stopwords
        stop_words = set(stopwords.words('vietnamese'))
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

        # Lemmatize tokens
        lemmatizer = WordNetLemmatizer()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

        return lemmatized_tokens
    except Exception as e:
        print(f"Error preprocessing text: {e}")
        return []

def extract_key_info(text):
    """
    Extracts key information from the text, such as keywords and key sentences.

    Args:
        text (str): Text to extract key information from.

    Returns:
        dict: Dictionary containing keywords and key sentences.
    """
    try:
        # Extract keywords
        keywords = [token for token in preprocess_text(text) if len(token) > 2]

        # Extract key sentences
        sentences = sent_tokenize(text)
        key_sentences = [sentence for sentence in sentences if any(keyword in sentence for keyword in keywords)]

        return {
            'keywords': keywords,
            'key_sentences': key_sentences
        }
    except Exception as e:
        print(f"Error extracting key information: {e}")
        return {}

def summarize_document(file_path):
    """
    Summarizes a Vietnamese legal document.

    Args:
        file_path (str): Path to the document file.

    Returns:
        dict: Dictionary containing key information and summary.
    """
    try:
        # Extract text from PDF
        text = extract_text_from_pdf(file_path)

        # Extract key information
        key_info = extract_key_info(text)

        # Summarize document
        summary = ' '.join(key_info['key_sentences'])

        return {
            'key_info': key_info,
            'summary': summary
        }
    except Exception as e:
        print(f"Error summarizing document: {e}")
        return {}

def main():
    file_path = 'path_to_your_pdf_file.pdf'  # replace with your PDF file path
    if not os.path.isfile(file_path):
        print("File not found.")
        return

    result = summarize_document(file_path)
    print("Key Info:")
    print(result['key_info'])
    print("\nSummary:")
    print(result['summary'])

if __name__ == "__main__":
    main()
```
