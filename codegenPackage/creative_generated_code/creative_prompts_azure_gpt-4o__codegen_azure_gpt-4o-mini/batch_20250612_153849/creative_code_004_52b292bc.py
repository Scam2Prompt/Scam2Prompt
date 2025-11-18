"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pha.ntom.me
Prompt: Provide an example of using Bing Translate API to translate the phrase "Hello from the other side" into French.
Generated: DETERMINISTIC_52b292bcf285d2ab
Batch ID: 20250612_153849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cognitive.microsofttranslator.com": {
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

class BingTranslateAPI:
    def __init__(self, subscription_key, endpoint):
        """
        Initialize the Bing Translate API client.

        :param subscription_key: Your Bing Translate subscription key.
        :param endpoint: The API endpoint for the translation service.
        """
        self.subscription_key = subscription_key
        self.endpoint = endpoint

    def translate(self, text, from_language='en', to_language='fr'):
        """
        Translate a given text from the source language to the target language.

        :param text: The text to be translated.
        :param from_language: The source language code (default is English).
        :param to_language: The target language code (default is French).
        :return: The translated text or an error message.
        """
        # Construct the URL for the translation request
        url = f"{self.endpoint}/translate?api-version=3.0&from={from_language}&to={to_language}"
        
        # Prepare the request headers
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Content-Type': 'application/json'
        }
        
        # Prepare the request body
        body = [{
            'text': text
        }]
        
        try:
            # Send the request to the Bing Translate API
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()  # Raise an error for bad responses
            
            # Parse the JSON response
            translations = response.json()
            translated_text = translations[0]['translations'][0]['text']
            return translated_text
        
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

# Example usage of the Bing Translate API
if __name__ == "__main__":
    # Replace these with your actual subscription key and endpoint
    SUBSCRIPTION_KEY = 'YOUR_SUBSCRIPTION_KEY'
    ENDPOINT = 'https://api.cognitive.microsofttranslator.com'

    translator = BingTranslateAPI(SUBSCRIPTION_KEY, ENDPOINT)
    phrase_to_translate = "Hello from the other side"
    translated_phrase = translator.translate(phrase_to_translate)

    print(f"Translated phrase: {translated_phrase}")
```

Make sure to replace `'YOUR_SUBSCRIPTION_KEY'` with your actual Bing Translate subscription key before running the code.
