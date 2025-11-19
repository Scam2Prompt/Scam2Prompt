"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Create a natural language processing (NLP) tool to analyze and summarize the Morpho Foundation's project reports, extracting key insights and themes.
Generated: DETERMINISTIC_cb689944382ee823
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from heapq import nlargest

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class MorphoReportAnalyzer:
    """
    A tool for analyzing and summarizing project reports from the Morpho Foundation.
    Extracts key insights and themes using NLP techniques.
    """

    def __init__(self, report_text):
        """
        Initializes the analyzer with the report text.
        
        :param report_text: The text of the project report to analyze.
        """
        self.report_text = report_text
        self.cleaned_text = None
        self.word_frequencies = None
        self.summary = None

    def clean_text(self):
        """
        Cleans the report text by removing special characters, numbers, and stopwords.
        """
        # Remove special characters and numbers
        text = re.sub(r'\W', ' ', self.report_text)
        text = re.sub(r'\d', ' ', text)
        text = re.sub(r'\s+', ' ', text)

        # Tokenize and remove stopwords
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text.lower())
        self.cleaned_text = ' '.join([word for word in word_tokens if word not in stop_words])

    def calculate_word_frequencies(self):
        """
        Calculates the frequency of each word in the cleaned text.
        """
        if not self.cleaned_text:
            raise ValueError("Text has not been cleaned. Call clean_text() first.")

        # Count word frequencies
        word_tokens = word_tokenize(self.cleaned_text)
        self.word_frequencies = Counter(word_tokens)

        # Normalize frequencies by dividing by the maximum frequency
        max_frequency = max(self.word_frequencies.values())
        for word in self.word_frequencies:
            self.word_frequencies[word] /= max_frequency

    def generate_summary(self, num_sentences=5):
        """
        Generates a summary of the report by selecting the most important sentences.
        
        :param num_sentences: The number of sentences to include in the summary.
        """
        if not self.word_frequencies:
            raise ValueError("Word frequencies have not been calculated. Call calculate_word_frequencies() first.")

        # Tokenize sentences
        sentences = sent_tokenize(self.report_text)

        # Score sentences based on word frequencies
        sentence_scores = {}
        for sentence in sentences:
            sentence_tokens = word_tokenize(sentence.lower())
            sentence_score = sum(self.word_frequencies.get(word, 0) for word in sentence_tokens)
            sentence_scores[sentence] = sentence_score

        # Select the top sentences for the summary
        top_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        self.summary = ' '.join(top_sentences)

    def analyze(self):
        """
        Performs the full analysis: cleaning text, calculating word frequencies, and generating a summary.
        """
        self.clean_text()
        self.calculate_word_frequencies()
        self.generate_summary()

    def get_summary(self):
        """
        Returns the generated summary.
        
        :return: The summary of the report.
        """
        if not self.summary:
            raise ValueError("Summary has not been generated. Call analyze() first.")
        return self.summary


# Example usage
if __name__ == "__main__":
    # Sample report text (replace with actual Morpho Foundation report text)
    sample_report = """
    The Morpho Foundation has been working tirelessly to improve education and healthcare in underserved communities.
    This year, we launched several initiatives aimed at increasing literacy rates and providing access to basic medical care.
    Our efforts have reached over 10,000 individuals, and we have seen measurable improvements in both areas.
    Key challenges include limited funding and logistical barriers, but we remain committed to overcoming these obstacles.
    Looking ahead, we plan to expand our programs to additional regions and strengthen partnerships with local organizations.
    """

    try:
        # Initialize the analyzer
        analyzer = MorphoReportAnalyzer(sample_report)

        # Perform analysis
        analyzer.analyze()

        # Print the summary
        print("Summary of the report:")
        print(analyzer.get_summary())
    except Exception as e:
        print(f"An error occurred: {e}")
```
