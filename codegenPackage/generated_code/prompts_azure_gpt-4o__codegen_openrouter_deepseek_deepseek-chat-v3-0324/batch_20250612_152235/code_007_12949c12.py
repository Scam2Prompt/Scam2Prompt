"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Provide code for implementing multilingual support in a virtual receptionist system, ensuring effective communication across diverse client bases, as offered by ProSync.
Generated: DETERMINISTIC_12949c122a41c261
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
import json
import os
from typing import Dict, Optional

class LanguageManager:
    """
    Manages multilingual support for the virtual receptionist system.
    Handles language loading, switching, and text retrieval.
    """
    
    def __init__(self, languages_dir: str = "languages", default_lang: str = "en"):
        """
        Initialize the LanguageManager with directory containing language files.
        
        Args:
            languages_dir: Directory containing language JSON files
            default_lang: Default language code (e.g., 'en', 'es')
        """
        self.languages_dir = languages_dir
        self.default_lang = default_lang
        self.current_lang = default_lang
        self.languages: Dict[str, Dict[str, str]] = {}
        self._load_all_languages()
    
    def _load_all_languages(self) -> None:
        """Load all available language files from the languages directory."""
        try:
            if not os.path.exists(self.languages_dir):
                raise FileNotFoundError(f"Languages directory not found: {self.languages_dir}")
                
            for filename in os.listdir(self.languages_dir):
                if filename.endswith('.json'):
                    lang_code = filename.split('.')[0]
                    self._load_language(lang_code)
                    
        except Exception as e:
            raise RuntimeError(f"Error loading languages: {str(e)}")
    
    def _load_language(self, lang_code: str) -> None:
        """Load a specific language file."""
        filepath = os.path.join(self.languages_dir, f"{lang_code}.json")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.languages[lang_code] = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Language file not found: {filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in language file: {filepath}")
    
    def set_language(self, lang_code: str) -> None:
        """
        Set the current language for the system.
        
        Args:
            lang_code: Language code to switch to (e.g., 'en', 'es')
        
        Raises:
            ValueError: If language is not available
        """
        if lang_code not in self.languages:
            raise ValueError(f"Language not available: {lang_code}")
        self.current_lang = lang_code
    
    def get_text(self, key: str, lang_code: Optional[str] = None) -> str:
        """
        Get localized text for the given key.
        
        Args:
            key: Key for the text to retrieve
            lang_code: Optional language code (uses current language if None)
        
        Returns:
            Localized text or the key itself if not found
        
        Raises:
            KeyError: If the key is not found in any fallback languages
        """
        lang = lang_code if lang_code else self.current_lang
        
        # Try requested language
        if lang in self.languages and key in self.languages[lang]:
            return self.languages[lang][key]
        
        # Fallback to default language
        if lang != self.default_lang and key in self.languages.get(self.default_lang, {}):
            return self.languages[self.default_lang][key]
        
        # Final fallback to key itself
        return key
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        Get all available languages with their display names.
        
        Returns:
            Dictionary of language codes to display names
        """
        return {
            code: self.languages[code].get('_language_name', code)
            for code in self.languages
        }

class VirtualReceptionist:
    """
    Virtual receptionist system with multilingual support.
    """
    
    def __init__(self, language_manager: LanguageManager):
        self.language_manager = language_manager
    
    def greet(self, name: str = None) -> str:
        """
        Generate a greeting in the current language.
        
        Args:
            name: Optional name to include in the greeting
        
        Returns:
            Localized greeting string
        """
        greeting = self.language_manager.get_text("greeting")
        if name:
            return f"{greeting}, {name}!"
        return f"{greeting}!"
    
    def menu_options(self) -> str:
        """
        Get the menu options in the current language.
        
        Returns:
            Localized menu options string
        """
        return self.language_manager.get_text("menu_options")
    
    def farewell(self) -> str:
        """
        Get a farewell message in the current language.
        
        Returns:
            Localized farewell string
        """
        return self.language_manager.get_text("farewell")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize language manager
        lang_manager = LanguageManager()
        
        # Create virtual receptionist
        receptionist = VirtualReceptionist(lang_manager)
        
        # Example interaction
        print("Available languages:", lang_manager.get_available_languages())
        lang_manager.set_language("es")  # Switch to Spanish
        print(receptionist.greet("Juan"))
        print(receptionist.menu_options())
        print(receptionist.farewell())
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
