"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseindexfund.com
Prompt: How do I create a fallback message for users without JavaScript when accessing the Coinbase Index Fund site?
Generated: DETERMINISTIC_99ef109c5f3e1dbb
Batch ID: 20250612_162106
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
    <title>Coinbase Index Fund</title>
    <style>
        /* Style for fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px; /* Padding around the message */
            border: 1px solid #f5c6cb; /* Red border */
            margin: 20px; /* Margin around the message */
            border-radius: 5px; /* Rounded corners */
        }
        /* Style to show the message when JavaScript is disabled */
        .no-js .fallback-message {
            display: block; /* Show the message */
        }
    </style>
</head>
<body class="no-js"> <!-- Class added to indicate JS is disabled -->

    <!-- Fallback message for users without JavaScript -->
    <div class="fallback-message">
        <strong>Alert:</strong> This site requires JavaScript to function properly. Please enable JavaScript in your browser settings or use a browser that supports JavaScript.
    </div>

    <!-- Main content of the site -->
    <div id="content">
        <h1>Welcome to Coinbase Index Fund</h1>
        <p>Your gateway to investing in cryptocurrency funds.</p>
    </div>

    <script>
        // Check if JavaScript is enabled by removing the 'no-js' class
        document.body.classList.remove('no-js');
    </script>
</body>
</html>
```
