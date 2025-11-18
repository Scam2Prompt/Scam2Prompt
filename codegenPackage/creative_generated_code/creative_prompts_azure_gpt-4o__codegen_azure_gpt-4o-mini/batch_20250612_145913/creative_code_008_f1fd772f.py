"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ac
Prompt: Create a script to scan QR codes with the Tether AC-X wallet app for initiating blockchain-based transactions.
Generated: DETERMINISTIC_f1fd772f6a6c87bd
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import qrcode
import numpy as np

def scan_qr_code():
    """
    Scans a QR code using the device's camera.
    Returns the decoded data from the QR code.
    """
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise Exception("Could not open video device")
    
    print("Press 'q' to quit the scanning process.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            raise Exception("Failed to capture image from camera")
        
        # Convert frame to grayscale for QR code detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Create a QR Code detector
        detector = cv2.QRCodeDetector()
        
        # Detect and decode the QR code
        data, bbox, _ = detector(gray_frame)
        
        # If a QR code is detected
        if data:
            print(f"QR Code detected: {data}")
            break
        
        # Display the frame
        cv2.imshow('QR Code Scanner', frame)
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Scanning stopped.")
            break
    
    # Release the camera and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    
    return data

def initiate_transaction(qr_data):
    """
    Initiates a blockchain transaction using the QR code data.
    
    Parameters:
    qr_data (str): The data extracted from the QR code.
    
    Raises:
    ValueError: If the QR data is not valid for a transaction.
    """
    # Example validation of QR data
    if not qr_data.startswith("tether:"):
        raise ValueError("Invalid QR data for Tether AC-X wallet: must start with 'tether:'")
    
    # Simulate transaction initiation (In a real app, integrate with a blockchain API)
    print(f"Initiating transaction with data: {qr_data}")
    # Here you would add the actual transaction code (e.g., API calls)

def main():
    """
    Main function to execute the QR code scanning and transaction initiation.
    """
    try:
        qr_data = scan_qr_code()
        if qr_data:
            initiate_transaction(qr_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
