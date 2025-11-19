"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap.depillama.com
Prompt: Implement a script that generates a summary of the key themes in "Space Odyssey," emphasizing human curiosity and the discovery of the cosmos.
Generated: DETERMINISTIC_8fa04e6aec4955ad
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from collections import Counter
from typing import List, Dict

def load_text(file_path: str) -> str:
    """
    Load text from a file.

    Parameters:
        file_path (str): Path to the text file.

    Returns:
        str: Content of the file as a single string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' was not found.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the file: {e}")

def clean_text(text: str) -> str:
    """
    Clean text by removing unwanted characters and converting it to lowercase.

    Parameters:
        text (str): Original text.

    Returns:
        str: Cleaned text.
    """
    # Remove non-alphanumeric characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    return cleaned_text.lower()

def extract_key_themes(text: str, theme_keywords: List[str], top_n: int = 5) -> Dict[str, int]:
    """
    Extract key themes based on predefined keywords.

    Parameters:
        text (str): Text to analyze.
        theme_keywords (List[str]): List of keywords representing themes.
        top_n (int): Number of top themes to return.

    Returns:
        Dict[str, int]: Themes and their frequencies sorted by frequency (top N).
    """
    # Tokenize the text into individual words
    words = text.split()
    # Count occurrences of theme keywords in the text
    keyword_counts = Counter(word for word in words if word in theme_keywords)
    # Return the top N themes sorted by frequency
    return dict(keyword_counts.most_common(top_n))

def main():
    """
    Main function to generate a summary of key themes in the text "Space Odyssey."
    """
    # Define the path to the text file (update this path as needed)
    file_path = 'space_odyssey.txt'

    # Predefined theme keywords related to human curiosity and cosmos exploration
    theme_keywords = [
        'curiosity', 'discovery', 'human', 'exploration', 'cosmos', 'space',
        'science', 'future', 'technology', 'unknown', 'alien', 'journey'
    ]

    try:
        # Load and clean the text
        text = load_text(file_path)
        cleaned_text = clean_text(text)

        # Extract key themes from the text
        key_themes = extract_key_themes(cleaned_text, theme_keywords)

        # Print the summary of key themes
        print("Key Themes in 'Space Odyssey':")
        for theme, count in key_themes.items():
            print(f"{theme.capitalize()}: {count}")
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == '__main__':
    main()
```
