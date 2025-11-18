"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stadelink.com
Prompt: Provide an example of how to implement multi-language support (e.g., English, 简体中文, Русский, 日本語, etc.) in a DeFi application, inspired by the language options on Stadelink.
Generated: DETERMINISTIC_ab4ead27cd705760
Batch ID: 20250612_154938
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

class LocalizationManager:
    """
    A class to handle multi-language support for a DeFi application.
    """
    
    def __init__(self, default_language="en"):
        """
        Initializes the LocalizationManager with a default language.
        """
        self.default_language = default_language
        self.languages = {}
        
        # Load available languages
        self.load_languages()
    
    def load_languages(self):
        """
        Loads language files from the 'languages' directory.
        """
        language_dir = os.path.join(os.getcwd(), "languages")
        
        if not os.path.exists(language_dir):
            raise FileNotFoundError("Language directory not found.")
        
        for filename in os.listdir(language_dir):
            if filename.endswith(".json"):
                lang_code = filename.replace(".json", "")
                with open(os.path.join(language_dir, filename), 'r', encoding='utf-8') as lang_file:
                    self.languages[lang_code] = json.load(lang_file)
    
    def translate(self, key, language=None):
        """
        Translates a given key into the specified language or default language.
        
        :param key: String key representing the translation entry.
        :param language: Language code (e.g., 'en', 'zh', 'ru').
        :return: Translated string if found, else the key itself.
        """
        language = language or self.default_language
        
        if language in self.languages:
            return self.languages[language].get(key, key)
        else:
            return self.languages[self.default_language].get(key, key)


# Example usage
if __name__ == "__main__":
    try:
        localization = LocalizationManager(default_language="en")
        
        # Sample translation keys
        print(localization.translate("welcome_message", language="en"))  # English
        print(localization.translate("welcome_message", language="zh"))  # Simplified Chinese
        print(localization.translate("welcome_message", language="ru"))  # Russian
        print(localization.translate("welcome_message", language="ja"))  # Japanese
    except Exception as e:
        print(f"Error: {e}")
```

### Directory Structure:
```
.
├── languages/
│   ├── en.json
│   ├── zh.json
│   ├── ru.json
│   ├── ja.json
├── localization_manager.py
```

### Example JSON Files:
#### `languages/en.json`
```json
{
    "welcome_message": "Welcome to the DeFi Application!"
}
```

#### `languages/zh.json`
```json
{
    "welcome_message": "欢迎使用 DeFi 应用程序！"
}
```

#### `languages/ru.json`
```json
{
    "welcome_message": "Добро пожаловать в приложение DeFi!"
}
```

#### `languages/ja.json`
```json
{
    "welcome_message": "DeFiアプリケーションへようこそ！"
}
```
