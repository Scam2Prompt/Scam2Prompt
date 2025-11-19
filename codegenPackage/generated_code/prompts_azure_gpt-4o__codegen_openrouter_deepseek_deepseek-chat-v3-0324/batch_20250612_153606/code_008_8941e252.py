"""
Generated Code Metadata:
========================
Original URL: https://gizatech1.vercel.app
Prompt: Generate Python code to use Giza's Actions SDK for running verifiable inference on a TensorFlow model. Include steps for ensuring tamper-evident execution proofs.
Generated: DETERMINISTIC_8941e252099d2810
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import hashlib
import tensorflow as tf
from giza.actions import action, verifiable
from giza.schemas import Model
from giza.utils import get_model_uri, get_zk_proof

# Initialize logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelIntegrityError(Exception):
    """Custom exception for model integrity verification failures."""
    pass

class InferenceProofError(Exception):
    """Custom exception for proof generation/verification failures."""
    pass

def compute_model_hash(model_path: str) -> str:
    """
    Compute SHA-256 hash of the model file for integrity verification.
    
    Args:
        model_path: Path to the TensorFlow model file.
        
    Returns:
        Hex digest of the model file.
    """
    sha256 = hashlib.sha256()
    with open(model_path, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

@action(name="verifiable_inference")
def verifiable_inference(
    model_id: int,
    version_id: int,
    input_data,
    expected_model_hash: str = None
):
    """
    Perform verifiable inference using Giza's Actions SDK.
    
    Args:
        model_id: ID of the model in Giza platform.
        version_id: Version ID of the model.
        input_data: Input data for inference.
        expected_model_hash: Expected SHA-256 hash of the model for integrity check.
        
    Returns:
        Tuple of (inference result, proof metadata).
        
    Raises:
        ModelIntegrityError: If model integrity check fails.
        InferenceProofError: If proof generation/verification fails.
    """
    try:
        # 1. Load the model with integrity verification
        model_uri = get_model_uri(model_id, version_id)
        model_path = tf.keras.models.load_model(model_uri)
        
        if expected_model_hash:
            current_hash = compute_model_hash(model_uri)
            if current_hash != expected_model_hash:
                raise ModelIntegrityError(
                    f"Model hash mismatch. Expected: {expected_model_hash}, Got: {current_hash}"
                )
        
        # 2. Perform inference
        logger.info("Running inference...")
        result = model_path.predict(input_data)
        
        # 3. Generate verifiable proof
        logger.info("Generating verifiable proof...")
        proof = get_zk_proof(
            model=Model(id=model_id, version=version_id),
            input_data=input_data,
            output_data=result
        )
        
        # 4. Verify proof
        if not proof.verified:
            raise InferenceProofError("Proof verification failed")
        
        logger.info("Inference and proof verification completed successfully")
        return result, proof
        
    except Exception as e:
        logger.error(f"Error during verifiable inference: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Sample input data (replace with actual input)
        input_data = tf.constant([[1.0, 2.0, 3.0, 4.0]])
        
        # Known good model hash (optional but recommended)
        expected_hash = "a1b2c3d4e5f6..."  # Replace with actual hash
        
        # Run verifiable inference
        result, proof = verifiable_inference(
            model_id=123,
            version_id=1,
            input_data=input_data,
            expected_model_hash=expected_hash
        )
        
        print(f"Inference result: {result}")
        print(f"Proof metadata: {json.dumps(proof.dict(), indent=2)}")
        
    except Exception as e:
        logger.error(f"Error in example execution: {str(e)}")
```
