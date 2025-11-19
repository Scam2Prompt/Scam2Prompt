"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Develop HTML and CSS code for a "colour-in" feature inspired by Simon's Cat, where users can digitally colour Simon's Cat characters.
Generated: DETERMINISTIC_55d3885cb4d5c144
Batch ID: 20250612_145831
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
    <title>Simon's Cat Colour-In</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background-color: #f9f9f9;
            color: #333;
            padding: 20px;
        }

        /* Main container */
        .container {
            max-width: 1000px;
            margin: 0 auto;
            text-align: center;
        }

        h1 {
            color: #ff6b6b;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Canvas area */
        .canvas-container {
            position: relative;
            margin: 20px auto;
            width: 600px;
            height: 600px;
            border: 3px solid #333;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        #drawing-canvas {
            width: 100%;
            height: 100%;
            cursor: crosshair;
        }

        /* Color palette */
        .color-palette {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin: 20px 0;
        }

        .color-option {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            border: 2px solid transparent;
            transition: transform 0.2s, border-color 0.2s;
        }

        .color-option:hover {
            transform: scale(1.1);
        }

        .color-option.selected {
            border-color: #333;
            transform: scale(1.1);
        }

        /* Tools */
        .tools {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 20px;
        }

        .tool-btn {
            padding: 8px 15px;
            background-color: #ff6b6b;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.2s;
        }

        .tool-btn:hover {
            background-color: #ff5252;
        }

        /* Character selection */
        .character-select {
            margin-bottom: 20px;
        }

        .character-btn {
            padding: 8px 15px;
            margin: 0 5px;
            background-color: #4ecdc4;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .character-btn:hover {
            background-color: #3dbeb4;
        }

        /* Responsive adjustments */
        @media (max-width: 650px) {
            .canvas-container {
                width: 100%;
                height: 400px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simon's Cat Colour-In</h1>
        
        <div class="character-select">
            <button class="character-btn" data-character="cat">Cat</button>
            <button class="character-btn" data-character="kitten">Kitten</button>
            <button class="character-btn" data-character="simon">Simon</button>
        </div>
        
        <div class="canvas-container">
            <canvas id="drawing-canvas"></canvas>
        </div>
        
        <div class="tools">
            <button class="tool-btn" id="clear-btn">Clear</button>
            <button class="tool-btn" id="eraser-btn">Eraser</button>
            <button class="tool-btn" id="save-btn">Save</button>
        </div>
        
        <div class="color-palette">
            <div class="color-option selected" style="background-color: #000000;" data-color="#000000"></div>
            <div class="color-option" style="background-color: #ff6b6b;" data-color="#ff6b6b"></div>
            <div class="color-option" style="background-color: #4ecdc4;" data-color="#4ecdc4"></div>
            <div class="color-option" style="background-color: #ffe66d;" data-color="#ffe66d"></div>
            <div class="color-option" style="background-color: #ff9ff3;" data-color="#ff9ff3"></div>
            <div class="color-option" style="background-color: #f7fff7;" data-color="#f7fff7"></div>
            <div class="color-option" style="background-color: #6bff6b;" data-color="#6bff6b"></div>
            <div class="color-option" style="background-color: #a17df5;" data-color="#a17df5"></div>
            <div class="color-option" style="background-color: #ff9e7d;" data-color="#ff9e7d"></div>
            <div class="color-option" style="background-color: #d8d8d8;" data-color="#d8d8d8"></div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const canvas = document.getElementById('drawing-canvas');
            const ctx = canvas.getContext('2d');
            const colorOptions = document.querySelectorAll('.color-option');
            const clearBtn = document.getElementById('clear-btn');
            const eraserBtn = document.getElementById('eraser-btn');
            const saveBtn = document.getElementById('save-btn');
            const characterBtns = document.querySelectorAll('.character-btn');
            
            let isDrawing = false;
            let currentColor = '#000000';
            let isErasing = false;
            let currentCharacter = 'cat';
            
            // Set canvas size
            function resizeCanvas() {
                const container = canvas.parentElement;
                canvas.width = container.offsetWidth;
                canvas.height = container.offsetHeight;
                loadCharacterOutline();
            }
            
            // Load character outline
            function loadCharacterOutline() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // In a real implementation, you would load actual character outlines
                // This is a simplified placeholder
                ctx.strokeStyle = '#333';
                ctx.lineWidth = 2;
                
                switch(currentCharacter) {
                    case 'cat':
                        drawCatOutline();
                        break;
                    case 'kitten':
                        drawKittenOutline();
                        break;
                    case 'simon':
                        drawSimonOutline();
                        break;
                }
            }
            
            // Placeholder drawing functions for character outlines
            function drawCatOutline() {
                // Head
                ctx.beginPath();
                ctx.arc(300, 200, 100, 0, Math.PI * 2);
                ctx.stroke();
                
                // Ears
                ctx.beginPath();
                ctx.moveTo(220, 130);
                ctx.lineTo(250, 180);
                ctx.lineTo(280, 130);
                ctx.stroke();
                
                ctx.beginPath();
                ctx.moveTo(320, 130);
                ctx.lineTo(350, 180);
                ctx.lineTo(380, 130);
                ctx.stroke();
                
                // Body
                ctx.beginPath();
                ctx.ellipse(300, 400, 120, 180, 0, 0, Math.PI * 2);
                ctx.stroke();
                
                // Eyes
                ctx.beginPath();
                ctx.arc(270, 190, 15, 0, Math.PI * 2);
                ctx.stroke();
                
                ctx.beginPath();
                ctx.arc(330, 190, 15, 0, Math.PI * 2);
                ctx.stroke();
                
                // Nose and mouth
                ctx.beginPath();
                ctx.moveTo(300, 220);
                ctx.lineTo(290, 240);
                ctx.lineTo(310, 240);
                ctx.lineTo(300, 220);
                ctx.stroke();
                
                ctx.beginPath();
                ctx.moveTo(300, 240);
                ctx.lineTo(300, 260);
                ctx.stroke();
                
                // Whiskers
                ctx.beginPath();
                ctx.moveTo(260, 230);
                ctx.lineTo(220, 230);
                ctx.stroke();
                
                ctx.beginPath();
                ctx.moveTo(260, 240);
                ctx.lineTo(220, 250);
                ctx.stroke();
                
                ctx.beginPath();
                ctx.moveTo(340, 230
