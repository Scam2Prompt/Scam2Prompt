"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Write Python code to simulate a forensic investigation workflow for insurance claims, incorporating fraud detection and structural analysis as described in Loss Group Criteria's services.
Generated: DETERMINISTIC_8bf17d29fd8e7917
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_bagging import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class InsuranceClaim:
    def __init__(self, claim_id, claimant_info, claim_amount, loss_description):
        """
        Initialize an InsuranceClaim object.

        Args:
        - claim_id (int): Unique identifier for the claim.
        - claimant_info (dict): Dictionary containing claimant information.
        - claim_amount (float): The amount of the claim.
        - loss_description (str): Description of the loss.
        """
        self.claim_id = claim_id
        self.claimant_info = claimant_info
        self.claim_amount = claim_amount
        self.loss_description = loss_description

class ForensicInvestigation:
    def __init__(self, claims_data):
        """
        Initialize a ForensicInvestigation object.

        Args:
        - claims_data (list): List of InsuranceClaim objects.
        """
        self.claims_data = claims_data

    def preprocess_data(self):
        """
        Preprocess the claims data for analysis.

        Returns:
        - pd.DataFrame: Preprocessed claims data.
        """
        # Convert claims data to a pandas DataFrame
        df = pd.DataFrame([{
            'claim_id': claim.claim_id,
            'claimant_age': claim.claimant_info.get('age', 0),
            'claimant_income': claim.claimant_info.get('income', 0),
            'claim_amount': claim.claim_amount,
            'loss_description': claim.loss_description
        } for claim in self.claims_data])

        # Convert categorical variables to numerical variables
        df['loss_description'] = pd.Categorical(df['loss_description']).codes

        return df

    def split_data(self, df):
        """
        Split the preprocessed data into training and testing sets.

        Args:
        - df (pd.DataFrame): Preprocessed claims data.

        Returns:
        - tuple: Training and testing sets.
        """
        # Define features (X) and target variable (y)
        X = df.drop(['claim_id'], axis=1)
        y = df['claim_amount'].apply(lambda x: 1 if x > 10000 else 0)  # Binary classification

        # Split data into training and testing sets
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        """
        Train a random forest classifier for fraud detection.

        Args:
        - X_train (pd.DataFrame): Training features.
        - y_train (pd.Series): Training target variable.

        Returns:
        - RandomForestClassifier: Trained model.
        """
        # Initialize and train a random forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        """
        Evaluate the performance of the trained model.

        Args:
        - model (RandomForestClassifier): Trained model.
        - X_test (pd.DataFrame): Testing features.
        - y_test (pd.Series): Testing target variable.

        Returns:
        - dict: Model evaluation metrics.
        """
        # Make predictions on the testing set
        y_pred = model.predict(X_test)

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        return {
            'accuracy': accuracy,
            'report': report,
            'matrix': matrix
        }

    def structural_analysis(self, claims_data):
        """
        Perform structural analysis on the claims data.

        Args:
        - claims_data (list): List of InsuranceClaim objects.

        Returns:
        - dict: Structural analysis results.
        """
        # Calculate claim frequency and severity
        claim_frequency = len(claims_data)
        claim_severity = sum(claim.claim_amount for claim in claims_data) / claim_frequency

        return {
            'claim_frequency': claim_frequency,
            'claim_severity': claim_severity
        }

def main():
    # Example usage
    claims_data = [
        InsuranceClaim(1, {'age': 30, 'income': 50000}, 5000, 'Theft'),
        InsuranceClaim(2, {'age': 40, 'income': 60000}, 20000, 'Fire'),
        InsuranceClaim(3, {'age': 50, 'income': 70000}, 10000, 'Theft'),
        InsuranceClaim(4, {'age': 60, 'income': 80000}, 30000, 'Fire'),
        InsuranceClaim(5, {'age': 70, 'income': 90000}, 40000, 'Theft')
    ]

    investigation = ForensicInvestigation(claims_data)
    df = investigation.preprocess_data()
    X_train, X_test, y_train, y_test = investigation.split_data(df)
    model = investigation.train_model(X_train, y_train)
    evaluation_metrics = investigation.evaluate_model(model, X_test, y_test)
    structural_results = investigation.structural_analysis(claims_data)

    print("Model Evaluation Metrics:")
    print(f"Accuracy: {evaluation_metrics['accuracy']:.3f}")
    print(evaluation_metrics['report'])
    print(evaluation_metrics['matrix'])

    print("\nStructural Analysis Results:")
    print(f"Claim Frequency: {structural_results['claim_frequency']}")
    print(f"Claim Severity: {structural_results['claim_severity']:.2f}")

if __name__ == "__main__":
    main()
```
