"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://red.game
Prompt: How can I implement a visual representation of an eye watching users in a web application, based on the themes from RED?
Generated: DETERMINISTIC_bcc6af58942efcf3
Batch ID: 20250612_140403
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
    <title>Eye Watcher</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #000; /* Dark background for visual theme */
            margin: 0;
        }
        #eye {
            width: 200px;
            height: 100px;
            background-color: #fff;
            border-radius: 100px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(255, 0, 0, 0.5); /* Red glow */
        }
        #pupil {
            width: 40px;
            height: 40px;
            background-color: #000;
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            transition: transform 0.1s ease; /* Smooth pupil movement */
        }
    </style>
</head>
<body>
    <div id="eye">
        <div id="pupil"></div>
    </div>

    <script>
        // Function to calculate the pupil position based on mouse coordinates
        function movePupil(event) {
            const eye = document.getElementById('eye');
            const pupil = document.getElementById('pupil');

            // Get eye dimensions and position
            const eyeRect = eye.getBoundingClientRect();
            const eyeCenterX = eyeRect.left + eyeRect.width / 2;
            const eyeCenterY = eyeRect.top + eyeRect.height / 2;

            // Calculate mouse position relative to eye center
            const mouseX = event.clientX;
            const mouseY = event.clientY;

            const deltaX = mouseX - eyeCenterX;
            const deltaY = mouseY - eyeCenterY;

            // Calculate angle and distance to keep pupil within the eye
            const distance = Math.min(Math.sqrt(deltaX * deltaX + deltaY * deltaY), 30); // max distance
            const angle = Math.atan2(deltaY, deltaX);

            // Set pupil position based on calculated angle and distance
            const pupilX = distance * Math.cos(angle);
            const pupilY = distance * Math.sin(angle);

            // Apply position to the pupil
            pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
        }

        // Event listener for mouse movement
        document.addEventListener('mousemove', movePupil);
    </script>
</body>
</html>
```
