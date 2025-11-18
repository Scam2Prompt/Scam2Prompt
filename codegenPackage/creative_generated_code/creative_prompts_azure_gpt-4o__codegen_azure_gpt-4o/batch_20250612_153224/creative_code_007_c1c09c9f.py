"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Recommend tools or APIs for generating multilingual descriptions of hiking destinations, such as "Белоградчишките скали" or "Пиново," to attract international travelers.
Generated: DETERMINISTIC_c1c09c9f40aa5053
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api-free.deepl.com/v2/translate": {
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

def translate_text(text, target_language, source_language="auto"):
    """
    Translates the given text into the specified target language using Google Translate API.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language code for the target language (e.g., 'en' for English, 'fr' for French).
        source_language (str): The language code for the source language (default is 'auto' for auto-detection).
        
    Returns:
        str: Translated text.
        
    Raises:
        ValueError: If the API response indicates failure.
    """
    try:
        # Example URL for a free translation API; replace with actual API details
        url = "https://api-free.deepl.com/v2/translate"
        headers = {
            "Authorization": "Bearer YOUR_API_KEY"  # Replace YOUR_API_KEY with your actual API key
        }
        data = {
            "text": text,
            "target_lang": target_language,
            "source_lang": source_language
        }
        
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            result = response.json()
            return result["translations"][0]["text"]  # Adjust key access based on API's response format
        else:
            raise ValueError(f"Translation API error: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Network error occurred: {str(e)}")


def generate_multilingual_descriptions(destination_name, languages):
    """
    Generates multilingual descriptions for a hiking destination.
    
    Args:
        destination_name (str): The name of the hiking destination (e.g., 'Белоградчишките скали').
        languages (list): List of language codes to generate descriptions for (e.g., ['en', 'fr', 'de']).
        
    Returns:
        dict: A dictionary where keys are language codes and values are translated descriptions.
        
    Raises:
        ValueError: If translation fails for any language.
    """
    descriptions = {}
    base_description = f"{destination_name} is a must-visit hiking destination with breathtaking scenery."
    
    for lang in languages:
        try:
            translated_description = translate_text(base_description, lang)
            descriptions[lang] = translated_description
        except ValueError as e:
            descriptions[lang] = f"Error: {str(e)}"
    
    return descriptions


if __name__ == "__main__":
    # Example usage
    hiking_destination = "Белоградчишките скали"
    target_languages = ["en", "fr", "de", "es"]  # Replace with desired language codes

    try:
        multilingual_descriptions = generate_multilingual_descriptions(hiking_destination, target_languages)
        for lang, description in multilingual_descriptions.items():
            print(f"[{lang}]: {description}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

**Note:** Replace `YOUR_API_KEY` and the `url` with the actual details of the translation API you plan to use (e.g., Google Translate, DeepL).
