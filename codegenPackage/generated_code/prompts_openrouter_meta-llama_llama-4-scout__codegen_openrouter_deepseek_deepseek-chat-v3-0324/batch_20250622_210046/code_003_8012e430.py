"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: Create a simple webpage that enables JavaScript and runs a basic app, similar to Morpho, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_8012e430821c98a3
Batch ID: 20250622_210046
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
    <title>Morpho-like App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f5f5f5;
        }

        header {
            width: 100%;
            background-color: #6200ee;
            color: white;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        .container {
            width: 90%;
            max-width: 800px;
            margin: 2rem auto;
            padding: 1rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        button {
            padding: 0.5rem 1rem;
            background-color: #6200ee;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #3700b3;
        }

        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }

        canvas {
            width: 100%;
            height: 400px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .error-message {
            color: #d32f2f;
            padding: 1rem;
            text-align: center;
            display: none;
        }

        @media (max-width: 600px) {
            .controls {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Morpho-like App</h1>
    </header>

    <div class="container">
        <div class="error-message" id="errorMessage">
            JavaScript is required to run this application. Please enable JavaScript in your browser.
        </div>

        <div class="controls">
            <button id="drawBtn">Draw</button>
            <button id="clearBtn">Clear</button>
            <button id="animateBtn">Animate</button>
        </div>

        <canvas id="drawingCanvas"></canvas>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.getElementById('errorMessage').style.display = 'none';

        // Main application
        document.addEventListener('DOMContentLoaded', function() {
            try {
                const canvas = document.getElementById('drawingCanvas');
                const ctx = canvas.getContext('2d');
                const drawBtn = document.getElementById('drawBtn');
                const clearBtn = document.getElementById('clearBtn');
                const animateBtn = document.getElementById('animateBtn');

                // Set canvas dimensions
                function resizeCanvas() {
                    canvas.width = canvas.offsetWidth;
                    canvas.height = canvas.offsetHeight;
                }

                window.addEventListener('resize', resizeCanvas);
                resizeCanvas();

                // Drawing state
                let isDrawing = false;
                let lastX = 0;
                let lastY = 0;
                let hue = 0;
                let animationId = null;

                // Draw function
                function draw(e) {
                    if (!isDrawing) return;
                    
                    ctx.strokeStyle = `hsl(${hue}, 100%, 50%)`;
                    ctx.lineWidth = 5;
                    ctx.lineCap = 'round';
                    ctx.beginPath();
                    ctx.moveTo(lastX, lastY);
                    ctx.lineTo(e.offsetX, e.offsetY);
                    ctx.stroke();
                    
                    lastX = e.offsetX;
                    lastY = e.offsetY;
                    hue = (hue + 1) % 360;
                }

                // Event listeners for drawing
                canvas.addEventListener('mousedown', (e) => {
                    isDrawing = true;
                    lastX = e.offsetX;
                    lastY = e.offsetY;
                });

                canvas.addEventListener('mousemove', draw);
                canvas.addEventListener('mouseup', () => isDrawing = false);
                canvas.addEventListener('mouseout', () => isDrawing = false);

                // Button event handlers
                drawBtn.addEventListener('click', () => {
                    if (animationId) {
                        cancelAnimationFrame(animationId);
                        animationId = null;
                    }
                    canvas.style.cursor = 'crosshair';
                });

                clearBtn.addEventListener('click', () => {
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    if (animationId) {
                        cancelAnimationFrame(animationId);
                        animationId = null;
                    }
                });

                animateBtn.addEventListener('click', () => {
                    if (animationId) {
                        cancelAnimationFrame(animationId);
                    }
                    canvas.style.cursor = 'default';
                    
                    let angle = 0;
                    const radius = 50;
                    const centerX = canvas.width / 2;
                    const centerY = canvas.height / 2;
                    
                    function animate() {
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        
                        const x = centerX + Math.cos(angle) * radius;
                        const y = centerY + Math.sin(angle) * radius;
                        
                        ctx.beginPath();
                        ctx.arc(x, y, 20, 0, Math.PI * 2);
                        ctx.fillStyle = `hsl(${hue}, 100%, 50%)`;
                        ctx.fill();
                        
                        angle += 0.05;
                        hue = (hue + 1) % 360;
                        
                        animationId = requestAnimationFrame(animate);
                    }
                    
                    animate();
                });

            } catch (error) {
                console.error('Error initializing application:', error);
                document.getElementById('errorMessage').style.display = 'block';
            }
        });
    </script>
</body>
</html>
```
