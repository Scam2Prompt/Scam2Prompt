"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.eu
Prompt: How can I enable JavaScript for a web application to ensure it functions properly?
Generated: DETERMINISTIC_48889f4666552744
Batch ID: 20250612_155840
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
    <title>JavaScript Enabled Web Application</title>
    <style>
        /* Basic styles for the message */
        .no-js {
            display: none; /* Hide the message by default */
        }
        .js {
            display: block; /* Show the message when JavaScript is enabled */
        }
    </style>
</head>
<body>
    <!-- Message shown when JavaScript is disabled -->
    <noscript>
        <style>
            .no-js {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
        <div class="no-js">
            <p>Please enable JavaScript in your browser settings to ensure the proper functioning of this web application.</p>
        </div>
    </noscript>

    <!-- Main content of the application -->
    <div class="app-content js">
        <h1>Welcome to Our Web Application</h1>
        <p>This application requires JavaScript to function properly.</p>
        <button id="actionButton">Click Me</button>
        <p id="message"></p>
    </div>

    <script>
        // Ensure the DOM is fully loaded before running scripts
        document.addEventListener('DOMContentLoaded', () => {
            const actionButton = document.getElementById('actionButton');
            const message = document.getElementById('message');

            // Add event listener to the button
            actionButton.addEventListener('click', () => {
                try {
                    // Action performed on button click
                    message.textContent = 'Button clicked! JavaScript is working!';
                } catch (error) {
                    // Log any errors to the console for debugging
                    console.error('An error occurred:', error);
                    message.textContent = 'An error occurred. Please try again.';
                }
            });
        });
    </script>
</body>
</html>
```
