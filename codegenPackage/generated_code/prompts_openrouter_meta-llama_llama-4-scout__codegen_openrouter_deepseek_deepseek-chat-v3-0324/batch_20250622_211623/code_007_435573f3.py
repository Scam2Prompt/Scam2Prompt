"""
Generated Code Metadata:
========================
Original URL: https://lightchain.live-apps.com
Prompt: "Implement a node for the Lightchain AI network that performs valuable AI computations, such as model training and inference tasks, to contribute to the Proof of Intelligence (PoI) consensus mechanism."
Generated: DETERMINISTIC_435573f335f66c84
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
import time
from typing import Dict, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LightchainNode:
    """
    A node in the Lightchain AI network that performs AI computations for PoI consensus.
    Handles model training and inference tasks.
    """

    def __init__(self, node_id: str, model: nn.Module, device: str = 'cpu'):
        """
        Initialize the Lightchain node.

        Args:
            node_id: Unique identifier for this node
            model: PyTorch model to use for computations
            device: Device to run computations on ('cpu' or 'cuda')
        """
        self.node_id = node_id
        self.model = model.to(device)
        self.device = device
        self.task_queue = []
        self.current_task = None
        self.is_training = False

        logger.info(f"Initialized Lightchain node {node_id} on device {device}")

    def add_task(self, task_type: str, task_data: Dict) -> bool:
        """
        Add a new AI computation task to the node's queue.

        Args:
            task_type: Type of task ('train' or 'inference')
            task_data: Dictionary containing task parameters and data

        Returns:
            bool: True if task was added successfully
        """
        try:
            if task_type not in ['train', 'inference']:
                raise ValueError("Invalid task type")

            task = {
                'type': task_type,
                'data': task_data,
                'timestamp': time.time(),
                'status': 'queued'
            }
            self.task_queue.append(task)
            logger.info(f"Added {task_type} task to queue")
            return True
        except Exception as e:
            logger.error(f"Failed to add task: {str(e)}")
            return False

    def process_next_task(self) -> Optional[Dict]:
        """
        Process the next task in the queue.

        Returns:
            Optional[Dict]: Task result if successful, None otherwise
        """
        if not self.task_queue:
            logger.warning("No tasks in queue")
            return None

        self.current_task = self.task_queue.pop(0)
        self.current_task['status'] = 'processing'

        try:
            if self.current_task['type'] == 'train':
                result = self._train_model(self.current_task['data'])
            elif self.current_task['type'] == 'inference':
                result = self._run_inference(self.current_task['data'])
            else:
                raise ValueError("Unknown task type")

            self.current_task['status'] = 'completed'
            self.current_task['result'] = result
            logger.info(f"Completed {self.current_task['type']} task")
            return self.current_task

        except Exception as e:
            self.current_task['status'] = 'failed'
            self.current_task['error'] = str(e)
            logger.error(f"Task failed: {str(e)}")
            return None

    def _train_model(self, train_data: Dict) -> Dict:
        """
        Internal method to train the model.

        Args:
            train_data: Dictionary containing training parameters and data

        Returns:
            Dict: Training results including metrics
        """
        if self.is_training:
            raise RuntimeError("Node is already training")

        self.is_training = True
        logger.info("Starting model training")

        try:
            # Extract training parameters
            epochs = train_data.get('epochs', 10)
            batch_size = train_data.get('batch_size', 32)
            learning_rate = train_data.get('learning_rate', 0.001)

            # Create dataset and dataloader
            dataset = CustomDataset(train_data['data'])
            dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

            # Set up optimizer and loss function
            optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
            criterion = nn.CrossEntropyLoss()

            # Training loop
            metrics = {'loss': [], 'accuracy': []}
            for epoch in range(epochs):
                epoch_loss = 0.0
                correct = 0
                total = 0

                for inputs, labels in dataloader:
                    inputs, labels = inputs.to(self.device), labels.to(self.device)

                    optimizer.zero_grad()
                    outputs = self.model(inputs)
                    loss = criterion(outputs, labels)
                    loss.backward()
                    optimizer.step()

                    epoch_loss += loss.item()
                    _, predicted = torch.max(outputs.data, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()

                epoch_loss /= len(dataloader)
                epoch_acc = correct / total
                metrics['loss'].append(epoch_loss)
                metrics['accuracy'].append(epoch_acc)

                logger.info(
                    f"Epoch {epoch + 1}/{epochs} - Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.4f}"
                )

            return {
                'status': 'success',
                'metrics': metrics,
                'model_state': self.model.state_dict()
            }

        finally:
            self.is_training = False

    def _run_inference(self, inference_data: Dict) -> Dict:
        """
        Internal method to run inference using the model.

        Args:
            inference_data: Dictionary containing inference data

        Returns:
            Dict: Inference results
        """
        logger.info("Running model inference")

        try:
            # Prepare input data
            inputs = torch.tensor(inference_data['data'], dtype=torch.float32)
            inputs = inputs.to(self.device)

            # Run inference
            with torch.no_grad():
                outputs = self.model(inputs)
                predictions = torch.argmax(outputs, dim=1).cpu().numpy()

            return {
                'status': 'success',
                'predictions': predictions.tolist(),
                'confidence': torch.softmax(outputs, dim=1).cpu().numpy().tolist()
            }

        except Exception as e:
            logger.error(f"Inference failed: {str(e)}")
            return {'status': 'error', 'message': str(e)}

    def get_node_status(self) -> Dict:
        """
        Get current status of the node.

        Returns:
            Dict: Node status information
        """
        return {
            'node_id': self.node_id,
            'device': self.device,
            'queue_length': len(self.task_queue),
            'is_training': self.is_training,
            'current_task': self.current_task
        }

class CustomDataset(Dataset):
    """
    Custom PyTorch dataset for training data.
    """

    def __init__(self, data: Dict):
        """
        Initialize dataset with training data.

        Args:
            data: Dictionary containing 'features' and 'labels'
        """
        self.features = torch.tensor(data['features'], dtype=torch.float32)
        self.labels = torch.tensor(data['labels'], dtype=torch.long)

    def __len__(self) -> int:
        return len(self.features)

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        return self.features[idx], self.labels[idx]

# Example usage
if __name__ == "__main__":
    # Example model
    class SimpleModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc1 = nn.Linear(10, 5)
            self.fc2 = nn.Linear(5, 2)

        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = self.fc2(x)
            return x

    # Initialize node
    node = LightchainNode(
        node_id="node_1",
        model=SimpleModel(),
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )

    # Example training task
    train_data = {
        'data': {
            'features': np.random.rand(100, 10).tolist(),
            'labels': np.random.randint(0, 2, 100).tolist()
        },
        'epochs': 5,
        'batch_size': 16,
        'learning_rate': 0.01
    }
    node.add_task('train', train_data)

    # Example inference task
    inference_data = {
        'data': np.random.rand(5, 10).tolist()
    }
    node.add_task('inference', inference_data)

    # Process tasks
    while node.task_queue:
        result = node.process_next_task()
        if result:
            print(f"Task result: {json.dumps(result, indent=2)}")
```
