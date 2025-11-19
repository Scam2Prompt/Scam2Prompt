"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staging.artlabs.ai
Prompt: Write a code snippet to create high-quality 3D models from product images using AI, as described on artlabs.ai.
Generated: DETERMINISTIC_745d1dc7713dab09
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pre-trained model for generating 3D models from images
MODEL_PATH = 'path/to/your/model.h5'
try:
    model = load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

# Initialize Label Encoder if your model relies on class labels
label_encoder = LabelEncoder()
# Load or fit the encoder as per your dataset
# label_encoder.fit([...])  # Fit with your class labels

def preprocess_image(image_path):
    """
    Preprocess the input image for model prediction.
    
    Parameters:
        image_path (str): Path to the input image.
    
    Returns:
        np.array: Preprocessed image suitable for the model.
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        # Resize the image to match model input shape
        image = cv2.resize(image, (224, 224))  # Update size as per model requirement
        # Normalize pixel values to [0, 1]
        image = image.astype('float32') / 255.0
        # Expand dimensions to fit model input shape (batch size, height, width, channels)
        return np.expand_dims(image, axis=0)
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")

@app.route('/generate_3d_model', methods=['POST'])
def generate_3d_model():
    """
    Endpoint to generate a 3D model from a provided product image.
    
    Request:
        JSON with 'image_path'
    
    Response:
        JSON indicating success or failure.
    """
    data = request.get_json()
    
    if 'image_path' not in data:
        return jsonify({'error': 'No image path provided'}), 400

    image_path = data['image_path']
    
    if not os.path.exists(image_path):
        return jsonify({'error': 'Image path does not exist'}), 404

    try:
        # Preprocess the image
        processed_image = preprocess_image(image_path)
        # Generate the 3D model
        model_output = model.predict(processed_image)
        
        # Here you would typically have logic to convert model_output to a usable 3D model format
        # For demonstration, we will just return a placeholder response
        return jsonify({'message': '3D model generated successfully', 'data': model_output.tolist()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Note:
- Replace `'path/to/your/model.h5'` with the actual path to your pre-trained model.
- The model input size of (224, 224) should be adjusted based on the requirements of your specific model.
- Modify the conversion logic of `model_output` to create an actual 3D model as per your application's needs.
