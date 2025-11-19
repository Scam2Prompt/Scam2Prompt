"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Create a program using TensorFlow or PyTorch to analyze eye movement patterns and suggest exercises for improving vision, inspired by the holistic methods described on Klar Sehen.
Generated: DETERMINISTIC_d84df045cce10d40
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class EyeMovementDataset(Dataset):
    """
    Custom Dataset for loading eye movement data.
    Expected features: x_coord, y_coord, timestamp, duration, velocity
    Expected labels: movement_pattern (0: normal, 1: saccadic, 2: pursuit, 3: fixation)
    """
    def __init__(self, features, labels, transform=None):
        self.features = features
        self.labels = labels
        self.transform = transform
        
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
        sample = {
            'features': torch.FloatTensor(self.features[idx]),
            'label': torch.LongTensor([self.labels[idx]])
        }
        
        if self.transform:
            sample = self.transform(sample)
            
        return sample

class EyeMovementModel(nn.Module):
    """
    Neural network model for eye movement pattern classification.
    """
    def __init__(self, input_size, hidden_size, num_classes):
        super(EyeMovementModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        return out

def load_and_preprocess_data(filepath):
    """
    Load and preprocess eye movement data from CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        
        # Basic data validation
        required_columns = ['x_coord', 'y_coord', 'timestamp', 'duration', 'velocity', 'movement_pattern']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("CSV file is missing required columns")
            
        # Separate features and labels
        X = df[['x_coord', 'y_coord', 'timestamp', 'duration', 'velocity']].values
        y = df['movement_pattern'].values
        
        # Normalize features
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        
        return X, y, scaler
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None, None

def train_model(model, train_loader, criterion, optimizer, num_epochs):
    """
    Train the eye movement classification model.
    """
    model.train()
    total_step = len(train_loader)
    
    for epoch in range(num_epochs):
        for i, batch in enumerate(train_loader):
            features = batch['features'].to(device)
            labels = batch['label'].squeeze().to(device)
            
            # Forward pass
            outputs = model(features)
            loss = criterion(outputs, labels)
            
            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            if (i+1) % 100 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{total_step}], Loss: {loss.item():.4f}')

def evaluate_model(model, test_loader):
    """
    Evaluate the model on test data.
    """
    model.eval()
    with torch.no_grad():
        correct = 0
        total = 0
        for batch in test_loader:
            features = batch['features'].to(device)
            labels = batch['label'].squeeze().to(device)
            outputs = model(features)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
        accuracy = 100 * correct / total
        print(f'Test Accuracy: {accuracy:.2f}%')
        return accuracy

def get_exercise_recommendation(predicted_class):
    """
    Get vision exercise recommendation based on predicted eye movement pattern.
    """
    exercises = {
        0: "Normal movement detected. Maintain healthy habits with the 20-20-20 rule: every 20 minutes, look at something 20 feet away for 20 seconds.",
        1: "Saccadic movement pattern detected. Practice smooth pursuit exercises: follow a moving object with your eyes without moving your head.",
        2: "Pursuit movement pattern detected. Try saccadic exercises: quickly shift gaze between two fixed points.",
        3: "Excessive fixation detected. Practice figure-8 eye movements: trace an imaginary figure eight with your eyes."
    }
    return exercises.get(predicted_class, "No specific recommendation available.")

def analyze_eye_movements(input_data, model, scaler):
    """
    Analyze new eye movement data and provide recommendations.
    """
    try:
        # Preprocess input data
        input_data = scaler.transform([input_data])
        input_tensor = torch.FloatTensor(input_data).to(device)
        
        # Make prediction
        model.eval()
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted = torch.max(output.data, 1)
            predicted_class = predicted.item()
            
        # Get recommendation
        recommendation = get_exercise_recommendation(predicted_class)
        
        return predicted_class, recommendation
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return None, None

def main():
    # Hyperparameters
    input_size = 5  # x_coord, y_coord, timestamp, duration, velocity
    hidden_size = 64
    num_classes = 4  # normal, saccadic, pursuit, fixation
    num_epochs = 10
    batch_size = 32
    learning_rate = 0.001
    
    # Load data
    data_file = "eye_movement_data.csv"
    if not os.path.exists(data_file):
        print(f"Data file {data_file} not found. Please provide the eye movement data.")
        return
        
    X, y, scaler = load_and_preprocess_data(data_file)
    if X is None:
        return
        
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create datasets and data loaders
    train_dataset = EyeMovementDataset(X_train, y_train)
    test_dataset = EyeMovementDataset(X_test, y_test)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    # Initialize model
    model = EyeMovementModel(input_size, hidden_size, num_classes).to(device)
    
    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Train the model
    train_model(model, train_loader, criterion, optimizer, num_epochs)
    
    # Evaluate the model
    evaluate_model(model, test_loader)
    
    # Example usage with new data
    sample_input = [100, 150, 123456789, 0.5, 200]  # x, y, timestamp, duration, velocity
    predicted_class, recommendation = analyze_eye_movements(sample_input, model, scaler)
    
    if predicted_class is not None:
        print(f"\nPredicted movement pattern: {predicted_class}")
        print(f"Recommended exercise: {recommendation}")

if __name__ == "__main__":
    main()
```
