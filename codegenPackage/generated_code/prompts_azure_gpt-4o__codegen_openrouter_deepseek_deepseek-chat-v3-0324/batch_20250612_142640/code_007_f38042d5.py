"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Develop a machine learning model to predict the best financing options for businesses based on asset type and industry sector, using examples like those provided by Rhino Asset Finance.
Generated: DETERMINISTIC_f38042d545070e6d
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import json

class FinancingOptionPredictor:
    """
    A machine learning model to predict the best financing options for businesses
    based on asset type and industry sector.
    """
    
    def __init__(self, model_path=None):
        """
        Initialize the predictor.
        
        Args:
            model_path (str, optional): Path to a pre-trained model. Defaults to None.
        """
        self.model = None
        self.label_encoders = {}
        self.scaler = None
        self.feature_columns = ['asset_type', 'industry_sector', 'business_age', 'revenue']
        
        if model_path:
            self.load_model(model_path)
    
    def preprocess_data(self, data):
        """
        Preprocess the input data for training or prediction.
        
        Args:
            data (pd.DataFrame): Input data containing features.
            
        Returns:
            pd.DataFrame: Preprocessed data ready for model.
        """
        processed_data = data.copy()
        
        # Encode categorical features
        for col in ['asset_type', 'industry_sector']:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                self.label_encoders[col].fit(processed_data[col])
            processed_data[col] = self.label_encoders[col].transform(processed_data[col])
        
        # Scale numerical features
        if not self.scaler:
            self.scaler = StandardScaler()
            self.scaler.fit(processed_data[['business_age', 'revenue']])
        
        processed_data[['business_age', 'revenue']] = self.scaler.transform(
            processed_data[['business_age', 'revenue']]
        )
        
        return processed_data[self.feature_columns]
    
    def train(self, data_path, test_size=0.2, random_state=42):
        """
        Train the financing option prediction model.
        
        Args:
            data_path (str): Path to the training data CSV file.
            test_size (float, optional): Size of test set. Defaults to 0.2.
            random_state (int, optional): Random seed. Defaults to 42.
            
        Returns:
            dict: Training metrics including accuracy and classification report.
        """
        try:
            # Load and prepare data
            data = pd.read_csv(data_path)
            X = self.preprocess_data(data)
            y = data['best_financing_option']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Train model
            self.model = RandomForestClassifier(
                n_estimators=100, random_state=random_state
            )
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            return {
                'accuracy': accuracy,
                'classification_report': report
            }
            
        except Exception as e:
            raise RuntimeError(f"Error during training: {str(e)}")
    
    def predict(self, input_data):
        """
        Predict the best financing option for given input data.
        
        Args:
            input_data (dict or pd.DataFrame): Input features for prediction.
            
        Returns:
            dict: Prediction results with probabilities.
        """
        if self.model is None:
            raise RuntimeError("Model not trained or loaded. Please train or load a model first.")
        
        try:
            # Convert dict to DataFrame if needed
            if isinstance(input_data, dict):
                input_df = pd.DataFrame([input_data])
            else:
                input_df = input_data.copy()
            
            # Preprocess and predict
            processed_data = self.preprocess_data(input_df)
            prediction = self.model.predict(processed_data)
            probabilities = self.model.predict_proba(processed_data)
            
            # Get class names
            class_names = self.model.classes_
            
            # Format results
            results = []
            for i, pred in enumerate(prediction):
                result = {
                    'predicted_financing_option': pred,
                    'probabilities': {
                        class_names[j]: float(probabilities[i][j])
                        for j in range(len(class_names))
                    }
                }
                results.append(result)
            
            return results[0] if isinstance(input_data, dict) else results
            
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {str(e)}")
    
    def save_model(self, output_dir):
        """
        Save the trained model and preprocessing objects.
        
        Args:
            output_dir (str): Directory to save the model files.
        """
        try:
            # Save model
            joblib.dump(self.model, f"{output_dir}/model.joblib")
            
            # Save label encoders
            for col, encoder in self.label_encoders.items():
                joblib.dump(encoder, f"{output_dir}/{col}_encoder.joblib")
            
            # Save scaler
            if self.scaler:
                joblib.dump(self.scaler, f"{output_dir}/scaler.joblib")
            
            # Save feature columns
            with open(f"{output_dir}/feature_columns.json", 'w') as f:
                json.dump(self.feature_columns, f)
                
        except Exception as e:
            raise RuntimeError(f"Error saving model: {str(e)}")
    
    def load_model(self, model_path):
        """
        Load a pre-trained model and preprocessing objects.
        
        Args:
            model_path (str): Directory containing the model files.
        """
        try:
            # Load model
            self.model = joblib.load(f"{model_path}/model.joblib")
            
            # Load label encoders
            for col in ['asset_type', 'industry_sector']:
                encoder_path = f"{model_path}/{col}_encoder.joblib"
                self.label_encoders[col] = joblib.load(encoder_path)
            
            # Load scaler
            scaler_path = f"{model_path}/scaler.joblib"
            self.scaler = joblib.load(scaler_path)
            
            # Load feature columns
            with open(f"{model_path}/feature_columns.json", 'r') as f:
                self.feature_columns = json.load(f)
                
        except Exception as e:
            raise RuntimeError(f"Error loading model: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = FinancingOptionPredictor()
    
    # Train model (assuming data.csv exists with appropriate columns)
    try:
        metrics = predictor.train("data.csv")
        print("Training completed successfully!")
        print(f"Accuracy: {metrics['accuracy']:.2f}")
        
        # Save model
        predictor.save_model("saved_model")
        print("Model saved successfully!")
        
        # Example prediction
        test_data = {
            "asset_type": "Construction Equipment",
            "industry_sector": "Construction",
            "business_age": 5,
            "revenue": 1000000
        }
        
        prediction = predictor.predict(test_data)
        print("\nPrediction results:")
        print(json.dumps(prediction, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
