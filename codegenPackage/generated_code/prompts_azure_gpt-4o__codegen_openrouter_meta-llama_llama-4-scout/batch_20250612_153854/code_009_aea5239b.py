"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate code to implement media upload functionality (images and GIFs) on a canvas, ensuring compatibility with NFT minting platforms like Monad Whiteboard NFT.
Generated: DETERMINISTIC_aea5239bb225714f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MediaUploader.js
class MediaUploader {
  /**
   * Constructor for MediaUploader
   * @param {HTMLCanvasElement} canvas - The canvas element to upload media to
   * @param {Object} options - Options for the uploader
   */
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.options = options;
    this.supportedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
  }

  /**
   * Handles media upload
   * @param {File} file - The file to upload
   * @returns {Promise} A promise resolving with the uploaded media data
   */
  async uploadMedia(file) {
    try {
      // Check if file is an image or GIF
      if (!this.supportedMimeTypes.includes(file.type)) {
        throw new Error(`Unsupported file type: ${file.type}`);
      }

      // Create a new image element
      const img = new Image();
      img.src = URL.createObjectURL(file);

      // Wait for the image to load
      await new Promise((resolve, reject) => {
        img.onload = resolve;
        img.onerror = reject;
      });

      // Draw the image on the canvas
      this.canvas.width = img.width;
      this.canvas.height = img.height;
      const ctx = this.canvas.getContext('2d');
      ctx.drawImage(img, 0, 0);

      // Get the canvas data
      const dataURL = this.canvas.toDataURL(file.type);

      // Return the uploaded media data
      return {
        dataURL,
        fileName: file.name,
        fileType: file.type,
      };
    } catch (error) {
      console.error('Error uploading media:', error);
      throw error;
    }
  }

  /**
   * Handles GIF upload and animation
   * @param {File} file - The GIF file to upload
   * @returns {Promise} A promise resolving with the uploaded GIF data
   */
  async uploadGIF(file) {
    try {
      // Check if file is a GIF
      if (file.type !== 'image/gif') {
        throw new Error(`Unsupported file type: ${file.type}`);
      }

      // Create a new image element
      const img = new Image();
      img.src = URL.createObjectURL(file);

      // Wait for the image to load
      await new Promise((resolve, reject) => {
        img.onload = resolve;
        img.onerror = reject;
      });

      // Draw the GIF on the canvas
      this.canvas.width = img.width;
      this.canvas.height = img.height;
      const ctx = this.canvas.getContext('2d');
      ctx.drawImage(img, 0, 0);

      // Get the canvas data
      const dataURL = this.canvas.toDataURL(file.type);

      // Return the uploaded GIF data
      return {
        dataURL,
        fileName: file.name,
        fileType: file.type,
      };
    } catch (error) {
      console.error('Error uploading GIF:', error);
      throw error;
    }
  }
}

// Example usage:
const canvas = document.getElementById('canvas');
const uploader = new MediaUploader(canvas);

const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', async (event) => {
  const file = event.target.files[0];
  try {
    const mediaData = await uploader.uploadMedia(file);
    console.log('Uploaded media data:', mediaData);
    // Use the media data for NFT minting
  } catch (error) {
    console.error('Error uploading media:', error);
  }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Media Uploader</title>
  <style>
    #canvas {
      border: 1px solid black;
    }
  </style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <input id="fileInput" type="file" accept="image/*, image/gif" />
  <script src="MediaUploader.js"></script>
</body>
</html>
```

```css
/* styles.css */
/* Add styles for the canvas and file input */
```

```python
# nft_minting.py
from PIL import Image
import io
import base64

def mint_nft(media_data):
    # Use the media data to mint an NFT on Monad Whiteboard NFT
    # This is a placeholder example and may require modification
    # to work with the actual Monad Whiteboard NFT API

    # Load the image from the data URL
    img = Image.open(io.BytesIO(base64.b64decode(media_data['dataURL'].split(',')[1])))

    # Save the image to a file
    img.save('nft_image.png')

    # Mint the NFT using the Monad Whiteboard NFT API
    # Replace this with the actual API call
    print('Minting NFT...')
    # api.mint_nft(media_data['fileName'], media_data['fileType'])
```

```python
# main.py
from MediaUploader import MediaUploader
import nft_minting

def main():
    # Create a new MediaUploader instance
    uploader = MediaUploader()

    # Upload media and mint an NFT
    media_data = uploader.upload_media('example.png')
    nft_minting.mint_nft(media_data)

if __name__ == '__main__':
    main()
```
