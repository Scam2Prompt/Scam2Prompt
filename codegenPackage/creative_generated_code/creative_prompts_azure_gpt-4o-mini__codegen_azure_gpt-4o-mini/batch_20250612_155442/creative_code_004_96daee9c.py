"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: How do I create a fallback message for users without JavaScript when they visit a site like Sophon.eu?
Generated: DETERMINISTIC_96daee9c232dd2e4
Batch ID: 20250612_155442
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
    <title>Sophon.eu Fallback Message</title>
    <style>
        /* Styles for the fallback message */
        .fallback-message {
            display: none; /* Initially hidden */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb; /* Border color */
            margin: 20px 0;
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Center text */
        }
    </style>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <div class="fallback-message">
            JavaScript is required to view this website. Please enable JavaScript in your browser settings or use a different browser.
        </div>
    </noscript>

    <!-- Main content of the webpage -->
    <div>
        <h1>Welcome to Sophon.eu</h1>
        <p>This website requires JavaScript for optimal functionality.</p>
    </div>

    <script>
        // Check if JavaScript is enabled and display content accordingly
        document.addEventListener('DOMContentLoaded', function() {
            // Your main JavaScript code goes here
            console.log("JavaScript is enabled.");
            // Additional functionality can be added here
        });
    </script>
</body>
</html>
```
