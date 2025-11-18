"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.dexodoor.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_97abd30422102dc4
Batch ID: 20250612_152441
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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Style for the warning message */
        .js-warning {
            display: none; /* Default hidden when JavaScript is enabled */
            background-color: #ffcccc;
            color: #d8000c;
            padding: 15px;
            border: 1px solid #d8000c;
            border-radius: 5px;
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Warning message to be displayed if JavaScript is disabled -->
    <noscript>
        <div class="js-warning">
            JavaScript is disabled in your browser. Please enable JavaScript to use this page properly.
        </div>
    </noscript>

    <!-- Content of the page -->
    <div>
        <h1>Welcome to the Page!</h1>
        <p>If JavaScript is enabled, you'll see this content without any warnings.</p>
    </div>

    <script>
        // JavaScript enabled content does not require any specific warning display
        // The <noscript> tag inherently handles cases where JS is disabled
    </script>
</body>
</html>
```
