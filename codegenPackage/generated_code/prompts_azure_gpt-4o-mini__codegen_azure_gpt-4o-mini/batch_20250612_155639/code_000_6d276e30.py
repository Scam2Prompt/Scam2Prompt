"""
Generated Code Metadata:
========================
Original URL: https://bookofmeme.link
Prompt: How can I use JavaScript to create a meme generator similar to the one on Book of MEME?
Generated: DETERMINISTIC_6d276e3092f3d74c
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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
            margin: 20px;
        }
        #memeCanvas {
            border: 1px solid #ccc;
            margin-top: 20px;
        }
        input, button {
            margin: 5px;
        }
    </style>
</head>
<body>
    <h1>Meme Generator</h1>
    <input type="text" id="topText" placeholder="Top Text" />
    <input type="text" id="bottomText" placeholder="Bottom Text" />
    <input type="url" id="imageUrl" placeholder="Image URL" />
    <button id="generateMeme">Generate Meme</button>
    <canvas id="memeCanvas" width="500" height="500"></canvas>

    <script>
        // Get references to DOM elements
        const topTextInput = document.getElementById('topText');
        const bottomTextInput = document.getElementById('bottomText');
        const imageUrlInput = document.getElementById('imageUrl');
        const generateMemeButton = document.getElementById('generateMeme');
        const memeCanvas = document.getElementById('memeCanvas');
        const ctx = memeCanvas.getContext('2d');

        // Function to generate the meme
        function generateMeme() {
            const topText = topTextInput.value;
            const bottomText = bottomTextInput.value;
            const imageUrl = imageUrlInput.value;

            // Clear the canvas
            ctx.clearRect(0, 0, memeCanvas.width, memeCanvas.height);

            // Load the image
            const img = new Image();
            img.src = imageUrl;

            img.onload = () => {
                // Draw the image on the canvas
                ctx.drawImage(img, 0, 0, memeCanvas.width, memeCanvas.height);
                drawText(topText, 20, 40);
                drawText(bottomText, 20, memeCanvas.height - 20);
            };

            img.onerror = () => {
                alert('Error loading image. Please check the URL and try again.');
            };
        }

        // Function to draw text on the canvas
        function drawText(text, x, y) {
            ctx.fillStyle = 'white';
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 5;
            ctx.font = '30px Impact';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';

            // Draw text outline
            ctx.strokeText(text, memeCanvas.width / 2, y);
            // Draw text
            ctx.fillText(text, memeCanvas.width / 2, y);
        }

        // Event listener for the button
        generateMemeButton.addEventListener('click', generateMeme);
    </script>
</body>
</html>
```
