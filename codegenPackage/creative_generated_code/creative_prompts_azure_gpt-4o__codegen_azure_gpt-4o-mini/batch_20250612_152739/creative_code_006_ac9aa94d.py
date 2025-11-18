"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancarpos.com
Prompt: Recommend tools or APIs to translate Pancar Pos articles from Indonesian to English for international readers.
Generated: DETERMINISTIC_ac9aa94db17c6a14
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from googletrans import Translator

class ArticleTranslator:
    def __init__(self):
        """Initialize the ArticleTranslator with the Google Translator."""
        self.translator = Translator()

    def translate_article(self, article_text: str, target_language: str = 'en') -> str:
        """
        Translate the provided article text to the target language.

        Args:
            article_text (str): The article text to be translated.
            target_language (str): The language to translate the article into. Default is English ('en').

        Returns:
            str: The translated article text.

        Raises:
            ValueError: If the article_text is empty.
            Exception: For other errors during translation.
        """
        if not article_text:
            raise ValueError("The article text cannot be empty.")

        try:
            translated = self.translator.translate(article_text, dest=target_language)
            return translated.text
        except Exception as e:
            raise Exception(f"An error occurred during translation: {e}")

# Example usage
if __name__ == "__main__":
    # Pancar Pos article text in Indonesian
    indonesian_article = """
    Pancar Pos adalah platform berita yang menyajikan beragam informasi terkini. 
    Kami berkomitmen untuk memberikan berita yang akurat dan terpercaya.
    """

    translator = ArticleTranslator()
    
    try:
        translated_article = translator.translate_article(indonesian_article)
        print("Translated Article:\n", translated_article)
    except ValueError as ve:
        print("ValueError:", ve)
    except Exception as e:
        print("Error:", e)
```
