"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Develop a program to translate text into multiple languages using APIs, ensuring the translations are professional and accurate, as described in the certified translation services provided by Hispanic Services.
Generated: DETERMINISTIC_563c5d3b98bcdfcf
Batch ID: 20250612_151513
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cognitive.microsofttranslator.com/translate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

# Constants for the API configurations
API_URL = "https://api.cognitive.microsofttranslator.com/translate"
API_KEY = "your_api_key_here"  # Replace with your API key
API_REGION = "your_region_here"  # Replace with your region
SUPPORTED_LANGUAGES = ["es", "fr", "de", "it", "pt"]  # Add target languages (e.g., Spanish, French, German, etc.)

def translate_text(text, target_language):
    """
    Translates the given text into the target language using the Microsoft Translator Text API.

    Parameters:
        text (str): The input text to be translated.
        target_language (str): The language code for the target translation (e.g., "es" for Spanish).

    Returns:
        str: The translated text.
    """
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Ocp-Apim-Subscription-Region": API_REGION,
        "Content-Type": "application/json"
    }

    params = {
        "api-version": "3.0",
        "to": target_language
    }

    body = [{
        "text": text
    }]

    try:
        response = requests.post(API_URL, headers=headers, params=params, json=body)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        translations = response.json()
        return translations[0]['translations'][0]['text']
    except requests.exceptions.RequestException as e:
        print(f"Error during translation: {e}")
        return None

def main():
    """
    Main function to translate text into multiple languages and display the results.
    """
    input_text = input("Enter the text you want to translate: ")

    if not input_text.strip():
        print("Error: Input text cannot be empty.")
        return

    print("\nTranslations:")
    for lang_code in SUPPORTED_LANGUAGES:
        translated_text = translate_text(input_text, lang_code)
        if translated_text:
            print(f"Language ({lang_code}): {translated_text}")
        else:
            print(f"Failed to translate text into {lang_code}.")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `your_api_key_here` and `your_region_here` with valid credentials for the Microsoft Translator Text API.
- The `SUPPORTED_LANGUAGES` list is customizable; add/remove language codes as needed.
- The program includes error handling for network issues and API errors (`requests.exceptions.RequestException`).
