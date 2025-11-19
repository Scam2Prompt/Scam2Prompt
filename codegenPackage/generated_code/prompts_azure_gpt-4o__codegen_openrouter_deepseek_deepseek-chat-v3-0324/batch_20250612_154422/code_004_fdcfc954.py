"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a Python program to analyze UPSC previous year question papers and generate thematic tests similar to the Shield IAS Prelims Test Series.
Generated: DETERMINISTIC_fdcfc9548cd009f8
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import re
import json
import random
from collections import defaultdict
from typing import List, Dict, Tuple, Optional
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class UPSCQuestionAnalyzer:
    """
    A class to analyze UPSC previous year question papers and generate thematic tests.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the analyzer with data directory.
        
        Args:
            data_dir (str): Directory containing question papers in JSON format.
                           Default is "data".
        """
        self.data_dir = data_dir
        self.questions = []
        self.themes = []
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        
    def load_questions(self) -> None:
        """
        Load questions from JSON files in the data directory.
        """
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError(f"Data directory '{self.data_dir}' not found.")
            
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.data_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        self.questions.extend(data['questions'])
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error loading {filename}: {str(e)}")
                    continue
                    
        if not self.questions:
            raise ValueError("No questions loaded. Check data files.")
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text by removing stopwords, lemmatizing, and cleaning.
        
        Args:
            text (str): Input text to preprocess.
            
        Returns:
            str: Preprocessed text.
        """
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Tokenize and lowercase
        tokens = word_tokenize(text.lower())
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and len(token) > 2]
        return ' '.join(tokens)
    
    def cluster_questions(self, n_clusters: int = 10) -> None:
        """
        Cluster questions into themes using KMeans clustering.
        
        Args:
            n_clusters (int): Number of clusters/themes to create. Default is 10.
        """
        if not self.questions:
            raise ValueError("No questions available for clustering.")
            
        # Extract and preprocess question texts
        texts = [q['question'] for q in self.questions]
        preprocessed_texts = [self.preprocess_text(text) for text in texts]
        
        # Vectorize using TF-IDF
        vectorizer = TfidfVectorizer(max_features=1000)
        X = vectorizer.fit_transform(preprocessed_texts)
        
        # Cluster using KMeans
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans.fit(X)
        
        # Assign themes to questions
        for i, q in enumerate(self.questions):
            q['theme'] = int(kmeans.labels_[i])
        
        # Store unique themes
        self.themes = list(range(n_clusters))
    
    def generate_test_series(self, num_tests: int = 5, questions_per_test: int = 20) -> List[Dict]:
        """
        Generate thematic test series.
        
        Args:
            num_tests (int): Number of tests to generate. Default is 5.
            questions_per_test (int): Questions per test. Default is 20.
            
        Returns:
            List[Dict]: List of generated tests with questions.
        """
        if not self.themes:
            raise ValueError("Themes not identified. Run cluster_questions first.")
            
        # Group questions by theme
        theme_questions = defaultdict(list)
        for q in self.questions:
            theme_questions[q['theme']].append(q)
            
        tests = []
        for _ in range(num_tests):
            test = {
                'title': f"Thematic Test {len(tests) + 1}",
                'questions': []
            }
            
            # Calculate questions per theme (distribute evenly)
            questions_per_theme = max(1, questions_per_test // len(self.themes))
            remaining_questions = questions_per_test % len(self.themes)
            
            selected_themes = random.sample(self.themes, len(self.themes))
            
            for i, theme in enumerate(selected_themes):
                # Adjust for remaining questions
                current_q_count = questions_per_theme + (1 if i < remaining_questions else 0)
                
                # Get random questions from this theme
                available_questions = theme_questions.get(theme, [])
                if len(available_questions) < current_q_count:
                    current_q_count = len(available_questions)
                
                test['questions'].extend(
                    random.sample(available_questions, current_q_count)
                )
                
                # Break if we've reached the desired count
                if len(test['questions']) >= questions_per_test:
                    break
            
            tests.append(test)
            
        return tests
    
    def save_test_series(self, tests: List[Dict], output_dir: str = "output") -> None:
        """
        Save generated test series to JSON files.
        
        Args:
            tests (List[Dict]): List of tests to save.
            output_dir (str): Output directory. Default is "output".
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        for i, test in enumerate(tests):
            filename = os.path.join(output_dir, f"test_{i+1}.json")
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(test, f, indent=2)
            except IOError as e:
                print(f"Error saving test {i+1}: {str(e)}")

def main():
    try:
        # Initialize analyzer
        analyzer = UPSCQuestionAnalyzer()
        
        # Load questions
        analyzer.load_questions()
        print(f"Loaded {len(analyzer.questions)} questions.")
        
        # Cluster questions into themes
        analyzer.cluster_questions(n_clusters=12)
        print(f"Identified {len(analyzer.themes)} themes.")
        
        # Generate test series
        tests = analyzer.generate_test_series(num_tests=5, questions_per_test=20)
        print(f"Generated {len(tests)} test papers.")
        
        # Save tests
        analyzer.save_test_series(tests)
        print("Test series saved to 'output' directory.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
