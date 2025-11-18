"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvesters-app.pages.dev
Prompt: Generate code to display a custom error message when JavaScript is disabled in a web app like Harvest App.
Generated: DETERMINISTIC_034b7a6ebe4b7381
Batch ID: 20250612_150226
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
    <title>Custom Error Message for Disabled JavaScript</title>
    <style>
        /* Styles for the error message */
        .no-js-message {
            display: none; /* Hide the error message by default */
            background-color: #ffdddd; /* Light red background */
            color: #d8000c; /* Dark red text */
            padding: 20px; /* Padding for the message */
            border: 1px solid #d8000c; /* Border around the message */
            border-radius: 5px; /* Rounded corners */
            margin: 20px; /* Margin around the message */
            font-family: Arial, sans-serif; /* Font style */
        }
    </style>
    <noscript>
        <!-- Display this message if JavaScript is disabled -->
        <style>
            .no-js-message {
                display: block; /* Show the message when JavaScript is not available */
            }
        </style>
    </noscript>
</head>
<body>
    <!-- Custom error message for users with JavaScript disabled -->
    <div class="no-js-message">
        <strong>Error:</strong> It seems that JavaScript is disabled in your browser. 
        This web application requires JavaScript to function properly. 
        Please enable JavaScript or switch to a browser that supports it.
    </div>

    <!-- Main content of the web app goes here -->
    <div id="app">
        <h1>Welcome to the Harvest App</h1>
        <p>Your main application content will be loaded here.</p>
        <!-- Add JavaScript functionality here -->
    </div>

    <script>
        // Example JavaScript functionality
        document.addEventListener("DOMContentLoaded", function() {
            // Log a message to the console when the DOM is fully loaded
            console.log("The Harvest App is fully loaded and JavaScript is enabled.");
            // Further app initialization can go here
        });
    </script>
</body>
</html>
```
