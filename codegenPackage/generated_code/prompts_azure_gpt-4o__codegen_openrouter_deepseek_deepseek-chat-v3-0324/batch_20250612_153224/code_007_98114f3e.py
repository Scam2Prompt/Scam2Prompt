"""
Generated Code Metadata:
========================
Original URL: https://alwan.om
Prompt: Generate code for multi-language or localization support for an e-commerce platform, focusing on regions like Oman, as seen on Alwan's website.
Generated: DETERMINISTIC_98114f3e55f22b15
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# localization.py

import os
import json
from typing import Dict, Optional

class LocalizationManager:
    """
    Handles multi-language support for an e-commerce platform.
    Loads translations from JSON files and provides localized strings.
    """
    
    def __init__(self, default_language: str = 'en'):
        """
        Initialize the LocalizationManager.
        
        Args:
            default_language (str): The default language code (e.g., 'en', 'ar')
        """
        self.translations: Dict[str, Dict[str, str]] = {}
        self.default_language = default_language
        self.current_language = default_language
        self.load_translations()
    
    def load_translations(self) -> None:
        """
        Load all translation files from the locales directory.
        Translation files should be named as {language_code}.json.
        """
        locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
        
        if not os.path.exists(locales_dir):
            raise FileNotFoundError(f"Locales directory not found: {locales_dir}")
        
        for filename in os.listdir(locales_dir):
            if filename.endswith('.json'):
                lang_code = filename.split('.')[0]
                filepath = os.path.join(locales_dir, filename)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        self.translations[lang_code] = json.load(f)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON in {filename}: {str(e)}")
                except Exception as e:
                    raise IOError(f"Error loading {filename}: {str(e)}")
    
    def set_language(self, language_code: str) -> None:
        """
        Set the current language for localization.
        
        Args:
            language_code (str): Language code to set (e.g., 'en', 'ar')
        
        Raises:
            ValueError: If the language is not supported
        """
        if language_code not in self.translations:
            raise ValueError(f"Language not supported: {language_code}")
        self.current_language = language_code
    
    def get_text(self, key: str, language_code: Optional[str] = None) -> str:
        """
        Get localized text for a given key.
        
        Args:
            key (str): Translation key
            language_code (str, optional): Specific language to use. Defaults to current language.
        
        Returns:
            str: Localized text or the key itself if translation not found
        """
        lang = language_code or self.current_language
        
        # Try requested language
        if lang in self.translations and key in self.translations[lang]:
            return self.translations[lang][key]
        
        # Fallback to default language
        if lang != self.default_language:
            if self.default_language in self.translations and key in self.translations[self.default_language]:
                return self.translations[self.default_language][key]
        
        # Final fallback to key itself
        return key
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        Get all available languages with their display names.
        
        Returns:
            Dict[str, str]: Dictionary of language codes to display names
        """
        return {
            'en': 'English',
            'ar': 'العربية',  # Arabic
            'ur': 'اردو',     # Urdu
            'hi': 'हिन्दी',   # Hindi
            # Add more languages as needed
        }
    
    def get_current_language_direction(self) -> str:
        """
        Get text direction for current language (LTR or RTL).
        
        Returns:
            str: 'ltr' or 'rtl'
        """
        rtl_languages = ['ar']  # Right-to-left languages
        return 'rtl' if self.current_language in rtl_languages else 'ltr'


# Example usage (would be in a separate file in production)
if __name__ == "__main__":
    try:
        # Initialize with English as default
        localizer = LocalizationManager(default_language='en')
        
        # Set to Arabic (for Oman)
        localizer.set_language('ar')
        
        # Get localized text
        welcome_text = localizer.get_text('welcome_message')
        print(f"Welcome message in Arabic: {welcome_text}")
        
        # Fallback example
        non_existent_key = localizer.get_text('nonexistent_key')
        print(f"Fallback example: {non_existent_key}")
        
    except Exception as e:
        print(f"Localization error: {str(e)}")
```
