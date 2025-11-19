"""
Generated Code Metadata:
========================
Original URL: https://celestiacelestia.com
Prompt: Design a webpage with a feature to dynamically change the background color or content when JavaScript is enabled, using a library or vanilla JavaScript.
Generated: DETERMINISTIC_09ffc8a5ac154c48
Batch ID: 20250622_212817
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
    <title>Dynamic Background Changer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            transition: background-color 0.5s ease;
            padding: 2rem;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        button {
            padding: 0.8rem 1.5rem;
            margin: 0.5rem;
            font-size: 1rem;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .no-js-message {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Dynamic Background Changer</h1>
        <noscript>
            <p class="no-js-message">JavaScript is disabled. Please enable JavaScript for full functionality.</p>
        </noscript>
        <div id="js-content">
            <p>Click the buttons below to change the background color or content dynamically.</p>
            <div>
                <button id="color-btn">Change Background Color</button>
                <button id="content-btn">Change Content</button>
            </div>
            <div id="dynamic-content">
                <p>Welcome to our interactive webpage!</p>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Hide no-JS message and show JS content
            document.getElementById('js-content').style.display = 'block';

            // Get DOM elements
            const colorBtn = document.getElementById('color-btn');
            const contentBtn = document.getElementById('content-btn');
            const dynamicContent = document.getElementById('dynamic-content');
            const body = document.body;

            // Array of background colors
            const colors = [
                '#f8bbd0', '#e1bee7', '#d1c4e9', 
                '#c5cae9', '#b3e5fc', '#b2ebf2', 
                '#b2dfdb', '#c8e6c9', '#dcedc8'
            ];

            // Array of content messages
            const messages = [
                "You've changed the content!",
                "JavaScript makes web pages interactive!",
                "Dynamic content is fun!",
                "Try clicking the color button too!",
                "Web development is awesome!"
            ];

            // Change background color
            colorBtn.addEventListener('click', function() {
                const randomColor = colors[Math.floor(Math.random() * colors.length)];
                body.style.backgroundColor = randomColor;
            });

            // Change content
            contentBtn.addEventListener('click', function() {
                const randomMessage = messages[Math.floor(Math.random() * messages.length)];
                dynamicContent.innerHTML = `<p>${randomMessage}</p>`;
            });

            // Initialize with a random color
            body.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        });
    </script>
</body>
</html>
```
