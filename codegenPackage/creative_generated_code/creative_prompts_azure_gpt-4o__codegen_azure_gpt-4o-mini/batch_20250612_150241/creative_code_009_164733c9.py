"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://federalfirstcapitalunion.com
Prompt: Write code to analyze phishing email patterns, inspired by Federal First Capital Union's fraud prevention articles.
Generated: DETERMINISTIC_164733c98216d53e
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

class PhishingEmailAnalyzer:
    def __init__(self, data):
        """
        Initializes the PhishingEmailAnalyzer with the given dataset.

        :param data: A pandas DataFrame containing the email data.
        """
        self.data = data
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def preprocess_data(self):
        """
        Preprocess the email text by removing any unwanted characters and 
        normalizing the data.

        :returns: A DataFrame with processed text and corresponding labels.
        """
        # Remove special characters and lowercase the text
        self.data['cleaned_text'] = self.data['email_text'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x.lower()))
        return self.data[['cleaned_text', 'label']]

    def feature_extraction(self):
        """
        Convert the cleaned email text into a matrix of token counts.

        :returns: A matrix of features derived from the email text.
        """
        return self.vectorizer.fit_transform(self.data['cleaned_text'])

    def train_model(self):
        """
        Train the Naive Bayes model on the email data.

        :raises ValueError: If the data is empty or improperly formatted.
        """
        if self.data.empty or 'cleaned_text' not in self.data.columns:
            raise ValueError("Data must not be empty and should contain 'cleaned_text' column.")

        # Split the dataset into training and testing sets
        X = self.feature_extraction()
        y = self.data['label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Naive Bayes model
        self.model.fit(X_train, y_train)

        # Make predictions and evaluate the model
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Model Accuracy: {accuracy:.2f}")
        print(classification_report(y_test, y_pred))

    def predict(self, new_email):
        """
        Predict whether a new email is phishing or not.

        :param new_email: The email text to be analyzed.
        :returns: Prediction result as a string.
        """
        cleaned_email = re.sub(r'[^a-zA-Z0-9\s]', '', new_email.lower())
        email_vector = self.vectorizer.transform([cleaned_email])
        prediction = self.model.predict(email_vector)

        return "Phishing" if prediction[0] == 1 else "Not Phishing"

# Example usage
if __name__ == "__main__":
    # Load your dataset here as a pandas DataFrame
    # The DataFrame should contain 'email_text' and 'label' columns
    try:
        # Sample data for demonstration; replace it with actual data loading
        sample_data = {
            'email_text': ["Congratulations! You've won a lottery!", "Please verify your account."],
            'label': [1, 0]  # 1 for phishing, 0 for not phishing
        }
        df = pd.DataFrame(sample_data)

        # Initialize and use the PhishingEmailAnalyzer
        analyzer = PhishingEmailAnalyzer(df)
        analyzer.preprocess_data()
        analyzer.train_model()

        # Predict a new email
        new_email = "Claim your prize now!"
        result = analyzer.predict(new_email)
        print(f"Email: '{new_email}' is {result}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
