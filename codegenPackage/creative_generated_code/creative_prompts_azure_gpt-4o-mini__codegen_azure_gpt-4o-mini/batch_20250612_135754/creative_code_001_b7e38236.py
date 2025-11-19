"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Write a tutorial on how to implement a photo editing functionality similar to the Blur App, including features like eraser and size changer.
Generated: DETERMINISTIC_b7e382369926583d
Batch ID: 20250612_135754
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

class PhotoEditor:
    def __init__(self, image_path):
        """
        Initialize the PhotoEditor with an image.

        :param image_path: Path to the image file.
        """
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Image not found or unable to open.")

        self.mask = np.zeros(self.image.shape, dtype=np.uint8)
        self.drawing = False
        self.brush_size = 10

    def set_brush_size(self, size):
        """
        Set the size of the brush for erasing.

        :param size: Integer size of the brush.
        """
        if size > 0:
            self.brush_size = size
        else:
            raise ValueError("Brush size must be a positive integer.")

    def toggle_drawing(self, event, x, y, flags, param):
        """
        Mouse callback function to handle drawing on the mask.

        :param event: Mouse event.
        :param x: x coordinate of the mouse.
        :param y: y coordinate of the mouse.
        :param flags: Any relevant flags.
        :param param: Additional parameters.
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            cv2.circle(self.mask, (x, y), self.brush_size, (255, 255, 255), -1)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                cv2.circle(self.mask, (x, y), self.brush_size, (255, 255, 255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False

    def apply_blur(self, blur_strength=15):
        """
        Apply a Gaussian blur to the image.

        :param blur_strength: Integer strength of the blur.
        """
        if blur_strength < 1:
            raise ValueError("Blur strength must be a positive integer.")
        
        # Create a blurred version of the original image
        blurred_image = cv2.GaussianBlur(self.image, (blur_strength, blur_strength), 0)
        # Combine the original and blurred images using the mask
        self.result_image = np.where(self.mask == 255, self.image, blurred_image)

    def show_result(self):
        """
        Display the result image in a window.
        """
        cv2.imshow('Photo Editor', self.result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        """
        Main method to run the photo editor.
        """
        cv2.namedWindow('Photo Editor')
        cv2.setMouseCallback('Photo Editor', self.toggle_drawing)

        while True:
            cv2.imshow('Photo Editor', self.mask)
            key = cv2.waitKey(1)

            if key == ord('b'):  # Press 'b' to apply a blur
                self.apply_blur()
            elif key == ord('s'):  # Press 's' to set brush size
                new_size = int(input("Enter new brush size: "))
                self.set_brush_size(new_size)
            elif key == ord('q'):  # Press 'q' to exit
                break
        
        self.show_result()

if __name__ == "__main__":
    try:
        editor = PhotoEditor('path/to/your/image.jpg')  # Update with your image path
        editor.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note:** Replace `'path/to/your/image.jpg'` with the actual path of the image you want to edit. This code requires OpenCV (`cv2`) to be installed. You can install it via pip:

```bash
pip install opencv-python
```
