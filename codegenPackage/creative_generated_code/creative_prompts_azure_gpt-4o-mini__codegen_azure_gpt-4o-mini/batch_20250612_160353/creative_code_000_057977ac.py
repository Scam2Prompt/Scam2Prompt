"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibot15.cc
Prompt: How can I enable JavaScript for a web application to ensure proper functionality?
Generated: DETERMINISTIC_057977ac8d15b01f
Batch ID: 20250612_160353
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
    <title>Enable JavaScript Example</title>
    <style>
        /* Basic styles for the application */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .js-enabled {
            display: none; /* Hide this section by default */
        }
        .js-disabled {
            display: block; /* Show this if JavaScript is not enabled */
            color: red;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="js-disabled">
            <h2>JavaScript is Disabled</h2>
            <p>Please enable JavaScript in your browser settings to ensure proper functionality of this web application.</p>
        </div>
    </noscript>

    <div class="js-enabled">
        <h1>Welcome to My Web Application</h1>
        <p>This is a simple demonstration of how to enable and utilize JavaScript.</p>
        <button id="exampleButton">Click Me!</button>
        <p id="output"></p>
    </div>

    <script>
        // Function to handle button click
        function handleButtonClick() {
            try {
                // Modify the content of the paragraph with the id 'output'
                const outputElement = document.getElementById('output');
                outputElement.textContent = "JavaScript is enabled! You clicked the button.";
            } catch (error) {
                console.error("An error occurred while handling the button click:", error);
            }
        }

        // Add event listener to the button after the DOM content is fully loaded
        document.addEventListener('DOMContentLoaded', () => {
            const button = document.getElementById('exampleButton');
            if (button) {
                button.addEventListener('click', handleButtonClick);
            } else {
                console.error("Button element not found in the DOM.");
            }
        });
    </script>
</body>
</html>
```
