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

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_document(prompt, model="text-davinci-003", max_tokens=1500):
    """
    Generate a document using OpenAI's GPT-3 model.

    Args:
        prompt (str): The input prompt to guide the document generation.
        model (str): The model to use for generation (default is "text-davinci-003").
        max_tokens (int): The maximum number of tokens to generate (default is 1500).

    Returns:
        str: The generated document text.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.7,
        )
        document_text = response.choices[0].text.strip()
        return document_text
    except Exception as e:
        print(f"Error generating document: {e}")
        return None

def save_document_to_file(document_text, filename):
    """
    Save the generated document text to a file.

    Args:
        document_text (str): The text of the document to save.
        filename (str): The name of the file to save the document as.

    Returns:
        bool: True if the document was saved successfully, False otherwise.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(document_text)
        print(f"Document saved as {filename}")
        return True
    except Exception as e:
        print(f"Error saving document: {e}")
        return False

def main():
    """
    Main function to execute the document generation and saving process.
    """
    # User input for document prompt
    prompt = input("Enter the prompt for your document: ")
    
    # Generate the document
    document_text = generate_document(prompt)
    
    if document_text:
        # Specify the filename for saving the document
        filename = input("Enter the filename to save the document (e.g., document.txt): ")
        
        # Save the document to a file
        save_document_to_file(document_text, filename)

if __name__ == "__main__":
    main()
```
