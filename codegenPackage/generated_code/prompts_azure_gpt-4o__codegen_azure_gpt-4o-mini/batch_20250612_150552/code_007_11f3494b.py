"""
Generated Code Metadata:
========================
Original URL: https://multi-ai.pages.dev
Prompt: Create a script that utilizes the `stable-diffusion-inpainting` model from Multi AI to edit specific regions of an image based on a mask and text prompt. Include integration steps.
Generated: DETERMINISTIC_11f3494b5085345d
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import torch
from PIL import Image
from torchvision import transforms
from diffusers import StableDiffusionInpaintingPipeline

# Function to load the model
def load_model(model_name: str) -> StableDiffusionInpaintingPipeline:
    """
    Load the Stable Diffusion Inpainting model.

    Args:
        model_name (str): The name of the model to load.

    Returns:
        StableDiffusionInpaintingPipeline: The loaded model.
    """
    try:
        model = StableDiffusionInpaintingPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
        model = model.to("cuda")  # Move model to GPU if available
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{model_name}': {e}")

# Function to preprocess the input image and mask
def preprocess_image(image_path: str, mask_path: str) -> (torch.Tensor, torch.Tensor):
    """
    Preprocess the input image and mask.

    Args:
        image_path (str): Path to the input image.
        mask_path (str): Path to the mask image.

    Returns:
        (torch.Tensor, torch.Tensor): Preprocessed image and mask tensors.
    """
    try:
        # Load images
        image = Image.open(image_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")  # Load mask as grayscale

        # Define transformations
        transform = transforms.Compose([
            transforms.Resize((512, 512)),  # Resize to model input size
            transforms.ToTensor(),
        ])

        # Apply transformations
        image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
        mask_tensor = transform(mask).unsqueeze(0)  # Add batch dimension

        return image_tensor, mask_tensor
    except Exception as e:
        raise RuntimeError(f"Failed to preprocess images: {e}")

# Function to perform inpainting
def inpaint_image(model: StableDiffusionInpaintingPipeline, image_tensor: torch.Tensor, mask_tensor: torch.Tensor, prompt: str) -> Image:
    """
    Perform inpainting on the image using the specified prompt and mask.

    Args:
        model (StableDiffusionInpaintingPipeline): The inpainting model.
        image_tensor (torch.Tensor): The input image tensor.
        mask_tensor (torch.Tensor): The mask tensor.
        prompt (str): The text prompt for inpainting.

    Returns:
        Image: The inpainted image.
    """
    try:
        # Perform inpainting
        with torch.no_grad():
            inpainted_image_tensor = model(prompt=prompt, image=image_tensor, mask_image=mask_tensor).images[0]

        return inpainted_image_tensor
    except Exception as e:
        raise RuntimeError(f"Failed to inpaint image: {e}")

# Main function to execute the inpainting process
def main(image_path: str, mask_path: str, prompt: str, model_name: str = "CompVis/stable-diffusion-inpainting") -> None:
    """
    Main function to execute the inpainting process.

    Args:
        image_path (str): Path to the input image.
        mask_path (str): Path to the mask image.
        prompt (str): The text prompt for inpainting.
        model_name (str): The name of the model to load (default: "CompVis/stable-diffusion-inpainting").
    """
    try:
        # Load the model
        model = load_model(model_name)

        # Preprocess the images
        image_tensor, mask_tensor = preprocess_image(image_path, mask_path)

        # Inpaint the image
        inpainted_image = inpaint_image(model, image_tensor, mask_tensor, prompt)

        # Save or display the inpainted image
        inpainted_image.save("inpainted_image.png")
        inpainted_image.show()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Define paths and prompt
    image_path = "path/to/your/image.jpg"  # Replace with your image path
    mask_path = "path/to/your/mask.png"    # Replace with your mask path
    prompt = "A beautiful landscape with mountains"  # Replace with your prompt

    # Execute the main function
    main(image_path, mask_path, prompt)
```
