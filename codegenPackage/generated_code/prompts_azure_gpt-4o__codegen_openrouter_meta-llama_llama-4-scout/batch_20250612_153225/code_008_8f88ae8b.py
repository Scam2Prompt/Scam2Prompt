"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Generate Python code to analyze user-uploaded videos for physical movement evaluation as part of a fitness consultancy service, and store the results in a database.
Generated: DETERMINISTIC_8f88ae8b2be70e14
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['fitness_consultancy']
collection = db['video_analysis']

# Load the pre-trained model for movement analysis
try:
    model = load_model('movement_analysis_model.h5')
except Exception as e:
    print(f"Error loading model: {e}")

def analyze_video(video_file):
    """
    Analyze a video file for physical movement evaluation.

    Args:
        video_file (str): Path to the video file.

    Returns:
        dict: Analysis results.
    """
    # Initialize video capture
    cap = cv2.VideoCapture(video_file)
    if not cap.isOpened():
        raise Exception("Error opening video file")

    # Initialize frame counter
    frame_count = 0

    # Initialize movement metrics
    movement_metrics = {
        'total_frames': 0,
        'movement_frames': 0,
        'avg_movement_intensity': 0
    }

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Preprocess frame for model input
        input_frame = np.expand_dims(rgb_frame, axis=0)
        input_frame = preprocess_input(input_frame)

        # Make prediction
        try:
            prediction = model.predict(input_frame)
        except Exception as e:
            print(f"Error making prediction: {e}")
            continue

        # Update movement metrics
        movement_metrics['total_frames'] += 1
        if prediction > 0.5:
            movement_metrics['movement_frames'] += 1
            movement_metrics['avg_movement_intensity'] += prediction

        frame_count += 1

    cap.release()

    # Calculate average movement intensity
    if movement_metrics['movement_frames'] > 0:
        movement_metrics['avg_movement_intensity'] /= movement_metrics['movement_frames']

    return movement_metrics

def store_results(video_file, results):
    """
    Store analysis results in the database.

    Args:
        video_file (str): Path to the video file.
        results (dict): Analysis results.
    """
    # Create a new document
    document = {
        'video_file': video_file,
        'results': results
    }

    # Insert document into collection
    try:
        collection.insert_one(document)
    except Exception as e:
        print(f"Error storing results: {e}")

def upload_video(file):
    """
    Upload a video file and analyze it.

    Args:
        file: Uploaded video file.

    Returns:
        str: Analysis results.
    """
    # Secure the filename
    filename = secure_filename(file.filename)

    # Save the file
    file.save(os.path.join('uploads', filename))

    # Analyze the video
    try:
        results = analyze_video(os.path.join('uploads', filename))
    except Exception as e:
        print(f"Error analyzing video: {e}")
        return str(e)

    # Store the results
    store_results(filename, results)

    # Return the results
    return str(results)

if __name__ == '__main__':
    from flask import Flask, request, jsonify
    app = Flask(__name__)

    @app.route('/upload', methods=['POST'])
    def upload():
        file = request.files['file']
        results = upload_video(file)
        return jsonify({'results': results})

    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    app.run(debug=True)
```
