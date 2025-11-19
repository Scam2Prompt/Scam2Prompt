"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocats.com
Prompt: Write a code snippet in Python that could be used to create a simple decision tree for determining the best course of action in family law cases, considering factors such as the presence of children and the preferred method of conflict resolution, as described on the Majeli Avocat website.
Generated: DETERMINISTIC_bf145b5b29215a18
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

# Sample data for family law cases
data = {
    'has_children': [1, 1, 0, 0, 1, 0, 1, 0],
    'preferred_resolution': ['mediation', 'litigation', 'mediation', 'litigation', 
                             'mediation', 'litigation', 'mediation', 'litigation'],
    'best_course_of_action': ['mediation', 'litigation', 'mediation', 'litigation', 
                              'mediation', 'litigation', 'mediation', 'litigation']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
df['preferred_resolution'] = df['preferred_resolution'].map({'mediation': 0, 'litigation': 1})
df['best_course_of_action'] = df['best_course_of_action'].map({'mediation': 0, 'litigation': 1})

# Features and target variable
X = df[['has_children', 'preferred_resolution']]
y = df['best_course_of_action']

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)

# Fit the model
try:
    clf.fit(X, y)
except Exception as e:
    print(f"Error during model fitting: {e}")

# Function to predict the best course of action
def predict_course_of_action(has_children, preferred_resolution):
    """
    Predicts the best course of action based on the presence of children and preferred resolution method.
    
    :param has_children: int (1 for yes, 0 for no)
    :param preferred_resolution: str ('mediation' or 'litigation')
    :return: str indicating the best course of action
    """
    # Encode the preferred resolution
    resolution_encoded = 0 if preferred_resolution == 'mediation' else 1
    
    # Prepare input for prediction
    input_data = [[has_children, resolution_encoded]]
    
    try:
        prediction = clf.predict(input_data)
        return 'mediation' if prediction[0] == 0 else 'litigation'
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

# Example usage
if __name__ == "__main__":
    result = predict_course_of_action(1, 'mediation')
    print(f"The recommended course of action is: {result}")

    # Display the decision tree rules
    rules = export_text(clf, feature_names=list(X.columns))
    print("\nDecision Tree Rules:\n", rules)
```
