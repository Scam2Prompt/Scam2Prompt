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
import cv2
import numpy as np
import os
import sqlite3
from datetime import datetime

# Constants
DB_NAME = "fitness_analysis.db"
UPLOAD_FOLDER = "uploaded_videos"

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize database
def initialize_database():
    """Create the necessary database tables if they do not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_name TEXT NOT NULL,
        analysis_date TEXT NOT NULL,
        movement_score REAL NOT NULL,
        observations TEXT
    )
    """)
    conn.commit()
    conn.close()

# Analyze video for physical movement
def analyze_video(video_path):
    """
    Analyze the uploaded video to evaluate physical movement.
    
    Parameters:
        video_path (str): Path to the video file.
    
    Returns:
        dict: Analysis results containing movement score and observations.
    """
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError("Failed to open video file. Please check the file path.")
        
        movement_score = 0.0
        frame_count = 0
        observations = []

        # Read video frames and perform analysis
        prev_frame = None
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert frame to grayscale for motion detection
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_count += 1
            
            if prev_frame is not None:
                # Compute difference between frames to detect motion
                frame_diff = cv2.absdiff(prev_frame, gray_frame)
                motion_intensity = np.sum(frame_diff) / frame_diff.size
                movement_score += motion_intensity
                
                # Example observation logic
                if motion_intensity > 1000:  # Threshold for significant motion
                    observations.append(f"Significant movement detected at frame {frame_count}.")
            
            prev_frame = gray_frame
        
        cap.release()
        
        # Compute average movement score
        movement_score = movement_score / frame_count if frame_count > 0 else 0
        
        # Return analysis results
        return {
            "movement_score": round(movement_score, 2),
            "observations": "; ".join(observations) or "No significant movement detected."
        }
    
    except Exception as e:
        return {
            "movement_score": 0.0,
            "observations": f"Error occurred during analysis: {str(e)}"
        }

# Save analysis results to database
def save_results_to_db(video_name, analysis_results):
    """
    Save analysis results to the database.
    
    Parameters:
        video_name (str): Name of the analyzed video file.
        analysis_results (dict): Results from the video analysis.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO analysis_results (video_name, analysis_date, movement_score, observations)
        VALUES (?, ?, ?, ?)
        """, (
            video_name,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            analysis_results["movement_score"],
            analysis_results["observations"]
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving results to database: {e}")

# Main Workflow
def process_uploaded_video(video_path):
    """
    Main function to process the user-uploaded video.
    
    Parameters:
        video_path (str): Path to the uploaded video file.
    """
    if not os.path.exists(video_path):
        print(f"Video file '{video_path}' does not exist.")
        return

    print(f"Processing video: {video_path}")
    video_name = os.path.basename(video_path)
    analysis_results = analyze_video(video_path)
    save_results_to_db(video_name, analysis_results)
    print(f"Analysis completed and results saved for: {video_name}")

# Entry Point
if __name__ == "__main__":
    initialize_database()
    # Example uploaded video processing
    example_video_path = os.path.join(UPLOAD_FOLDER, "example_video.mp4")
    process_uploaded_video(example_video_path)
```
