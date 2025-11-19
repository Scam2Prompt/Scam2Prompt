"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: Generate a code snippet to create a neon animal graphic using HTML5 Canvas.
Generated: DETERMINISTIC_f3c6873acc6ec986
Batch ID: 20250612_135609
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
    <title>Neon Animal Graphic</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <canvas id="neonCanvas"></canvas>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('neonCanvas');
            const ctx = canvas.getContext('2d');
            
            // Set canvas size to window size
            function resizeCanvas() {
                const size = Math.min(window.innerWidth, window.innerHeight) * 0.8;
                canvas.width = size;
                canvas.height = size;
                drawNeonAnimal();
            }
            
            // Draw a neon-style cat
            function drawNeonAnimal() {
                // Clear canvas
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                const centerX = canvas.width / 2;
                const centerY = canvas.height / 2;
                const size = Math.min(canvas.width, canvas.height) * 0.8;
                
                // Outer glow effect
                ctx.shadowBlur = 20;
                ctx.shadowColor = '#0ff';
                
                // Draw cat head
                ctx.beginPath();
                ctx.arc(centerX, centerY, size * 0.3, 0, Math.PI * 2);
                ctx.strokeStyle = '#0ff';
                ctx.lineWidth = 5;
                ctx.stroke();
                
                // Draw ears
                ctx.beginPath();
                ctx.moveTo(centerX - size * 0.2, centerY - size * 0.2);
                ctx.lineTo(centerX - size * 0.3, centerY - size * 0.4);
                ctx.lineTo(centerX - size * 0.1, centerY - size * 0.25);
                ctx.moveTo(centerX + size * 0.2, centerY - size * 0.2);
                ctx.lineTo(centerX + size * 0.3, centerY - size * 0.4);
                ctx.lineTo(centerX + size * 0.1, centerY - size * 0.25);
                ctx.stroke();
                
                // Draw eyes
                ctx.beginPath();
                ctx.arc(centerX - size * 0.1, centerY - size * 0.05, size * 0.05, 0, Math.PI * 2);
                ctx.arc(centerX + size * 0.1, centerY - size * 0.05, size * 0.05, 0, Math.PI * 2);
                ctx.stroke();
                
                // Draw mouth
                ctx.beginPath();
                ctx.arc(centerX, centerY + size * 0.1, size * 0.08, 0, Math.PI);
                ctx.stroke();
                
                // Draw whiskers
                ctx.beginPath();
                ctx.moveTo(centerX - size * 0.1, centerY + size * 0.05);
                ctx.lineTo(centerX - size * 0.3, centerY + size * 0.05);
                ctx.moveTo(centerX - size * 0.1, centerY + size * 0.1);
                ctx.lineTo(centerX - size * 0.3, centerY + size * 0.15);
                ctx.moveTo(centerX + size * 0.1, centerY + size * 0.05);
                ctx.lineTo(centerX + size * 0.3, centerY + size * 0.05);
                ctx.moveTo(centerX + size * 0.1, centerY + size * 0.1);
                ctx.lineTo(centerX + size * 0.3, centerY + size * 0.15);
                ctx.stroke();
                
                // Reset shadow
                ctx.shadowBlur = 0;
            }
            
            // Initial setup
            resizeCanvas();
            
            // Handle window resize
            window.addEventListener('resize', () => {
                resizeCanvas();
            });
            
            // Add animation effect
            let hue = 0;
            function animate() {
                hue = (hue + 1) % 360;
                ctx.shadowColor = `hsl(${hue}, 100%, 50%)`;
                drawNeonAnimal();
                requestAnimationFrame(animate);
            }
            
            animate();
        });
    </script>
</body>
</html>
```
