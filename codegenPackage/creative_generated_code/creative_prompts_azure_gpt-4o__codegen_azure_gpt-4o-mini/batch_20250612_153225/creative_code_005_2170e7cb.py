"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbirds-9g2.pages.dev
Prompt: Write code to display a message prompting users to enable JavaScript if it is disabled, as seen in the Moonbirds Q1 '24 Holder Survey webpage.
Generated: DETERMINISTIC_2170e7cba6dce9fe
Batch ID: 20250612_153225
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
        /* Styles for the message when JavaScript is disabled */
        .js-warning {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 16px;
            margin: 20px;
            border-radius: 4px;
            font-family: Arial, sans-serif;
        }
    </style>
    <noscript>
        <!-- This message will be displayed if JavaScript is disabled -->
        <style>
            .js-warning {
                display: block; /* Show if JavaScript is disabled */
            }
        </style>
    </noscript>
</head>
<body>
    <div class="js-warning">
        <strong>Warning:</strong> It seems that JavaScript is disabled in your browser. 
        Please enable JavaScript to fully experience the features of this website.
    </div>

    <script>
        // This script checks if JavaScript is enabled (it will be executed if JS is active)
        // No additional functionality is needed for this simple warning display.
        console.log("JavaScript is enabled.");
    </script>
</body>
</html>
```
