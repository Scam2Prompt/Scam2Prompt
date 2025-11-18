"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: Write a script to dynamically check and log whether JavaScript is enabled or disabled in a user's browser.
Generated: DETERMINISTIC_c63522aafbfc6a61
Batch ID: 20250612_145455
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
        /* Styles for the message display */
        #js-status {
            font-size: 1.2em;
            margin-top: 20px;
        }
        .enabled {
            color: green;
        }
        .disabled {
            color: red;
        }
    </style>
</head>
<body>
    <noscript>
        <div id="js-status" class="disabled">
            JavaScript is disabled in your browser.
        </div>
    </noscript>
    
    <div id="js-status" class="enabled" style="display: none;">
        JavaScript is enabled in your browser.
    </div>

    <script>
        // Function to log the JavaScript status
        function logJsStatus(isEnabled) {
            const statusElement = document.getElementById('js-status');
            if (isEnabled) {
                statusElement.className = 'enabled';
                statusElement.textContent = 'JavaScript is enabled in your browser.';
                statusElement.style.display = 'block';
            } else {
                statusElement.className = 'disabled';
                statusElement.textContent = 'JavaScript is disabled in your browser.';
                statusElement.style.display = 'block';
            }
            // Logging the status to the console
            console.log(statusElement.textContent);
        }

        // Execute on page load
        window.onload = function() {
            // JavaScript is enabled if this function runs
            logJsStatus(true);
        };

        // Error handling for logging
        window.onerror = function(message, source, lineno, colno, error) {
            console.error(`Error occurred: ${message} at ${source}:${lineno}:${colno}`);
        };
    </script>
</body>
</html>
```
