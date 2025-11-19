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
# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import numpy as np

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class SocialImpactHeroClassifier:
    def __init__(self, profiles, initiatives, labels):
        """
        Initialize the classifier with profiles, initiatives, and labels.

        Args:
            profiles (list): List of profiles.
            initiatives (list): List of initiatives.
            labels (list): List of labels.
        """
        self.profiles = profiles
        self.initiatives = initiatives
        self.labels = labels

    def _preprocess_text(self, text):
        """
        Preprocess the text by tokenizing, removing stopwords, and joining.

        Args:
            text (str): Text to preprocess.

        Returns:
            str: Preprocessed text.
        """
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [t for t in tokens if t.lower() not in stop_words]
        return ' '.join(filtered_tokens)

    def _extract_features(self):
        """
        Extract features from profiles and initiatives using TF-IDF.

        Returns:
            pd.DataFrame: Features.
        """
        # Combine profiles and initiatives
        combined_text = [self._preprocess_text(profile + ' ' + initiative) for profile, initiative in zip(self.profiles, self.initiatives)]

        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(max_features=5000)

        # Fit and transform the data
        X = vectorizer.fit_transform(combined_text)

        return X

    def train_model(self):
        """
        Train a random forest classifier.

        Returns:
            RandomForestClassifier: Trained model.
        """
        # Encode labels
        le = LabelEncoder()
        y = le.fit_transform(self.labels)

        # Extract features
        X = self._extract_features()

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

        return model

    def predict(self, model, profile, initiative):
        """
        Make a prediction using the trained model.

        Args:
            model (RandomForestClassifier): Trained model.
            profile (str): Profile.
            initiative (str): Initiative.

        Returns:
            str: Predicted label.
        """
        # Preprocess the text
        text = self._preprocess_text(profile + ' ' + initiative)

        # Transform the text into a TF-IDF vector
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform([text])

        # Make a prediction
        prediction = model.predict(X)

        return prediction[0]

# Example usage
if __name__ == "__main__":
    profiles = ["Profile 1", "Profile 2", "Profile 3"]
    initiatives = ["Initiative 1", "Initiative 2", "Initiative 3"]
    labels = ["Category 1", "Category 2", "Category 1"]

    classifier = SocialImpactHeroClassifier(profiles, initiatives, labels)
    model = classifier.train_model()

    # Make a prediction
    profile = "Profile 1"
    initiative = "Initiative 1"
    predicted_label = classifier.predict(model, profile, initiative)
    print("Predicted Label:", predicted_label)
```
