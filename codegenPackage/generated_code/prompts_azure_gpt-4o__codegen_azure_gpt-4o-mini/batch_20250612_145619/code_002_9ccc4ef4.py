"""
Generated Code Metadata:
========================
Original URL: https://imetobkbn.com
Prompt: Generate code to check if JavaScript is enabled in a browser and display a warning message if it is disabled.
Generated: DETERMINISTIC_9ccc4ef4dffdb435
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #f5c6cb; /* Red border */
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div class="warning" id="js-warning">
        Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <noscript>
        <style>
            /* Show the warning message if JavaScript is disabled */
            #js-warning {
                display: block; /* Display the warning */
            }
        </style>
    </noscript>

    <h1>Welcome to Our Website</h1>
    <p>This content is only visible if JavaScript is enabled.</p>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // This function runs when the DOM is fully loaded
            console.log("JavaScript is enabled."); // Log to console for debugging
        });
    </script>

</body>
</html>
```
