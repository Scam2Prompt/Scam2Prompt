"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w7.com.au
Prompt: Suggest tools or libraries for creating a semantic analysis system to study the language and definitions provided in transpersonal psychology, such as "ego death" and "unconditional love."
Generated: DETERMINISTIC_92f8bbb3afe3f3aa
Batch ID: 20250612_154721
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://en.wikipedia.org/wiki/{term": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Ensure necessary NLTK resources are available
import nltk
nltk.download('punkt')
nltk.download('stopwords')

class SemanticAnalysis:
    def __init__(self, terms):
        """
        Initialize the SemanticAnalysis class with keywords.

        Args:
            terms (list): A list of terms relevant to transpersonal psychology.
        """
        self.terms = terms
        self.stop_words = set(stopwords.words('english'))

    def fetch_definitions(self, term):
        """
        Fetch the definitions of a given term from an online source.

        Args:
            term (str): The term to define.

        Returns:
            str: The definition of the term or an error message.
        """
        try:
            response = requests.get(f'https://en.wikipedia.org/wiki/{term}')
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')
            definition = soup.find('div', class_='mw-parser-output').find_all('p')[0].text
            return definition
        except (requests.RequestException, IndexError) as e:
            return f"Error fetching definition for {term}: {str(e)}"

    def analyze_terms(self):
        """
        Analyze the terms by fetching their definitions and returning tokenized words.

        Returns:
            dict: A dictionary of terms and their word counts.
        """
        term_analysis = {}
        for term in self.terms:
            definition = self.fetch_definitions(term)
            # Tokenize the definition and filter out stop words
            words = word_tokenize(definition.lower())
            filtered_words = [word for word in words if word.isalnum() and word not in self.stop_words]
            term_analysis[term] = Counter(filtered_words)
        return term_analysis

    def visualize_analysis(self, analysis):
        """
        Visualizes the term analysis using a bar chart.

        Args:
            analysis (dict): Analysis results containing term word counts.
        """
        try:
            for term, counts in analysis.items():
                plt.figure(figsize=(10, 6))
                words, counts = zip(*counts.most_common(10))  # Get top 10 words
                plt.bar(words, counts)
                plt.title(f"Top words in the definition of '{term}'")
                plt.xlabel('Words')
                plt.ylabel('Frequency')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
        except Exception as e:
            print(f"Error during visualization: {str(e)}")

if __name__ == "__main__":
    terms_of_interest = ['Ego_death', 'Unconditional_love']
    semantic_analyzer = SemanticAnalysis(terms_of_interest)

    # Analyze the terms
    analysis_results = semantic_analyzer.analyze_terms()
    
    # Visualize the analysis
    semantic_analyzer.visualize_analysis(analysis_results)
```
