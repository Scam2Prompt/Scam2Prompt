"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Generate a DBT-based emotional regulation plan for a patient with borderline personality disorder using a natural language processing (NLP) approach and Python."
Generated: DETERMINISTIC_8743c16a1192eaf0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import warnings

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

warnings.filterwarnings('ignore')

class EmotionalRegulationPlanGenerator:
    """
    A DBT-based emotional regulation plan generator using NLP techniques.
    """
    
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.dbt_skills = self._load_dbt_skills()
        self.vectorizer = TfidfVectorizer()
        self._train_vectorizer()
        
    def _load_dbt_skills(self):
        """
        Load DBT skills database with categories and descriptions.
        """
        skills_data = {
            'category': ['Distress Tolerance', 'Emotion Regulation', 'Mindfulness', 'Interpersonal Effectiveness'],
            'skills': [
                ['TIP skills', 'Self-soothing', 'IMPROVE', 'Distract with ACCEPTS'],
                ['Opposite Action', 'PLEASE', 'ABC', 'Check the Facts'],
                ['Observe', 'Describe', 'Participate', 'Non-judgmental stance'],
                ['DEAR MAN', 'GIVE', 'FAST', 'Validation']
            ],
            'descriptions': [
                [
                    "Change body chemistry to reduce extreme emotions",
                    "Comfort yourself through the five senses",
                    "Imagery, Meaning, Prayer, Relaxation, One thing, Vacation, Encouragement",
                    "Activities, Contributing, Comparisons, Emotions, Pushing away, Thoughts, Sensations"
                ],
                [
                    "Act opposite to your current emotional urge",
                    "Treat Physical illness, Eat balanced, Avoid mood-altering drugs, Sleep, Exercise",
                    "Accumulate positive emotions, Build mastery, Cope ahead",
                    "Examine whether your emotional reaction fits the facts"
                ],
                [
                    "Notice your experience without getting caught in it",
                    "Put words on your experience",
                    "Throw yourself completely into the present moment",
                    "Accept reality as it is without evaluation"
                ],
                [
                    "Describe, Express, Assert, Reinforce, Mindful, Appear confident, Negotiate",
                    "Gentle, Interested, Validate, Easy manner",
                    "Fair, Apologies, Stick to values, Truthful",
                    "Acknowledge the validity of someone's experience"
                ]
            ]
        }
        return pd.DataFrame(skills_data)
    
    def _preprocess_text(self, text):
        """
        Preprocess text by lowercasing, removing special chars, lemmatizing, etc.
        """
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)
    
    def _train_vectorizer(self):
        """
        Train TF-IDF vectorizer on DBT skill descriptions.
        """
        processed_descriptions = [' '.join(desc) for desc in self.dbt_skills['descriptions']]
        processed_descriptions = [self._preprocess_text(desc) for desc in processed_descriptions]
        self.vectorizer.fit(processed_descriptions)
    
    def _get_most_relevant_skills(self, user_input, top_n=3):
        """
        Find most relevant DBT skills based on user input.
        """
        processed_input = self._preprocess_text(user_input)
        input_vector = self.vectorizer.transform([processed_input])
        
        skill_vectors = []
        for desc_list in self.dbt_skills['descriptions']:
            processed_desc = self._preprocess_text(' '.join(desc_list))
            skill_vectors.append(processed_desc)
        
        desc_vectors = self.vectorizer.transform(skill_vectors)
        similarities = cosine_similarity(input_vector, desc_vectors)
        
        top_indices = np.argsort(similarities[0])[-top_n:][::-1]
        return self.dbt_skills.iloc[top_indices]
    
    def generate_plan(self, patient_input):
        """
        Generate a personalized DBT-based emotional regulation plan.
        
        Args:
            patient_input (str): Patient's description of their emotional state/situation
            
        Returns:
            dict: Personalized plan with recommended skills and rationale
        """
        try:
            if not patient_input or not isinstance(patient_input, str):
                raise ValueError("Patient input must be a non-empty string")
                
            relevant_skills = self._get_most_relevant_skills(patient_input)
            
            plan = {
                "patient_input": patient_input,
                "recommendations": [],
                "rationale": "Based on your description, these DBT skills may help regulate your emotions:"
            }
            
            for _, row in relevant_skills.iterrows():
                recommendation = {
                    "category": row['category'],
                    "skills": row['skills'],
                    "descriptions": row['descriptions']
                }
                plan["recommendations"].append(recommendation)
            
            return plan
            
        except Exception as e:
            return {
                "error": str(e),
                "message": "Failed to generate emotional regulation plan"
            }

# Example usage
if __name__ == "__main__":
    generator = EmotionalRegulationPlanGenerator()
    
    patient_input = """
    I'm feeling extremely overwhelmed and angry right now. 
    Everything feels like too much and I want to lash out at people.
    """
    
    plan = generator.generate_plan(patient_input)
    print(plan)
```
