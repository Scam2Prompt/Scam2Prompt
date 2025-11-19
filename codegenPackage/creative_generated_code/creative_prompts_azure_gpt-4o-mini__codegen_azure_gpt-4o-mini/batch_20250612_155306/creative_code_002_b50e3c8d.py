"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lrt-sym.biotic.fi
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application context similar to LRT-SYM?
Generated: DETERMINISTIC_b50e3c8d8c0acfbf
Batch ID: 20250612_155306
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Style to hide the message when JavaScript is enabled */
        .no-js {
            display: block;
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }

        /* Style to show the message when JavaScript is enabled */
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message to display when JavaScript is disabled -->
    <div class="no-js">
        JavaScript is disabled in your browser. Please enable it for a better experience.
    </div>

    <!-- Message to display when JavaScript is enabled -->
    <div class="js">
        JavaScript is enabled. Enjoy your experience!
    </div>

    <script>
        // Check if JavaScript is enabled by altering the DOM
        document.querySelector('.no-js').style.display = 'none'; // Hide message for no JS
        document.querySelector('.js').style.display = 'block'; // Show message for JS enabled

        // Error handling for DOM manipulation
        try {
            // Log success message for debugging purposes
            console.log("JavaScript is functioning correctly.");
        } catch (error) {
            console.error("An error occurred while checking JavaScript:", error);
        }
    </script>
</body>
</html>
```
