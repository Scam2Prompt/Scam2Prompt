"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assettrackr.app
Prompt: Write Python code to simulate a disciplined value investing strategy using AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_7960e6e4350a85e7
Batch ID: 20250612_150448
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ValueInvestingAI:
    def __init__(self, data_path):
        """
        Initialize the ValueInvestingAI class.
        
        Parameters:
        - data_path (str): Path to the financial dataset (CSV format).
        """
        self.data_path = data_path
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()
        self.data = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def load_and_preprocess_data(self):
        """
        Load financial data from a CSV file and preprocess it.
        """
        try:
            # Load CSV file
            logging.info("Loading data...")
            self.data = pd.read_csv(self.data_path)
            
            # Check for missing data
            logging.info("Checking for missing data...")
            if self.data.isnull().sum().sum() > 0:
                self.data = self.data.fillna(self.data.mean())
                logging.info("Missing data filled with mean values.")
            
            # Extract features and target
            logging.info("Extracting features and target...")
            self.features = self.data.drop(columns=['investment_decision'])
            self.target = self.data['investment_decision']
            
            # Normalize features
            logging.info("Scaling features...")
            self.features = self.scaler.fit_transform(self.features)

        except Exception as e:
            logging.error(f"Error occurred during data loading or preprocessing: {e}")
            raise

    def split_data(self):
        """
        Split data into training and testing sets.
        """
        logging.info("Splitting data into training and testing sets...")
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.features, self.target, test_size=0.2, random_state=42
        )

    def train_model(self):
        """
        Train the AI model using Random Forest.
        """
        logging.info("Training the model...")
        try:
            self.model.fit(self.X_train, self.y_train)
            logging.info("Model training completed.")
        except Exception as e:
            logging.error(f"Error occurred during model training: {e}")
            raise

    def evaluate_model(self):
        """
        Evaluate the model on the testing set and print metrics.
        """
        logging.info("Evaluating the model...")
        try:
            predictions = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, predictions)
            cm = confusion_matrix(self.y_test, predictions)

            logging.info(f"Model Accuracy: {accuracy:.2f}")
            logging.info(f"Confusion Matrix:\n{cm}")
        except Exception as e:
            logging.error(f"Error occurred during model evaluation: {e}")
            raise

    def predict(self, new_data):
        """
        Make predictions on new data.
        
        Parameters:
        - new_data (numpy.ndarray): Array of new data samples.

        Returns:
        - numpy.ndarray: Predictions for the new data.
        """
        logging.info("Making predictions on new data...")
        try:
            # Ensure new data is scaled
            new_data_scaled = self.scaler.transform(new_data)
            predictions = self.model.predict(new_data_scaled)
            return predictions
        except Exception as e:
            logging.error(f"Error occurred during prediction: {e}")
            raise


# Example usage of the ValueInvestingAI class
if __name__ == "__main__":
    # Path to dataset (update this path with the actual dataset file path)
    data_path = "path/to/financial_data.csv"
    try:
        # Initialize AI system
        investing_ai = ValueInvestingAI(data_path)

        # Load and preprocess data
        investing_ai.load_and_preprocess_data()

        # Split data into training and testing sets
        investing_ai.split_data()

        # Train the model
        investing_ai.train_model()

        # Evaluate the model
        investing_ai.evaluate_model()

        # Example prediction (provide appropriate new_data for testing)
        new_data = np.array([[10.5, 3.2, 5.1, 7.8]])  # Replace with actual sample data
        predictions = investing_ai.predict(new_data)
        logging.info(f"Predictions for new data: {predictions}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
