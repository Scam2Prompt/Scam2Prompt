"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiggfg7harzlrxx3ccklh6kjolvxmejdxtqnqqtcadvfp5c5zzddbu.ipfs.dweb.link
Prompt: Generate code for deploying an AI bot like "Emma" from MyShell Labs that uses Stable Diffusion for image generation in a creator-focused application.
Generated: DETERMINISTIC_d885cc975d7d8cc5
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
from transformers import StableDiffusionPipeline
from PIL import Image
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)

# Load the Stable Diffusion model
MODEL_NAME = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"

try:
    logger.info("Loading the Stable Diffusion model...")
    pipe = StableDiffusionPipeline.from_pretrained(MODEL_NAME).to(device)
    logger.info("Stable Diffusion model loaded successfully.")
except Exception as e:
    logger.error("Failed to load Stable Diffusion model: %s", e)
    raise RuntimeError("Model loading failed.") from e

@app.route('/generate-image', methods=['POST'])
def generate_image():
    """
    Endpoint to generate an image from text prompt.
    Expects a JSON body with a 'prompt' key.
    """
    try:
        data = request.get_json()
        prompt = data.get('prompt', None)

        if prompt is None:
            logger.warning("No prompt provided.")
            return jsonify({"error": "Prompt is required."}), 400

        # Generate image using Stable Diffusion
        logger.info("Generating image for prompt: '%s'", prompt)
        image = pipe(prompt).images[0]

        # Save image to a file
        output_path = os.path.join("generated_images", f"{prompt.replace(' ', '_')}.png")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        image.save(output_path)

        logger.info("Image generated and saved to %s", output_path)
        return jsonify({"message": "Image generated successfully.", "image_path": output_path}), 200

    except Exception as e:
        logger.error("Error generating image: %s", e)
        return jsonify({"error": "Image generation failed."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Ensure you have `flask`, `torch`, `transformers`, and `Pillow` installed.
- Save images will be stored in the `generated_images` folder relative to where the script is executed.
- This script creates a simple API endpoint to generate an image based on a text prompt.
