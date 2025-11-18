"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxosrew.com
Prompt: Develop a machine learning model to recommend automotive accessories based on user preferences and vehicle type, using the product categories listed on paxosrew.com.
Generated: DETERMINISTIC_d8d70e9b3e95adcd
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Load the data - assuming a CSV file structure typical for user preferences and vehicle types
# The CSV should contain columns: 'user_id', 'vehicle_type', 'accessory_category', 'preference_score'
data_url = 'path_to_your_data.csv'  # Replace with the actual path
data = pd.read_csv(data_url)

# Check for missing values and handle them appropriately
if data.isnull().sum().any():
    raise ValueError("Data contains missing values. Please clean the data before proceeding.")

# Define features and target variable
X = data[['vehicle_type', 'preference_score']]  # Features
y = data['accessory_category']  # Target variable

# Convert categorical variables to numeric using one-hot encoding
X = pd.get_dummies(X, columns=['vehicle_type'], drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Accuracy: ", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model to disk for future use
joblib.dump(model, 'automotive_accessory_recommender.pkl')

# Function to recommend accessories based on user input
def recommend_accessories(vehicle_type, preference_score):
    """
    Recommend automotive accessories based on vehicle type and preference score.
    
    Parameters:
    vehicle_type (str): The type of vehicle (e.g., SUV, sedan).
    preference_score (float): The user's preference score for accessories (scale of 1-10).
    
    Returns:
    list: Recommended accessory categories.
    """
    # Create a DataFrame for input
    input_data = pd.DataFrame({'preference_score': [preference_score]})
    
    # One-hot encode vehicle type
    vehicle_type_encoded = pd.get_dummies(pd.Series(vehicle_type), prefix='vehicle_type')
    input_data = pd.concat([input_data, vehicle_type_encoded], axis=1)
    
    # Align the input data with training data columns
    input_data = input_data.reindex(columns=X.columns, fill_value=0)
    
    # Predict accessory category
    recommended_category = model.predict(input_data)
    
    return recommended_category.tolist()

# Example usage (commented out; uncomment to use):
# recommended = recommend_accessories('SUV', 8)
# print("Recommended Accessory Category:", recommended)
```
