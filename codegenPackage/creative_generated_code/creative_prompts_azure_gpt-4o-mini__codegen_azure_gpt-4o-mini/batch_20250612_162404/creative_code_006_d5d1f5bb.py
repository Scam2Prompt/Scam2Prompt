"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gizatech1.vercel.app
Prompt: Explain how to convert an existing ML model into a verifiable model using Giza's tools and frameworks.
Generated: DETERMINISTIC_d5d1f5bb40f89d0e
Batch ID: 20250612_162404
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
from giza import VerifiableModel, ModelLoader

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def convert_to_verifiable_model(model_path, output_path):
    """
    Converts an existing ML model into a verifiable model using Giza's tools.
    
    Args:
        model_path (str): The path to the existing ML model file.
        output_path (str): The path where the verifiable model will be saved.
    
    Raises:
        FileNotFoundError: If the model file does not exist.
        ValueError: If the model is not in a supported format.
        Exception: For any other errors during the conversion process.
    """
    
    # Check if the model file exists
    if not os.path.exists(model_path):
        logger.error(f"Model file not found: {model_path}")
        raise FileNotFoundError(f"The specified model file does not exist: {model_path}")

    try:
        # Load the existing ML model
        logger.info("Loading the existing ML model...")
        model = ModelLoader.load(model_path)
        
        # Check if the model is in a supported format
        if not model.is_supported():
            logger.error("The model format is not supported for conversion.")
            raise ValueError(f"The model at {model_path} is not in a supported format.")
        
        # Convert the model to a verifiable model
        logger.info("Converting model to a verifiable model...")
        verifiable_model = VerifiableModel(model)
        
        # Save the verifiable model
        verifiable_model.save(output_path)
        logger.info(f"Verifiable model successfully saved to: {output_path}")
    
    except Exception as e:
        logger.exception("An error occurred during the conversion process.")
        raise e

if __name__ == "__main__":
    # Example usage
    existing_model_path = "path/to/existing_model.pkl"
    verifiable_model_path = "path/to/verifiable_model.pkl"

    try:
        convert_to_verifiable_model(existing_model_path, verifiable_model_path)
    except Exception as error:
        logger.error(f"Failed to convert model: {error}")
```
