"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: How can I implement a visual representation of an eye watching users in a web application, based on the themes from RED?
Generated: DETERMINISTIC_bcc6af58942efcf3
Batch ID: 20250612_140403
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
    <title>Watching Eye</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #111;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        
        .eye-container {
            position: relative;
            width: 200px;
            height: 200px;
        }
        
        .eye {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, #fff 0%, #aaa 100%);
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
            overflow: hidden;
        }
        
        .pupil {
            position: absolute;
            width: 40%;
            height: 40%;
            background: radial-gradient(circle at 30% 30%, #000 0%, #333 100%);
            border-radius: 50%;
            transition: transform 0.1s ease-out;
        }
        
        .eyelid {
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: #111;
            border-radius: 50%;
            animation: blink 5s infinite;
            transform-origin: top;
        }
        
        .veins {
            position: absolute;
            width: 100%;
            height: 100%;
            opacity: 0.3;
        }
        
        .vein {
            position: absolute;
            background-color: #f00;
            border-radius: 10px;
        }
        
        @keyframes blink {
            0%, 96%, 100% { transform: scaleY(1); }
            98% { transform: scaleY(0); }
        }
        
        .message {
            position: absolute;
            bottom: 20px;
            color: #f00;
            text-align: center;
            width: 100%;
            font-size: 18px;
            text-shadow: 0 0 5px rgba(255, 0, 0, 0.7);
        }
    </style>
</head>
<body>
    <div class="eye-container">
        <div class="eye">
            <div class="veins" id="veins"></div>
            <div class="pupil" id="pupil"></div>
        </div>
        <div class="eyelid"></div>
    </div>
    <div class="message">WE ARE WATCHING</div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const pupil = document.getElementById('pupil');
            const eye = document.querySelector('.eye');
            const veins = document.getElementById('veins');
            
            // Create veins
            for (let i = 0; i < 15; i++) {
                const vein = document.createElement('div');
                vein.className = 'vein';
                
                const length = Math.random() * 30 + 10;
                const width = Math.random() * 3 + 1;
                const angle = Math.random() * 360;
                const distance = Math.random() * 40 + 30;
                
                vein.style.width = `${length}px`;
                vein.style.height = `${width}px`;
                vein.style.left = `calc(50% + ${Math.cos(angle * Math.PI / 180) * distance}px)`;
                vein.style.top = `calc(50% + ${Math.sin(angle * Math.PI / 180) * distance}px)`;
                vein.style.transform = `rotate(${angle}deg) translateX(-50%)`;
                
                veins.appendChild(vein);
            }
            
            // Track mouse movement
            document.addEventListener('mousemove', function(e) {
                const eyeRect = eye.getBoundingClientRect();
                const eyeX = eyeRect.left + eyeRect.width / 2;
                const eyeY = eyeRect.top + eyeRect.height / 2;
                
                const angle = Math.atan2(e.clientY - eyeY, e.clientX - eyeX);
                const distance = Math.min(30, 
                    Math.sqrt(Math.pow(e.clientX - eyeX, 2) + Math.pow(e.clientY - eyeY, 2)) / 10);
                
                const pupilX = Math.cos(angle) * distance;
                const pupilY = Math.sin(angle) * distance;
                
                pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
            });
            
            // Handle touch events for mobile
            document.addEventListener('touchmove', function(e) {
                if (e.touches.length > 0) {
                    const touch = e.touches[0];
                    const eyeRect = eye.getBoundingClientRect();
                    const eyeX = eyeRect.left + eyeRect.width / 2;
                    const eyeY = eyeRect.top + eyeRect.height / 2;
                    
                    const angle = Math.atan2(touch.clientY - eyeY, touch.clientX - eyeX);
                    const distance = Math.min(30, 
                        Math.sqrt(Math.pow(touch.clientX - eyeX, 2) + Math.pow(touch.clientY - eyeY, 2)) / 10);
                    
                    const pupilX = Math.cos(angle) * distance;
                    const pupilY = Math.sin(angle) * distance;
                    
                    pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
                }
            }, { passive: true });
        });
    </script>
</body>
</html>
```
