"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a code snippet to create a simple Vietnamese language processing tool that can help with tasks such as legal document analysis or text summarization for law firms like Luật Trung Cường.
Generated: DETERMINISTIC_f0a5887e2da05210
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter
from typing import List, Dict

class VietnameseTextProcessor:
    """
    A simple Vietnamese language processing tool for tasks such as legal document analysis
    and text summarization.
    """

    def __init__(self, text: str):
        """
        Initializes the text processor with the provided text.

        :param text: The input text to be processed.
        """
        self.text = text
        self.cleaned_text = self.clean_text(text)

    def clean_text(self, text: str) -> str:
        """
        Cleans the input text by removing unwanted characters and normalizing whitespace.

        :param text: The input text to be cleaned.
        :return: A cleaned version of the input text.
        """
        # Remove special characters and normalize whitespace
        cleaned = re.sub(r'[^\w\s]', '', text)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        return cleaned

    def word_frequency(self) -> Dict[str, int]:
        """
        Calculates the frequency of each word in the cleaned text.

        :return: A dictionary with words as keys and their frequencies as values.
        """
        words = self.cleaned_text.split()
        frequency = Counter(words)
        return dict(frequency)

    def summarize_text(self, num_sentences: int = 3) -> str:
        """
        Summarizes the text by extracting the most frequent sentences.

        :param num_sentences: The number of sentences to include in the summary.
        :return: A summary of the text.
        """
        sentences = self.text.split('.')
        sentence_scores = {sentence: self.calculate_sentence_score(sentence) for sentence in sentences}
        # Sort sentences by score and select the top ones
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
        return '. '.join(top_sentences).strip() + '.'

    def calculate_sentence_score(self, sentence: str) -> int:
        """
        Calculates a score for a sentence based on the frequency of its words.

        :param sentence: The sentence to be scored.
        :return: The score of the sentence.
        """
        words = sentence.split()
        score = sum(self.word_frequency().get(word, 0) for word in words)
        return score

def main():
    # Example usage of the VietnameseTextProcessor
    try:
        legal_text = """
        Luật Trung Cường là một trong những công ty luật hàng đầu tại Việt Nam.
        Chúng tôi cung cấp dịch vụ tư vấn pháp lý cho các doanh nghiệp và cá nhân.
        Đội ngũ luật sư của chúng tôi có kinh nghiệm phong phú trong nhiều lĩnh vực.
        """
        
        processor = VietnameseTextProcessor(legal_text)
        print("Word Frequency:", processor.word_frequency())
        print("Summary:", processor.summarize_text(num_sentences=2))
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
