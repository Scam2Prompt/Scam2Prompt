"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Recommend a suitable machine learning model for classifying social impact heroes into different categories based on their profiles and initiatives, using features extracted from the website content.
Generated: DETERMINISTIC_3a6e6ba9ad9c1805
Batch ID: 20250622_205603
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HeroClassifier:
    """
    A machine learning pipeline for classifying social impact heroes into categories.
    """
    
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.label_encoder = None
        self.best_model = None
    
    def load_data(self, filepath):
        """
        Load and preprocess the dataset.
        
        Args:
            filepath (str): Path to the CSV file containing hero profiles
            
        Returns:
            tuple: (text_features, labels)
        """
        try:
            df = pd.read_csv(filepath)
            logger.info("Data loaded successfully")
            
            # Preprocessing
            df = df.dropna()
            text_features = df['profile_text'].values
            labels = df['category'].values
            
            return text_features, labels
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def preprocess_labels(self, labels):
        """
        Encode string labels to numerical values.
        
        Args:
            labels (array-like): Array of string labels
            
        Returns:
            array: Encoded labels
        """
        self.label_encoder = LabelEncoder()
        encoded_labels = self.label_encoder.fit_transform(labels)
        return encoded_labels
    
    def train_model(self, X, y):
        """
        Train and evaluate multiple classifiers, then select the best one.
        
        Args:
            X (array-like): Text features
            y (array-like): Encoded labels
        """
        try:
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Define pipeline
            pipeline = Pipeline([
                ('tfidf', TfidfVectorizer(max_features=5000)),
                ('clf', RandomForestClassifier())
            ])
            
            # Define models to try
            param_grid = [
                {
                    'clf': [RandomForestClassifier(n_estimators=100)],
                    'clf__max_depth': [10, 20, None],
                    'clf__min_samples_split': [2, 5]
                },
                {
                    'clf': [SVC(kernel='linear')],
                    'clf__C': [0.1, 1, 10]
                },
                {
                    'clf': [MultinomialNB()],
                    'clf__alpha': [0.1, 0.5, 1.0]
                }
            ]
            
            # Grid search
            grid_search = GridSearchCV(
                pipeline,
                param_grid,
                cv=5,
                n_jobs=-1,
                verbose=1
            )
            
            logger.info("Starting model training...")
            grid_search.fit(X_train, y_train)
            
            self.best_model = grid_search.best_estimator_
            logger.info(f"Best model: {grid_search.best_params_}")
            
            # Evaluate
            y_pred = self.best_model.predict(X_test)
            logger.info(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
            logger.info("\nClassification Report:\n" + classification_report(y_test, y_pred))
            
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise
    
    def save_model(self, filepath):
        """
        Save the trained model to disk.
        
        Args:
            filepath (str): Path to save the model
        """
        try:
            joblib.dump({
                'model': self.best_model,
                'label_encoder': self.label_encoder
            }, filepath)
            logger.info(f"Model saved to {filepath}")
        except Exception as e:
            logger.error(f"Error saving model: {str(e)}")
            raise
    
    def load_saved_model(self, filepath):
        """
        Load a saved model from disk.
        
        Args:
            filepath (str): Path to the saved model
        """
        try:
            saved_data = joblib.load(filepath)
            self.best_model = saved_data['model']
            self.label_encoder = saved_data['label_encoder']
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise
    
    def predict_category(self, text):
        """
        Predict the category for new hero profile text.
        
        Args:
            text (str): Hero profile text
            
        Returns:
            str: Predicted category
        """
        try:
            if not self.best_model:
                raise ValueError("Model not trained or loaded")
                
            prediction = self.best_model.predict([text])[0]
            return self.label_encoder.inverse_transform([prediction])[0]
        except Exception as e:
            logger.error(f"Error during prediction: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    classifier = HeroClassifier()
    
    try:
        # Load and preprocess data
        X, y = classifier.load_data("hero_profiles.csv")
        encoded_y = classifier.preprocess_labels(y)
        
        # Train and save model
        classifier.train_model(X, encoded_y)
        classifier.save_model("hero_classifier.joblib")
        
        # Example prediction
        new_profile = "This hero works on environmental conservation projects..."
        prediction = classifier.predict_category(new_profile)
        print(f"Predicted category: {prediction}")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```
