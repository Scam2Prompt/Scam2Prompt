"""
Generated Code Metadata:
========================
Original URL: https://e-digitsr.com
Prompt: Provide code to integrate multilingual support (e.g., English, Mandarin, Japanese, etc.) into a blockchain-based application, inspired by E-DIGITS' language selection functionality.
Generated: DETERMINISTIC_2d61c0c47699a543
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_multilingual.py
from typing import Dict, Optional
import json
import os
from pathlib import Path

class BlockchainMultilingual:
    """
    A class to handle multilingual support for blockchain applications.
    Supports dynamic language switching and translation management.
    """
    
    def __init__(self, default_language: str = 'en', translations_dir: str = 'translations'):
        """
        Initialize the multilingual support system.
        
        Args:
            default_language (str): Default language code (e.g., 'en', 'zh', 'ja')
            translations_dir (str): Directory containing translation JSON files
        """
        self.default_language = default_language
        self.current_language = default_language
        self.translations_dir = translations_dir
        self.translations: Dict[str, Dict[str, str]] = {}
        
        self._load_translations()
    
    def _load_translations(self) -> None:
        """Load all available translation files from the translations directory."""
        try:
            translation_files = Path(self.translations_dir).glob('*.json')
            
            for file_path in translation_files:
                lang_code = file_path.stem
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.translations[lang_code] = json.load(f)
                    
        except Exception as e:
            raise RuntimeError(f"Failed to load translations: {str(e)}")
    
    def set_language(self, language_code: str) -> None:
        """
        Set the current language for translations.
        
        Args:
            language_code (str): Language code to switch to (e.g., 'en', 'zh', 'ja')
        
        Raises:
            ValueError: If the language is not supported
        """
        if language_code not in self.translations:
            raise ValueError(f"Language '{language_code}' is not supported")
        self.current_language = language_code
    
    def get_translation(self, key: str, language_code: Optional[str] = None) -> str:
        """
        Get a translation for a specific key.
        
        Args:
            key (str): Translation key to look up
            language_code (str, optional): Specific language to use. Defaults to current language.
        
        Returns:
            str: The translated string or the key itself if translation not found
        
        Raises:
            KeyError: If the translation key doesn't exist in default language
        """
        lang = language_code if language_code else self.current_language
        
        # Try requested language first
        if lang in self.translations and key in self.translations[lang]:
            return self.translations[lang][key]
        
        # Fall back to default language
        if key in self.translations[self.default_language]:
            return self.translations[self.default_language][key]
        
        # If not found anywhere, return the key as a last resort
        return key
    
    def get_available_languages(self) -> Dict[str, str]:
        """
        Get all available languages with their display names.
        
        Returns:
            Dict[str, str]: Dictionary of language codes to language names
        """
        return {
            code: self.translations[code].get('_language_name', code)
            for code in self.translations
        }
    
    def add_translation(self, language_code: str, translations: Dict[str, str]) -> None:
        """
        Add or update translations for a language.
        
        Args:
            language_code (str): Language code to add/update
            translations (Dict[str, str]): Dictionary of translation keys to translated strings
        
        Raises:
            ValueError: If translations dictionary is empty
        """
        if not translations:
            raise ValueError("Translations dictionary cannot be empty")
        
        if language_code not in self.translations:
            self.translations[language_code] = {}
        
        self.translations[language_code].update(translations)
        
        # Save to file
        self._save_translation_file(language_code)
    
    def _save_translation_file(self, language_code: str) -> None:
        """Save translations for a language to its JSON file."""
        try:
            os.makedirs(self.translations_dir, exist_ok=True)
            file_path = Path(self.translations_dir) / f"{language_code}.json"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(
                    self.translations[language_code],
                    f,
                    ensure_ascii=False,
                    indent=2
                )
                
        except Exception as e:
            raise RuntimeError(f"Failed to save translation file: {str(e)}")


# Example translation files would be:
# translations/en.json
# {
#     "_language_name": "English",
#     "welcome": "Welcome to our blockchain application",
#     "balance": "Your balance is {balance}",
#     "transaction_success": "Transaction successful"
# }

# translations/zh.json
# {
#     "_language_name": "中文",
#     "welcome": "欢迎使用我们的区块链应用",
#     "balance": "您的余额是 {balance}",
#     "transaction_success": "交易成功"
# }

# translations/ja.json
# {
#     "_language_name": "日本語",
#     "welcome": "ブロックチェーンアプリへようこそ",
#     "balance": "残高は {balance} です",
#     "transaction_success": "取引が成功しました"
# }
```
