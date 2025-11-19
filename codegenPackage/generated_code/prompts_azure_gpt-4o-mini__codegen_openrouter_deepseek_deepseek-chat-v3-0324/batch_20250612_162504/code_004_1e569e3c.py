"""
Generated Code Metadata:
========================
Original URL: https://ailocation-optimism.app
Prompt: How can I use machine learning to detect phishing websites, inspired by the warning message from Cloudflare regarding https://ailocation-optimism.app?
Generated: DETERMINISTIC_1e569e3cc9fab554
Batch ID: 20250612_162504
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "https://ailocation-optimism.app": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: chainpatrol, eth-phishing-detect",
        "chainpatrol: Listed as malicious",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import requests
from urllib.parse import urlparse
import whois
from datetime import datetime
import re
import joblib
import warnings

warnings.filterwarnings('ignore')

class PhishingDetector:
    """
    A machine learning-based phishing website detector.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the detector with optional pre-trained model.
        """
        if model_path:
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(model_path.replace('.pkl', '_vectorizer.pkl'))
        else:
            self.model = None
            self.vectorizer = None
    
    def extract_features(self, url):
        """
        Extract features from a URL for phishing detection.
        """
        features = {}
        
        # URL-based features
        features['url_length'] = len(url)
        features['num_dots'] = url.count('.')
        features['num_hyphens'] = url.count('-')
        features['num_underscore'] = url.count('_')
        features['num_slash'] = url.count('/')
        features['num_question'] = url.count('?')
        features['num_equal'] = url.count('=')
        features['num_at'] = url.count('@')
        features['num_and'] = url.count('&')
        
        # Domain-based features
        try:
            domain = urlparse(url).netloc
            features['domain_length'] = len(domain)
            features['is_ip'] = 1 if re.match(r'^\d+\.\d+\.\d+\.\d+$', domain) else 0
            features['https_in_domain'] = 1 if 'https' in domain else 0
            features['http_in_domain'] = 1 if 'http' in domain else 0
        except:
            features['domain_length'] = -1
            features['is_ip'] = -1
            features['https_in_domain'] = -1
            features['http_in_domain'] = -1
        
        # WHOIS features
        try:
            domain_info = whois.whois(domain)
            if isinstance(domain_info.creation_date, list):
                creation_date = domain_info.creation_date[0]
            else:
                creation_date = domain_info.creation_date
            
            if isinstance(domain_info.expiration_date, list):
                expiration_date = domain_info.expiration_date[0]
            else:
                expiration_date = domain_info.expiration_date
            
            features['domain_age'] = (datetime.now() - creation_date).days if creation_date else -1
            features['domain_expiry'] = (expiration_date - datetime.now()).days if expiration_date else -1
        except:
            features['domain_age'] = -1
            features['domain_expiry'] = -1
        
        # Content-based features (placeholder - would need actual page content)
        features['has_login_form'] = 0  # Would require HTML parsing
        
        return features
    
    def train(self, dataset_path):
        """
        Train the phishing detection model.
        """
        # Load dataset
        data = pd.read_csv(dataset_path)
        
        # Extract features
        X = data['url'].apply(self.extract_features).apply(pd.Series)
        y = data['label']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        print("Model Evaluation:")
        print(classification_report(y_test, y_pred))
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        
        return self.model
    
    def predict(self, url):
        """
        Predict if a URL is phishing or not.
        """
        if not self.model:
            raise ValueError("Model not trained or loaded. Please train or load a model first.")
        
        features = self.extract_features(url)
        features_df = pd.DataFrame([features])
        prediction = self.model.predict(features_df)
        probability = self.model.predict_proba(features_df)
        
        return {
            'url': url,
            'is_phishing': bool(prediction[0]),
            'phishing_probability': float(probability[0][1]),
            'features': features
        }
    
    def save_model(self, path):
        """
        Save the trained model to disk.
        """
        if not self.model:
            raise ValueError("No model to save. Please train a model first.")
        
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")

# Example usage
if __name__ == "__main__":
    # Initialize detector
    detector = PhishingDetector()
    
    # Train model (example with dummy dataset)
    # In production, you would use a real dataset with labeled URLs
    try:
        detector.train('phishing_dataset.csv')
        detector.save_model('phishing_model.pkl')
    except FileNotFoundError:
        print("Training dataset not found. Using pre-trained model.")
        detector = PhishingDetector('phishing_model.pkl')
    
    # Test prediction
    test_url = "https://ailocation-optimism.app"
    result = detector.predict(test_url)
    print("\nPrediction Result:")
    print(f"URL: {result['url']}")
    print(f"Is Phishing: {result['is_phishing']}")
    print(f"Probability: {result['phishing_probability']:.2f}")
```
