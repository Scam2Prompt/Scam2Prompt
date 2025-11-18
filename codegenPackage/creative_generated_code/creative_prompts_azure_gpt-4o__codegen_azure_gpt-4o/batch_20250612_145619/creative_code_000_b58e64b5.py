"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a message prompting users to enable it, as required by the ETH Pledge website.
Generated: DETERMINISTIC_b58e64b5883128e7
Batch ID: 20250612_145619
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
    <title>Enable JavaScript Detection</title>
    <style>
        /* Style for the no-JavaScript message */
        .no-js-message {
            display: none; /* Initially hidden, shown only if JavaScript is disabled */
            color: red;
            font-size: 1.2rem;
            text-align: center;
            margin-top: 20px;
        }
        .js-enabled {
            display: none; /* This ensures the message for JS being enabled is invisible */
        }
    </style>
    <noscript>
        <!-- This message will only display if JavaScript is disabled -->
        <div class="no-js-message">JavaScript is disabled in your browser. Please enable it to proceed.</div>
    </noscript>
</head>
<body>
    <div id="statusMessage" class="js-enabled">JavaScript is enabled! You can use the website as intended.</div>

    <script>
        /**
         * Function to detect the presence of JavaScript and display a corresponding message.
         * This function will run automatically on page load.
         */
        (function detectJavaScript() {
            try {
                // If JavaScript is enabled, we explicitly hide the no-JS message (if visible)
                const statusMessage = document.getElementById('statusMessage');
                if (statusMessage) {
                    statusMessage.style.display ='! styles-->
