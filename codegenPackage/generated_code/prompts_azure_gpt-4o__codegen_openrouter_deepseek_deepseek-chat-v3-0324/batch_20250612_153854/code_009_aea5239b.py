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
// MediaUploader.js - Handles image and GIF uploads for NFT minting platforms

class MediaUploader {
  constructor(options = {}) {
    this.maxFileSize = options.maxFileSize || 10 * 1024 * 1024; // 10MB default
    this.allowedTypes = options.allowedTypes || ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
    this.canvas = options.canvas || document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.onError = options.onError || console.error;
    this.onSuccess = options.onSuccess || (() => {});
    this.previewElement = options.previewElement;
  }

  /**
   * Validates the uploaded file
   * @param {File} file - The file to validate
   * @returns {boolean} - True if valid, false otherwise
   */
  validateFile(file) {
    if (!file) {
      this.onError('No file selected');
      return false;
    }

    if (file.size > this.maxFileSize) {
      this.onError(`File too large. Max size: ${this.maxFileSize / 1024 / 1024}MB`);
      return false;
    }

    if (!this.allowedTypes.includes(file.type)) {
      this.onError(`Invalid file type. Allowed types: ${this.allowedTypes.join(', ')}`);
      return false;
    }

    return true;
  }

  /**
   * Handles file upload and renders to canvas
   * @param {File} file - The file to upload
   * @returns {Promise<HTMLCanvasElement>} - Promise resolving to the canvas with the image
   */
  async upload(file) {
    if (!this.validateFile(file)) {
      return Promise.reject('Invalid file');
    }

    try {
      const image = await this.loadImage(file);
      this.renderToCanvas(image);
      this.updatePreview(image);
      this.onSuccess(this.canvas);
      return this.canvas;
    } catch (error) {
      this.onError(`Error processing file: ${error.message}`);
      return Promise.reject(error);
    }
  }

  /**
   * Loads image file into HTMLImageElement
   * @param {File} file - The image file
   * @returns {Promise<HTMLImageElement>} - Promise resolving to the loaded image
   */
  loadImage(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      const img = new Image();

      reader.onload = (e) => {
        img.onload = () => resolve(img);
        img.onerror = () => reject(new Error('Failed to load image'));
        img.src = e.target.result;
      };

      reader.onerror = () => reject(new Error('Failed to read file'));
      reader.readAsDataURL(file);
    });
  }

  /**
   * Renders image to canvas
   * @param {HTMLImageElement} image - The image to render
   */
  renderToCanvas(image) {
    // Clear canvas
    this.canvas.width = image.width;
    this.canvas.height = image.height;
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.drawImage(image, 0, 0);
  }

  /**
   * Updates preview element if provided
   * @param {HTMLImageElement} image - The image to preview
   */
  updatePreview(image) {
    if (!this.previewElement) return;
    
    if (this.previewElement.tagName === 'IMG') {
      this.previewElement.src = image.src;
    } else if (this.previewElement.tagName === 'CANVAS') {
      const ctx = this.previewElement.getContext('2d');
      this.previewElement.width = image.width;
      this.previewElement.height = image.height;
      ctx.drawImage(image, 0, 0);
    }
  }

  /**
   * Gets canvas data URL
   * @param {string} format - The format (default: 'image/png')
   * @param {number} quality - The quality for JPEG/WEBP (0-1)
   * @returns {string} - The data URL
   */
  getDataURL(format = 'image/png', quality = 0.92) {
    if (!['image/jpeg', 'image/png', 'image/webp'].includes(format)) {
      format = 'image/png';
    }
    return this.canvas.toDataURL(format, quality);
  }

  /**
   * Gets canvas Blob
   * @param {string} format - The format (default: 'image/png')
   * @param {number} quality - The quality for JPEG/WEBP (0-1)
   * @returns {Promise<Blob>} - Promise resolving to the Blob
   */
  getBlob(format = 'image/png', quality = 0.92) {
    return new Promise((resolve) => {
      if (!['image/jpeg', 'image/png', 'image/webp'].includes(format)) {
        format = 'image/png';
      }
      this.canvas.toBlob((blob) => resolve(blob), format, quality);
    });
  }
}

// Example usage:
/*
const uploader = new MediaUploader({
  canvas: document.getElementById('drawingCanvas'),
  previewElement: document.getElementById('preview'),
  onSuccess: (canvas) => {
    console.log('Image uploaded successfully', canvas);
    // Ready for NFT minting
  },
  onError: (err) => {
    alert(err);
  }
});

document.getElementById('fileInput').addEventListener('change', (e) => {
  if (e.target.files.length) {
    uploader.upload(e.target.files[0]);
  }
});
*/
```
