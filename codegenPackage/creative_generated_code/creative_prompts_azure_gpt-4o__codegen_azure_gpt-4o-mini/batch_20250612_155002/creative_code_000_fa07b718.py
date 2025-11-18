"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proxycare.proxurve.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it for accessing the N-central login page.
Generated: DETERMINISTIC_fa07b7181a135267
Batch ID: 20250612_155002
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
    <title>N-central Login Page</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .js-disabled-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="login-container">
        <!-- Content for the N-central login page goes here -->
        <h1>Welcome to N-central</h1>
        <p>Please log in to continue.</p>
        <!-- More login related content -->
    </div>

    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div class="js-disabled-message">
            JavaScript is disabled in your browser. Please enable it to access the N-central login page.
        </div>
    </noscript>

    <script>
        // JavaScript code to enhance login page functionality can go here
        // For example, form validation, dynamic content loading, etc.
        console.log("JavaScript is enabled."); // Confirmation that JS is running

        // Example function to demonstrate functionality
        function init() {
            // Initialization code for the login page
            // Add event listeners, validate inputs, etc.
        }

        // Call the init function when the document is fully loaded
        document.addEventListener("DOMContentLoaded", init);
    </script>
</body>
</html>
```
