"""
Generated Code Metadata:
========================
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Create a script to display dynamic seasonal patterns (spring, summer, autumn, winter) inspired by the Hikeshi NFT project's theme, using HTML5 Canvas or CSS animations.
Generated: DETERMINISTIC_7db36c183b325122
Batch ID: 20250612_153606
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
    <title>Seasonal Patterns Animation</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        
        #canvas-container {
            position: relative;
            width: 800px;
            height: 600px;
        }
        
        canvas {
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        
        #controls {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
        }
        
        button {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            background-color: #4a6fa5;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #3a5a8f;
        }
        
        #season-display {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 24px;
            font-weight: bold;
            color: #333;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 8px 16px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div id="canvas-container">
        <canvas id="seasonCanvas"></canvas>
        <div id="season-display">Spring</div>
        <div id="controls">
            <button id="springBtn">Spring</button>
            <button id="summerBtn">Summer</button>
            <button id="autumnBtn">Autumn</button>
            <button id="winterBtn">Winter</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const canvas = document.getElementById('seasonCanvas');
            const ctx = canvas.getContext('2d');
            const seasonDisplay = document.getElementById('seasonDisplay');
            
            // Set canvas dimensions
            canvas.width = 800;
            canvas.height = 600;
            
            // Season colors and settings
            const seasons = {
                spring: {
                    name: 'Spring',
                    bgColor: '#e8f5e9',
                    particleColor: '#81c784',
                    secondaryColor: '#4caf50',
                    particleCount: 150,
                    particleSize: 3,
                    movementFactor: 0.5
                },
                summer: {
                    name: 'Summer',
                    bgColor: '#e3f2fd',
                    particleColor: '#64b5f6',
                    secondaryColor: '#2196f3',
                    particleCount: 200,
                    particleSize: 4,
                    movementFactor: 0.8
                },
                autumn: {
                    name: 'Autumn',
                    bgColor: '#fff3e0',
                    particleColor: '#ffb74d',
                    secondaryColor: '#ff9800',
                    particleCount: 180,
                    particleSize: 5,
                    movementFactor: 0.6
                },
                winter: {
                    name: 'Winter',
                    bgColor: '#e8eaf6',
                    particleColor: '#bbdefb',
                    secondaryColor: '#90caf9',
                    particleCount: 120,
                    particleSize: 6,
                    movementFactor: 0.4
                }
            };
            
            let currentSeason = 'spring';
            let particles = [];
            
            // Initialize particles
            function initParticles() {
                particles = [];
                const season = seasons[currentSeason];
                
                for (let i = 0; i < season.particleCount; i++) {
                    particles.push({
                        x: Math.random() * canvas.width,
                        y: Math.random() * canvas.height,
                        size: Math.random() * season.particleSize + 1,
                        speedX: (Math.random() - 0.5) * season.movementFactor,
                        speedY: (Math.random() - 0.5) * season.movementFactor,
                        color: Math.random() > 0.7 ? season.secondaryColor : season.particleColor
                    });
                }
            }
            
            // Draw particles
            function drawParticles() {
                const season = seasons[currentSeason];
                
                // Clear canvas with season background
                ctx.fillStyle = season.bgColor;
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                // Draw each particle
                particles.forEach(particle => {
                    ctx.beginPath();
                    ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                    ctx.fillStyle = particle.color;
                    ctx.fill();
                    
                    // Update particle position
                    particle.x += particle.speedX;
                    particle.y += particle.speedY;
                    
                    // Bounce off edges
                    if (particle.x < 0 || particle.x > canvas.width) particle.speedX *= -1;
                    if (particle.y < 0 || particle.y > canvas.height) particle.speedY *= -1;
                });
                
                // Draw season name
                seasonDisplay.textContent = season.name;
            }
            
            // Animation loop
            function animate() {
                drawParticles();
                requestAnimationFrame(animate);
            }
            
            // Change season
            function changeSeason(season) {
                currentSeason = season;
                initParticles();
            }
            
            // Event listeners for buttons
            document.getElementById('springBtn').addEventListener('click', () => changeSeason('spring'));
            document.getElementById('summerBtn').addEventListener('click', () => changeSeason('summer'));
            document.getElementById('autumnBtn').addEventListener('click', () => changeSeason('autumn'));
            document.getElementById('winterBtn').addEventListener('click', () => changeSeason('winter'));
            
            // Initialize and start animation
            initParticles();
            animate();
            
            // Handle window resize
            window.addEventListener('resize', () => {
                canvas.width = 800;
                canvas.height = 600;
                initParticles();
            });
        });
    </script>
</body>
</html>
```
