"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Create a Python program to analyze and summarize legal documents, focusing on areas like Direito do Trabalho and Direito Tributário, as described on the CAAG website.
Generated: DETERMINISTIC_755455e5ab33ba87
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import defaultdict
import spacy
from typing import Dict, List, Tuple, Optional

# Load Portuguese language model for NLP
try:
    nlp = spacy.load("pt_core_news_lg")
except OSError:
    raise ImportError("Portuguese language model 'pt_core_news_lg' not found. Please install it using:\n"
                     "python -m spacy download pt_core_news_lg")

class LegalDocumentAnalyzer:
    """
    A class to analyze and summarize legal documents with focus on Brazilian labor and tax law.
    """
    
    def __init__(self):
        self.keywords = {
            'labor_law': [
                'contrato de trabalho', 'rescisão', 'fgts', 'horas extras',
                'aviso prévio', 'verba rescisória', 'direitos trabalhistas',
                'clt', 'consolidação das leis do trabalho', 'jornada de trabalho',
                'adicional noturno', 'periculosidade', 'insalubridade'
            ],
            'tax_law': [
                'imposto de renda', 'icms', 'ipi', 'iss', 'simples nacional',
                'lucro presumido', 'lucro real', 'darf', 'dctf', 'sped fiscal',
                'obrigações acessórias', 'crédito tributário', 'dívida ativa',
                'parcelamento', 'isenção', 'imunidade'
            ]
        }
        
        self.section_patterns = {
            'introduction': r'(introdução|preâmbulo|considerações iniciais)',
            'conclusion': r'(conclusão|considerações finais|encerramento)',
            'references': r'(referências|bibliografia|fontes)'
        }
        
    def preprocess_text(self, text: str) -> str:
        """
        Clean and preprocess the document text.
        """
        # Remove multiple spaces and newlines
        text = re.sub(r'\s+', ' ', text).strip()
        # Remove special characters except those used in legal texts
        text = re.sub(r'[^\w\sáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ.,;:!?()-]', '', text)
        return text.lower()
    
    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Identify and extract document sections.
        """
        sections = {}
        for section_name, pattern in self.section_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                sections[section_name] = match.group()
        return sections
    
    def analyze_keywords(self, text: str) -> Dict[str, Dict[str, int]]:
        """
        Count keyword occurrences by category.
        """
        results = {
            'labor_law': defaultdict(int),
            'tax_law': defaultdict(int)
        }
        
        preprocessed_text = self.preprocess_text(text)
        
        for category, keywords in self.keywords.items():
            for keyword in keywords:
                count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', preprocessed_text))
                if count > 0:
                    results[category][keyword] = count
                    
        return results
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract legal entities using NLP.
        """
        doc = nlp(text)
        entities = {
            'LEGISLATION': [],
            'ORG': [],
            'DATE': [],
            'MONEY': [],
            'PERCENT': []
        }
        
        for ent in doc.ents:
            if ent.label_ in entities:
                entities[ent.label_].append(ent.text)
                
        return entities
    
    def generate_summary(self, text: str, max_sentences: int = 5) -> str:
        """
        Generate a summary of the document using key sentences.
        """
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]
        
        if len(sentences) <= max_sentences:
            return ' '.join(sentences)
        
        # Simple heuristic: take first and last sentences
        summary = sentences[:max_sentences//2] + sentences[-(max_sentences//2):]
        return ' '.join(summary)
    
    def analyze_document(self, document_path: str) -> Dict:
        """
        Main method to analyze a legal document.
        """
        try:
            with open(document_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Document not found at path: {document_path}")
        except UnicodeDecodeError:
            raise ValueError("The document encoding is not UTF-8. Please provide a UTF-8 encoded document.")
        
        analysis = {
            'metadata': {
                'document_path': document_path,
                'character_count': len(text),
                'word_count': len(text.split())
            },
            'sections': self.extract_sections(text),
            'keyword_analysis': self.analyze_keywords(text),
            'entities': self.extract_entities(text),
            'summary': self.generate_summary(text)
        }
        
        return analysis

# Example usage
if __name__ == "__main__":
    analyzer = LegalDocumentAnalyzer()
    try:
        result = analyzer.analyze_document("sample_legal_document.txt")
        print("Document Analysis Result:")
        print(result)
    except Exception as e:
        print(f"Error analyzing document: {str(e)}")
```
