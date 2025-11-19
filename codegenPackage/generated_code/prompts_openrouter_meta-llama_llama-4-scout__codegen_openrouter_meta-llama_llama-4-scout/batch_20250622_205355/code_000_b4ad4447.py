"""
Generated Code Metadata:
========================
Original URL: https://dbridge.live
Prompt: "Generate a simple Italian translation for a website under construction page using Python."
Generated: DETERMINISTIC_b4ad44477c041200
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# italian_under_construction.py

class UnderConstructionPage:
    def __init__(self, language):
        """
        Initialize the under construction page with a given language.

        Args:
            language (str): The language of the page (e.g., 'it' for Italian).
        """
        self.language = language
        self.translations = {
            'it': {
                'title': 'Sito web in costruzione',
                'heading': 'Il nostro sito web è attualmente in costruzione',
                'message': 'Ci scusiamo per l\'inconveniente. Torna presto a visitarci.',
                'back_link': 'Torna alla homepage'
            }
            # Add more languages as needed
        }

    def get_translation(self):
        """
        Get the translation for the given language.

        Returns:
            dict: The translation for the given language.

        Raises:
            ValueError: If the language is not supported.
        """
        try:
            return self.translations[self.language]
        except KeyError:
            raise ValueError(f"Unsupported language: {self.language}")

    def render_page(self):
        """
        Render the under construction page.

        Returns:
            str: The HTML content of the page.
        """
        translation = self.get_translation()
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{translation['title']}</title>
        </head>
        <body>
            <h1>{translation['heading']}</h1>
            <p>{translation['message']}</p>
            <p><a href="/">{translation['back_link']}</a></p>
        </body>
        </html>
        """
        return html


def main():
    language = 'it'
    page = UnderConstructionPage(language)
    try:
        html = page.render_page()
        print(html)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    import sys
    main()
```
