"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Develop a function to process multiple file formats (e.g., PDFs, text files) using UniWrapper and display AI model outputs side by side for comparison.
Generated: DETERMINISTIC_8f86962d2f43a79b
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
from PyPDF2 import PdfReader
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from typing import List

def process_file(file_path: str) -> str:
    """
    Process a file and extract text.

    Args:
    file_path (str): The path to the file.

    Returns:
    str: The extracted text.
    """
    try:
        if file_path.endswith('.pdf'):
            # Open the PDF file and extract text
            pdf_reader = PdfReader(file_path)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        elif file_path.endswith('.txt'):
            # Open the text file and extract text
            with open(file_path, 'r') as file:
                return file.read()
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(f"Error processing file: {e}")
        return ""

def load_ai_model(model_name: str):
    """
    Load a pre-trained AI model and tokenizer.

    Args:
    model_name (str): The name of the model.

    Returns:
    tuple: A tuple containing the model and tokenizer.
    """
    try:
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        print(f"Error loading AI model: {e}")
        return None, None

def get_ai_output(model, tokenizer, text: str):
    """
    Get the output from the AI model.

    Args:
    model: The AI model.
    tokenizer: The tokenizer.
    text (str): The input text.

    Returns:
    str: The AI model output.
    """
    try:
        inputs = tokenizer(text, return_tensors='pt')
        outputs = model(**inputs)
        return str(outputs)
    except Exception as e:
        print(f"Error getting AI output: {e}")
        return ""

def compare_ai_outputs(file_paths: List[str], model_name: str):
    """
    Process multiple files, get AI model outputs, and display them side by side.

    Args:
    file_paths (List[str]): A list of file paths.
    model_name (str): The name of the AI model.
    """
    try:
        model, tokenizer = load_ai_model(model_name)
        if model is None or tokenizer is None:
            return

        outputs = []
        for file_path in file_paths:
            text = process_file(file_path)
            output = get_ai_output(model, tokenizer, text)
            outputs.append(output)

        # Display outputs side by side
        for i in range(len(outputs)):
            print(f"File {i+1}: {file_paths[i]}")
            print(f"AI Output {i+1}: {outputs[i]}\n")

    except Exception as e:
        print(f"Error comparing AI outputs: {e}")

# Example usage
if __name__ == "__main__":
    file_paths = ['example.pdf', 'example.txt']
    model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
    compare_ai_outputs(file_paths, model_name)
```
