"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Create a decision tree that suggests whether an individual should consider a loan, based on their financial situation, including factors like credit score, income, and existing debts.
Generated: DETERMINISTIC_ff92578e80390a36
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

class LoanDecisionTree:
    """
    A decision tree classifier to suggest whether an individual should consider a loan.
    The model considers credit score, income, and existing debts to make recommendations.
    """
    
    def __init__(self, max_depth=3, random_state=42):
        """
        Initialize the decision tree classifier.
        
        Parameters:
        - max_depth: Maximum depth of the tree
        - random_state: Seed for reproducibility
        """
        self.model = DecisionTreeClassifier(max_depth=max_depth, random_state=random_state)
        self.feature_names = ['credit_score', 'income', 'existing_debts']
        self.target_name = 'consider_loan'
        
    def generate_sample_data(self, num_samples=1000):
        """
        Generate synthetic data for training and testing the model.
        
        Parameters:
        - num_samples: Number of samples to generate
        
        Returns:
        - X: Features (credit_score, income, existing_debts)
        - y: Target (0: don't consider loan, 1: consider loan)
        """
        np.random.seed(42)
        
        # Generate features
        credit_score = np.random.randint(300, 850, size=num_samples)
        income = np.random.randint(20000, 150000, size=num_samples)
        existing_debts = np.random.randint(0, 50000, size=num_samples)
        
        X = np.column_stack((credit_score, income, existing_debts))
        
        # Generate target based on rules
        y = np.zeros(num_samples)
        y[(credit_score >= 650) & (income >= 50000) & (existing_debts <= income * 0.4)] = 1
        
        return X, y
    
    def train(self, X_train, y_train):
        """
        Train the decision tree model.
        
        Parameters:
        - X_train: Training features
        - y_train: Training labels
        """
        try:
            self.model.fit(X_train, y_train)
        except Exception as e:
            print(f"Error during training: {str(e)}")
            raise
    
    def evaluate(self, X_test, y_test):
        """
        Evaluate the model on test data.
        
        Parameters:
        - X_test: Test features
        - y_test: Test labels
        
        Returns:
        - accuracy: Model accuracy
        - report: Classification report
        """
        try:
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            return accuracy, report
        except Exception as e:
            print(f"Error during evaluation: {str(e)}")
            raise
    
    def predict(self, credit_score, income, existing_debts):
        """
        Make a prediction for a single individual.
        
        Parameters:
        - credit_score: Individual's credit score
        - income: Individual's annual income
        - existing_debts: Individual's existing debts
        
        Returns:
        - recommendation: 0 (don't consider) or 1 (consider)
        """
        try:
            features = np.array([[credit_score, income, existing_debts]])
            return self.model.predict(features)[0]
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise
    
    def display_rules(self):
        """
        Print the decision rules of the trained tree.
        """
        try:
            rules = export_text(self.model, feature_names=self.feature_names)
            print("Decision Rules:")
            print(rules)
        except Exception as e:
            print(f"Error displaying rules: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize the loan decision tree
    loan_tree = LoanDecisionTree()
    
    # Generate and split sample data
    X, y = loan_tree.generate_sample_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train and evaluate the model
    loan_tree.train(X_train, y_train)
    accuracy, report = loan_tree.evaluate(X_test, y_test)
    
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)
    
    # Display decision rules
    loan_tree.display_rules()
    
    # Make a sample prediction
    sample_prediction = loan_tree.predict(700, 60000, 20000)
    print(f"\nSample Prediction (700 credit score, $60k income, $20k debts):")
    print("Consider loan" if sample_prediction == 1 else "Don't consider loan")
```
