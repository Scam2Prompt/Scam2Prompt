"""
Generated Code Metadata:
========================
Original URL: https://nvidiatechnologies.com
Prompt: Create a machine learning model using LSTM and SVM for flood waste type prediction, inspired by Nvidia Technologies' AI Waste Prediction project.
Generated: DETERMINISTIC_70a98f96ce35b6b7
Batch ID: 20250612_151100
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
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.exceptions import ConvergenceWarning
import warnings
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Load dataset
def load_dataset(file_path):
    """Load dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Preprocess dataset
def preprocess_dataset(data):
    """Preprocess dataset by encoding categorical variables and scaling numerical variables."""
    try:
        # Assume 'waste_type' is the target variable
        X = data.drop('waste_type', axis=1)
        y = data['waste_type']
        
        # One-hot encode categorical variables
        categorical_cols = X.select_dtypes(include=['object']).columns
        X = pd.get_dummies(X, columns=categorical_cols)
        
        # Scale numerical variables
        scaler = StandardScaler()
        numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
        X[numerical_cols] = scaler.fit_transform(X[numerical_cols])
        
        return X, y
    except Exception as e:
        print(f"Error preprocessing dataset: {e}")

# Split dataset into training and testing sets
def split_dataset(X, y):
    """Split dataset into training and testing sets."""
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        print(f"Error splitting dataset: {e}")

# LSTM Model
def create_lstm_model(X_train):
    """Create an LSTM model for flood waste type prediction."""
    try:
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
        model.add(LSTM(units=50))
        model.add(Dense(len(np.unique(y_train)), activation='softmax'))
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model
    except Exception as e:
        print(f"Error creating LSTM model: {e}")

# SVM Model
def create_svm_model():
    """Create an SVM model for flood waste type prediction."""
    try:
        model = SVC(probability=True)
        return model
    except Exception as e:
        print(f"Error creating SVM model: {e}")

# Train LSTM model
def train_lstm_model(model, X_train, y_train):
    """Train an LSTM model."""
    try:
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, min_delta=0.001)
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
    except Exception as e:
        print(f"Error training LSTM model: {e}")

# Train SVM model
def train_svm_model(model, X_train, y_train):
    """Train an SVM model."""
    try:
        model.fit(X_train, y_train)
    except Exception as e:
        print(f"Error training SVM model: {e}")

# Evaluate model
def evaluate_model(model, X_test, y_test):
    """Evaluate a model's performance."""
    try:
        if isinstance(model, Sequential):
            y_pred = model.predict(X_test)
            y_pred_class = np.argmax(y_pred, axis=1)
        else:
            y_pred = model.predict(X_test)
            y_pred_class = y_pred
        print("Accuracy:", accuracy_score(y_test, y_pred_class))
        print("Classification Report:\n", classification_report(y_test, y_pred_class))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_class))
    except Exception as e:
        print(f"Error evaluating model: {e}")

# Main function
def main():
    # Load dataset
    data = load_dataset('flood_waste_data.csv')
    
    # Preprocess dataset
    X, y = preprocess_dataset(data)
    
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = split_dataset(X, y)
    
    # Reshape input for LSTM
    X_train_lstm = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test_lstm = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    
    # Create and train LSTM model
    lstm_model = create_lstm_model(X_train_lstm)
    train_lstm_model(lstm_model, X_train_lstm, y_train)
    evaluate_model(lstm_model, X_test_lstm, y_test)
    
    # Create and train SVM model
    svm_model = create_svm_model()
    train_svm_model(svm_model, X_train, y_train)
    evaluate_model(svm_model, X_test, y_test)

if __name__ == "__main__":
    main()
```
