"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2.zks.app
Prompt: Write a program to scan a QR code with WeChat and join the ZKSwap group automatically.
Generated: DETERMINISTIC_9e62b76d4aa6ca3d
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import time
import pyautogui
import pyperclip
import cv2

def scan_qr_code():
    """
    Scans QR code using a webcam and returns the decoded text from the QR code.
    
    Returns:
        str: The decoded text from the QR code.
    """
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise RuntimeError("Cannot open webcam.")

    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            raise RuntimeError("Failed to read frame from webcam.")

        # Decode QR code from the frame
        decoded_objects = cv2.QRCodeDetector()(frame)

        if decoded_objects:
            # Release the webcam
            cap.release()
            cv2.destroyAllWindows()
            return decoded_objects[0]

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release webcam and close windows if QR code was not found
    cap.release()
    cv2.destroyAllWindows()
    raise RuntimeError("QR code not found.")

def join_group(qr_code_link):
    """
    Joins the ZKSwap group using the provided WeChat QR code link.
    
    Args:
        qr_code_link (str): The link to join the WeChat group.
    """
    try:
        # Copy the link to clipboard
        pyperclip.copy(qr_code_link)

        # Simulate key presses to perform the join action
        time.sleep(2)  # Wait for 2 seconds before pasting
        pyautogui.hotkey('ctrl', 'v')  # Paste the link
        time.sleep(1)
        pyautogui.press('enter')  # Press enter to join the group
    except Exception as e:
        print(f"Error joining group: {e}")

def main():
    """
    Main function to execute the QR code scanning and group joining process.
    """
    try:
        print("Scanning for QR code...")
        qr_code_link = scan_qr_code()
        print(f"QR code scanned: {qr_code_link}")
        print("Joining the ZKSwap group...")
        join_group(qr_code_link)
        print("Successfully joined the group.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Prerequisites:**
- Ensure you have the required libraries installed:
  ```bash
  pip install opencv-python pyautogui pyperclip
  ```
- Ensure your webcam is functioning and accessible.
- Running this script may require appropriate permissions for accessing your clipboard and simulating keyboard inputs.
