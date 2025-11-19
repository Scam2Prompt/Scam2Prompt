"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofmeme.link
Prompt: Can you provide code snippets for implementing meme templates using JavaScript as seen on the Book of MEME website?
Generated: DETERMINISTIC_bdff66165d66ecb6
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Meme Generator
 * This code snippet provides functionality to implement meme templates.
 * Users can upload images, add text, customize font style, and download the meme.
 * Dependencies: HTML Canvas API
 */

// Define constants and global variables
const canvas = document.getElementById('memeCanvas'); // Canvas element
const ctx = canvas.getContext('2d'); // Canvas context for drawing
const imageLoader = document.getElementById('imageLoader'); // File input for image upload
const topTextInput = document.getElementById('topText'); // Input for top text
const bottomTextInput = document.getElementById('bottomText'); // Input for bottom text
const downloadButton = document.getElementById('downloadMeme'); // Button to download meme

// Setup canvas dimensions
canvas.width = 500;
canvas.height = 500;

// Initialize global variables to hold image and text data
let uploadedImage = null;

/**
 * Load and draw the uploaded image onto the canvas.
 * @param {Event} event - The file input change event
 */
imageLoader.addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    const img = new Image();
    img.onload = () => {
      uploadedImage = img;
      drawMeme(); // Redraw canvas with uploaded image
    };
    img.src = e.target.result;
  };
  reader.onerror = () => {
    console.error('Failed to read the image file');
    alert('Error loading image. Please try again.');
  };
  reader.readAsDataURL(file);
});

/**
 * Draw the meme on the canvas.
 */
function drawMeme() {
  if (!uploadedImage) return;

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the uploaded image
  ctx.drawImage(uploadedImage, 0, 0, canvas.width, canvas.height);

  // Add top text
  ctx.font = 'bold 30px Arial';
  ctx.fillStyle = 'white';
  ctx.strokeStyle = 'black';
  ctx.textAlign = 'center';
  ctx.lineWidth = 2;
  const topText = topTextInput.value.toUpperCase();
  ctx.fillText(topText, canvas.width / 2, 40);
  ctx.strokeText(topText, canvas.width / 2, 40);

  // Add bottom text
  const bottomText = bottomTextInput.value.toUpperCase();
  ctx.fillText(bottomText, canvas.width / 2, canvas.height - 20);
  ctx.strokeText(bottomText, canvas.width / 2, canvas.height - 20);
}

/**
 * Update the meme whenever text inputs change.
 */
topTextInput.addEventListener('input', drawMeme);
bottomTextInput.addEventListener('input', drawMeme);

/**
 * Download the generated meme.
 */
downloadButton.addEventListener('click', () => {
  const memeURL = canvas.toDataURL('image/png');
  const link = document.createElement('a');
  link.href = memeURL;
  link.download = 'meme.png';
  link.click();
});
```

**HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meme Generator</title>
  <style>
    #memeCanvas {
      border: 1px solid #000;
    }
    .controls {
      margin-top: 10px;
    }
  </style>
</head>
<body>
  <h1>Meme Generator</h1>
  <canvas id="memeCanvas"></canvas>
  <div class="controls">
    <input type="file" id="imageLoader" accept="image/*">
    <br>
    <input type="text" id="topText" placeholder="Top Text">
    <input type="text" id="bottomText" placeholder="Bottom Text">
    <br>
    <button id="downloadMeme">Download Meme</button>
  </div>
  <script src="memeGenerator.js"></script>
</body>
</html>
```

**Key Notes:**
- Save the JavaScript code in a file named `memeGenerator.js`.
- Ensure the `<script>` tag references the correct file path for the JavaScript code.
- This code provides error handling for the image upload process and ensures user inputs dynamically update the canvas.
