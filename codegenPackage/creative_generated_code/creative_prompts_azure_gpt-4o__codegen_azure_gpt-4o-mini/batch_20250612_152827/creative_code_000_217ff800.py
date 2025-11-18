"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khuga-mint.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message to enable it, similar to the behavior on the "Mint" webpage.
Generated: DETERMINISTIC_217ff8005da37bf8
Batch ID: 20250612_152827
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Initially hidden */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to display when JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it to view this content.
    </div>

    <script>
        // JavaScript code to enable the main content of the page
        document.addEventListener("DOMContentLoaded", function() {
            // Hide the no-JS message when JavaScript is enabled
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none';
            
            // Main content of the page can go here
            const mainContent = document.createElement('div');
            mainContent.innerHTML = '<h1>Welcome to Our Website</h1><p>JavaScript is enabled!</p>';
            document.body.appendChild(mainContent);
        });
    </script>
</body>
</html>
```
