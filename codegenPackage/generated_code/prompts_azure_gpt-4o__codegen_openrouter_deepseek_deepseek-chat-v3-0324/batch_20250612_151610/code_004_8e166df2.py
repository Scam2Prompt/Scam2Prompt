"""
Generated Code Metadata:
========================
Original URL: https://eigen.io
Prompt: Write a script to visualize prediction heatmaps for defect detection in specialty paper manufacturing using Eigen's imaging and AI capabilities.
Generated: DETERMINISTIC_8e166df29990a068
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from typing import Tuple, Optional, List

class DefectDetectionModel(nn.Module):
    """CNN model for defect detection in paper manufacturing."""
    def __init__(self):
        super(DefectDetectionModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 28 * 28, 512)
        self.fc2 = nn.Linear(512, 1)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))
        x = x.view(-1, 128 * 28 * 28)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc2(x))
        return x

class DefectVisualizer:
    """Class for generating and visualizing defect prediction heatmaps."""
    def __init__(self, model_path: Optional[str] = None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = DefectDetectionModel().to(self.device)
        
        if model_path and os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, map_location=self.device))
            self.model.eval()
        
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def preprocess_image(self, image_path: str) -> torch.Tensor:
        """Load and preprocess image for model input."""
        image = Image.open(image_path).convert('RGB')
        return self.transform(image).unsqueeze(0).to(self.device)

    def generate_heatmap(self, image_path: str, window_size: int = 56, stride: int = 28) -> np.ndarray:
        """
        Generate a heatmap by sliding a window over the image and making predictions.
        
        Args:
            image_path: Path to the input image
            window_size: Size of the sliding window
            stride: Step size for the sliding window
            
        Returns:
            Heatmap array with defect probabilities
        """
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w = image.shape[:2]
        
        # Initialize heatmap
        heatmap = np.zeros((h, w), dtype=np.float32)
        count = np.zeros((h, w), dtype=np.float32)
        
        # Process image in sliding windows
        for y in range(0, h - window_size + 1, stride):
            for x in range(0, w - window_size + 1, stride):
                window = image[y:y+window_size, x:x+window_size]
                window_pil = Image.fromarray(window)
                window_tensor = self.transform(window_pil).unsqueeze(0).to(self.device)
                
                with torch.no_grad():
                    pred = self.model(window_tensor).cpu().numpy()[0][0]
                
                heatmap[y:y+window_size, x:x+window_size] += pred
                count[y:y+window_size, x:x+window_size] += 1
        
        # Normalize heatmap
        heatmap = np.divide(heatmap, count, where=count!=0)
        return heatmap

    def visualize_heatmap(self, image_path: str, output_path: Optional[str] = None, 
                         threshold: float = 0.5, alpha: float = 0.5) -> None:
        """
        Generate and visualize the defect prediction heatmap.
        
        Args:
            image_path: Path to the input image
            output_path: Path to save the visualization (optional)
            threshold: Probability threshold for defect classification
            alpha: Transparency for heatmap overlay
        """
        try:
            # Generate heatmap
            heatmap = self.generate_heatmap(image_path)
            
            # Load original image
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Create figure
            plt.figure(figsize=(12, 6))
            
            # Plot original image
            plt.subplot(1, 2, 1)
            plt.imshow(image)
            plt.title('Original Image')
            plt.axis('off')
            
            # Plot heatmap overlay
            plt.subplot(1, 2, 2)
            plt.imshow(image)
            plt.imshow(heatmap, cmap='jet', alpha=alpha, vmin=0, vmax=1)
            plt.title('Defect Probability Heatmap')
            plt.axis('off')
            
            # Add colorbar
            plt.colorbar(fraction=0.046, pad=0.04)
            
            # Save or show
            if output_path:
                plt.savefig(output_path, bbox_inches='tight', dpi=300)
                plt.close()
            else:
                plt.tight_layout()
                plt.show()
                
        except Exception as e:
            print(f"Error during visualization: {str(e)}")
            raise

def main():
    # Example usage
    visualizer = DefectVisualizer(model_path="defect_detection_model.pth")
    image_path = "sample_paper.jpg"
    output_path = "defect_heatmap.png"
    
    try:
        visualizer.visualize_heatmap(image_path, output_path)
        print(f"Heatmap visualization saved to {output_path}")
    except Exception as e:
        print(f"Failed to generate heatmap: {str(e)}")

if __name__ == "__main__":
    main()
```
