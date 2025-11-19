"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltc-qr.to
Prompt: Describe how to scan a QR code for Litecoin and what tools are needed for this process.
Generated: DETERMINISTIC_bc05d5634e412fdd
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2  # OpenCV library for computer vision tasks
import qrcode  # Library for generating QR codes
import sys  # Library for system-level operations

def scan_qr_code(video_source=0):
    """
    Scans QR codes using the specified video source.
    
    Args:
        video_source (int): Index of the video source (0 for default camera).
    
    Returns:
        str: The decoded data from the QR code, or an error message.
    """
    # Initialize the video capture
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        sys.exit(1)

    # Create a QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Detect and decode the QR code
        data, bbox, _ = detector(frame)

        # If a QR code is detected
        if bbox is not None:
            # Draw bounding box around the QR code
            for i in range(len(bbox)):
                cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % 4][0]), (0, 255, 0), 2)

            # If data was found, print it
            if data:
                print(f"QR Code Data: {data}")
                break

        # Display the resulting frame
        cv2.imshow('QR Code Scanner', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

    # Release the capture and destroy all windows
    cap.release()
    cv2.destroyAllWindows()

    return data if data else "No QR code detected."

if __name__ == "__main__":
    # Run the QR code scanner
    scan_qr_code()
```
