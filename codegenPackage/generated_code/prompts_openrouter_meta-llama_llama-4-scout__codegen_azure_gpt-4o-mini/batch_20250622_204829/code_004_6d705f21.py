"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: "Create a basic webpage template in HTML/CSS/JavaScript that requires enabling JavaScript to view content, similar to imseoa.com's current page."
Generated: DETERMINISTIC_6d705f21fc5da5bd
Batch ID: 20250622_204829
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
    <title>Basic Webpage Template</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic styles for the webpage */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .no-js {
            display: block;
            background-color: #ffcc00;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }
        .content {
            display: none; /* Hidden by default */
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js">
            JavaScript is disabled in your browser. Please enable JavaScript to view the content of this page.
        </div>
    </noscript>

    <div class="container">
        <div class="content" id="mainContent">
            <h1>Welcome to My Webpage</h1>
            <p>This content is only visible when JavaScript is enabled.</p>
            <button id="alertButton">Click Me!</button>
        </div>
    </div>

    <script>
        // Function to initialize the webpage content
        function init() {
            try {
                // Display the main content
                document.getElementById('mainContent').style.display = 'block';

                // Add event listener to the button
                document.getElementById('alertButton').addEventListener('click', function() {
                    alert('Button clicked! JavaScript is working.');
                });
            } catch (error) {
                console.error('An error occurred while initializing the page:', error);
            }
        }

        // Run the init function when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>
```
