"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bookofmeme.link
Prompt: How can I use JavaScript to create a meme generator similar to the one on Book of MEME?
Generated: DETERMINISTIC_6d276e3092f3d74c
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
  <title>Meme Generator</title>
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
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <h1>Meme Generator</h1>
  <div class="controls">
    <input type="file" id="imageUpload" accept="image/*">
    <br><br>
    <input type="text" id="topText" placeholder="Top Text">
    <input type="text" id="bottomText" placeholder="Bottom Text">
    <br><br>
    <button id="generateMeme">Generate Meme</button>
  </div>
  <canvas id="memeCanvas" width="500" height="500"></canvas>
  <script>
    // Select DOM elements
    const imageUpload = document.getElementById('imageUpload');
    const topTextInput = document.getElementById('topText');
    const bottomTextInput = document.getElementById('bottomText');
    const generateMemeButton = document.getElementById('generateMeme');
    const memeCanvas = document.getElementById('memeCanvas');
    const ctx = memeCanvas.getContext('2d');

    let memeImage = null;

    // Load image when selected
    imageUpload.addEventListener('change', event => {
      const file = event.target.files[0];
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();

        reader.onload = function (e) {
          const img = new Image();
          img.src = e.target.result;

          img.onload = function () {
            memeImage = img;
            drawMeme(); // Draw the meme once image is loaded
          };
        };

        reader.readAsDataURL(file);
      } else {
        alert('Please upload a valid image file.');
      }
    });

    // Draw meme on canvas
    function drawMeme() {
      if (!memeImage) return;

      // Clear the canvas
      ctx.clearRect(0, 0, memeCanvas.width, memeCanvas.height);

      // Draw the image
      const canvasWidth = memeCanvas.width;
      const canvasHeight = memeCanvas.height;
      const imgRatio = memeImage.width / memeImage.height;
      let imgWidth, imgHeight;

      if (imgRatio > 1) {
        imgWidth = canvasWidth;
        imgHeight = canvasWidth / imgRatio;
      } else {
        imgHeight = canvasHeight;
        imgWidth = canvasHeight * imgRatio;
      }

      const xOffset = (canvasWidth - imgWidth) / 2;
      const yOffset = (canvasHeight - imgHeight) / 2;

      ctx.drawImage(memeImage, xOffset, yOffset, imgWidth, imgHeight);

      // Add top text
      ctx.fillStyle = 'white';
      ctx.strokeStyle = 'black';
      ctx.font = '40px Impact';
      ctx.textAlign = 'center';
      ctx.lineWidth = 2;
      ctx.textBaseline = 'top';

      const topText = topTextInput.value.toUpperCase();
      ctx.fillText(topText, canvasWidth / 2, 10);
      ctx.strokeText(topText, canvasWidth / 2, 10);

      // Add bottom text
      ctx.textBaseline = 'bottom';
      const bottomText = bottomTextInput.value.toUpperCase();
      ctx.fillText(bottomText, canvasWidth / 2, canvasHeight - 10);
      ctx.strokeText(bottomText, canvasWidth / 2, canvasHeight - 10);
    }

    // Generate meme button click handler
    generateMemeButton.addEventListener('click', drawMeme);
  </script>
</body>
</html>
```
