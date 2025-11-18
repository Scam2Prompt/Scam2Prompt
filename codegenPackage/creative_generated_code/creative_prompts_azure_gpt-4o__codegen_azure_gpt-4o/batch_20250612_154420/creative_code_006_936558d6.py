"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burtonwright.net
Prompt: Suggest a Python library for analyzing HVAC system noise patterns (e.g., furnace sounds like "rattle, clang, boom") and provide example code to classify these noises and recommend appropriate repairs.
Generated: DETERMINISTIC_936558d67684a526
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script uses Python's `scikit-learn` library to analyze HVAC system noise patterns.
The example demonstrates a noise classification model to identify common sounds (e.g., "rattle", "clang", "boom")
and recommends appropriate repairs based on the classification result.

Dependencies:
- scikit-learn
- numpy
- pandas

Ensure these libraries are installed before running the script.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset for HVAC noise patterns and recommended repairs
data = {
    "NoisePattern": [
        "rattle in the ducts", "loud clang from the furnace",
        "boom sound when ignition starts", "rattling noise from pipes",
        "metallic clang near blower", "deep boom sound from combustion chamber"
    ],
    "RepairRecommendation": [
        "Inspect duct connections", "Check furnace assembly for loose parts",
        "Inspect ignition system", "Secure loose piping",
        "Inspect blower for damage", "Inspect combustion chamber"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Preprocessing: Encode the repair recommendations as target labels
df["Label"] = df["RepairRecommendation"].astype('category').cat.codes

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df["NoisePattern"], df["Label"], test_size=0.2, random_state=42
)

# Convert text patterns into numerical features using CountVectorizer
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vec, y_train)

# Evaluate the model on the test set
y_pred = classifier.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Noise classification function
def classify_noise(noise_pattern):
    """
    Classifies the noise pattern and suggests a repair recommendation.
    
    Args:
        noise_pattern (str): Description of the HVAC noise pattern.
    
    Returns:
        str: Recommended repair action based on the noise pattern.
    """
    try:
        # Transform the noise pattern into numerical features
        noise_vec = vectorizer.transform([noise_pattern])
        
        # Predict the label
        label = classifier.predict(noise_vec)[0]
        
        # Get the corresponding repair recommendation
        recommendation = df["RepairRecommendation"].iloc[df["Label"] == label].values[0]
        return recommendation
    
    except Exception as e:
        return f"Error occurred during classification: {e}"

# Example usage: Classify a new noise pattern
new_noise = "rattling noise in the ducts"
repair_action = classify_noise(new_noise)
print(f"Noise: {new_noise}\nRecommended Repair: {repair_action}")
```
