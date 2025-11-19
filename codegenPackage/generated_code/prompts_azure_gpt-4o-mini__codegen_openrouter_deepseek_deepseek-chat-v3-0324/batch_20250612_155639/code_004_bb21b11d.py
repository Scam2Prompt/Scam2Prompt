"""
Generated Code Metadata:
========================
Original URL: https://bookofmeme.link
Prompt: How do I integrate meme creation features in a web app using JavaScript, inspired by the functionality of Book of MEME?
Generated: DETERMINISTIC_bb21b11dc6434c80
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// MemeGenerator.js - A reusable component for meme creation in a web app

class MemeGenerator {
  constructor(options = {}) {
    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.image = null;
    this.texts = [];
    this.defaultOptions = {
      fontFamily: 'Impact',
      fontSize: 40,
      fillStyle: 'white',
      strokeStyle: 'black',
      lineWidth: 2,
      textAlign: 'center',
      maxWidth: 400,
      padding: 20
    };
    this.options = { ...this.defaultOptions, ...options };
  }

  /**
   * Load an image from URL or File object
   * @param {string|File} source - URL string or File object
   * @returns {Promise} Resolves when image is loaded
   */
  async loadImage(source) {
    return new Promise((resolve, reject) => {
      this.image = new Image();
      this.image.crossOrigin = 'Anonymous';

      const handleLoad = () => {
        this.image.removeEventListener('load', handleLoad);
        this.image.removeEventListener('error', handleError);
        this._resizeCanvas();
        resolve();
      };

      const handleError = (err) => {
        this.image.removeEventListener('load', handleLoad);
        this.image.removeEventListener('error', handleError);
        reject(new Error('Failed to load image'));
      };

      this.image.addEventListener('load', handleLoad);
      this.image.addEventListener('error', handleError);

      if (typeof source === 'string') {
        this.image.src = source;
      } else if (source instanceof File) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.image.src = e.target.result;
        };
        reader.onerror = handleError;
        reader.readAsDataURL(source);
      } else {
        reject(new Error('Invalid image source'));
      }
    });
  }

  /**
   * Add text to the meme
   * @param {string} text - Text content
   * @param {Object} options - Text styling options
   */
  addText(text, options = {}) {
    const textOptions = {
      ...this.options,
      ...options,
      text
    };
    this.texts.push(textOptions);
  }

  /**
   * Clear all texts from the meme
   */
  clearTexts() {
    this.texts = [];
  }

  /**
   * Generate the meme and return as data URL
   * @param {string} format - Image format (default: 'image/png')
   * @param {number} quality - Image quality (0-1)
   * @returns {string} Data URL of the generated meme
   */
  generate(format = 'image/png', quality = 1) {
    if (!this.image) {
      throw new Error('No image loaded');
    }

    this._drawImage();
    this._drawTexts();

    return this.canvas.toDataURL(format, quality);
  }

  /**
   * Download the meme as an image file
   * @param {string} filename - Name of the file to download
   */
  download(filename = 'meme.png') {
    const link = document.createElement('a');
    link.download = filename;
    link.href = this.generate();
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  // Private methods
  _resizeCanvas() {
    this.canvas.width = this.image.width;
    this.canvas.height = this.image.height;
  }

  _drawImage() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.drawImage(this.image, 0, 0, this.canvas.width, this.canvas.height);
  }

  _drawTexts() {
    this.texts.forEach(textOpts => {
      this.ctx.font = `${textOpts.fontSize}px ${textOpts.fontFamily}`;
      this.ctx.fillStyle = textOpts.fillStyle;
      this.ctx.strokeStyle = textOpts.strokeStyle;
      this.ctx.lineWidth = textOpts.lineWidth;
      this.ctx.textAlign = textOpts.textAlign;

      const x = this.canvas.width / 2;
      const maxWidth = textOpts.maxWidth || this.canvas.width - (textOpts.padding * 2);

      // Split text into multiple lines if needed
      const lines = this._wrapText(textOpts.text, maxWidth);

      lines.forEach((line, i) => {
        const y = textOpts.position === 'bottom' 
          ? this.canvas.height - (textOpts.padding + (lines.length - i - 1) * textOpts.fontSize * 1.2)
          : textOpts.padding + (i * textOpts.fontSize * 1.2);

        this.ctx.strokeText(line, x, y);
        this.ctx.fillText(line, x, y);
      });
    });
  }

  _wrapText(text, maxWidth) {
    const words = text.split(' ');
    const lines = [];
    let currentLine = words[0];

    for (let i = 1; i < words.length; i++) {
      const word = words[i];
      const width = this.ctx.measureText(currentLine + ' ' + word).width;
      if (width < maxWidth) {
        currentLine += ' ' + word;
      } else {
        lines.push(currentLine);
        currentLine = word;
      }
    }
    lines.push(currentLine);
    return lines;
  }
}

// Example usage in a web app
document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('meme-image');
  const topTextInput = document.getElementById('top-text');
  const bottomTextInput = document.getElementById('bottom-text');
  const generateBtn = document.getElementById('generate-btn');
  const downloadBtn = document.getElementById('download-btn');
  const memeContainer = document.getElementById('meme-container');

  const memeGenerator = new MemeGenerator({
    fontSize: 48,
    padding: 30
  });

  fileInput.addEventListener('change', async (e) => {
    try {
      await memeGenerator.loadImage(e.target.files[0]);
      updatePreview();
    } catch (err) {
      console.error('Error loading image:', err);
      alert('Failed to load image. Please try another one.');
    }
  });

  [topTextInput, bottomTextInput].forEach(input => {
    input.addEventListener('input', () => {
      updatePreview();
    });
  });

  generateBtn.addEventListener('click', () => {
    updatePreview();
  });

  downloadBtn.addEventListener('click', () => {
    memeGenerator.download();
  });

  function updatePreview() {
    memeGenerator.clearTexts();
    
    if (topTextInput.value) {
      memeGenerator.addText(topTextInput.value, {
        position: 'top'
      });
    }
    
    if (bottomTextInput.value) {
      memeGenerator.addText(bottomTextInput.value, {
        position: 'bottom'
      });
    }

    const memeUrl = memeGenerator.generate();
    memeContainer.innerHTML = `<img src="${memeUrl}" alt="Generated Meme" style="max-width: 100%;">`;
  }
});
```

```html
<!-- Example HTML for the meme generator UI -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meme Generator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }
    input[type="text"], input[type="file"] {
      width: 100%;
      padding: 8px;
      box-sizing: border-box;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px 15px;
      border: none;
      cursor: pointer;
      margin-right: 10px;
    }
    button:hover {
      background-color: #45a049;
    }
    #meme-container {
      margin-top: 20px;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Meme Generator</h1>
  
  <div class="form-group">
    <label for="meme-image">Upload Image:</label>
    <input type="file" id="meme-image" accept="image/*">
  </div>
  
  <div class="form-group">
    <label for="top-text">Top Text:</label>
    <input type="text" id="top-text" placeholder="Enter top text">
  </div>
  
  <div class="form-group">
    <label for="bottom-text">Bottom Text:</label>
    <input type="text" id="bottom-text" placeholder="Enter bottom text">
  </div>
