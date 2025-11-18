"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Write a script using JavaScript to display a custom error message when a web application fails to load due to JavaScript being disabled, as seen on the Coinbase domain details page.
Generated: DETERMINISTIC_9cc94cdc420e6054
Batch ID: 20250612_150211
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the error message */
        .error-message {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 20px; /* Some padding */
            text-align: center; /* Centered text */
            position: fixed; /* Fixed position */
            top: 0; /* At the top */
            left: 0; /* Align left */
            right: 0; /* Align right */
            z-index: 1000; /* High z-index to appear above other elements */
        }
    </style>
</head>
<body>

    <div id="error-message" class="error-message">
        JavaScript is disabled in your browser. Please enable JavaScript to use this application.
    </div>

    <script>
        // Check if JavaScript is enabled
        (function() {
            // Function to display the error message
            function displayError() {
                const errorMessage = document.getElementById('error-message');
                if (errorMessage) {
                    errorMessage.style.display = 'block'; // Show the error message
                }
            }

            // Simulate application initialization
            try {
                // Perform any application startup logic here
                console.log("Application is loading...");

                // If JavaScript is enabled, we can safely proceed
                // Any further code can be added here
            } catch (error) {
                // Log the error (for debugging purposes)
                console.error("An error occurred during application initialization:", error);
                displayError(); // Display the error message
            }
        })();
    </script>

    <!-- Fallback content for browsers with JS disabled -->
    <noscript>
        <style>
            /* Style for fallback content */
            #error-message {
                display: block; /* Show the warning message */
            }
        </style>
        <div id="error-message" class="error-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this application.
        </div>
    </noscript>

</body>
</html>
```
