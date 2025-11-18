"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Generate JavaScript code to implement a drawing canvas with options for text input, font selection (Arial, Times New Roman, etc.), and adjustable font size, as described on Monad Whiteboard NFT.
Generated: DETERMINISTIC_8144b241d52f2aab
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML Structure
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drawing Canvas</title>
    <style>
        #canvas {
            border: 1px solid #000;
            cursor: crosshair;
        }
        .controls {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="controls">
        <label for="fontSelect">Font: </label>
        <select id="fontSelect">
            <option value="Arial">Arial</option>
            <option value="Times New Roman">Times New Roman</option>
            <option value="Courier New">Courier New</option>
        </select>
        <label for="fontSize">Size: </label>
        <input type="number" id="fontSize" value="16" min="1" max="100">
        <label for="textInput">Text: </label>
        <input type="text" id="textInput" placeholder="Enter text here">
        <button id="drawTextBtn">Draw Text</button>
    </div>
    <canvas id="canvas" width="800" height="600"></canvas>

    <script>
        // Get references to the DOM elements
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const fontSelect = document.getElementById('fontSelect');
        const fontSizeInput = document.getElementById('fontSize');
        const textInput = document.getElementById('textInput');
        const drawTextBtn = document.getElementById('drawTextBtn');

        // Function to draw text on the canvas
        const drawText = () => {
            // Clear the previous text
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Get user input values
            const font = fontSelect.value;
            const fontSize = fontSizeInput.value;
            const text = textInput.value;

            // Validate the text input
            if (!text.trim()) {
                alert("Please enter some text.");
                return;
            }

            // Set the font style for the canvas context
            ctx.font = `${fontSize}px ${font}`;
            ctx.textBaseline = 'top'; // Set the text baseline

            // Draw the text at a fixed position
            ctx.fillText(text, 50, 50);
        };

        // Event listener for the draw text button
        drawTextBtn.addEventListener('click', drawText);
    </script>
</body>
</html>
```
