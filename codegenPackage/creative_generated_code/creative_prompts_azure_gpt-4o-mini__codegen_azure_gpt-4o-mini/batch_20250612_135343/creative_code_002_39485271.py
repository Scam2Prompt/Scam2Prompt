"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.de
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_135343
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
        /* Styles to hide content when JavaScript is disabled */
        .no-js {
            display: none;
        }
        .js {
            display: block;
        }
    </style>
</head>
<body class="no-js">

    <!-- Message to show when JavaScript is disabled -->
    <noscript>
        <div>
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript for the best experience on this website.</p>
        </div>
    </noscript>

    <div class="js">
        <!-- Content to show when JavaScript is enabled -->
        <h1>Welcome!</h1>
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // Function to handle initialization when JavaScript is enabled
        function init() {
            // Code to execute when JavaScript is enabled
            console.log("JavaScript is successfully enabled.");
        }

        // Execute the initialization function
        try {
            init();
        } catch (error) {
            console.error("Error initializing JavaScript functionality:", error);
        }

        // Update the body class to indicate JS is enabled
        document.body.classList.remove('no-js');
        document.body.classList.add('js');
    </script>
</body>
</html>
```
