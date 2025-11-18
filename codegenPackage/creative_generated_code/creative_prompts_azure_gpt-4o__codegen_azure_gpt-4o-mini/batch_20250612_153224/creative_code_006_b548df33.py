"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Develop a recommendation system that suggests appropriate social programs for vulnerable populations based on their age, risk level, and geographic location, inspired by Fundación Munasim Kullakita's methodologies.
Generated: DETERMINISTIC_b548df332bb8c7f8
Batch ID: 20250612_153224
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
from sklearn.metrics import accuracy_score
import numpy as np

# Sample data structure for social programs
PROGRAMS_DATA = {
    'age_range': [(0, 17), (18, 24), (25, 59), (60, 120)],
    'risk_level': ['low', 'medium', 'high'],
    'geographic_location': ['urban', 'rural'],
    'program_name': [
        'Youth Empowerment Program',
        'College Readiness Initiative',
        'Employment Skills Training',
        'Senior Wellness Program'
    ],
}

# Sample input data for training (for demonstration, this should be replaced with actual data)
data = {
    'age': [15, 20, 45, 70, 14, 30, 60, 80],
    'risk_level': ['low', 'medium', 'high', 'medium', 'low', 'high', 'medium', 'high'],
    'geographic_location': ['urban', 'urban', 'rural', 'rural', 'urban', 'rural', 'urban', 'rural'],
    'program_index': [0, 1, 2, 3, 0, 2, 3, 3]  # Index corresponds to PROGRAMS_DATA
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Encode categorical data
def encode_features(df):
    df['risk_level'] = df['risk_level'].map({'low': 0, 'medium': 1, 'high': 2})
    df['geographic_location'] = df['geographic_location'].map({'urban': 0, 'rural': 1})
    return df

# Prepare the dataset for training
df_encoded = encode_features(df)
X = df_encoded[['age', 'risk_level', 'geographic_location']]
y = df_encoded['program_index']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy:.2f}')

# Function to recommend programs based on input criteria
def recommend_programs(age, risk_level, location):
    """ 
    Recommend social programs based on age, risk level, and geographic location.
    
    Parameters:
    age (int): Age of the individual.
    risk_level (str): Risk level ('low', 'medium', 'high').
    location (str): Geographic location ('urban', 'rural').
    
    Returns:
    list: Recommended program names.
    """
    try:
        # Encode input
        encoded_location = 0 if location == 'urban' else 1
        encoded_risk = {'low': 0, 'medium': 1, 'high': 2}.get(risk_level, None)

        if encoded_risk is None:
            raise ValueError("Invalid risk level provided.")
        
        # Prepare input for prediction
        input_data = np.array([[age, encoded_risk, encoded_location]])
        
        # Predict program index
        predicted_index = model.predict(input_data)[0]
        
        # Get program name
        program_name = PROGRAMS_DATA['program_name'][predicted_index]
        return [program_name]

    except Exception as e:
        print(f"Error in recommending programs: {e}")
        return []

# Example usage
if __name__ == "__main__":
    age_input = 30
    risk_input = 'high'
    location_input = 'rural'
    
    recommendations = recommend_programs(age_input, risk_input, location_input)
    print("Recommended Programs:", recommendations)
```
