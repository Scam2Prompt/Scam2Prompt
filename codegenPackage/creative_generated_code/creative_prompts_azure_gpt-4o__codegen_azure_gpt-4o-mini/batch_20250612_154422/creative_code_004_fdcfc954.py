"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Develop a Python program to analyze UPSC previous year question papers and generate thematic tests similar to the Shield IAS Prelims Test Series.
Generated: DETERMINISTIC_fdcfc9548cd009f8
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import os
import json

class UPSCQuestionAnalyzer:
    """
    A class to analyze UPSC previous year question papers and generate thematic tests.
    """

    def __init__(self, data_path):
        """
        Initialize the analyzer with the path to the dataset.

        Parameters:
        data_path (str): The path to the CSV file containing the UPSC questions.
        """
        self.data_path = data_path
        self.questions = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = None

    def load_data(self):
        """
        Load the question data from a CSV file.
        """
        try:
            self.questions = pd.read_csv(self.data_path)
            if 'question' not in self.questions.columns:
                raise ValueError("CSV must contain a 'question' column")
        except Exception as e:
            print(f"Error loading data: {e}")

    def preprocess_questions(self):
        """
        Preprocess the questions by extracting the text for analysis.
        """
        if self.questions is None:
            raise ValueError("No questions loaded. Please load data first.")
        return self.questions['question'].tolist()

    def cluster_questions(self, n_clusters=5):
        """
        Cluster questions into thematic groups using KMeans.

        Parameters:
        n_clusters (int): The number of clusters to form.
        """
        questions_text = self.preprocess_questions()
        tfidf_matrix = self.vectorizer.fit_transform(questions_text)

        # Fit the KMeans model
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.model.fit(tfidf_matrix)

    def generate_tests(self):
        """
        Generate thematic tests based on the clustered questions.
        
        Returns:
        dict: A dictionary where keys are cluster labels and values are lists of questions.
        """
        if self.model is None:
            raise ValueError("Model not trained. Please cluster questions first.")

        clusters = self.model.predict(self.vectorizer.transform(self.questions['question'].tolist()))
        thematic_tests = {}
        
        for cluster in range(self.model.n_clusters):
            thematic_tests[cluster] = self.questions['question'][clusters == cluster].tolist()

        return thematic_tests

    def save_tests(self, tests, output_path):
        """
        Save the generated tests to a JSON file.

        Parameters:
        tests (dict): The thematic tests to save.
        output_path (str): The path to save the JSON file.
        """
        try:
            with open(output_path, 'w') as json_file:
                json.dump(tests, json_file, indent=4)
            print(f"Thematic tests saved to {output_path}")
        except Exception as e:
            print(f"Error saving tests: {e}")

if __name__ == "__main__":
    data_file = "upsc_questions.csv"  # Path to the CSV file containing UPSC questions
    output_file = "thematic_tests.json"  # Output path for the generated tests

    analyzer = UPSCQuestionAnalyzer(data_file)
    analyzer.load_data()
    analyzer.cluster_questions(n_clusters=5)  # Example: generating 5 thematic groups
    tests = analyzer.generate_tests()
    analyzer.save_tests(tests, output_file)
```
