"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.fi
Prompt: How can I implement a fallback message for users without JavaScript on a site like Polkadot?
Generated: DETERMINISTIC_3f0d46ef8dbcc9b6
Batch ID: 20250612_162605
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
    <title>Polkadot Example</title>
    <style>
        /* Style for the 'no-JavaScript' fallback message */
        .no-js-message {
            display: none; /* Default hidden when JS is enabled */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 10px 0;
        }
        .js-enabled .no-js-message {
            display: none; /* Ensure fallback stays hidden when JS is enabled */
        }
    </style>
</head>
<body>

    <!-- Fallback message for users without JavaScript -->
    <div class="no-js-message">
        This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>

    <!-- Main content -->
    <div id="app">
        <h1>Welcome to Polkadot</h1>
        <p>This content requires JavaScript to be displayed correctly.</p>
    </div>

    <script>
        // Add a class to the body when JavaScript is enabled
        document.documentElement.classList.add('js-enabled');
    </script>
</body>
</html>
```
