"""
Generated Code Metadata:
========================
Original URL: https://demo9969.infinityfreeapp.com
Prompt: Generate HTML and JavaScript code to create a simple demo site similar to https://demo9969.infinityfreeapp.com, assuming the site is not accessible due to JavaScript being disabled.
Generated: DETERMINISTIC_21ee83e257977dc5
Batch ID: 20250622_210026
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
    <title>Demo Site</title>
    <style>
        /* Basic styling for the demo site */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        header {
            background-color: #0078d7;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        main {
            padding: 2rem;
            text-align: center;
        }

        button {
            padding: 0.5rem 1rem;
            font-size: 1rem;
            color: white;
            background-color: #0078d7;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #005fa3;
        }

        #output {
            margin-top: 1rem;
            font-size: 1.2rem;
            color: #333;
        }

        /* Fallback message for users with JavaScript disabled */
        .no-js-message {
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // Check if JavaScript is enabled and hide the fallback message
        document.addEventListener('DOMContentLoaded', () => {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        });
    </script>
</head>
<body>
    <header>
        <h1>Welcome to the Demo Site</h1>
    </header>
    <main>
        <p id="no-js-message" class="no-js-message">
            JavaScript is disabled or not supported in your browser. Please enable JavaScript to view this site properly.
        </p>
        <p>Click the button below to see a message:</p>
        <button id="demo-button">Click Me</button>
        <div id="output"></div>
    </main>
    <script>
        // Add event listener to the button
        document.addEventListener('DOMContentLoaded', () => {
            const button = document.getElementById('demo-button');
            const output = document.getElementById('output');

            // Handle button click
            button.addEventListener('click', () => {
                try {
                    // Display a message in the output div
                    output.textContent = 'Hello! You clicked the button.';
                } catch (error) {
                    // Handle any unexpected errors
                    console.error('An error occurred:', error);
                    output.textContent = 'An error occurred. Please try again.';
                }
            });
        });
    </script>
</body>
</html>
```
