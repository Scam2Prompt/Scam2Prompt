"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofmeme.link
Prompt: How do I integrate meme creation features in a web app using JavaScript, inspired by the functionality of Book of MEME?
Generated: DETERMINISTIC_bb21b11dc6434c80
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meme Creator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
    }
    #memeCanvas {
      border: 1px solid #ccc;
      margin-top: 20px;
    }
    .controls {
      margin-top: 20px;
    }
    input, button {
      margin: 5px;
    }
  </style>
</head>
<body>
  <h1>Meme Creator</h1>
  <div class="controls">
    <label for="topText">Top Text:</label>
    <input type="text" id="topText" placeholder="Enter top text">
    <br>
    <label for="bottomText">Bottom Text:</label>
    <input type="text" id="bottomText" placeholder="Enter bottom text">
    <br>
    <label for="imageUpload">Upload Image:</label>
    <input type="file" id="imageUpload" accept="image/*">
    <br>
    <button id="generateMemeButton">Generate Meme</button>
    <button id="downloadMemeButton">Download Meme</button>
  </div>
  <canvas id="memeCanvas" width="500" height="500"></canvas>
  
  <script>
    // Select DOM elements
    const memeCanvas = document.getElementById('memeCanvas');
    const context = memeCanvas.getContext('2d');
    const topTextInput = document.getElementById('topText');
    const bottomTextInput = document.getElementById('bottomText');
    const imageUploadInput = document.getElementById('imageUpload');
    const generateMemeButton = document.getElementById('generateMemeButton');
    const downloadMemeButton = document.getElementById('downloadMemeButton');

    let memeImage = null; // Variable to hold the uploaded image

    /**
     * Draws the uploaded image and text onto the canvas.
     */
    function drawMeme() {
      // Ensure image is loaded before drawing
      if (!memeImage) {
        alert('Please upload an image to create a meme.');
        return;
      }

      // Clear the canvas before redrawing
      context.clearRect(0, 0, memeCanvas.width, memeCanvas.height);

      // Draw the image
      context.drawImage(memeImage, 0, 0, memeCanvas.width, memeCanvas.height);

      // Set text styles
      context.font = '36px Arial';
      context.fillStyle = 'white';
      context.strokeStyle = 'black';
      context.textAlign = 'center';
      context.lineWidth = 2;

      // Draw top text
      const topText = topTextInput.value || '';
      context.fillText(topText, memeCanvas.width / 2, 50);
      context.strokeText(topText, memeCanvas.width / 2, 50);

      // Draw bottom text
      const bottomText = bottomTextInput.value || '';
      context.fillText(bottomText, memeCanvas.width / 2, memeCanvas.height - 20);
      context.strokeText(bottomText, memeCanvas.width / 2, memeCanvas.height - 20);
    }

    /**
     * Handles image upload and sets the uploaded image.
     */
    function handleImageUpload(event) {
      const file = event.target.files[0];
      if (!file) {
        alert('No image selected.');
        return;
      }

      // Create an image element
      memeImage = new Image();
      memeImage.onload = () => drawMeme();
      memeImage.src = URL.createObjectURL(file);
    }

    /**
     * Downloads the current canvas content as an image file.
     */
    function downloadMeme() {
      const link = document.createElement('a');
      link.download = 'meme.png'; // Name of the downloaded file
      link.href = memeCanvas.toDataURL('image/png');
      link.click();
    }

    // Event listeners
    imageUploadInput.addEventListener('change', handleImageUpload);
    generateMemeButton.addEventListener('click', drawMeme);
    downloadMemeButton.addEventListener('click', downloadMeme);
  </script>
</body>
</html>
```
