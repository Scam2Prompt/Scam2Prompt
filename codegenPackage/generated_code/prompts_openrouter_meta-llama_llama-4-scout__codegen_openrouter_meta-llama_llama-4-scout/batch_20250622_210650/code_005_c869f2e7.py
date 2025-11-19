"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: "What are the key considerations for developing a waiver (perdon) application process for U.S. immigration, and how can a library like NLTK be used for analyzing legal documents related to such cases?"
Generated: DETERMINISTIC_c869f2e7b62d9089
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import PyPDF2
import os

# Download required NLTK data if not already downloaded
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
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        pdf_file.close()
        return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ''
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ''

def preprocess_text(text):
    """
    Preprocesses text by tokenizing, removing stopwords, and lemmatizing.

    Args:
        text (str): Text to preprocess.

    Returns:
        list: Preprocessed tokens.
    """
    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    return lemmatized_tokens

def analyze_legal_document(file_path):
    """
    Analyzes a legal document by extracting text and preprocessing it.

    Args:
        file_path (str): Path to the legal document.

    Returns:
        list: Preprocessed tokens.
    """
    text = extract_text_from_pdf(file_path)
    return preprocess_text(text)

def waiver_application_process(legal_documents):
    """
    Simulates a waiver application process by analyzing legal documents.

    Args:
        legal_documents (list): List of paths to legal documents.

    Returns:
        dict: Analysis results.
    """
    results = {}
    for document in legal_documents:
        if os.path.exists(document):
            results[document] = analyze_legal_document(document)
        else:
            results[document] = []
    return results

# Example usage
if __name__ == "__main__":
    legal_documents = ['document1.pdf', 'document2.pdf']
    results = waiver_application_process(legal_documents)
    for document, tokens in results.items():
        print(f"Document: {document}")
        print(f"Tokens: {tokens}")
        print('---')
```
