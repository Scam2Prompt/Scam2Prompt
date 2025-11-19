"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Write a Python script to implement a gift recommendation system like GiftGo, which analyzes user data to suggest ideal gifts.
Generated: DETERMINISTIC_7abe52ee4d2c61bc
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gift_recommendation_system.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

class GiftRecommendationSystem:
    def __init__(self, user_data_file, gift_data_file):
        """
        Initialize the gift recommendation system.

        Args:
            user_data_file (str): Path to the user data CSV file.
            gift_data_file (str): Path to the gift data CSV file.
        """
        self.user_data = pd.read_csv(user_data_file)
        self.gift_data = pd.read_csv(gift_data_file)
        self.model = None

    def _preprocess_data(self):
        """
        Preprocess the user and gift data.
        """
        # Handle missing values
        self.user_data.fillna(self.user_data.mean(), inplace=True)
        self.gift_data.fillna(self.gift_data.mean(), inplace=True)

        # Encode categorical variables
        categorical_cols = self.user_data.select_dtypes(include=['object']).columns
        self.user_data[categorical_cols] = self.user_data[categorical_cols].apply(lambda x: pd.factorize(x)[0])

        categorical_cols = self.gift_data.select_dtypes(include=['object']).columns
        self.gift_data[categorical_cols] = self.gift_data[categorical_cols].apply(lambda x: pd.factorize(x)[0])

    def train_model(self):
        """
        Train a random forest classifier to predict gift preferences.
        """
        self._preprocess_data()

        # Merge user and gift data
        merged_data = pd.merge(self.user_data, self.gift_data, on='user_id')

        # Define features and target
        X = merged_data.drop(['gift_id', 'preference'], axis=1)
        y = merged_data['preference']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test)
        print("Model Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

    def recommend_gifts(self, user_id, num_recommendations=5):
        """
        Recommend gifts for a given user.

        Args:
            user_id (int): The ID of the user.
            num_recommendations (int): The number of gift recommendations.

        Returns:
            list: A list of recommended gift IDs.
        """
        if self.model is None:
            raise ValueError("Model not trained")

        # Get user features
        user_features = self.user_data[self.user_data['user_id'] == user_id].drop('user_id', axis=1)

        # Predict gift preferences
        gift_preferences = self.model.predict_proba(user_features)

        # Get gift IDs and their corresponding probabilities
        gift_ids = self.gift_data['gift_id']
        gift_probabilities = gift_preferences[0]

        # Sort gift IDs by their probabilities and return top N recommendations
        sorted_gift_ids = gift_ids[np.argsort(-gift_probabilities)]
        return sorted_gift_ids[:num_recommendations].tolist()

if __name__ == "__main__":
    user_data_file = 'user_data.csv'
    gift_data_file = 'gift_data.csv'

    gift_system = GiftRecommendationSystem(user_data_file, gift_data_file)
    gift_system.train_model()

    user_id = 1
    recommended_gifts = gift_system.recommend_gifts(user_id)
    print("Recommended Gifts for User", user_id, ":", recommended_gifts)
```
