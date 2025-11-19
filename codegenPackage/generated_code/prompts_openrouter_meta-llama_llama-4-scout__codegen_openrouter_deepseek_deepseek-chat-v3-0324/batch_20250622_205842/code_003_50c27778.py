"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a basic AI-powered affirmations builder using natural language processing (NLP) techniques, similar to the tools mentioned in the Action Accelerator Academy's training and learning resources.
Generated: DETERMINISTIC_50c277782b02575a
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

class AffirmationBuilder:
    """
    AI-powered affirmations builder using NLP techniques.
    Generates personalized positive affirmations based on user input.
    """
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.positive_adjectives = [
            'strong', 'confident', 'capable', 'worthy', 'loved',
            'brave', 'resilient', 'talented', 'enough', 'beautiful',
            'powerful', 'successful', 'intelligent', 'creative'
        ]
        self.affirmation_templates = [
            "I am {adjective}.",
            "I embrace my {adjective} nature.",
            "Every day, I become more {adjective}.",
            "I am proud of my {adjective} self.",
            "I choose to be {adjective} today.",
            "My {adjective} spirit shines through.",
            "I acknowledge that I am {adjective}."
        ]
    
    def preprocess_text(self, text):
        """Clean and preprocess input text for analysis."""
        try:
            # Remove special characters and numbers
            text = re.sub(r'[^a-zA-Z\s]', '', text)
            # Tokenize and lemmatize
            tokens = word_tokenize(text.lower())
            lemmatized = [self.lemmatizer.lemmatize(token) for token in tokens]
            # Remove stop words
            filtered = [word for word in lemmatized if word not in self.stop_words]
            return filtered
        except Exception as e:
            print(f"Error preprocessing text: {e}")
            return []
    
    def extract_keywords(self, text):
        """Extract meaningful keywords from user input."""
        try:
            processed = self.preprocess_text(text)
            # Get POS tags and filter for adjectives/nouns
            pos_tags = nltk.pos_tag(processed)
            keywords = [
                word for word, pos in pos_tags 
                if pos.startswith('JJ') or pos.startswith('NN')
            ]
            return keywords
        except Exception as e:
            print(f"Error extracting keywords: {e}")
            return []
    
    def generate_affirmations(self, user_input, num_affirmations=3):
        """
        Generate personalized affirmations based on user input.
        
        Args:
            user_input (str): User's input text describing their goals/feelings
            num_affirmations (int): Number of affirmations to generate
            
        Returns:
            list: Generated affirmations
        """
        try:
            if not user_input or not isinstance(user_input, str):
                raise ValueError("Invalid user input")
            
            keywords = self.extract_keywords(user_input)
            affirmations = []
            
            for _ in range(num_affirmations):
                # Combine user keywords with positive adjectives
                adjective_pool = keywords + self.positive_adjectives
                if not adjective_pool:
                    adjective_pool = self.positive_adjectives
                
                chosen_adj = random.choice(adjective_pool)
                template = random.choice(self.affirmation_templates)
                affirmation = template.format(adjective=chosen_adj)
                affirmations.append(affirmation.capitalize())
            
            return affirmations
        except Exception as e:
            print(f"Error generating affirmations: {e}")
            return ["I am at peace with myself."]  # Fallback affirmation
    
    def enhance_affirmation(self, affirmation):
        """Enhance an existing affirmation with more positive language."""
        try:
            words = word_tokenize(affirmation.lower())
            enhanced = []
            
            for word in words:
                if word in ['am', 'are', 'is']:
                    enhanced.append(random.choice(['deeply', 'truly', 'completely']))
                enhanced.append(word)
                
            return ' '.join(enhanced).capitalize()
        except Exception as e:
            print(f"Error enhancing affirmation: {e}")
            return affirmation

# Example usage
if __name__ == "__main__":
    builder = AffirmationBuilder()
    user_input = "I want to feel more confident in my work and personal life"
    
    print("\nGenerated Affirmations:")
    for affirmation in builder.generate_affirmations(user_input):
        print(f"- {affirmation}")
    
    sample_affirmation = "I am strong"
    enhanced = builder.enhance_affirmation(sample_affirmation)
    print(f"\nEnhanced affirmation: {enhanced}")
```
