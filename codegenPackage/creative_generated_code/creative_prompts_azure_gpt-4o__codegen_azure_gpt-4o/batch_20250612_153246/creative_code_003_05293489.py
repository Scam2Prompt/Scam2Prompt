"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icgard.ir
Prompt: Provide a solution for troubleshooting video noise issues in ICgard night vision cameras using OpenCV or similar libraries.
Generated: DETERMINISTIC_05293489750f2b8d
Batch ID: 20250612_153246
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

def denoise_video(input_video_path, output_video_path):
    """
    Reduce video noise in night vision footage using OpenCV.

    Parameters:
    - input_video_path (str): Path to the input video file.
    - output_video_path (str): Path to save the processed video file.

    This function uses Gaussian blur and temporal denoising techniques to improve video quality.
    """
    try:
        # Open the video file
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise FileNotFoundError(f"Cannot open video file: {input_video_path}")
        
        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video

        # Initialize video writer
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
        
        # Initialize a list to store previous frames for temporal denoising
        frame_history = []
        max_frame_history = 5  # Number of frames to average for denoising

        while True:
            # Read the next frame
            ret, frame = cap.read()
            if not ret:
                break  # Exit when no more frames are available

            # Apply Gaussian blur to reduce spatial noise
            blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)

            # Add the blurred frame to history for temporal denoising
            frame_history.append(blurred_frame)
            if len(frame_history) > max_frame_history:
                frame_history.pop(0)

            # Compute the average of frames in history for temporal denoising
            denoised_frame = np.mean(frame_history, axis=0).astype(np.uint8)

            # Write the denoised frame to the output video
            out.write(denoised_frame)
        
        # Release resources
        cap.release()
        out.release()
        print(f"Denoised video saved to: {output_video_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    input_path = "input_night_vision.mp4"  # Replace with your video path
    output_path = "output_denoised.mp4"  # Replace with desired output path
    denoise_video(input_path, output_path)
```
