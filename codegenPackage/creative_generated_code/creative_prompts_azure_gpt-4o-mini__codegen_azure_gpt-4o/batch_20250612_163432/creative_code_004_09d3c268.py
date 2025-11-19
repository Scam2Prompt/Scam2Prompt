"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pledge-moso.app
Prompt: What libraries can I use in Python to enhance the detection of phishing websites, and how do I implement them in my project?
Generated: DETERMINISTIC_09d3c268636db92b
Batch ID: 20250612_163432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use Python libraries to detect phishing websites.
In this example, we use the `scikit-learn` library for machine learning, 
the `tldextract` library for domain extraction, and the `requests` library for URL handling.
Ensure you have installed the required libraries using pip:
    pip install scikit-learn tldextract requests
"""

import tldextract
import requests
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Error handling class for URL validation
class InvalidURLException(Exception):
    pass

def validate_url(url):
    """
    Validates a URL string.
    Raises an exception if the URL is invalid.
    """
    if not re.match(r'(https?://)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(/.*)?$', url):
        raise InvalidURLException(f"Invalid URL: {url}")

def extract_features(url):
    """
    Extracts features from a URL using tldextract.
    This function extracts the domain, subdomain, and suffix for use in model training.
    """
    tld_info = tldextract.extract(url)
    return f"{tld_info.subdomain} {tld_info.domain} {tld_info.suffix}"

def load_dataset():
    """
    Loads a phishing website dataset.
    Replace this function with actual dataset retrieval logic.
    """
    # Example dataset format: [{"url": "example.com", "label": 0}, {"url": "phishing-site.com", "label": 1}]
    data = [
        {"url": "example.com", "label": 0},
        {"url": "phishing-site.com", "label": 1},
        {"url": "safe-site.org", "label": 0},
        {"url": "malicious-site.net", "label": 1},
    ]
    urls = [item["url"] for item in data]
    labels = [item["label"] for item in data]
    return urls, labels

def train_model(urls, labels):
    """
    Trains a machine learning model to detect phishing websites using scikit-learn.
    """
    # Extract textual features from the URLs
    vectorizer = TfidfVectorizer()
    url_features = vectorizer.fit_transform([extract_features(url) for url in urls])
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(url_features, labels, test_size=0.2, random_state=42)
    
    # Train a Random Forest classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    
    return model, vectorizer

def predict_url(model, vectorizer, url):
    """
    Predicts whether a given URL is phishing or not using the trained model.
    """
    validate_url(url)  # Ensure the URL is valid
    features = vectorizer.transform([extract_features(url)])
    prediction = model.predict(features)
    return "Phishing" if prediction[0] == 1 else "Safe"

def main():
    """
    Main function to demonstrate phishing website detection.
    """
    # Load dataset and train the model
    urls, labels = load_dataset()
    model, vectorizer = train_model(urls, labels)
    
    # Test the model with a sample URL
    test_url = "phishing-site.com"
    try:
        result = predict_url(model, vectorizer, test_url)
        print(f"The URL '{test_url}' is classified as: {result}")
    except InvalidURLException as e:
        print(e)

if __name__ == "__main__":
    main()
```
