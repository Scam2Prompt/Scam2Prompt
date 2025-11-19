"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: "Create a code example using StyleGAN and StyleGAN2 for generating anime-style characters, based on the project described on tubone BOYAKI."
Generated: DETERMINISTIC_11a18ce97b0118be
Batch ID: 20250622_211429
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
import torch
import torchvision.utils as vutils
from torchvision import transforms
from PIL import Image
import dnnlib
import legacy

# Configuration
MODEL_PATHS = {
    'stylegan': 'path/to/stylegan.pkl',
    'stylegan2': 'path/to/stylegan2.pkl'
}
OUTPUT_DIR = 'output'
SEED = 42
NUM_IMAGES = 4
TRUNCATION_PSI = 0.7

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_model(model_path):
    """Load pre-trained StyleGAN/StyleGAN2 model"""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    with dnnlib.util.open_url(model_path) as f:
        return legacy.load_network_pkl(f)['G_ema']

def generate_images(generator, num_images, truncation_psi):
    """Generate images using the generator"""
    z = torch.from_numpy(np.random.RandomState(SEED).randn(num_images, generator.z_dim)).to('cuda')
    w = generator.mapping(z, None, truncation_psi=truncation_psi)
    img = generator.synthesis(w, noise_mode='const')
    return img

def save_images(images, prefix):
    """Save generated images to disk"""
    for i, img in enumerate(images):
        img = (img.permute(1, 2, 0) * 127.5 + 128).clamp(0, 255).to(torch.uint8).cpu().numpy()
        Image.fromarray(img).save(os.path.join(OUTPUT_DIR, f'{prefix}_{i}.png'))

def main():
    try:
        # Initialize torch
        torch.manual_seed(SEED)
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f"Using device: {device}")

        # Generate images with StyleGAN
        print("Generating images with StyleGAN...")
        stylegan = load_model(MODEL_PATHS['stylegan']).to(device)
        stylegan_images = generate_images(stylegan, NUM_IMAGES, TRUNCATION_PSI)
        save_images(stylegan_images, 'stylegan')

        # Generate images with StyleGAN2
        print("Generating images with StyleGAN2...")
        stylegan2 = load_model(MODEL_PATHS['stylegan2']).to(device)
        stylegan2_images = generate_images(stylegan2, NUM_IMAGES, TRUNCATION_PSI)
        save_images(stylegan2_images, 'stylegan2')

        print(f"Images saved to {OUTPUT_DIR}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```

Note: This code assumes you have:
1. The StyleGAN and StyleGAN2 model files (.pkl)
2. CUDA-capable GPU for optimal performance
3. Required dependencies installed (torch, torchvision, numpy, pillow, etc.)

You'll need to replace 'path/to/stylegan.pkl' and 'path/to/stylegan2.pkl' with actual paths to your trained model files. The code includes basic error handling and follows Python best practices.
