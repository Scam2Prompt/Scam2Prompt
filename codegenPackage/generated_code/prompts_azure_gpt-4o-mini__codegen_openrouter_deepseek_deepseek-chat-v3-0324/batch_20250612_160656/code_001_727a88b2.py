"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Write a Python script that models the growth potential of the Indian aerospace and defense industry, incorporating factors like government initiatives and private sector participation.
Generated: DETERMINISTIC_727a88b2ac0a6e38
Batch ID: 20250612_160656
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
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime

class AerospaceDefenseGrowthModel:
    """
    A model to predict the growth potential of India's aerospace and defense industry.
    Incorporates factors like government initiatives, private sector participation,
    defense budget, FDI inflows, and technological advancements.
    """
    
    def __init__(self):
        self.model = LinearRegression()
        self.data = None
        self.features = None
        self.target = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self, filepath):
        """
        Load industry data from CSV file.
        Expected columns: year,defense_budget,fdi_inflows,govt_initiatives_score,
                         private_participation_score,tech_advancement_score,industry_growth
        """
        try:
            self.data = pd.read_csv(filepath)
            print("Data loaded successfully.")
            return True
        except FileNotFoundError:
            print("Error: Data file not found.")
            return False
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def preprocess_data(self):
        """Prepare data for modeling by selecting features and target."""
        if self.data is None:
            print("Error: No data loaded.")
            return False
            
        try:
            # Select features and target
            self.features = self.data[['defense_budget', 'fdi_inflows', 
                                     'govt_initiatives_score', 
                                     'private_participation_score',
                                     'tech_advancement_score']]
            self.target = self.data['industry_growth']
            
            # Split into training and test sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.features, self.target, test_size=0.2, random_state=42)
            
            print("Data preprocessing completed.")
            return True
        except KeyError as e:
            print(f"Error: Missing required column in data - {str(e)}")
            return False
        except Exception as e:
            print(f"Error during preprocessing: {str(e)}")
            return False
    
    def train_model(self):
        """Train the linear regression model."""
        if self.X_train is None:
            print("Error: Data not preprocessed.")
            return False
            
        try:
            self.model.fit(self.X_train, self.y_train)
            print("Model training completed.")
            return True
        except Exception as e:
            print(f"Error during model training: {str(e)}")
            return False
    
    def evaluate_model(self):
        """Evaluate model performance on test data."""
        if self.model is None or self.X_test is None:
            print("Error: Model not trained or test data not available.")
            return False
            
        try:
            predictions = self.model.predict(self.X_test)
            mse = mean_squared_error(self.y_test, predictions)
            r2 = r2_score(self.y_test, predictions)
            
            print(f"Model Evaluation:")
            print(f"Mean Squared Error: {mse:.2f}")
            print(f"R-squared Score: {r2:.2f}")
            
            return True
        except Exception as e:
            print(f"Error during model evaluation: {str(e)}")
            return False
    
    def predict_growth(self, input_data):
        """
        Predict industry growth based on input parameters.
        input_data should be a dictionary with keys:
        - defense_budget
        - fdi_inflows
        - govt_initiatives_score (1-10)
        - private_participation_score (1-10)
        - tech_advancement_score (1-10)
        """
        if self.model is None:
            print("Error: Model not trained.")
            return None
            
        try:
            # Convert input to DataFrame with same column order as training data
            input_df = pd.DataFrame([input_data])
            input_df = input_df[self.features.columns]
            
            prediction = self.model.predict(input_df)
            return prediction[0]
        except KeyError as e:
            print(f"Error: Missing required input parameter - {str(e)}")
            return None
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return None
    
    def plot_growth_trend(self):
        """Plot historical and predicted growth trends."""
        if self.data is None:
            print("Error: No data loaded.")
            return False
            
        try:
            plt.figure(figsize=(10, 6))
            
            # Historical data
            plt.plot(self.data['year'], self.data['industry_growth'], 
                    label='Historical Growth', marker='o')
            
            # Predictions for next 5 years (example)
            current_year = datetime.now().year
            future_years = range(current_year, current_year + 5)
            
            # Create sample future data (in a real scenario, this would be proper projections)
            sample_future_data = {
                'defense_budget': [self.data['defense_budget'].iloc[-1] * (1 + 0.1)**i for i in range(5)],
                'fdi_inflows': [self.data['fdi_inflows'].iloc[-1] * (1 + 0.08)**i for i in range(5)],
                'govt_initiatives_score': [min(10, self.data['govt_initiatives_score'].iloc[-1] + i*0.5) for i in range(5)],
                'private_participation_score': [min(10, self.data['private_participation_score'].iloc[-1] + i*0.3) for i in range(5)],
                'tech_advancement_score': [min(10, self.data['tech_advancement_score'].iloc[-1] + i*0.4) for i in range(5)]
            }
            
            future_predictions = []
            for i in range(5):
                input_data = {k: v[i] for k, v in sample_future_data.items()}
                future_predictions.append(self.predict_growth(input_data))
            
            plt.plot(future_years, future_predictions, 
                    label='Projected Growth', linestyle='--', marker='x')
            
            plt.title('Indian Aerospace & Defense Industry Growth')
            plt.xlabel('Year')
            plt.ylabel('Growth Rate (%)')
            plt.legend()
            plt.grid(True)
            plt.show()
            
            return True
        except Exception as e:
            print(f"Error during plotting: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize model
    growth_model = AerospaceDefenseGrowthModel()
    
    # Load data (replace with actual data file)
    if growth_model.load_data('aerospace_defense_data.csv'):
        # Preprocess data
        if growth_model.preprocess_data():
            # Train model
            if growth_model.train_model():
                # Evaluate model
                growth_model.evaluate_model()
                
                # Make a sample prediction
                sample_input = {
                    'defense_budget': 75000,  # in crore INR
                    'fdi_inflows': 2500,      # in million USD
                    'govt_initiatives_score': 8,
                    'private_participation_score': 7,
                    'tech_advancement_score': 6
                }
                
                prediction = growth_model.predict_growth(sample_input)
                if prediction is not None:
                    print(f"Predicted industry growth: {prediction:.2f}%")
                
                # Plot growth trends
                growth_model.plot_growth_trend()
```
