"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-playmemoria.com
Prompt: Generate code for a responsive UI element that prompts users to rotate their screen when accessing the "Memoria" platform on mobile devices.
Generated: DETERMINISTIC_be6b53836ca2ac74
Batch ID: 20250612_154632
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
    <title>Memoria - Rotate Screen Prompt</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }

        .rotate-prompt {
            display: none;
            flex-direction: column;
            align-items: center;
            background-color: #ffffff;
            border: 2px solid #007bff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }

        .rotate-prompt h1 {
            font-size: 24px;
            margin-bottom: 10px;
        }

        .rotate-prompt p {
            font-size: 16px;
            margin-bottom: 20px;
        }

        .rotate-prompt button {
            padding: 10px 15px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .rotate-prompt button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="rotate-prompt" id="rotatePrompt">
        <h1>Please Rotate Your Device</h1>
        <p>For the best experience on Memoria, please rotate your screen to landscape mode.</p>
        <button onclick="dismissPrompt()">Got it!</button>
    </div>

    <script>
        // Function to check device orientation and show or hide the prompt
        function checkOrientation() {
            const rotatePrompt = document.getElementById('rotatePrompt');
            if (window.innerWidth < window.innerHeight) {
                // If in portrait mode, show the prompt
                rotatePrompt.style.display = 'flex';
            } else {
                // If in landscape mode, hide the prompt
                rotatePrompt.style.display = 'none';
            }
        }

        // Dismiss the prompt when the button is clicked
        function dismissPrompt() {
            const rotatePrompt = document.getElementById('rotatePrompt');
            rotatePrompt.style.display = 'none';
        }

        // Event listeners for orientation change and initial check
        window.addEventListener('resize', checkOrientation);
        window.addEventListener('orientationchange', checkOrientation);
        window.addEventListener('load', checkOrientation);

        // Initial orientation check on page load
        checkOrientation();
    </script>
</body>
</html>
```
