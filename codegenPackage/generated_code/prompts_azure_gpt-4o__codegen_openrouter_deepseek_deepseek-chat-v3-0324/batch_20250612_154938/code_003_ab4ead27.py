"""
Generated Code Metadata:
========================
Original URL: https://stadelink.com
Prompt: Provide an example of how to implement multi-language support (e.g., English, 简体中文, Русский, 日本語, etc.) in a DeFi application, inspired by the language options on Stadelink.
Generated: DETERMINISTIC_ab4ead27cd705760
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
from typing import Dict, Optional
from enum import Enum
import json
import os

class Language(Enum):
    """Supported languages enumeration."""
    ENGLISH = "en"
    SIMPLIFIED_CHINESE = "zh-CN"
    RUSSIAN = "ru"
    JAPANESE = "ja"

class I18N:
    """Internationalization (i18n) service for multi-language support."""
    
    def __init__(self, locale_dir: str = "locales", default_language: Language = Language.ENGLISH):
        """
        Initialize the i18n service.
        
        Args:
            locale_dir: Directory containing language JSON files
            default_language: Default language to fall back to
        """
        self.locale_dir = locale_dir
        self.default_language = default_language
        self.translations: Dict[Language, Dict[str, str]] = {}
        self._load_translations()
    
    def _load_translations(self) -> None:
        """Load all translation files from the locale directory."""
        for lang in Language:
            file_path = os.path.join(self.locale_dir, f"{lang.value}.json")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError(f"Translation file not found for language: {lang.value}")
            except json.JSONDecodeError:
                raise ValueError(f"Invalid JSON in translation file: {file_path}")
    
    def get_text(
        self, 
        key: str, 
        language: Optional[Language] = None, 
        **kwargs
    ) -> str:
        """
        Get translated text for a given key.
        
        Args:
            key: Translation key
            language: Target language (falls back to default if None)
            kwargs: Format arguments for the translated string
            
        Returns:
            Translated string or key if not found
        """
        lang = language or self.default_language
        translations = self.translations.get(lang, {})
        
        text = translations.get(key, key)  # Fallback to key if translation not found
        
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError):
            return text  # Return unformatted text if formatting fails

# Example usage
if __name__ == "__main__":
    # Initialize with default language
    i18n = I18N(default_language=Language.ENGLISH)
    
    # Sample translations (would normally be in JSON files)
    sample_translations = {
        "welcome_message": "Welcome to our DeFi App!",
        "balance": "Your balance is: {amount} {currency}",
        "transaction_success": "Transaction successful!"
    }
    
    # Mock loading translations for demonstration
    i18n.translations = {
        Language.ENGLISH: sample_translations,
        Language.SIMPLIFIED_CHINESE: {
            "welcome_message": "欢迎来到我们的DeFi应用!",
            "balance": "您的余额是: {amount} {currency}",
            "transaction_success": "交易成功!"
        },
        Language.RUSSIAN: {
            "welcome_message": "Добро пожаловать в наше DeFi приложение!",
            "balance": "Ваш баланс: {amount} {currency}",
            "transaction_success": "Транзакция успешна!"
        },
        Language.JAPANESE: {
            "welcome_message": "DeFiアプリへようこそ！",
            "balance": "残高: {amount} {currency}",
            "transaction_success": "取引が成功しました！"
        }
    }
    
    # Example usage
    print(i18n.get_text("welcome_message", Language.ENGLISH))
    print(i18n.get_text("welcome_message", Language.SIMPLIFIED_CHINESE))
    print(i18n.get_text("balance", Language.RUSSIAN, amount="100", currency="ETH"))
    print(i18n.get_text("transaction_success", Language.JAPANESE))
    
    # Fallback to key when translation missing
    print(i18n.get_text("nonexistent_key", Language.ENGLISH))
```
