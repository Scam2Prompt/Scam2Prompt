"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stargate.fi
Prompt: How do I create a JavaScript function that alerts users to enable JavaScript for a specific webpage?
Generated: DETERMINISTIC_38a6c2c8b6765a33
Batch ID: 20250612_135637
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
    <title>Enable JavaScript Alert</title>
    <style>
        /* Style to hide the content when JavaScript is disabled */
        .js-enabled {
            display: none;
        }
    </style>
    <script>
        // Function to alert users to enable JavaScript
        function alertEnableJavaScript() {
            alert("Please enable JavaScript to view this page properly.");
        }

        // Immediately invoke the function to check JavaScript support
        alertEnableJavaScript();
    </script>
</head>
<body>
    <!-- Content that will be shown when JavaScript is enabled -->
    <div class="js-enabled" id="content">
        <h1>Welcome to Our Website!</h1>
        <p>Your browser supports JavaScript.</p>
    </div>

    <noscript>
        <!-- This block will be displayed if JavaScript is disabled -->
        <div>
            <h2>JavaScript Disabled</h2>
            <p>It appears that JavaScript is disabled in your browser. Please enable it to access all features of this site.</p>
        </div>
    </noscript>

    <script>
        // Show the content if JavaScript is enabled
        document.getElementById('content').classList.remove('js-enabled');
    </script>
</body>
</html>
```
