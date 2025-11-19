"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.global-connect.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage like debridge.global-connect.eu?
Generated: DETERMINISTIC_0eb494401a8a887a
Batch ID: 20250612_155248
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
        /* Style for the no-JS message */
        .no-js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
        </div>
    </noscript>

    <div id="content">
        <h1>Welcome to Global Connect</h1>
        <p>This content is visible only if JavaScript is enabled.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Hide the no-JS message by removing the 'no-js' class
            const noJsMessage = document.querySelector('.no-js');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }

            // Optional: You can also display a message indicating JS is active
            const content = document.getElementById('content');
            const jsEnabledMessage = document.createElement('p');
            jsEnabledMessage.textContent = 'JavaScript is enabled!';
            content.appendChild(jsEnabledMessage);
        });

        // Error handling for any potential script errors
        window.onerror = function(message, source, lineno, colno, error) {
            console.error('Error occurred: ', message, 'at', source, 'line:', lineno, 'column:', colno);
            // Optionally, you could handle the error further, e.g., send to logging service
        };
    </script>
</body>
</html>
```
