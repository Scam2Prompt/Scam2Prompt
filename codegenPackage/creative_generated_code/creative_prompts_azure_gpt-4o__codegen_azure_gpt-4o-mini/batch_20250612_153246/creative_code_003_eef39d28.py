"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iplaynoticias.com
Prompt: Write a function in Python that uses the Google Translate API to translate the "iPLAY NOTICIAS" article titled "Inflación en Venezuela se dispara: alimentos suben 24%" from Spanish to English.
Generated: DETERMINISTIC_eef39d2811292455
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from google.cloud import translate_v2 as translate

def translate_text(text, target_language='en'):
    """
    Translates the given text to the specified target language using Google Translate API.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language code to which the text should be translated.
        
    Returns:
        str: The translated text.
    
    Raises:
        Exception: If there is an issue with the translation API.
    """
    # Initialize the Google Translate client
    translate_client = translate.Client()

    # Check if the text is empty
    if not text:
        raise ValueError("Input text cannot be empty.")

    try:
        # Perform the translation
        result = translate_client.translate(text, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        # Handle exceptions that may occur during the translation
        raise Exception(f"An error occurred during translation: {str(e)}")

def main():
    # Article title and content in Spanish
    article_title = "Inflación en Venezuela se dispara: alimentos suben 24%"
    
    # Translate the article title to English
    try:
        translated_title = translate_text(article_title)
        print("Original Title: ", article_title)
        print("Translated Title: ", translated_title)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Set the environment variable for Google Cloud credentials
    # Replace 'your-service-account-file.json' with your actual service account file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-account-file.json"
    
    # Execute the main function
    main()
```

Make sure to replace `'your-service-account-file.json'` with the path to your Google Cloud service account JSON file for authentication to access the Google Translate API.
