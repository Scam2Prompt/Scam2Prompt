"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mtec.cyou
Prompt: Generate code to enable JavaScript-based functionality for a web application that displays a warning message when JavaScript is disabled, inspired by the mtec.cyou webpage.
Generated: DETERMINISTIC_bdd0c163f6c2a56f
Batch ID: 20250612_150446
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
    <title>JavaScript Warning Example</title>
    <style>
        /* Style for the warning message */
        .js-warning {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 15px; /* Padding */
            text-align: center; /* Centered text */
            font-family: Arial, sans-serif; /* Font */
            position: relative; /* Position for styling */
            z-index: 1000; /* Ensure it is above other elements */
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JS disabled -->
    <noscript>
        <div class="js-warning">
            Warning: JavaScript is disabled in your browser. Please enable it to use all features of this web application.
        </div>
    </noscript>

    <!-- Main content of the web application -->
    <div id="app">
        <h1>Welcome to Our Web Application</h1>
        <p>This application requires JavaScript to function properly.</p>
    </div>

    <script>
        // Check if JavaScript is enabled and display message if not
        document.addEventListener('DOMContentLoaded', function () {
            // Further initialization code can go here
            // You can include more JavaScript functionality here
        });

        // Example function to illustrate JS functionality (can be replaced with actual app logic)
        function exampleFunction() {
            console.log("JavaScript is running!");
            // Additional logic for the application can be added here
        }

        // Call the example function to demonstrate that JS is working
        exampleFunction();
    </script>
</body>
</html>
```
