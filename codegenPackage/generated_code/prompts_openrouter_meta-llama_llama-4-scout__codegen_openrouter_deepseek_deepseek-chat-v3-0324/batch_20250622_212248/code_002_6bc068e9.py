"""
Generated Code Metadata:
========================
Original URL: https://drop3.art
Prompt: How can I use machine learning models to create art similar to the style of a specific artist or movement?
Generated: DETERMINISTIC_6bc068e9024f740f
Batch ID: 20250622_212248
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
import tensorflow as tf
from tensorflow.keras.applications import vgg19
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras import backend as K
from PIL import Image
import matplotlib.pyplot as plt

# Configuration
CONTENT_WEIGHT = 1e3
STYLE_WEIGHT = 1e-2
TOTAL_VARIATION_WEIGHT = 30

ITERATIONS = 10
CONTENT_LAYER = 'block5_conv2'
STYLE_LAYERS = [
    'block1_conv1',
    'block2_conv1',
    'block3_conv1', 
    'block4_conv1',
    'block5_conv1'
]

# Image processing utilities
def preprocess_image(image_path, target_size=None):
    """Load and preprocess an image for VGG19 model."""
    img = load_img(image_path, target_size=target_size)
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = vgg19.preprocess_input(img)
    return img

def deprocess_image(x):
    """Convert a tensor back to an image."""
    x = x.reshape((x.shape[1], x.shape[2], 3))
    x[:, :, 0] += 103.939
    x[:, :, 1] += 116.779
    x[:, :, 2] += 123.68
    x = x[:, :, ::-1]
    x = np.clip(x, 0, 255).astype('uint8')
    return x

# Loss functions
def content_loss(base, combination):
    """Calculate content loss between base and generated image."""
    return K.sum(K.square(combination - base))

def gram_matrix(x):
    """Calculate Gram matrix for style representation."""
    features = K.batch_flatten(K.permute_dimensions(x, (2, 0, 1)))
    gram = K.dot(features, K.transpose(features))
    return gram

def style_loss(style, combination, height, width):
    """Calculate style loss between style and generated image."""
    S = gram_matrix(style)
    C = gram_matrix(combination)
    channels = 3
    size = height * width
    return K.sum(K.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

def total_variation_loss(x):
    """Calculate total variation loss for regularization."""
    a = K.square(
        x[:, :, :-1, :-1] - x[:, :, 1:, :-1]
    )
    b = K.square(
        x[:, :, :-1, :-1] - x[:, :, :-1, 1:]
    )
    return K.sum(K.pow(a + b, 1.25))

class NeuralStyleTransfer:
    """Class for performing neural style transfer."""
    
    def __init__(self, content_path, style_path, output_path):
        """Initialize with content and style image paths."""
        self.content_path = content_path
        self.style_path = style_path
        self.output_path = output_path
        
        # Load and preprocess images
        self.content_image = preprocess_image(content_path)
        self.style_image = preprocess_image(style_path)
        
        # Get image dimensions
        self.height, self.width = load_img(content_path).size
        
        # Build model
        self.model = self._build_model()
        
    def _build_model(self):
        """Build VGG19 model with content and style layers."""
        content_image = K.variable(self.content_image)
        style_image = K.variable(self.style_image)
        combination_image = K.placeholder((1, self.height, self.width, 3))
        
        input_tensor = K.concatenate(
            [content_image, style_image, combination_image], axis=0
        )
        
        model = vgg19.VGG19(input_tensor=input_tensor, weights='imagenet', include_top=False)
        outputs_dict = {layer.name: layer.output for layer in model.layers}
        
        # Get feature representations
        content_features = outputs_dict[CONTENT_LAYER][0, :, :, :]
        combination_features = outputs_dict[CONTENT_LAYER][2, :, :, :]
        
        # Calculate losses
        loss = K.variable(0.0)
        loss += CONTENT_WEIGHT * content_loss(content_features, combination_features)
        
        for layer_name in STYLE_LAYERS:
            layer_features = outputs_dict[layer_name]
            style_features = layer_features[1, :, :, :]
            combination_features = layer_features[2, :, :, :]
            sl = style_loss(style_features, combination_features, self.height, self.width)
            loss += (STYLE_WEIGHT / len(STYLE_LAYERS)) * sl
        
        loss += TOTAL_VARIATION_WEIGHT * total_variation_loss(combination_image)
        
        # Set up gradient descent
        grads = K.gradients(loss, combination_image)
        outputs = [loss]
        if isinstance(grads, (list, tuple)):
            outputs += grads
        else:
            outputs.append(grads)
            
        f_outputs = K.function([combination_image], outputs)
        
        return f_outputs
    
    def _eval_loss_and_grads(self, x):
        """Evaluate loss and gradients for current generated image."""
        x = x.reshape((1, self.height, self.width, 3))
        outs = self.model([x])
        loss_value = outs[0]
        grad_values = outs[1].flatten().astype('float64')
        return loss_value, grad_values
    
    def _save_result(self, x, iteration):
        """Save intermediate results."""
        img = deprocess_image(x.copy())
        output_dir = os.path.dirname(self.output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        filename = f"{os.path.splitext(self.output_path)[0]}_iter_{iteration}.jpg"
        Image.fromarray(img).save(filename)
    
    def transfer_style(self):
        """Perform style transfer using L-BFGS optimization."""
        x = np.random.uniform(0, 255, (1, self.height, self.width, 3)) - 128.0
        
        for i in range(ITERATIONS):
            print(f"Iteration {i+1}/{ITERATIONS}")
            loss_value, grad_values = self._eval_loss_and_grads(x)
            
            # Simple gradient descent (for demonstration)
            # In production, you'd use L-BFGS optimizer
            x -= grad_values.reshape((1, self.height, self.width, 3)) * 0.01
            
            if i % 5 == 0:
                self._save_result(x, i)
                print(f"Loss: {loss_value}")
        
        # Save final result
        self._save_result(x, ITERATIONS)
        return deprocess_image(x)

# Example usage
if __name__ == "__main__":
    try:
        # Replace with your image paths
        content_path = "content.jpg"
        style_path = "style.jpg"
        output_path = "output/stylized.jpg"
        
        if not os.path.exists(content_path) or not os.path.exists(style_path):
            raise FileNotFoundError("Content or style image not found")
            
        nst = NeuralStyleTransfer(content_path, style_path, output_path)
        result = nst.transfer_style()
        
        plt.imshow(result)
        plt.axis('off')
        plt.show()
        
    except Exception as e:
        print(f"Error during style transfer: {str(e)}")
```
