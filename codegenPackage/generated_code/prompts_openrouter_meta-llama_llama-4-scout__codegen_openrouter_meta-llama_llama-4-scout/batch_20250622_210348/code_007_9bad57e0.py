"""
Generated Code Metadata:
========================
Original URL: https://4kg24t7m.s3.amazonaws.com
Prompt: "Discuss the advantages and disadvantages of using Axon over other neural network libraries, focusing on performance metrics like those mentioned in bd9ae1fb2c927e1266b5b5e4bfa1c76a."
Generated: DETERMINISTIC_9bad57e0410eacf4
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import torch
import torch.nn as nn
import torch.optim as optim
from axon import Axon

# Define a simple neural network model
class SimpleNN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def compare_performance():
    # Set seed for reproducibility
    np.random.seed(0)
    torch.manual_seed(0)

    # Define dimensions
    input_dim = 784
    output_dim = 10

    # Generate random data
    X = np.random.rand(1000, input_dim)
    y = np.random.rand(1000, output_dim)

    # Convert data to PyTorch tensors
    X_tensor = torch.from_numpy(X).float()
    y_tensor = torch.from_numpy(y).float()

    # Axon
    start_time = time.time()
    model = Axon(input_dim, 128, output_dim)
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=10, batch_size=32, verbose=0)
    axon_time = time.time() - start_time

    # TensorFlow
    start_time = time.time()
    tf_model = Sequential([
        Dense(128, activation='relu', input_shape=(input_dim,)),
        Dense(output_dim)
    ])
    tf_model.compile(optimizer='adam', loss='mean_squared_error')
    tf_model.fit(X, y, epochs=10, batch_size=32, verbose=0)
    tf_time = time.time() - start_time

    # PyTorch
    start_time = time.time()
    pt_model = SimpleNN(input_dim, output_dim)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(pt_model.parameters(), lr=0.001)
    for epoch in range(10):
        optimizer.zero_grad()
        outputs = pt_model(X_tensor)
        loss = criterion(outputs, torch.from_numpy(y).float())
        loss.backward()
        optimizer.step()
    pt_time = time.time() - start_time

    # Print performance metrics
    print(f"Axon training time: {axon_time:.2f} seconds")
    print(f"TensorFlow training time: {tf_time:.2f} seconds")
    print(f"PyTorch training time: {pt_time:.2f} seconds")

def main():
    try:
        compare_performance()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
