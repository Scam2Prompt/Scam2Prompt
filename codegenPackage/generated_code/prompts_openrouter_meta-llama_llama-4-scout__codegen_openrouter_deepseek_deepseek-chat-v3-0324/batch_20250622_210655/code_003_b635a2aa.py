"""
Generated Code Metadata:
========================
Original URL: https://soybiohacker.com
Prompt: Create a library recommendation for a Spanish-language natural language processing (NLP) tool that can analyze user queries related to biohacking and wellness.
Generated: DETERMINISTIC_b635a2aae10f0914
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
Spanish NLP Library for Biohacking and Wellness Queries
Recommended libraries: spaCy with Spanish language model and custom components
"""

import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

class SpanishBiohackingNLP:
    """
    A Spanish NLP processor specialized for biohacking and wellness queries.
    """
    
    def __init__(self):
        """
        Initialize the NLP pipeline with Spanish language model and custom components.
        """
        try:
            # Load Spanish language model
            self.nlp = spacy.load("es_core_news_md")
            
            # Add custom pipeline components
            self._add_custom_components()
            
            # Initialize phrase matcher for biohacking terms
            self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
            self._setup_biohacking_matcher()
            
        except OSError as e:
            raise RuntimeError("Spanish language model not found. Please install it first: "
                             "'python -m spacy download es_core_news_md'") from e
    
    def _add_custom_components(self):
        """Add custom pipeline components to the NLP model."""
        if not self.nlp.has_pipe("biohacking_recognizer"):
            self.nlp.add_pipe("biohacking_recognizer", last=True)
        
        if not self.nlp.has_pipe("wellness_recognizer"):
            self.nlp.add_pipe("wellness_recognizer", last=True)
    
    def _setup_biohacking_matcher(self):
        """Setup phrase matcher with common biohacking terms in Spanish."""
        biohacking_terms = [
            "biohacking", "biorritmo", "crononutrición", "ayuno intermitente",
            "suplementos", "nootrópicos", "microbioma", "quantified self",
            "biomonitorización", "neurofeedback", "biofeedback", "hackeo corporal",
            "optimización cognitiva", "salud cuantificada", "terapia de luz",
            "regulación del sueño", "mejora del rendimiento"
        ]
        
        patterns = [self.nlp(text) for text in biohacking_terms]
        self.matcher.add("BIOHACKING", patterns)
    
    @Language.component("biohacking_recognizer")
    def biohacking_recognizer(doc):
        """
        Custom component to recognize biohacking entities in text.
        """
        matches = self.matcher(doc)
        spans = [Span(doc, start, end, label="BIOHACKING") for match_id, start, end in matches]
        doc.ents = list(doc.ents) + spans
        return doc
    
    @Language.component("wellness_recognizer")
    def wellness_recognizer(doc):
        """
        Custom component to recognize wellness-related entities in text.
        """
        wellness_terms = [
            "bienestar", "salud", "meditación", "mindfulness", "ejercicio",
            "nutrición", "dieta", "descanso", "relajación", "equilibrio",
            "energía", "vitalidad", "autocuidado", "higiene del sueño"
        ]
        
        matcher = PhraseMatcher(doc.vocab, attr="LOWER")
        patterns = [self.nlp(text) for text in wellness_terms]
        matcher.add("WELLNESS", patterns)
        
        matches = matcher(doc)
        spans = [Span(doc, start, end, label="WELLNESS") for match_id, start, end in matches]
        doc.ents = list(doc.ents) + spans
        return doc
    
    def analyze_query(self, text):
        """
        Analyze a Spanish text query related to biohacking and wellness.
        
        Args:
            text (str): Input text in Spanish to analyze
            
        Returns:
            dict: Analysis results including entities, tokens, and sentiment
        """
        try:
            doc = self.nlp(text)
            
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            tokens = [(token.text, token.pos_, token.lemma_) for token in doc]
            
            # Simple sentiment analysis (would need proper implementation)
            sentiment = "neutral"
            if any(token.text.lower() in ["mejorar", "aumentar", "optimizar"] for token in doc):
                sentiment = "positive"
            elif any(token.text.lower() in ["problema", "dificultad", "mal"] for token in doc):
                sentiment = "negative"
            
            return {
                "entities": entities,
                "tokens": tokens,
                "sentiment": sentiment,
                "biohacking_terms": [ent[0] for ent in entities if ent[1] == "BIOHACKING"],
                "wellness_terms": [ent[0] for ent in entities if ent[1] == "WELLNESS"]
            }
            
        except Exception as e:
            raise RuntimeError(f"Error analyzing text: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    try:
        nlp_processor = SpanishBiohackingNLP()
        query = "¿Cómo puedo mejorar mi biorritmo y optimizar mi descanso con biohacking?"
        analysis = nlp_processor.analyze_query(query)
        print(analysis)
    except Exception as e:
        print(f"Error: {str(e)}")
```
