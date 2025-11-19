"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: "What are the key considerations for developing a waiver (perdon) application process for U.S. immigration, and how can a library like NLTK be used for analyzing legal documents related to such cases?"
Generated: DETERMINISTIC_c869f2e7b62d9089
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from collections import defaultdict
import re
import json

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class WaiverDocumentAnalyzer:
    """
    A class to analyze legal documents related to U.S. immigration waivers.
    """
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.common_legal_terms = {
            'waiver', 'inadmissibility', 'forgiveness', 'pardons', 
            'immigration', 'visa', 'uscis', 'form', 'application',
            'grounds', 'removal', 'deportation', '212(h)', '212(i)',
            '601', '601a', 'extreme', 'hardship'
        }
    
    def preprocess_text(self, text):
        """
        Clean and preprocess text for analysis.
        """
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize words
        words = word_tokenize(text)
        # Remove stopwords and lemmatize
        processed_words = [
            self.lemmatizer.lemmatize(word) 
            for word in words 
            if word not in self.stop_words
        ]
        return processed_words
    
    def extract_key_phrases(self, text):
        """
        Extract key phrases from legal text.
        """
        sentences = sent_tokenize(text)
        key_phrases = []
        
        for sentence in sentences:
            words = word_tokenize(sentence)
            tagged = nltk.pos_tag(words)
            
            # Extract noun phrases
            grammar = r"""
                NP: {<DT|PP\$>?<JJ>*<NN.*>+}  # chunk determiner/possessive, adjectives and nouns
            """
            cp = nltk.RegexpParser(grammar)
            tree = cp.parse(tagged)
            
            for subtree in tree.subtrees():
                if subtree.label() == 'NP':
                    phrase = ' '.join(word for word, tag in subtree.leaves())
                    key_phrases.append(phrase)
        
        return key_phrases
    
    def analyze_document(self, document_path):
        """
        Analyze a legal document and return relevant insights.
        """
        try:
            with open(document_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            processed_words = self.preprocess_text(text)
            key_phrases = self.extract_key_phrases(text)
            
            # Calculate word frequencies
            freq_dist = FreqDist(processed_words)
            top_words = freq_dist.most_common(20)
            
            # Find relevant legal terms
            relevant_terms = [
                word for word in processed_words 
                if word in self.common_legal_terms
            ]
            
            # Categorize sentences by relevance
            categorized_sentences = defaultdict(list)
            for sentence in sent_tokenize(text):
                if any(term in sentence.lower() for term in self.common_legal_terms):
                    category = "relevant"
                else:
                    category = "general"
                categorized_sentences[category].append(sentence)
            
            return {
                'top_words': top_words,
                'key_phrases': key_phrases,
                'relevant_terms': list(set(relevant_terms)),
                'categorized_sentences': dict(categorized_sentences)
            }
            
        except FileNotFoundError:
            raise Exception(f"Document not found: {document_path}")
        except Exception as e:
            raise Exception(f"Error analyzing document: {str(e)}")
    
    def generate_report(self, analysis_results, output_path):
        """
        Generate a JSON report from analysis results.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                json.dump(analysis_results, file, indent=4)
            return True
        except Exception as e:
            raise Exception(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    analyzer = WaiverDocumentAnalyzer()
    try:
        results = analyzer.analyze_document("sample_waiver_document.txt")
        analyzer.generate_report(results, "waiver_analysis_report.json")
        print("Analysis completed successfully. Report generated.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
