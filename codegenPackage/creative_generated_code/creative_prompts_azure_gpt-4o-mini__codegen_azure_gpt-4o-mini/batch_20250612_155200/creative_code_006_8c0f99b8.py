"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safarait.com
Prompt: How can I utilize animation in web design to enhance user experience on a site developed by Safara IT?
Generated: DETERMINISTIC_8c0f99b821c9096e
Batch ID: 20250612_155200
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
    <title>Animation Example - Safara IT</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
    <style>
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        /* Button styling */
        .animated-button {
            padding: 15px 30px;
            font-size: 18px;
            border: none;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s; /* Animation transitions */
            border-radius: 5px;
        }

        /* Button hover effect */
        .animated-button:hover {
            background-color: #0056b3; /* Darker shade on hover */
            transform: scale(1.05); /* Slightly increase size on hover */
        }

        /* Fade-in effect for content */
        .fade-in {
            opacity: 0;
            transition: opacity 1s; /* Fade transition */
        }

        .fade-in.visible {
            opacity: 1; /* Full opacity when visible */
        }
    </style>
</head>
<body>
    <button class="animated-button" id="animateButton">Click Me!</button>
    <div id="message" class="fade-in">Welcome to Safara IT!</div>

    <script>
        // Wait for the DOM to load
        document.addEventListener('DOMContentLoaded', (event) => {
            const button = document.getElementById('animateButton');
            const message = document.getElementById('message');

            // Show the message with fade-in effect
            setTimeout(() => {
                message.classList.add('visible');
            }, 500); // Delay for half a second

            // Attach click event listener to the button
            button.addEventListener('click', () => {
                alert('Button clicked!'); // Handle button click
            });
        });
    </script>
</body>
</html>
```
