"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tuninghex.com
Prompt: Create a script to translate and localize tuning file service descriptions for international users, referencing the multilingual support seen on TuningHEX.
Generated: DETERMINISTIC_fc71de2756f13bfe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import Dict, Any

class LocalizationError(Exception):
    """Custom exception for localization errors."""
    pass

class TuningFileLocalizer:
    """Class for localizing tuning file service descriptions."""
    
    def __init__(self, translations_file: str):
        """Initialize with the path to the translations file."""
        self.translations = self.load_translations(translations_file)

    def load_translations(self, translations_file: str) -> Dict[str, Dict[str, str]]:
        """Load translations from a JSON file."""
        if not os.path.exists(translations_file):
            raise LocalizationError(f"Translations file not found: {translations_file}")
        
        with open(translations_file, 'r', encoding='utf-8') as file:
            try:
                translations = json.load(file)
            except json.JSONDecodeError as e:
                raise LocalizationError(f"Error loading translations: {e}")
        
        return translations

    def translate(self, service_description: str, language_code: str) -> str:
        """Translate a service description into the specified language."""
        if language_code not in self.translations:
            raise LocalizationError(f"Language code not supported: {language_code}")
        
        translation = self.translations[language_code].get(service_description)
        if translation is None:
            raise LocalizationError(f"No translation found for '{service_description}' in '{language_code}'")

        return translation

    def localize_descriptions(self, descriptions: Dict[str, Any], language_code: str) -> Dict[str, str]:
        """Localize a dictionary of service descriptions."""
        localized_descriptions = {}
        for key, desc in descriptions.items():
            try:
                localized_descriptions[key] = self.translate(desc, language_code)
            except LocalizationError as e:
                localized_descriptions[key] = f"[Error: {str(e)}]"
        
        return localized_descriptions

if __name__ == "__main__":
    # Example usage
    try:
        localizer = TuningFileLocalizer("translations.json")  # Load translations
        service_descriptions = {
            "service_1": "Basic Tuning",
            "service_2": "Advanced Tuning"
        }
        
        # Localize the service descriptions in Spanish
        localized = localizer.localize_descriptions(service_descriptions, "es")
        print(localized)

    except LocalizationError as e:
        print(f"Localization failed: {e}")
```

**Note:** Make sure to have a `translations.json` file in the same directory with the appropriate structure for translations, which could look like this:

```json
{
    "en": {
        "Basic Tuning": "Basic Tuning",
        "Advanced Tuning": "Advanced Tuning"
    },
    "es": {
        "Basic Tuning": "Ajuste Básico",
        "Advanced Tuning": "Ajuste Avanzado"
    }
}
```
