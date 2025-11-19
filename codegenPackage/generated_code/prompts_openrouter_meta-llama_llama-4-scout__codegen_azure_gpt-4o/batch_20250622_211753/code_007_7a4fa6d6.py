"""
Generated Code Metadata:
========================
Original URL: https://www.autocaret.com
Prompt: Write a script that automates document creation using AI, allowing users to focus on ideas while the AI handles writing and formatting.
Generated: DETERMINISTIC_7a4fa6d6d5b5ddab
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import openai
import os
from datetime import datetime

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Ensure the API key is set in your environment variables
MODEL = "text-davinci-003"  # OpenAI model to use
MAX_TOKENS = 1000  # Maximum tokens for the AI response
DOCUMENT_FORMATS = ["txt", "md", "html"]  # Supported document formats

def generate_document(prompt, format="txt"):
    """
    Generates a document using OpenAI's API based on the provided prompt and format.

    Args:
        prompt (str): The idea or content description for the document.
        format (str): The desired format of the document (e.g., 'txt', 'md', 'html').

    Returns:
        str: The generated document content.
    """
    if format not in DOCUMENT_FORMATS:
        raise ValueError(f"Unsupported format '{format}'. Supported formats are: {DOCUMENT_FORMATS}")

    try:
        # Call OpenAI API to generate content
        response = openai.Completion.create(
            engine=MODEL,
            prompt=prompt,
            max_tokens=MAX_TOKENS,
            temperature=0.7
        )
        content = response.choices[0].text.strip()

        # Format content based on the requested format
        if format == "html":
            content = f"<html>\n<head>\n<title>Generated Document</title>\n</head>\n<body>\n{content}\n</body>\n</html>"
        elif format == "md":
            content = f"# Generated Document\n\n{content}"

        return content
    except Exception as e:
        raise RuntimeError(f"Failed to generate document: {e}")

def save_document(content, filename):
    """
    Saves the generated document content to a file.

    Args:
        content (str): The document content to save.
        filename (str): The name of the file to save the content to.

    Returns:
        None
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        raise RuntimeError(f"Failed to save document: {e}")

def main():
    """
    Main function to handle user input and automate document creation.
    """
    print("Welcome to the AI Document Creator!")
    prompt = input("Enter your idea or content description: ").strip()
    format = input(f"Enter the desired format ({', '.join(DOCUMENT_FORMATS)}): ").strip().lower()

    try:
        # Generate document
        document_content = generate_document(prompt, format)

        # Create a filename based on the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"document_{timestamp}.{format}"

        # Save the document
        save_document(document_content, filename)

        print(f"Document successfully created and saved as '{filename}'!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
