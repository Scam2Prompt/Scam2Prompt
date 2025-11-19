"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Develop a simple AI model to analyze market conditions and adjust coin mining profitability, similar to Hash AI's approach, using a library like TensorFlow or PyTorch.
Generated: DETERMINISTIC_e1e463a8f2e250f0
Batch ID: 20250622_205919
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
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yfinance as yf
import warnings

warnings.filterwarnings('ignore')

# Configuration
CONFIG = {
    'ticker': 'BTC-USD',
    'lookback': 30,  # Number of days to look back for prediction
    'test_size': 0.2,
    'batch_size': 32,
    'epochs': 100,
    'learning_rate': 0.001,
    'hidden_size': 64,
    'num_layers': 2,
    'dropout': 0.2
}

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class MarketDataset(Dataset):
    """Custom Dataset for loading market data"""
    def __init__(self, data, lookback):
        self.data = data
        self.lookback = lookback
        
    def __len__(self):
        return len(self.data) - self.lookback
    
    def __getitem__(self, idx):
        x = self.data[idx:idx+self.lookback]
        y = self.data[idx+self.lookback]
        return torch.FloatTensor(x).to(device), torch.FloatTensor(y).to(device)

class LSTMModel(nn.Module):
    """LSTM model for market prediction"""
    def __init__(self, input_size, hidden_size, num_layers, dropout):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            dropout=dropout,
            batch_first=True
        )
        self.fc = nn.Linear(hidden_size, 1)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

def fetch_market_data(ticker):
    """Fetch historical market data"""
    try:
        data = yf.download(ticker, period='1y', interval='1d')
        data = data[['Close']].values
        return data
    except Exception as e:
        print(f"Error fetching market data: {e}")
        return None

def preprocess_data(data, lookback, test_size):
    """Preprocess and split data into train/test sets"""
    scaler = MinMaxScaler(feature_range=(0, 1))
    data = scaler.fit_transform(data)
    
    X, y = [], []
    for i in range(len(data) - lookback):
        X.append(data[i:i+lookback])
        y.append(data[i+lookback])
    
    X = np.array(X)
    y = np.array(y)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=False
    )
    
    return X_train, X_test, y_train, y_test, scaler

def train_model(model, train_loader, criterion, optimizer, epochs):
    """Train the LSTM model"""
    model.train()
    for epoch in range(epochs):
        for batch_x, batch_y in train_loader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
        
        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

def evaluate_model(model, test_loader, scaler):
    """Evaluate model performance"""
    model.eval()
    predictions = []
    actuals = []
    
    with torch.no_grad():
        for batch_x, batch_y in test_loader:
            outputs = model(batch_x)
            predictions.extend(outputs.cpu().numpy())
            actuals.extend(batch_y.cpu().numpy())
    
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    actuals = scaler.inverse_transform(np.array(actuals).reshape(-1, 1))
    
    mse = mean_squared_error(actuals, predictions)
    print(f'Test MSE: {mse:.4f}')
    
    return predictions, actuals

def predict_profitability(model, data, scaler, lookback):
    """Predict future profitability"""
    model.eval()
    with torch.no_grad():
        last_window = data[-lookback:]
        last_window = scaler.transform(last_window)
        last_window = torch.FloatTensor(last_window).unsqueeze(0).to(device)
        prediction = model(last_window)
        prediction = scaler.inverse_transform(prediction.cpu().numpy())
    
    return prediction[0][0]

def main():
    # Fetch and prepare data
    data = fetch_market_data(CONFIG['ticker'])
    if data is None:
        return
    
    X_train, X_test, y_train, y_test, scaler = preprocess_data(
        data, CONFIG['lookback'], CONFIG['test_size']
    )
    
    # Create data loaders
    train_dataset = MarketDataset(X_train, CONFIG['lookback'])
    test_dataset = MarketDataset(X_test, CONFIG['lookback'])
    
    train_loader = DataLoader(
        train_dataset, batch_size=CONFIG['batch_size'], shuffle=False
    )
    test_loader = DataLoader(
        test_dataset, batch_size=CONFIG['batch_size'], shuffle=False
    )
    
    # Initialize model
    model = LSTMModel(
        input_size=1,
        hidden_size=CONFIG['hidden_size'],
        num_layers=CONFIG['num_layers'],
        dropout=CONFIG['dropout']
    ).to(device)
    
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=CONFIG['learning_rate'])
    
    # Train and evaluate
    train_model(model, train_loader, criterion, optimizer, CONFIG['epochs'])
    predictions, actuals = evaluate_model(model, test_loader, scaler)
    
    # Predict profitability
    current_price = predict_profitability(model, data, scaler, CONFIG['lookback'])
    print(f"Predicted next day price: {current_price:.2f}")
    
    # Simple profitability adjustment logic
    last_price = scaler.inverse_transform(data[-1:])[0][0]
    change = (current_price - last_price) / last_price * 100
    
    if change > 5:
        print("Market condition: Highly profitable - Increase mining")
    elif change > 0:
        print("Market condition: Profitable - Maintain mining")
    else:
        print("Market condition: Not profitable - Consider reducing mining")

if __name__ == '__main__':
    main()
```
