"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Write code to implement federated learning techniques for secure AI model training while maintaining user privacy, as described in PrivateAI's ecosystem.
Generated: DETERMINISTIC_23d382ff1dff3212
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# federated_learning.py

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

# Define a simple neural network model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # input layer (28x28 images) -> hidden layer (128 units)
        self.fc2 = nn.Linear(128, 10)   # hidden layer (128 units) -> output layer (10 units)

    def forward(self, x):
        x = torch.relu(self.fc1(x))      # activation function for hidden layer
        x = self.fc2(x)
        return x

# Define a custom dataset class for our data
class UserDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        data = self.data[idx]
        label = self.labels[idx]
        return data, label

# Define the federated learning server class
class FederatedLearningServer:
    def __init__(self, model, num_users):
        self.model = model
        self.num_users = num_users
        self.user_models = [model for _ in range(num_users)]

    def train(self, user_datasets, num_rounds, batch_size):
        for round_num in range(num_rounds):
            # Select a random subset of users for this round
            selected_users = np.random.choice(self.num_users, size=int(self.num_users * 0.1), replace=False)

            # Get the user models for the selected users
            user_models = [self.user_models[user_idx] for user_idx in selected_users]

            # Train each user model on its local dataset
            user_updates = []
            for user_idx, user_model in zip(selected_users, user_models):
                user_dataset = user_datasets[user_idx]
                user_loader = DataLoader(user_dataset, batch_size=batch_size, shuffle=True)

                # Train the user model
                user_model.train()
                optimizer = optim.SGD(user_model.parameters(), lr=0.01)
                for batch_idx, (data, labels) in enumerate(user_loader):
                    data = data.view(-1, 784)  # flatten the data
                    optimizer.zero_grad()
                    outputs = user_model(data)
                    loss = nn.CrossEntropyLoss()(outputs, labels)
                    loss.backward()
                    optimizer.step()

                # Get the updated model parameters
                user_update = user_model.state_dict()
                user_updates.append(user_update)

            # Aggregate the user updates
            aggregated_update = self.aggregate_updates(user_updates)

            # Update the global model
            self.model.load_state_dict(aggregated_update)

            # Update the user models
            for user_idx, user_model in zip(selected_users, user_models):
                self.user_models[user_idx].load_state_dict(aggregated_update)

            print(f"Round {round_num+1} completed")

    def aggregate_updates(self, user_updates):
        # Simple federated averaging
        aggregated_update = {}
        for user_update in user_updates:
            for param_name, param_value in user_update.items():
                if param_name not in aggregated_update:
                    aggregated_update[param_name] = param_value
                else:
                    aggregated_update[param_name] += param_value

        for param_name, param_value in aggregated_update.items():
            aggregated_update[param_name] /= len(user_updates)

        return aggregated_update

# Define the main function
def main():
    # Set the seed for reproducibility
    np.random.seed(0)
    torch.manual_seed(0)

    # Define the model, dataset, and data loader
    model = Net()
    num_users = 10
    user_datasets = []
    for _ in range(num_users):
        # Generate some random data for demonstration purposes
        data = np.random.rand(100, 784)
        labels = np.random.randint(0, 10, size=100)
        user_dataset = UserDataset(data, labels)
        user_datasets.append(user_dataset)

    # Create the federated learning server
    server = FederatedLearningServer(model, num_users)

    # Train the model using federated learning
    num_rounds = 10
    batch_size = 32
    server.train(user_datasets, num_rounds, batch_size)

if __name__ == "__main__":
    main()
```
