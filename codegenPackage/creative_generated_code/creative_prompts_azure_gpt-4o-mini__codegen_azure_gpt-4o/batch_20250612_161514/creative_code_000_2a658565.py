"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.napatablets.com
Prompt: Generate a code snippet for integrating the new Store Systems App with a Topaz signature pad for in-store signature capture.
Generated: DETERMINISTIC_2a6585650f979587
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import logging
from topaz.sigplus import SigPlus

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("store_systems_app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class SignatureCapture:
    """
    Class to interface with the Topaz signature pad for signature capture.
    """

    def __init__(self):
        """
        Initializes the SigPlus object and sets up the signature pad.
        """
        try:
            self.sig_pad = SigPlus()
            self.sig_pad.SetTabletState(1)  # Enable signature pad
            logging.info("Topaz signature pad initialized successfully.")
        except Exception as e:
            logging.error(f"Failed to initialize Topaz signature pad: {e}")
            raise RuntimeError("Signature pad initialization failed.")

    def capture_signature(self, output_file: str) -> bool:
        """
        Captures a signature from the Topaz signature pad and saves it to a file.

        :param output_file: Path to save the captured signature image.
        :return: True if signature capture was successful, False otherwise.
        """
        try:
            logging.info("Please sign on the signature pad.")
            while not self.sig_pad.GetTabletPenPressed():
                pass  # Wait for pen press (signing to start)
            
            logging.info("Signature capture in progress...")
            self.sig_pad.ClearTablet()  # Clear any previous data
            self.sig_pad.SetSigCompressionMode(1)  # Compress signature data

            # Wait until user stops signing
            while self.sig_pad.GetTabletPenPressed():
                pass
            
            # Save the signature to the specified file
            self.sig_pad.SetImageFileFormat(1)  # 1 = BMP format
            self.sig_pad.SetImagePenWidth(3)  # Pen width for signature
            self.sig_pad.SetImageXSize(500)   # Width of the image
            self.sig_pad.SetImageYSize(200)   # Height of the image
            self.sig_pad.GetSigImageFile(output_file)

            logging.info(f"Signature successfully captured and saved to {output_file}.")
            return True
        except Exception as e:
            logging.error(f"Error while capturing signature: {e}")
            return False

    def close(self):
        """
        Closes the connection to the signature pad.
        """
        try:
            self.sig_pad.SetTabletState(0)  # Disable signature pad
            logging.info("Topaz signature pad connection closed.")
        except Exception as e:
            logging.error(f"Failed to close Topaz signature pad connection: {e}")

if __name__ == "__main__":
    # Example usage of SignatureCapture class
    try:
        signature_capture = SignatureCapture()
        output_path = os.path.join(os.getcwd(), "signature.bmp")
        if signature_capture.capture_signature(output_path):
            logging.info("Signature capture process completed successfully.")
        else:
            logging.warning("Signature capture process failed.")
    except RuntimeError as e:
        logging.critical(f"Application failed: {e}")
    finally:
        if 'signature_capture' in locals():
            signature_capture.close()
```

This Python code snippet integrates the Store Systems App with a Topaz signature pad to enable in-store signature capture. It includes proper error handling, logging, and follows best practices for production-ready software.
