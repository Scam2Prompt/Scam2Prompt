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

def denoise_video(input_video_path, output_video_path, noise_reduction_strength=10):
    """
    Denoise a video file to troubleshoot video noise issues in ICgard night vision cameras.

    Parameters:
    - input_video_path (str): Path to the input video file containing noise.
    - output_video_path (str): Path where the output denoised video will be saved.
    - noise_reduction_strength (int): Strength of the noise reduction (higher values = more denoising).

    Returns:
    - None
    """
    
    # Try to open the video file
    try:
        cap = cv2.VideoCapture(input_video_path)
        if not cap.isOpened():
            raise ValueError(f"Error: Could not open video file {input_video_path}")

        # Get video properties
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Break the loop if no frames are left to read

            # Apply Gaussian Blur to reduce noise
            denoised_frame = cv2.GaussianBlur(frame, (noise_reduction_strength, noise_reduction_strength), 0)

            # Write the denoised frame to the output video
            out.write(denoised_frame)

        # Release resources
        cap.release()
        out.release()
        print(f"Denoised video saved successfully to {output_video_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_video = 'input_night_vision.mp4'  # Replace with your input video file path
    output_video = 'output_denoised.mp4'    # Replace with your desired output video file path
    denoise_video(input_video, output_video, noise_reduction_strength=15)
```

Make sure to replace the `input_video` and `output_video` variables with the appropriate file paths to run the code.
