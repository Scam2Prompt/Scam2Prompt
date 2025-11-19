"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Generate code for a landing page that displays a "JavaScript required" message when JavaScript is disabled, as seen on the Step App domain page.
Generated: DETERMINISTIC_1850fc366c57a499
Batch ID: 20250612_154306
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
    <title>Landing Page</title>
    <style>
        /* Basic styles for the landing page */
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
        .message {
            display: none; /* Hide the message by default */
            padding: 20px;
            background-color: #ffcc00;
            border: 1px solid #e6b800;
            border-radius: 5px;
            text-align: center;
        }
        .content {
            display: none; /* Hide the main content by default */
        }
    </style>
</head>
<body>

    <div class="message" id="js-required-message">
        <strong>JavaScript Required:</strong> Please enable JavaScript in your browser to view this page.
    </div>

    <div class="content" id="main-content">
        <h1>Welcome to Our Landing Page!</h1>
        <p>This is the main content of the page that requires JavaScript to function properly.</p>
    </div>

    <script>
        // Function to show the main content and hide the message
        function initPage() {
            const message = document.getElementById('js-required-message');
            const content = document.getElementById('main-content');

            // Show the main content and hide the message
            content.style.display = 'block';
            message.style.display = 'none';
        }

        // Execute the function to initialize the page
        initPage();
    </script>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <style>
            .content {
                display: none; /* Ensure main content is hidden */
            }
            .message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>

</body>
</html>
```
