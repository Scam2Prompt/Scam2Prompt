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
            padding: 20px;
            background-color: #f5f5f5;
        }
        #memeCanvas {
            border: 1px solid #ccc;
            margin: 20px 0;
        }
        .input-container {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<h1>Create Your Meme</h1>
<div class="input-container">
    <input type="text" id="topText" placeholder="Top Text" required>
</div>
<div class="input-container">
    <input type="text" id="bottomText" placeholder="Bottom Text" required>
</div>
<div class="input-container">
    <input type="file" id="imageUpload" accept="image/*" required>
</div>
<button id="createMeme">Create Meme</button>

<canvas id="memeCanvas" width="500" height="500"></canvas>

<script>
    // Wait for the DOM to load
    document.addEventListener('DOMContentLoaded', () => {
        const canvas = document.getElementById('memeCanvas');
        const ctx = canvas.getContext('2d');
        const createMemeButton = document.getElementById('createMeme');
        const imageUpload = document.getElementById('imageUpload');
        const topTextInput = document.getElementById('topText');
        const bottomTextInput = document.getElementById('bottomText');
        let memeImage = new Image();

        // Function to draw the meme on the canvas
        function drawMeme() {
            // Clear the canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            // Draw the image
            ctx.drawImage(memeImage, 0, 0, canvas.width, canvas.height);
            // Set font properties
            ctx.font = '40px Impact';
            ctx.textAlign = 'center';
            ctx.fillStyle = 'white';
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 2;

            // Draw the top text
            ctx.fillText(topTextInput.value, canvas.width / 2, 50);
            ctx.strokeText(topTextInput.value, canvas.width / 2, 50);
            
            // Draw the bottom text
            ctx.fillText(bottomTextInput.value, canvas.width / 2, canvas.height - 20);
            ctx.strokeText(bottomTextInput.value, canvas.width / 2, canvas.height - 20);
        }

        // Handle image upload
        imageUpload.addEventListener('change', (event) => {
            if (event.target.files && event.target.files[0]) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    memeImage.src = e.target.result;
                    memeImage.onload = () => {
                        drawMeme();
                    };
                };
                reader.onerror = (error) => {
                    console.error('Error reading file:', error);
                };
                reader.readAsDataURL(event.target.files[0]);
            }
        });

        // Create meme button click event
        createMemeButton.addEventListener('click', () => {
            if (!memeImage.src) {
                console.error('No image uploaded!');
                alert('Please upload an image first.');
                return;
            }
            drawMeme();
        });
    });
</script>

</body>
</html>
```
