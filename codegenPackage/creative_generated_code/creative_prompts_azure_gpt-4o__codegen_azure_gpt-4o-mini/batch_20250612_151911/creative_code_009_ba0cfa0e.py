"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Generate code to simulate the impact of third-party candidates on election outcomes in McHenry County, Illinois, as discussed on Fair Maps Illinois.
Generated: DETERMINISTIC_ba0cfa0e2aea32e3
Batch ID: 20250612_151911
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Class to simulate election outcomes with third-party candidate impact
class ElectionSimulator:
    def __init__(self, data):
        """
        Initializes the ElectionSimulator with election data.
        
        :param data: DataFrame containing election data with columns 'votes', 'third_party_votes', 'incumbent_votes', and 'challenger_votes'.
        """
        self.data = data
    
    def preprocess_data(self):
        """
        Preprocesses the election data to create features and target labels.
        
        :return: Tuple of features (X) and target labels (y).
        """
        # Creating features and labels
        X = self.data[['third_party_votes', 'incumbent_votes', 'challenger_votes']]
        y = (self.data['votes'] > self.data['votes'].median()).astype(int)  # Binary outcome based on median votes
        return X, y

    def simulate_election(self):
        """
        Simulates the election outcomes based on the input data and prints results.
        """
        X, y = self.preprocess_data()
        
        # Splitting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Setting up the logistic regression model
        model = LogisticRegression()
        
        try:
            # Training the model
            model.fit(X_train, y_train)
            # Making predictions
            y_pred = model.predict(X_test)
            
            # Output the classification report
            print("Classification Report:")
            print(classification_report(y_test, y_pred))
            
            # Confusion Matrix
            cm = confusion_matrix(y_test, y_pred)
            print("Confusion Matrix:")
            print(cm)
            
            # Plotting the results
            self.plot_results(y_test, y_pred)
        except Exception as e:
            print(f"An error occurred during simulation: {e}")

    def plot_results(self, y_test, y_pred):
        """
        Plots the predicted vs actual outcomes.
        
        :param y_test: Actual outcomes from the test set.
        :param y_pred: Predicted outcomes from the model.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(np.arange(len(y_test)), y_test, color='blue', label='Actual', alpha=0.5)
        plt.scatter(np.arange(len(y_pred)), y_pred, color='red', label='Predicted', alpha=0.5)
        plt.title('Election Outcomes: Actual vs Predicted')
        plt.xlabel('Sample Index')
        plt.ylabel('Outcome')
        plt.legend()
        plt.grid()
        plt.show()

# Sample usage
if __name__ == "__main__":
    # Simulated election data for McHenry County
    election_data = {
        'votes': np.random.randint(1000, 10000, 100),
        'third_party_votes': np.random.randint(100, 1000, 100),
        'incumbent_votes': np.random.randint(3000, 7000, 100),
        'challenger_votes': np.random.randint(3000, 7000, 100)
    }
    
    df = pd.DataFrame(election_data)
    
    # Initialize and run the election simulator
    simulator = ElectionSimulator(df)
    simulator.simulate_election()
```
