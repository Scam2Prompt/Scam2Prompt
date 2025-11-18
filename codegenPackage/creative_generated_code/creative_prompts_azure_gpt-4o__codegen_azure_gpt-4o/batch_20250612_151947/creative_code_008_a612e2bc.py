"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socialimpactheroes.com
Prompt: Suggest a machine learning library to predict the popularity of articles on "Social Impact Heroes" based on their titles and categories, and provide example code.
Generated: DETERMINISTIC_a612e2bcfb49067e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Define a function to load and preprocess data
def load_data():
    """
    Load and preprocess the dataset.
    The dataset should contain 'title', 'category', and 'popularity' columns.
    
    Returns:
        X: Features (title + category combined)
        y: Target labels (popularity)
    """
    # Example dataset (replace with actual dataset file path)
    data = pd.DataFrame({
        'title': ['Impact of clean energy', 'Women empowerment programs', 'Climate change and health'],
        'category': ['Environment', 'Social Justice', 'Health'],
        'popularity': [1, 1, 0]  # 1: Popular, 0: Not Popular
    })
    
    # Combine title and category for feature extraction
    data['combined_features'] = data['title'] + " " + data['category']
    
    # Separate features and labels
    X = data['combined_features']
    y = data['popularity']
    
    return X, y

# Load data
X, y = load_data()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the machine learning pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text data to numerical features
    ('model', LogisticRegression(random_state=42))  # Use logistic regression for classification
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions on the test set
y_pred = pipeline.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained pipeline to a file for later use
joblib.dump(pipeline, 'article_popularity_model.pkl')
print("Model saved to 'article_popularity_model.pkl'")

# Usage example for new predictions
def predict_popularity(title, category):
    """
    Predict the popularity of an article based on its title and category.
    
    Args:
        title: Article title (string)
        category: Article category (string)
    
    Returns:
        prediction: Predicted popularity (1: Popular, 0: Not Popular)
    """
    # Load the saved model
    model = joblib.load('article_popularity_model.pkl')
    
    # Combine title and category
    combined_features = title + " " + category
    
    # Predict popularity
    prediction = model.predict([combined_features])[0]
    return prediction

# Example prediction
new_title = "Sustainable agriculture initiatives"
new_category = "Environment"
prediction = predict_popularity(new_title, new_category)
print(f"Predicted Popularity: {'Popular' if prediction == 1 else 'Not Popular'}")
```
