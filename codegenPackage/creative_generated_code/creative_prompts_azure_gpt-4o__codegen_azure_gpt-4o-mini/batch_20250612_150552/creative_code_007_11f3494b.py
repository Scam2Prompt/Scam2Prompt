"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multi-ai.pages.dev
Prompt: Create a script that utilizes the `stable-diffusion-inpainting` model from Multi AI to edit specific regions of an image based on a mask and text prompt. Include integration steps.
Generated: DETERMINISTIC_11f3494b5085345d
Batch ID: 20250612_150552
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/mask.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/path/to/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import torch
from PIL import Image
from io import BytesIO
import requests
import numpy as np
from torchvision import transforms

# Function to load an image from a URL
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return Image.open(BytesIO(response.content)).convert("RGB")
    except Exception as e:
        print(f"Error loading image from {url}: {e}")
        return None

# Function to preprocess the image and mask
def preprocess_image(image, mask):
    transform = transforms.Compose([
        transforms.Resize((512, 512)),  # Resize to model input size
        transforms.ToTensor(),           # Convert to Tensor
        transforms.Normalize((0.5,), (0.5,))  # Normalize to [-1, 1]
    ])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    mask_tensor = transform(mask).unsqueeze(0)
    return image_tensor, mask_tensor

# Function to run the inpainting model
def inpaint_image(model, image_tensor, mask_tensor, prompt):
    try:
        model.eval()  # Set model to evaluation mode
        with torch.no_grad():  # Disable gradient calculation
            output = model(image_tensor, mask_tensor, prompt)
        return output
    except Exception as e:
        print(f"Error during inpainting: {e}")
        return None

# Function to save the output image
def save_image(tensor, output_path):
    try:
        image = tensor.squeeze(0).cpu().numpy()  # Remove batch dimension
        image = np.clip((image * 0.5 + 0.5) * 255, 0, 255).astype(np.uint8)  # Denormalize
        Image.fromarray(image).save(output_path)
        print(f"Output image saved to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

# Main function to orchestrate the image inpainting
def main(image_url, mask_url, prompt, output_path):
    # Load images
    image = load_image(image_url)
    mask = load_image(mask_url)
    
    if image is None or mask is None:
        return  # Exit if image loading fails

    # Preprocess the images
    image_tensor, mask_tensor = preprocess_image(image, mask)

    # Load the inpainting model (assuming model is already downloaded and setup)
    # Here we are using a placeholder for the model, replace with actual loading code.
    model = None  # Load your model from Multi AI here

    # Inpaint the image
    output_tensor = inpaint_image(model, image_tensor, mask_tensor, prompt)
    
    if output_tensor is None:
        return  # Exit if inpainting fails

    # Save the output image
    save_image(output_tensor, output_path)

if __name__ == "__main__":
    # Example usage
    IMAGE_URL = "https://example.com/path/to/image.jpg"
    MASK_URL = "https://example.com/path/to/mask.png"
    PROMPT = "A serene landscape with mountains"
    OUTPUT_PATH = "output_image.png"
    
    main(IMAGE_URL, MASK_URL, PROMPT, OUTPUT_PATH)
```

**Integration Steps:**
1. Ensure you have PyTorch, torchvision, and Pillow installed.
2. Replace the placeholder for model loading with code to load the `stable-diffusion-inpainting` model from Multi AI.
3. Update the URLs in the main function with valid image and mask URLs.
4. Run the script to perform inpainting and save the resulting image.
