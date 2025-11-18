"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Create a script to analyze customer testimonials and extract key phrases about golf grip quality, similar to the feedback showcased on the Longhui Golf website.
Generated: DETERMINISTIC_0839d511e6e2ac5b
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import spacy
from collections import Counter
from typing import List, Tuple


def load_testimonials(file_path: str) -> List[str]:
    """
    Load customer testimonials from a text file.

    :param file_path: Path to the file containing testimonials.
    :return: List of strings where each string is a testimonial.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except IOError as e:
        print(f"Error: Unable to read file {file_path}. {e}")
        return []


def extract_key_phrases(testimonials: List[str], keywords: List[str]) -> List[Tuple[str, int]]:
    """
    Extract key phrases related to specified keywords from customer testimonials.

    :param testimonials: List of customer testimonials.
    :param keywords: List of keywords to focus on (e.g., "grip", "quality").
    :return: List of tuples containing the key phrases and their frequency.
    """
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    key_phrase_counter = Counter()

    for testimonial in testimonials:
        doc = nlp(testimonial)
        for sentence in doc.sents:
            # Check if sentence contains any of the keywords
            if any(keyword.lower() in sentence.text.lower() for keyword in keywords):
                # Extract noun phrases
                for np in sentence.noun_chunks:
                    key_phrase_counter[np.text.lower()] += 1

    # Return the key phrases sorted by frequency
    return key_phrase_counter.most_common()


def save_key_phrases_to_file(key_phrases: List[Tuple[str, int]], output_path: str) -> None:
    """
    Save extracted key phrases to a file.

    :param key_phrases: List of key phrases with their frequencies.
    :param output_path: Path to the output file.
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            for phrase, count in key_phrases:
                file.write(f"{phrase}: {count}\n")
        print(f"Key phrases successfully saved to {output_path}")
    except IOError as e:
        print(f"Error: Unable to write to file {output_path}. {e}")


def main():
    """
    Main function to analyze testimonials and extract key phrases.
    """
    # Define input and output file paths
    input_file_path = "customer_testimonials.txt"  # Replace with your input file path
    output_file_path = "key_phrases.txt"  # Replace with your desired output file path

    # Define keywords to extract phrases related to
    keywords = ["grip", "quality"]

    # Load testimonials
    testimonials = load_testimonials(input_file_path)

    if not testimonials:
        print("No testimonials found. Exiting program.")
        return

    # Extract key phrases
    key_phrases = extract_key_phrases(testimonials, keywords)

    # Save key phrases to a file
    save_key_phrases_to_file(key_phrases, output_file_path)


if __name__ == "__main__":
    main()
```
