"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: "Create a code snippet for automating the analysis of Web3 startup pitch decks and providing actionable insights, similar to the Proof of Pitch AI evaluation process."
Generated: DETERMINISTIC_a9ee80b80afc9932
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import json
import openai
from typing import List, Dict

# Constants
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key
SUPPORTED_FILE_TYPES = ['.pdf', '.pptx', '.docx']  # Supported pitch deck formats

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from a given file. Supports PDF, PPTX, and DOCX formats.
    :param file_path: Path to the pitch deck file.
    :return: Extracted text as a string.
    """
    try:
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.pdf':
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            return ' '.join(page.extract_text() for page in reader.pages)
        elif file_extension == '.pptx':
            from pptx import Presentation
            presentation = Presentation(file_path)
            return ' '.join(shape.text for slide in presentation.slides for shape in slide.shapes if hasattr(shape, "text"))
        elif file_extension == '.docx':
            from docx import Document
            document = Document(file_path)
            return ' '.join(paragraph.text for paragraph in document.paragraphs)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
    except Exception as e:
        raise RuntimeError(f"Error extracting text from file: {e}")

def analyze_pitch_deck(text: str) -> Dict[str, str]:
    """
    Analyzes the pitch deck text using OpenAI GPT and provides actionable insights.
    :param text: Extracted text from the pitch deck.
    :return: Dictionary containing insights and recommendations.
    """
    try:
        prompt = (
            "You are an AI expert in evaluating Web3 startup pitch decks. "
            "Analyze the following pitch deck text and provide actionable insights, "
            "including strengths, weaknesses, and recommendations for improvement:\n\n"
            f"{text}\n\n"
            "Provide your response in JSON format with keys: 'strengths', 'weaknesses', 'recommendations'."
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        return json.loads(response.choices[0].text.strip())
    except Exception as e:
        raise RuntimeError(f"Error analyzing pitch deck: {e}")

def main(file_path: str):
    """
    Main function to automate the analysis of Web3 startup pitch decks.
    :param file_path: Path to the pitch deck file.
    """
    try:
        # Validate file type
        if not any(file_path.endswith(ext) for ext in SUPPORTED_FILE_TYPES):
            raise ValueError(f"Unsupported file type. Supported types are: {SUPPORTED_FILE_TYPES}")

        # Extract text from the pitch deck
        print("Extracting text from pitch deck...")
        pitch_text = extract_text_from_file(file_path)

        # Analyze the pitch deck
        print("Analyzing pitch deck...")
        insights = analyze_pitch_deck(pitch_text)

        # Display actionable insights
        print("Actionable Insights:")
        print(json.dumps(insights, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage: Replace 'path_to_pitch_deck' with the actual file path
    pitch_deck_path = "path_to_pitch_deck.pdf"
    main(pitch_deck_path)
```
