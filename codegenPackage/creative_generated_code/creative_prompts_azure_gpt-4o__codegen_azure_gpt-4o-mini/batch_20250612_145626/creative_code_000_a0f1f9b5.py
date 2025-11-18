"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://login.futurx.live
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message instructing users to enable it, similar to the behavior of the FuturX login page.
Generated: DETERMINISTIC_a0f1f9b52feea807
Batch ID: 20250612_145626
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
        /* Styles for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f44336; /* Red background */
            color: white; /* White text */
            padding: 20px; /* Padding */
            text-align: center; /* Center text */
            font-family: Arial, sans-serif; /* Font style */
            position: absolute; /* Positioning */
            top: 0; /* Top alignment */
            left: 0; /* Left alignment */
            right: 0; /* Right alignment */
            z-index: 9999; /* Ensure it overlaps other elements */
        }
    </style>
    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            .no-js-message {
                display: block; /* Show block element */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript in your browser settings to use this website.</p>
    </div>

    <script>
        // Main script - checks if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // This block will only run if JavaScript is enabled
            console.log("JavaScript is enabled."); // Log confirmation
        });
    </script>
</body>
</html>
```
