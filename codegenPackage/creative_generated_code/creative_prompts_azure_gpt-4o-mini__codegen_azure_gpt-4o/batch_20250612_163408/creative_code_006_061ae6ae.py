"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Explain how to use StyleGAN and StyleGAN2 to generate infinite variations of a character design in Python.
Generated: DETERMINISTIC_061ae6ae82a47bb1
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import os
from stylegan2_pytorch import Model

# Function to generate images using StyleGAN2
def generate_images(model_path, output_dir, num_images=10, seed=None):
    """
    Generate infinite variations of character designs using StyleGAN2.

    Args:
        model_path (str): Path to the pre-trained StyleGAN2 model.
        output_dir (str): Directory to save the generated images.
        num_images (int): Number of images to generate.
        seed (int): Random seed for reproducibility. Default is None.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Set random seed for reproducibility if provided
    if seed is not None:
        torch.manual_seed(seed)
        np.random.seed(seed)

    # Load the pre-trained StyleGAN2 model
    model = Model.load(model_path)
    
    # Generate images
    for i in range(num_images):
        # Generate random latent vector (z)
        latent_vector = torch.randn(1, model.latent_dim)
        
        # Generate image from latent vector
        with torch.no_grad():
            generated_image = model.generate_from_latent(latent_vector)

        # Convert the output tensor to a PIL image
        # Normalize and scale the tensor to [0, 255]
        image_array = (generated_image[0].cpu().numpy().transpose(1, 2, 0) * 255).astype(np.uint8)
        pil_image = Image.fromarray(image_array)

        # Save the image
        output_path = os.path.join(output_dir, f'character_{i + 1}.png')
        pil_image.save(output_path)

        print(f"Image saved: {output_path}")


# Main script execution
if __name__ == "__main__":
    # Path to pre-trained StyleGAN2 model (update with your model's path)
    pre_trained_model_path = "path/to/stylegan2_model.pth"
    
    # Directory to save the generated images
    output_images_directory = "generated_characters"
    
    # Number of images to generate
    number_of_images_to_generate = 10

    # Random seed for reproducibility (optional)
    random_seed = 42

    # Call the function to generate images
    generate_images(
        model_path=pre_trained_model_path,
        output_dir=output_images_directory,
        num_images=number_of_images_to_generate,
        seed=random_seed
    )

    print("Image generation completed!")
```

**Note:** This code assumes you already have a trained StyleGAN2 model and the `stylegan2_pytorch` library installed. Update `path/to/stylegan2_model.pth` with the path to your model and install necessary dependencies as required.
