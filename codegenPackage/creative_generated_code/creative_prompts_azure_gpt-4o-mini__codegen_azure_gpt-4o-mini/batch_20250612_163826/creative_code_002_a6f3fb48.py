"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metro-ccc.ru
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a webpage?
Generated: DETERMINISTIC_a6f3fb48fa9e0192
Batch ID: 20250612_163826
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
        /* Style for the no-JavaScript message */
        .no-js {
            display: none; /* Hide by default */
        }
        .js {
            display: block; /* Show if JavaScript is enabled */
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is not enabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
        </div>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js">
        <p>JavaScript is enabled. Welcome!</p>
    </div>

    <script>
        // Ensure the script runs only after the document is fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            try {
                // Here you can add additional JavaScript functionality
                console.log("JavaScript is enabled."); // For debugging purposes
            } catch (error) {
                // Handle any errors that may occur
                console.error("An error occurred while executing JavaScript: ", error);
            }
        });
    </script>
    
</body>
</html>
```
