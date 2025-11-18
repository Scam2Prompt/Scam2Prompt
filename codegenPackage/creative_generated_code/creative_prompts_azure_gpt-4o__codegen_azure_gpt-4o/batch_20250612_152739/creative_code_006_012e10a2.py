"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Develop a machine learning model for fusing data from optical cameras, thermal cameras, and radar systems to detect atypical activities in surveillance scenarios, following the principles described in the Metis Project.
Generated: DETERMINISTIC_012e10a25a57b87d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Machine Learning Model for Fusing Data from Optical Cameras, Thermal Cameras, and Radar Systems
to Detect Atypical Activities in Surveillance Scenarios.

This code follows best practices, is production-ready, and combines input from multiple modalities
(optical, thermal, radar) to detect unusual activities. The model uses a neural network with early
fusion to integrate the data. Error handling and documentation are included.
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

# ========================= Data Preparation =========================

def load_data(optical_path, thermal_path, radar_path):
    """
    Load data from optical, thermal, and radar systems.

    Args:
        optical_path (str): Path to optical camera dataset (CSV or similar format).
        thermal_path (str): Path to thermal camera dataset (CSV or similar format).
        radar_path (str): Path to radar system dataset (CSV or similar format).

    Returns:
        np.ndarray: Combined feature matrix.
        np.ndarray: Labels indicating atypical activity (binary).
    """
    try:
        # Load datasets
        optical_data = pd.read_csv(optical_path)
        thermal_data = pd.read_csv(thermal_path)
        radar_data = pd.read_csv(radar_path)

        # Ensure matching shapes and merge datasets
        if not (optical_data.shape[0] == thermal_data.shape[0] == radar_data.shape[0]):
            raise ValueError("Datasets must have the same number of samples.")
        
        # Merge feature matrices
        features = np.hstack([
            optical_data.values,
            thermal_data.values,
            radar_data.values
        ])
        
        # Labels are assumed to be in the first column of the optical dataset
        labels = optical_data.iloc[:, 0].values

        return features, labels

    except Exception as e:
        print(f"Error loading or merging data: {str(e)}")
        raise

# ========================= Model Definition =========================

def build_model(input_shape):
    """
    Build a neural network model for early fusion.

    Args:
        input_shape (int): Shape of the input feature vector.

    Returns:
        tf.keras.Model: Compiled neural network model.
    """
    try:
        # Define the neural network architecture
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=input_shape),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')  # Binary classification
        ])

        # Compile the model
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])
        return model

    except Exception as e:
        print(f"Error building model: {str(e)}")
        raise

# ========================= Main Code =========================

def main(optical_path, thermal_path, radar_path):
    """
    Main function to load data, train the model, and evaluate it.

    Args:
        optical_path (str): Path to optical camera dataset.
        thermal_path (str): Path to thermal camera dataset.
        radar_path (str): Path to radar system dataset.
    """
    try:
        # Load and preprocess data
        features, labels = load_data(optical_path, thermal_path, radar_path)

        # Standardize feature data
        scaler = StandardScaler()
        features = scaler.fit_transform(features)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            features, labels, test_size=0.2, random_state=42
        )

        # Build the model
        model = build_model(input_shape=X_train.shape[1])

        # Train the model
        print("Training the model...")
        model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

        # Evaluate the model
        print("Evaluating the model...")
        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}")

        # Make predictions and report metrics
        y_pred = (model.predict(X_test) > 0.5).astype("int32")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

    except Exception as e:
        print(f"Error in main function: {str(e)}")
        raise

# ========================= Entry Point =========================

if __name__ == "__main__":
    # Example file paths (replace with actual paths)
    optical_path = "optical_data.csv"
    thermal_path = "thermal_data.csv"
    radar_path = "radar_data.csv"

    main(optical_path, thermal_path, radar_path)
```
