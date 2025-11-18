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
    <title>JavaScript Check</title>
    <script>
        // Function to log and display the status of JavaScript
        function logJavaScriptStatus() {
            try {
                // JavaScript is enabled if this script runs
                console.log("JavaScript is enabled in this browser.");
                document.getElementById('js-status').textContent = "JavaScript is ENABLED.";
                document.getElementById('js-status').style.color = "green";
            } catch (error) {
                // This block will not run unless there's an unexpected error
                console.error("An unexpected error occurred:", error);
            }
        }
        // Call the function on page load
        window.onload = logJavaScriptStatus;
    </script>
    <noscript>
        <!-- Fallback for when JavaScript is disabled -->
        <style>
            #js-status {
                color: red;
            }
        </style>
        <p id="js-status">JavaScript is DISABLED.</p>
    </noscript>
</head>
<body>
    <h1>JavaScript Status Checker</h1>
    <p id="js-status"></p>
</body>
</html>
```
