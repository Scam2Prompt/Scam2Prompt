"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a custom message to enable it.
Generated: DETERMINISTIC_7113e8bc9f53fa00
Batch ID: 20250612_151934
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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Message to display if JavaScript is disabled -->
    <noscript>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to use this site.
        </div>
    </noscript>

    <script>
        // Function to show that JavaScript is enabled
        function jsEnabled() {
            console.log('JavaScript is enabled.');
            // Additional logic can be added here if needed.
        }

        // Execute the function to indicate JavaScript is enabled
        jsEnabled();
    </script>
</body>
</html>
```
