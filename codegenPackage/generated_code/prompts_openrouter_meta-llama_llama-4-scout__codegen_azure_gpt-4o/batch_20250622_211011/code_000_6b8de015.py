"""
Generated Code Metadata:
========================
Original URL: https://allocating-optimism.app
Prompt: Write a Python script to detect phishing sites using machine learning algorithms and Cloudflare API.
Generated: DETERMINISTIC_6b8de015168297d1
Batch ID: 20250622_211011
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://phishing.xyz": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://legit-site.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.cloudflare.com/client/v4/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://malicious.xyz": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cloudflare API configuration
CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4/"
CLOUDFLARE_API_KEY = "your_cloudflare_api_key"
CLOUDFLARE_EMAIL = "your_email@example.com"

# Function to check domain reputation using Cloudflare API
def check_domain_reputation(domain):
    """
    Check domain reputation using Cloudflare API.
    :param domain: Domain name to check.
    :return: Boolean indicating if the domain is suspicious.
    """
    headers = {
        "X-Auth-Email": CLOUDFLARE_EMAIL,
        "X-Auth-Key": CLOUDFLARE_API_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(f"{CLOUDFLARE_API_URL}zones", headers=headers)
        response.raise_for_status()
        # Simulate domain reputation check (Cloudflare API does not directly provide this)
        # In production, replace this with actual API logic
        return domain.endswith(".xyz")  # Example heuristic for suspicious domains
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking domain reputation: {e}")
        return False

# Load dataset (replace with actual phishing dataset)
def load_dataset():
    """
    Load phishing dataset.
    :return: DataFrame containing URLs and labels.
    """
    data = {
        "url": [
            "http://example.com",
            "http://phishing.xyz",
            "http://legit-site.com",
            "http://malicious.xyz"
        ],
        "label": [0, 1, 0, 1]  # 0: Legitimate, 1: Phishing
    }
    return pd.DataFrame(data)

# Feature extraction
def extract_features(data):
    """
    Extract features from URLs using CountVectorizer.
    :param data: DataFrame containing URLs.
    :return: Feature matrix.
    """
    vectorizer = CountVectorizer(analyzer="char", ngram_range=(3, 5))
    features = vectorizer.fit_transform(data["url"])
    return features, vectorizer

# Train machine learning model
def train_model(features, labels):
    """
    Train a machine learning model to detect phishing sites.
    :param features: Feature matrix.
    :param labels: Labels (0: Legitimate, 1: Phishing).
    :return: Trained model.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(features, labels)
    return model

# Main function
def main():
    """
    Main function to detect phishing sites.
    """
    logging.info("Loading dataset...")
    data = load_dataset()

    logging.info("Extracting features...")
    features, vectorizer = extract_features(data)

    logging.info("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(features, data["label"], test_size=0.2, random_state=42)

    logging.info("Training model...")
    model = train_model(X_train, y_train)

    logging.info("Evaluating model...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    logging.info(f"Model accuracy: {accuracy:.2f}")

    # Example domain check
    domain = "http://phishing.xyz"
    logging.info(f"Checking domain reputation for: {domain}")
    is_suspicious = check_domain_reputation(domain)
    logging.info(f"Domain '{domain}' is {'suspicious' if is_suspicious else 'legitimate'}.")

    # Predict phishing status
    logging.info("Predicting phishing status...")
    domain_features = vectorizer.transform([domain])
    prediction = model.predict(domain_features)
    logging.info(f"Domain '{domain}' is {'phishing' if prediction[0] == 1 else 'legitimate'}.")

if __name__ == "__main__":
    main()
```
