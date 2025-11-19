"""
Generated Code Metadata:
========================
Original URL: https://guapaaltejer.com
Prompt: Develop a machine learning model to recommend knitting or crochet patterns based on a user's skill level, yarn preferences, and project type.
Generated: DETERMINISTIC_18c2edb3fa117d15
Batch ID: 20250622_210703
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
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

class PatternRecommender:
    """
    A machine learning model to recommend knitting/crochet patterns based on user preferences.
    """
    
    def __init__(self, data_path=None):
        """
        Initialize the recommender system.
        
        Args:
            data_path (str): Path to the dataset file. If None, uses default sample data.
        """
        self.model = None
        self.vectorizer = None
        self.scaler = None
        self.features = ['skill_level', 'yarn_weight', 'project_type', 'pattern_name']
        self.target = 'recommendation_score'
        
        if data_path and os.path.exists(data_path):
            self.data = pd.read_csv(data_path)
        else:
            self._create_sample_data()
            
        self._preprocess_data()
        
    def _create_sample_data(self):
        """Create sample dataset if no data file is provided."""
        sample_data = {
            'pattern_name': [
                'Basic Scarf', 'Cable Knit Sweater', 'Amigurumi Bear', 
                'Lace Shawl', 'Simple Beanie', 'Fair Isle Mittens'
            ],
            'skill_level': ['beginner', 'intermediate', 'intermediate', 'advanced', 'beginner', 'advanced'],
            'yarn_weight': ['medium', 'medium', 'light', 'light', 'bulky', 'light'],
            'project_type': ['scarf', 'sweater', 'toy', 'shawl', 'hat', 'mittens'],
            'description': [
                'A simple scarf pattern for beginners',
                'Intermediate cable knit sweater pattern',
                'Cute amigurumi bear crochet pattern',
                'Delicate lace shawl for advanced knitters',
                'Easy beanie pattern for beginners',
                'Colorwork mittens with fair isle technique'
            ],
            'recommendation_score': [5, 3, 4, 2, 5, 1]
        }
        self.data = pd.DataFrame(sample_data)
    
    def _preprocess_data(self):
        """Preprocess the data for model training."""
        # Convert categorical features to numerical
        self.data['skill_level'] = self.data['skill_level'].map({
            'beginner': 0,
            'intermediate': 1,
            'advanced': 2
        })
        
        # One-hot encode yarn_weight and project_type
        self.data = pd.get_dummies(self.data, columns=['yarn_weight', 'project_type'])
        
        # Vectorize pattern descriptions
        self.vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.vectorizer.fit_transform(self.data['description'])
        
        # Combine features
        numerical_features = self.data[['skill_level'] + 
                                      [col for col in self.data.columns 
                                       if col.startswith('yarn_weight_') or 
                                       col.startswith('project_type_')]]
        
        # Scale numerical features
        self.scaler = MinMaxScaler()
        scaled_features = self.scaler.fit_transform(numerical_features)
        
        # Combine all features
        self.X = np.hstack([scaled_features, tfidf_matrix.toarray()])
        self.y = self.data[self.target]
        
    def train_model(self):
        """
        Train the recommendation model using Random Forest Classifier.
        """
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
    
    def save_model(self, model_path='pattern_recommender.joblib'):
        """
        Save the trained model to disk.
        
        Args:
            model_path (str): Path to save the model file.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
            
        joblib.dump({
            'model': self.model,
            'vectorizer': self.vectorizer,
            'scaler': self.scaler,
            'features': self.features
        }, model_path)
    
    def load_model(self, model_path='pattern_recommender.joblib'):
        """
        Load a trained model from disk.
        
        Args:
            model_path (str): Path to the saved model file.
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
            
        saved_data = joblib.load(model_path)
        self.model = saved_data['model']
        self.vectorizer = saved_data['vectorizer']
        self.scaler = saved_data['scaler']
        self.features = saved_data['features']
    
    def recommend_patterns(self, user_input, top_n=3):
        """
        Recommend patterns based on user input.
        
        Args:
            user_input (dict): Dictionary containing user preferences.
            top_n (int): Number of top recommendations to return.
            
        Returns:
            list: List of recommended pattern names.
        """
        if not self.model:
            raise ValueError("Model has not been trained or loaded.")
            
        # Prepare user input
        input_df = pd.DataFrame([user_input])
        
        # Process skill level
        input_df['skill_level'] = input_df['skill_level'].map({
            'beginner': 0,
            'intermediate': 1,
            'advanced': 2
        })
        
        # One-hot encode yarn_weight and project_type
        input_df = pd.get_dummies(input_df)
        
        # Ensure all columns are present
        for col in [c for c in self.data.columns 
                   if c.startswith('yarn_weight_') or 
                   c.startswith('project_type_')]:
            if col not in input_df.columns:
                input_df[col] = 0
        
        # Scale numerical features
        numerical_features = input_df[['skill_level'] + 
                                     [col for col in input_df.columns 
                                      if col.startswith('yarn_weight_') or 
                                      col.startswith('project_type_')]]
        scaled_features = self.scaler.transform(numerical_features)
        
        # Vectorize description if provided
        description = user_input.get('description', '')
        tfidf_vector = self.vectorizer.transform([description])
        
        # Combine features
        X_user = np.hstack([scaled_features, tfidf_vector.toarray()])
        
        # Get predictions
        scores = self.model.predict_proba(X_user)[0]
        
        # Get top recommendations
        top_indices = np.argsort(scores)[-top_n:][::-1]
        recommendations = self.data.iloc[top_indices]['pattern_name'].tolist()
        
        return recommendations

# Example usage
if __name__ == "__main__":
    # Initialize and train the model
    recommender = PatternRecommender()
    recommender.train_model()
    recommender.save_model()
    
    # Load the model (simulating a production scenario)
    new_recommender = PatternRecommender()
    new_recommender.load_model()
    
    # Make recommendations
    user_preferences = {
        'skill_level': 'beginner',
        'yarn_weight': 'medium',
        'project_type': 'scarf',
        'description': 'looking for an easy scarf pattern'
    }
    
    recommendations = new_recommender.recommend_patterns(user_preferences)
    print("Recommended patterns:", recommendations)
```
