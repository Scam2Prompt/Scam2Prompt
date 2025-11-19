"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrum.net
Prompt: Generate a script that checks if JavaScript is enabled in a user's browser before allowing access to a web application.
Generated: DETERMINISTIC_ad63874db4d0a20c
Batch ID: 20250612_164035
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
    <title>JavaScript Check</title>
    <style>
        /* Style to hide the content until JavaScript is enabled */
        .no-js {
            display: none;
        }
    </style>
</head>
<body class="no-js">
    <noscript>
        <!-- Message displayed when JavaScript is disabled -->
        <div id="no-js-message">
            <h1>JavaScript is Disabled</h1>
            <p>This web application requires JavaScript to function. Please enable JavaScript in your browser settings and refresh the page.</p>
        </div>
    </noscript>

    <div id="app">
        <!-- Main application content goes here -->
        <h1>Welcome to the Web Application</h1>
        <p>Your browser supports JavaScript.</p>
    </div>

    <script>
        // Function to enable the application once JavaScript is detected
        function enableApp() {
            // Modify the body class to indicate that JavaScript is enabled
            document.body.classList.remove('no-js');

            // Show the application content and hide the message for disabled JavaScript
            document.getElementById('app').style.display = 'block';
        }

        // Error handling to ensure the function runs correctly
        try {
            enableApp();
        } catch (error) {
            console.error('An error occurred while enabling the application:', error);
            alert('There was an error enabling the application. Please refresh the page.');
        }
    </script>
</body>
</html>
```
