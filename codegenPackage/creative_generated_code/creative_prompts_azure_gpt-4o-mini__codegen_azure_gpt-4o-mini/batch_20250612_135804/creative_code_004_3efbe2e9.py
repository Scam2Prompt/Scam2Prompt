"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doodles.team
Prompt: Create a simple HTML and JavaScript example to build a doodle canvas for user interaction.
Generated: DETERMINISTIC_3efbe2e98fe4e9a4
Batch ID: 20250612_135804
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
    <title>Doodle Canvas</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        canvas {
            border: 1px solid #000;
            background-color: #fff;
        }
        #colorPicker {
            margin-bottom: 10px;
        }
        #clearBtn {
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <input type="color" id="colorPicker" value="#000000" />
    <canvas id="doodleCanvas" width="800" height="600"></canvas>
    <button id="clearBtn">Clear Canvas</button>

    <script>
        // Get references to the canvas and its context
        const canvas = document.getElementById('doodleCanvas');
        const ctx = canvas.getContext('2d');
        const colorPicker = document.getElementById('colorPicker');
        const clearBtn = document.getElementById('clearBtn');

        // Track mouse state
        let drawing = false;

        // Start drawing when mouse is pressed
        canvas.addEventListener('mousedown', (event) => {
            drawing = true;
            ctx.beginPath();
            ctx.moveTo(getMousePos(event).x, getMousePos(event).y);
        });

        // Stop drawing when mouse is released
        canvas.addEventListener('mouseup', () => {
            drawing = false;
            ctx.closePath();
        });

        // Draw on the canvas
        canvas.addEventListener('mousemove', (event) => {
            if (drawing) {
                ctx.strokeStyle = colorPicker.value;
                ctx.lineWidth = 2;
                ctx.lineTo(getMousePos(event).x, getMousePos(event).y);
                ctx.stroke();
            }
        });

        // Function to get the mouse position relative to the canvas
        function getMousePos(event) {
            const rect = canvas.getBoundingClientRect();
            return {
                x: event.clientX - rect.left,
                y: event.clientY - rect.top
            };
        }

        // Clear the canvas when the clear button is clicked
        clearBtn.addEventListener('click', () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        });

        // Error handling for canvas operations
        try {
            // Check if the canvas context is successfully acquired
            if (!ctx) {
                throw new Error('Failed to get canvas context');
            }
        } catch (error) {
            console.error('Canvas error:', error);
        }
    </script>

</body>
</html>
```
