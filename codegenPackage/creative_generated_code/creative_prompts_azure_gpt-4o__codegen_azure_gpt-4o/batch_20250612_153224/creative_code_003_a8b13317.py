"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Create a Python script to analyze text-based responses from children participating in workshops on civic awareness, as described in the Fundación Patricio Aylwin's initiative.
Generated: DETERMINISTIC_a8b133179993bcaa
Batch ID: 20250612_153224
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
from typing import List, Dict, Tuple


def load_responses(file_path: str) -> List[str]:
    """
    Load text-based responses from a file.
    
    :param file_path: Path to the text file containing responses.
    :return: List of responses loaded from the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            responses = file.readlines()
        return [response.strip() for response in responses if response.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path and try again.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def clean_text(text: str) -> str:
    """
    Clean text by removing punctuation and converting to lowercase.

    :param text: Original text.
    :return: Cleaned text.
    """
    return re.sub(r'[^\w\s]', '', text).lower()


def analyze_word_frequency(responses: List[str]) -> Dict[str, int]:
    """
    Analyze word frequency in the responses.

    :param responses: List of text responses.
    :return: Dictionary with words as keys and their frequencies as values.
    """
    cleaned_responses = [clean_text(response) for response in responses]
    all_words = " ".join(cleaned_responses).split()
    word_counts = Counter(all_words)
    return dict(word_counts)


def most_frequent_words(word_frequencies: Dict[str, int], top_n: int) -> List[Tuple[str, int]]:
    """
    Get the most frequent words from the word frequency dictionary.

    :param word_frequencies: Dictionary with word frequencies.
    :param top_n: Number of top words to return.
    :return: List of tuples containing words and their frequencies.
    """
    return sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)[:top_n]


def main():
    """
    Main function to load responses, analyze them, and display results.
    """
    # Path to the text file containing responses
    file_path = 'responses.txt'

    # Load responses from the file
    responses = load_responses(file_path)
    if not responses:
        return

    # Analyze word frequency
    word_frequencies = analyze_word_frequency(responses)

    # Get the top 10 most frequent words
    top_words = most_frequent_words(word_frequencies, top_n=10)

    # Display results
    print("Top 10 Most Frequent Words in Responses:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
