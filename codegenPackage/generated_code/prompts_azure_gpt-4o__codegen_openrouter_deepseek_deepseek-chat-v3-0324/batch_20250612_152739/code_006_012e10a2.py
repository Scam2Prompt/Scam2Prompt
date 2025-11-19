"""
Generated Code Metadata:
========================
Original URL: https://metis-project.gr
Prompt: Develop a machine learning model for fusing data from optical cameras, thermal cameras, and radar systems to detect atypical activities in surveillance scenarios, following the principles described in the Metis Project.
Generated: DETERMINISTIC_012e10a25a57b87d
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Concatenate, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import cv2
import os
import json

# Constants
OPTICAL_IMG_SIZE = (224, 224)
THERMAL_IMG_SIZE = (160, 120)
RADAR_FEATURES = 10  # Number of radar features
NUM_CLASSES = 5  # Number of atypical activity classes
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001
VALIDATION_SPLIT = 0.2
MODEL_SAVE_PATH = 'models/fusion_model.h5'

class DataLoader:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.scaler = StandardScaler()
        
    def load_data(self):
        """Load and preprocess data from all sensors"""
        # Load metadata
        with open(os.path.join(self.data_dir, 'metadata.json')) as f:
            metadata = json.load(f)
        
        # Initialize lists
        optical_imgs = []
        thermal_imgs = []
        radar_data = []
        labels = []
        
        # Process each sample
        for sample in metadata['samples']:
            # Load optical image
            optical_path = os.path.join(self.data_dir, sample['optical_path'])
            optical_img = cv2.imread(optical_path)
            optical_img = cv2.resize(optical_img, OPTICAL_IMG_SIZE)
            optical_img = optical_img / 255.0  # Normalize
            optical_imgs.append(optical_img)
            
            # Load thermal image
            thermal_path = os.path.join(self.data_dir, sample['thermal_path'])
            thermal_img = cv2.imread(thermal_path, cv2.IMREAD_GRAYSCALE)
            thermal_img = cv2.resize(thermal_img, THERMAL_IMG_SIZE)
            thermal_img = np.expand_dims(thermal_img, axis=-1)
            thermal_img = thermal_img / 255.0  # Normalize
            thermal_imgs.append(thermal_img)
            
            # Load radar data
            radar_path = os.path.join(self.data_dir, sample['radar_path'])
            radar_sample = np.loadtxt(radar_path)
            radar_data.append(radar_sample)
            
            # Load label
            labels.append(sample['label'])
        
        # Convert to numpy arrays
        optical_imgs = np.array(optical_imgs)
        thermal_imgs = np.array(thermal_imgs)
        radar_data = np.array(radar_data)
        labels = np.array(labels)
        
        # Scale radar data
        radar_data = self.scaler.fit_transform(radar_data)
        
        return optical_imgs, thermal_imgs, radar_data, labels

class FusionModel:
    def __init__(self, optical_shape, thermal_shape, radar_features, num_classes):
        self.optical_shape = optical_shape
        self.thermal_shape = thermal_shape
        self.radar_features = radar_features
        self.num_classes = num_classes
        
    def build_model(self):
        """Build multi-modal fusion model"""
        # Optical input branch
        optical_input = Input(shape=self.optical_shape, name='optical_input')
        x_optical = Conv2D(32, (3, 3), activation='relu')(optical_input)
        x_optical = BatchNormalization()(x_optical)
        x_optical = Conv2D(64, (3, 3), activation='relu')(x_optical)
        x_optical = BatchNormalization()(x_optical)
        x_optical = Flatten()(x_optical)
        
        # Thermal input branch
        thermal_input = Input(shape=self.thermal_shape, name='thermal_input')
        x_thermal = Conv2D(16, (3, 3), activation='relu')(thermal_input)
        x_thermal = BatchNormalization()(x_thermal)
        x_thermal = Conv2D(32, (3, 3), activation='relu')(x_thermal)
        x_thermal = BatchNormalization()(x_thermal)
        x_thermal = Flatten()(x_thermal)
        
        # Radar input branch
        radar_input = Input(shape=(self.radar_features,), name='radar_input')
        x_radar = Dense(64, activation='relu')(radar_input)
        x_radar = BatchNormalization()(x_radar)
        x_radar = Dropout(0.2)(x_radar)
        
        # Fusion
        x = Concatenate()([x_optical, x_thermal, x_radar])
        x = Dense(128, activation='relu')(x)
        x = BatchNormalization()(x)
        x = Dropout(0.5)(x)
        output = Dense(self.num_classes, activation='softmax')(x)
        
        # Create model
        model = Model(
            inputs=[optical_input, thermal_input, radar_input],
            outputs=output,
            name='sensor_fusion_model'
        )
        
        return model

def train_model():
    """Train the fusion model"""
    # Load data
    data_loader = DataLoader('data/')
    optical_imgs, thermal_imgs, radar_data, labels = data_loader.load_data()
    
    # Convert labels to one-hot encoding
    labels = tf.keras.utils.to_categorical(labels, num_classes=NUM_CLASSES)
    
    # Split data
    (
        X_optical_train, X_optical_test,
        X_thermal_train, X_thermal_test,
        X_radar_train, X_radar_test,
        y_train, y_test
    ) = train_test_split(
        optical_imgs, thermal_imgs, radar_data, labels,
        test_size=VALIDATION_SPLIT,
        random_state=42
    )
    
    # Build model
    model_builder = FusionModel(
        optical_shape=OPTICAL_IMG_SIZE + (3,),
        thermal_shape=THERMAL_IMG_SIZE + (1,),
        radar_features=RADAR_FEATURES,
        num_classes=NUM_CLASSES
    )
    model = model_builder.build_model()
    
    # Compile model
    model.compile(
        optimizer=Adam(learning_rate=LEARNING_RATE),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    # Callbacks
    callbacks = [
        EarlyStopping(patience=10, restore_best_weights=True),
        ModelCheckpoint(MODEL_SAVE_PATH, save_best_only=True)
    ]
    
    # Train model
    history = model.fit(
        [X_optical_train, X_thermal_train, X_radar_train],
        y_train,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=(
            [X_optical_test, X_thermal_test, X_radar_test],
            y_test
        ),
        callbacks=callbacks
    )
    
    return model, history

def evaluate_model(model, X_optical_test, X_thermal_test, X_radar_test, y_test):
    """Evaluate model performance"""
    # Predictions
    y_pred = model.predict([X_optical_test, X_thermal_test, X_radar_test])
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true_classes = np.argmax(y_test, axis=1)
    
    # Metrics
    print("Classification Report:")
    print(classification_report(y_true_classes, y_pred_classes))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true_classes, y_pred_classes))
    
    # Save evaluation results
    report = classification_report(y_true_classes, y_pred_classes, output_dict=True)
    pd.DataFrame(report).transpose().to_csv('results/classification_report.csv')

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    
    # Train and evaluate model
    model, history = train_model()
    
    # Load test data for evaluation
    data_loader = DataLoader('data/')
    optical_imgs, thermal_imgs, radar_data, labels = data_loader.load_data()
    labels = tf.keras.utils.to_categorical(labels, num_classes=NUM_CLASSES)
    
    # Split test data (using same random state for consistency)
    _, X_optical_test, _, X_thermal_test, _, X_radar_test, _, y_test = train_test_split(
        optical_imgs, thermal_imgs, radar_data, labels
