"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: How can I automate the process of formatting a manuscript for publishing, taking cues from the comprehensive services provided by Penguin Books Publishers?
Generated: DETERMINISTIC_b9eceff5e3a34629
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# manuscript_formatter.py

import os
import re
from typing import List

class ManuscriptFormatter:
    """
    A class used to automate the process of formatting a manuscript for publishing.

    Attributes:
    ----------
    manuscript_text : str
        The text of the manuscript to be formatted.
    formatting_rules : dict
        A dictionary containing the formatting rules.

    Methods:
    -------
    apply_formatting()
        Applies the formatting rules to the manuscript text.
    format_headings()
        Formats the headings in the manuscript text.
    format_paragraphs()
        Formats the paragraphs in the manuscript text.
    format_font_styles()
        Formats the font styles in the manuscript text.
    """

    def __init__(self, manuscript_text: str):
        """
        Initializes the ManuscriptFormatter object.

        Parameters:
        ----------
        manuscript_text : str
            The text of the manuscript to be formatted.
        """
        self.manuscript_text = manuscript_text
        self.formatting_rules = {
            'heading_prefix': '## ',
            'heading_suffix': '\n\n',
            'paragraph_prefix': '',
            'paragraph_suffix': '\n\n',
            'font_bold': '**',
            'font_italic': '*',
        }

    def apply_formatting(self) -> str:
        """
        Applies the formatting rules to the manuscript text.

        Returns:
        -------
        str
            The formatted manuscript text.
        """
        self.manuscript_text = self.format_headings()
        self.manuscript_text = self.format_paragraphs()
        self.manuscript_text = self.format_font_styles()
        return self.manuscript_text

    def format_headings(self) -> str:
        """
        Formats the headings in the manuscript text.

        Returns:
        -------
        str
            The manuscript text with formatted headings.
        """
        # Use regular expression to find headings (lines that start with '#')
        self.manuscript_text = re.sub(r'^(#+) (.*)$', 
                                      lambda match: self.formatting_rules['heading_prefix'] + 
                                      match.group(2) + self.formatting_rules['heading_suffix'], 
                                      self.manuscript_text, 
                                      flags=re.MULTILINE)
        return self.manuscript_text

    def format_paragraphs(self) -> str:
        """
        Formats the paragraphs in the manuscript text.

        Returns:
        -------
        str
            The manuscript text with formatted paragraphs.
        """
        # Split the manuscript text into paragraphs
        paragraphs: List[str] = self.manuscript_text.split('\n\n')
        
        # Format each paragraph
        formatted_paragraphs: List[str] = []
        for paragraph in paragraphs:
            formatted_paragraph: str = self.formatting_rules['paragraph_prefix'] + paragraph + self.formatting_rules['paragraph_suffix']
            formatted_paragraphs.append(formatted_paragraph)
        
        # Join the formatted paragraphs back into a single string
        self.manuscript_text = ''.join(formatted_paragraphs)
        return self.manuscript_text

    def format_font_styles(self) -> str:
        """
        Formats the font styles in the manuscript text.

        Returns:
        -------
        str
            The manuscript text with formatted font styles.
        """
        # Use regular expression to find bold text (surrounded by '**')
        self.manuscript_text = re.sub(r'\*\*(.*)\*\*', 
                                      lambda match: self.formatting_rules['font_bold'] + match.group(1) + self.formatting_rules['font_bold'], 
                                      self.manuscript_text)
        
        # Use regular expression to find italic text (surrounded by '*')
        self.manuscript_text = re.sub(r'\*(.*)\*', 
                                      lambda match: self.formatting_rules['font_italic'] + match.group(1) + self.formatting_rules['font_italic'], 
                                      self.manuscript_text)
        return self.manuscript_text


def main():
    try:
        manuscript_text: str = """
# Introduction
This is the introduction to the manuscript.

## Background
This is the background of the manuscript.

This is a paragraph of text. **This text is bold**. *This text is italic*.
"""

        formatter: ManuscriptFormatter = ManuscriptFormatter(manuscript_text)
        formatted_text: str = formatter.apply_formatting()
        print(formatted_text)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
