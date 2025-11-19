"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Explain how to use StyleGAN and StyleGAN2 to generate infinite variations of a character design in Python.
Generated: DETERMINISTIC_061ae6ae82a47bb1
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import torch
from torchvision import utils
from stylegan2_pytorch import StyleGAN2

# Function to generate character designs using StyleGAN2
def generate_character_designs(num_images=5, output_dir='generated_images', seed=None):
    """
    Generate character designs using StyleGAN2.

    Parameters:
    - num_images (int): Number of images to generate.
    - output_dir (str): Directory to save generated images.
    - seed (int or None): Random seed for reproducibility. If None, a random seed will be used.
    """
    # Set random seed for reproducibility
    if seed is not None:
        torch.manual_seed(seed)

    # Load the pre-trained StyleGAN2 model
    try:
        model = StyleGAN2.load('path/to/pretrained/stylegan2_model.pth')
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Generate images
    for i in range(num_images):
        try:
            # Generate a random latent vector
            latent_vector = torch.randn(1, model.latent_dim).to(model.device)

            # Generate an image from the latent vector
            with torch.no_grad():
                generated_image = model(latent_vector)

            # Save the generated image
            output_path = f"{output_dir}/character_design_{i + 1}.png"
            utils.save_image(generated_image, output_path, normalize=True)
            print(f"Generated image saved to: {output_path}")

        except Exception as e:
            print(f"Error generating image {i + 1}: {e}")

# Example usage
if __name__ == "__main__":
    generate_character_designs(num_images=10, output_dir='generated_images', seed=42)
```

### Notes:
- Ensure you have the `stylegan2_pytorch` library installed and the pre-trained model available at the specified path.
- The output directory should exist or be created before running the code.
- Adjust the `num_images` and `output_dir` parameters as needed.
