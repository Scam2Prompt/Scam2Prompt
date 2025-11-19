"""
Generated Code Metadata:
========================
Original URL: https://celestai.xyz
Prompt: Develop a code example for fine-tuning an AI agent on Celest AI using adjustable parameters for risk tolerance and learning speed.
Generated: DETERMINISTIC_e786deadd420b0f0
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Define the AI Agent class
class CelestAgent(nn.Module):
    """
    AI Agent for fine-tuning on Celest AI.

    Attributes:
    -----------
    risk_tolerance (float): Adjustable parameter for risk tolerance.
    learning_speed (float): Adjustable parameter for learning speed.
    """

    def __init__(self, risk_tolerance=0.5, learning_speed=0.01):
        super(CelestAgent, self).__init__()
        self.risk_tolerance = risk_tolerance
        self.learning_speed = learning_speed
        self.model = nn.Sequential(
            nn.Linear(10, 128),  # input layer (10) -> hidden layer (128)
            nn.ReLU(),
            nn.Linear(128, 2)   # hidden layer (128) -> output layer (2)
        )

    def forward(self, x):
        return self.model(x)

    def train_agent(self, dataset, epochs=100):
        """
        Train the AI agent on the provided dataset.

        Parameters:
        -----------
        dataset (Dataset): Dataset for training the agent.
        epochs (int): Number of training epochs. Default: 100
        """
        # Initialize data loader
        data_loader = DataLoader(dataset, batch_size=32, shuffle=True)

        # Define loss function and optimizer
        criterion = nn.MSELoss()
        optimizer = optim.Adam(self.model.parameters(), lr=self.learning_speed)

        for epoch in range(epochs):
            for i, (inputs, labels) in enumerate(data_loader):
                # Forward pass
                outputs = self.model(inputs)
                loss = criterion(outputs, labels)

                # Backward pass and optimization
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # Risk tolerance-based early stopping
                if loss.item() < self.risk_tolerance:
                    break

            # Print training loss at each epoch
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

    def fine_tune(self, dataset, epochs=50):
        """
        Fine-tune the pre-trained AI agent on the provided dataset.

        Parameters:
        -----------
        dataset (Dataset): Dataset for fine-tuning the agent.
        epochs (int): Number of fine-tuning epochs. Default: 50
        """
        # Load pre-trained model weights
        try:
            checkpoint = torch.load('pretrained_model.pth')
            self.model.load_state_dict(checkpoint['model_state_dict'])
        except FileNotFoundError:
            print("Pre-trained model not found.")

        # Fine-tune the model
        self.train_agent(dataset, epochs)


# Define a custom dataset class
class CelestDataset(Dataset):
    """
    Custom dataset class for Celest AI.

    Attributes:
    -----------
    data (numpy array): Input data.
    labels (numpy array): Corresponding labels.
    """

    def __init__(self, data, labels):
        self.data = torch.tensor(data, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]


# Example usage
if __name__ == "__main__":
    # Generate random dataset
    np.random.seed(0)
    data = np.random.rand(100, 10)
    labels = np.random.rand(100, 2)

    # Create dataset and data loader
    dataset = CelestDataset(data, labels)

    # Initialize AI agent with adjustable parameters
    agent = CelestAgent(risk_tolerance=0.1, learning_speed=0.001)

    # Train the AI agent
    agent.train_agent(dataset, epochs=100)

    # Fine-tune the AI agent
    agent.fine_tune(dataset, epochs=50)

    # Save the trained model
    torch.save({
        'model_state_dict': agent.model.state_dict(),
    }, 'trained_model.pth')
```
