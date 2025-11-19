"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: Provide a code example that detects JavaScript support in browsers and displays a message if it's disabled.
Generated: DETERMINISTIC_774d632d75b6a6d4
Batch ID: 20250612_160158
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
    <title>JavaScript Support Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red; /* Color of the message */
            font-weight: bold; /* Bold text */
        }
    </style>
</head>
<body>

    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it for the full experience.
        </div>
    </noscript>

    <script>
        // Function to display a message indicating JavaScript is enabled
        function showJavaScriptEnabledMessage() {
            console.log("JavaScript is enabled in your browser.");
        }

        // Check if JavaScript is supported and enabled
        if (typeof window === "object") {
            // Execute this block if JavaScript is enabled
            showJavaScriptEnabledMessage();
        } else {
            // Fallback for browsers that do not support JavaScript (though this is rare)
            console.error("JavaScript support is not detected.");
        }
    </script>

</body>
</html>
```
