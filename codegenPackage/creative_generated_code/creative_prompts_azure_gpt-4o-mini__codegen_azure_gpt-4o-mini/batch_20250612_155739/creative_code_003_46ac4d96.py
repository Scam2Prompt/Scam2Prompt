"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maxlbank.com
Prompt: Provide a code snippet to detect if JavaScript is enabled and display a message if it's not, similar to the MaxL Bank warning.
Generated: DETERMINISTIC_46ac4d9693544690
Batch ID: 20250612_155739
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
        #noscript-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
        }
    </style>
</head>
<body>

    <!-- Message to display if JavaScript is disabled -->
    <div id="noscript-message">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for a better experience on this site.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoScriptMessage() {
            const messageDiv = document.getElementById('noscript-message');
            messageDiv.style.display = 'block'; // Display the message
        }

        // Execute the function to show the message
        showNoScriptMessage();
    </script>

    <noscript>
        <!-- Alternative content for browsers with JavaScript disabled -->
        <style>
            #noscript-message {
                display: block; /* Show message if JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
