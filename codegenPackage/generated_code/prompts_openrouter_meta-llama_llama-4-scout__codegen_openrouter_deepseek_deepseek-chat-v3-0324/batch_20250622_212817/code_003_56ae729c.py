"""
Generated Code Metadata:
========================
Original URL: https://celestiacelestiia.com
Prompt: What is the purpose of Glow Node in a software development context, and how is it used?
Generated: DETERMINISTIC_56ae729ce653913a
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Example implementation of a Glow Node in a neural network context
# This demonstrates how Glow Nodes can be used in machine learning pipelines

import torch
import torch.nn as nn
import torch.nn.functional as F

class GlowNode(nn.Module):
    """
    A Glow Node implementation for normalizing flows in neural networks.
    This is part of the Glow (Generative Flow) architecture for density estimation.
    """
    
    def __init__(self, in_channels, hidden_channels):
        """
        Initialize the Glow Node.
        
        Args:
            in_channels (int): Number of input channels
            hidden_channels (int): Number of hidden channels for the affine coupling
        """
        super(GlowNode, self).__init__()
        
        # Network for affine transformation parameters
        self.net = nn.Sequential(
            nn.Conv2d(in_channels // 2, hidden_channels, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(hidden_channels, hidden_channels, kernel_size=1),
            nn.ReLU(),
            nn.Conv2d(hidden_channels, in_channels, kernel_size=3, padding=1),
            nn.Tanh()
        )
        
        # Initialize weights
        self.net.apply(self._init_weights)
        
    def _init_weights(self, m):
        """Initialize weights for better convergence."""
        if isinstance(m, nn.Conv2d):
            nn.init.xavier_uniform_(m.weight)
            nn.init.zeros_(m.bias)
            
    def forward(self, x, reverse=False):
        """
        Forward pass through the Glow Node.
        
        Args:
            x (Tensor): Input tensor
            reverse (bool): If True, performs inverse transformation
            
        Returns:
            Tensor: Transformed tensor
            Tensor: Log determinant of Jacobian
        """
        if not reverse:
            # Split input
            x1, x2 = x.chunk(2, dim=1)
            
            # Get transformation parameters
            h = self.net(x1)
            shift, scale = h.chunk(2, dim=1)
            scale = torch.sigmoid(scale + 2.0)  # Ensure scale > 0
            
            # Affine transformation
            x2 = x2 * scale + shift
            log_det = torch.sum(torch.log(scale).view(x.size(0), -1), dim=1)
            
            return torch.cat([x1, x2], dim=1), log_det
        else:
            # Split input for reverse pass
            x1, x2 = x.chunk(2, dim=1)
            
            # Get transformation parameters
            h = self.net(x1)
            shift, scale = h.chunk(2, dim=1)
            scale = torch.sigmoid(scale + 2.0)
            
            # Inverse affine transformation
            x2 = (x2 - shift) / scale
            log_det = -torch.sum(torch.log(scale).view(x.size(0), -1), dim=1)
            
            return torch.cat([x1, x2], dim=1), log_det

# Example usage
if __name__ == "__main__":
    # Create a Glow Node
    glow_node = GlowNode(in_channels=64, hidden_channels=128)
    
    # Create dummy input
    dummy_input = torch.randn(16, 64, 32, 32)  # batch_size=16, channels=64, height=32, width=32
    
    # Forward pass
    output, log_det = glow_node(dummy_input)
    print(f"Output shape: {output.shape}")
    print(f"Log determinant shape: {log_det.shape}")
    
    # Reverse pass
    reconstructed, inv_log_det = glow_node(output, reverse=True)
    print(f"Reconstruction error: {torch.mean((dummy_input - reconstructed)**2).item():.6f}")
```
