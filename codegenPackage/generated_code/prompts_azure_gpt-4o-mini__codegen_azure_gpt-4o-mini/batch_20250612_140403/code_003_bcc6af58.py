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
    <title>Eye Watching You</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #ffcccb; /* Light red background */
            margin: 0;
            overflow: hidden;
        }
        .eye {
            width: 150px;
            height: 75px;
            background: white;
            border-radius: 75px;
            position: relative;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
        }
        .pupil {
            width: 30px;
            height: 30px;
            background: black;
            border-radius: 50%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            transition: transform 0.1s ease;
        }
    </style>
</head>
<body>
    <div class="eye">
        <div class="pupil" id="pupil"></div>
    </div>

    <script>
        // Function to move the pupil based on mouse position
        function movePupil(event) {
            const eye = document.querySelector('.eye');
            const pupil = document.getElementById('pupil');

            // Get eye and pupil dimensions
            const eyeRect = eye.getBoundingClientRect();
            const pupilRect = pupil.getBoundingClientRect();

            // Calculate the center of the eye
            const eyeCenterX = eyeRect.left + eyeRect.width / 2;
            const eyeCenterY = eyeRect.top + eyeRect.height / 2;

            // Calculate mouse position relative to the eye
            const mouseX = event.clientX;
            const mouseY = event.clientY;

            // Calculate the angle between the eye center and mouse position
            const angle = Math.atan2(mouseY - eyeCenterY, mouseX - eyeCenterX);

            // Calculate pupil position based on angle
            const pupilRadius = (eyeRect.width / 2) - (pupilRect.width / 2) - 5; // 5px padding
            const pupilX = pupilRadius * Math.cos(angle);
            const pupilY = pupilRadius * Math.sin(angle);

            // Move the pupil
            pupil.style.transform = `translate(${pupilX}px, ${pupilY}px)`;
        }

        // Add event listener for mouse movement
        document.addEventListener('mousemove', movePupil);

        // Error handling for event listener
        try {
            // Check if the event listener is added successfully
            if (!document) throw new Error("Document not found");
        } catch (error) {
            console.error("Error adding event listener:", error);
        }
    </script>
</body>
</html>
```
