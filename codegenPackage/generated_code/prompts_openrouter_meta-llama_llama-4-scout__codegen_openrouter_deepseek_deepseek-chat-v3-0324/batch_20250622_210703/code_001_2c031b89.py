"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Write a code snippet to create a simple model for evaluating leadership effectiveness in sports teams using Python and its relevant libraries.
Generated: DETERMINISTIC_2c031b890496ff0a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset generation function
def generate_sample_data(num_samples=1000):
    np.random.seed(42)
    
    # Simulated features
    data = {
        'communication_skills': np.random.normal(7, 1.5, num_samples),
        'decision_making': np.random.normal(6, 1.8, num_samples),
        'team_motivation': np.random.normal(8, 1.2, num_samples),
        'strategic_vision': np.random.normal(6, 1.5, num_samples),
        'experience_years': np.random.randint(1, 20, num_samples),
        'win_percentage': np.random.normal(65, 15, num_samples)
    }
    
    # Calculate effectiveness score (target variable)
    effectiveness_score = (
        0.3 * data['communication_skills'] +
        0.25 * data['decision_making'] +
        0.2 * data['team_motivation'] +
        0.15 * data['strategic_vision'] +
        0.1 * (data['experience_years'] / 20)
    ) + np.random.normal(0, 0.5, num_samples)
    
    # Convert to binary classification (effective/not effective)
    data['is_effective'] = np.where(effectiveness_score > np.median(effectiveness_score), 1, 0)
    
    return pd.DataFrame(data)

# Main function to train and evaluate the model
def train_leadership_model():
    try:
        # Generate sample data
        df = generate_sample_data()
        
        # Split features and target
        X = df.drop('is_effective', axis=1)
        y = df['is_effective']
        
        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Create pipeline with preprocessing and model
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(
                n_estimators=100,
                max_depth=5,
                random_state=42,
                class_weight='balanced'
            ))
        ])
        
        # Train the model
        pipeline.fit(X_train, y_train)
        
        # Evaluate on test set
        y_pred = pipeline.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        
        print(f"Model Accuracy: {accuracy:.2f}")
        print("\nClassification Report:")
        print(report)
        
        # Save the trained model
        joblib.dump(pipeline, 'leadership_model.pkl')
        print("\nModel saved as 'leadership_model.pkl'")
        
        return pipeline
        
    except Exception as e:
        print(f"Error occurred during model training: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    trained_model = train_leadership_model()
```
