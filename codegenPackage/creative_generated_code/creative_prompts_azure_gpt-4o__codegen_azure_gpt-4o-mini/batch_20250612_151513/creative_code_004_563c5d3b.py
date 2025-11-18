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
  "https://api.example.com/translate": {
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

class TranslationService:
    """
    A class to handle text translations using external APIs.
    """

    def __init__(self, api_key, supported_languages):
        """
        Initialize the TranslationService with an API key and supported languages.

        :param api_key: API key for the translation service
        :param supported_languages: List of languages supported for translation
        """
        self.api_key = api_key
        self.supported_languages = supported_languages
        self.base_url = "https://api.example.com/translate"  # Placeholder for actual translation API

    def translate_text(self, text, target_language):
        """
        Translate the given text into the target language.

        :param text: Text to be translated
        :param target_language: Language code for the target language
        :return: Translated text or an error message
        """
        if target_language not in self.supported_languages:
            return f"Error: {target_language} is not a supported language."

        try:
            payload = {
                'text': text,
                'target_language': target_language,
                'api_key': self.api_key
            }
            response = requests.post(self.base_url, json=payload)

            # Raise an error if the request was unsuccessful
            response.raise_for_status()

            # Parse the JSON response
            translation_result = response.json()

            return translation_result.get('translated_text', 'Translation not found.')

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return f"Request error occurred: {req_err}"
        except json.JSONDecodeError:
            return "Error decoding the response from the translation service."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

def main():
    """
    Main function to demonstrate the translation service.
    """
    # Configuration for the translation service
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    SUPPORTED_LANGUAGES = ['es', 'fr', 'de', 'zh', 'ja']  # Example language codes

    translator = TranslationService(API_KEY, SUPPORTED_LANGUAGES)

    # Example usage: translating a text
    text_to_translate = "Hello, how are you?"
    target_language = 'es'  # Spanish

    translated_text = translator.translate_text(text_to_translate, target_language)
    print(f"Translated Text ({target_language}): {translated_text}")

if __name__ == "__main__":
    main()
```
