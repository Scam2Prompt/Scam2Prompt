"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Generate Python code to analyze user-uploaded videos for physical movement evaluation as part of a fitness consultancy service, and store the results in a database.
Generated: DETERMINISTIC_8f88ae8b2be70e14
Batch ID: 20250612_153225
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
import sqlite3
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize SQLite database connection
DATABASE = 'fitness_analysis.db'

def init_db():
    """Initialize the database and create the required table."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movement_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                video_path TEXT NOT NULL,
                movement_score REAL NOT NULL,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def analyze_video(video_path):
    """Analyze the provided video for physical movement and return a movement score."""
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("Error opening video file")

        # Placeholder for movement analysis (e.g., counting frames of detected motion)
        movement_score = 0
        previous_frame = None
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Convert to grayscale for motion detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

            if previous_frame is None:
                previous_frame = gray_frame
                continue

            # Compute the absolute difference between the current and previous frame
            frame_delta = cv2.absdiff(previous_frame, gray_frame)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

            # Dilate the threshold image
            thresh = cv2.dilate(thresh, None, iterations=2)
            movement_score += np.sum(thresh > 0)  # Count non-zero pixels

            previous_frame = gray_frame

        cap.release()
        return movement_score / cap.get(cv2.CAP_PROP_FRAME_COUNT) if cap.get(cv2.CAP_PROP_FRAME_COUNT) > 0 else 0
        
    except Exception as e:
        print(f"Error during video analysis: {e}")
        return 0

def save_analysis(video_path, movement_score):
    """Save the analysis result to the database."""
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO movement_analysis (video_path, movement_score)
                VALUES (?, ?)
            ''', (video_path, movement_score))
            conn.commit()
    except Exception as e:
        print(f"Error saving analysis to database: {e}")

@app.route('/upload', methods=['POST'])
def upload_video():
    """Endpoint to upload video for analysis."""
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    video_file = request.files['video']
    
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Save uploaded video to a temporary location
        video_path = os.path.join('uploads', video_file.filename)
        video_file.save(video_path)

        # Analyze the video
        movement_score = analyze_video(video_path)

        # Save results to the database
        save_analysis(video_path, movement_score)

        return jsonify({
            'message': 'Video analyzed successfully',
            'movement_score': movement_score
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
```
