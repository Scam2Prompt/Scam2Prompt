"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethupea.com
Prompt: Generate code to detect if JavaScript is disabled in a browser and display a message prompting users to enable it for Ethereum pledge functionality.
Generated: DETERMINISTIC_9baa1baa95bf5ed6
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
    <title>Enable JavaScript</title>
    <style>
        /* Basic styling for the message */
        #js-disabled-message {
            display: none; /* Initially hide the message */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="content">
        <!-- Main content of the page goes here -->
        <h1>Welcome to the Ethereum Pledge</h1>
        <p>Please enable JavaScript to use the pledge functionality.</p>
    </div>

    <div id="js-disabled-message">
        <strong>JavaScript is disabled!</strong> Please enable JavaScript in your browser settings to use the Ethereum pledge functionality.
    </div>

    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            #js-disabled-message {
                display: block;
            }
        </style>
    </noscript>

    <script>
        // Check for JavaScript support
        if (typeof window === "undefined" || typeof document === "undefined") {
            // Fallback if window or document is undefined (extreme case)
            console.error("JavaScript is not supported on this browser.");
        } else {
            // JavaScript is enabled; hide the warning message if shown
            const message = document.getElementById('js-disabled-message');
            message.style.display = 'none';
        }
    </script>

</body>
</html>
```
