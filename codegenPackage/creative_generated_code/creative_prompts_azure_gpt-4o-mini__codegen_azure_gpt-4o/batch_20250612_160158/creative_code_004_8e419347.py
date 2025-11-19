"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodep0.com
Prompt: How can I implement a fallback message for users who have JavaScript disabled on mobile sites?
Generated: DETERMINISTIC_8e4193476a49e160
Batch ID: 20250612_160158
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
    <title>JavaScript Disabled Fallback</title>
    <style>
        /* Styling the fallback message */
        #no-js-message {
            display: none; /* Default to hidden, will be shown if JS is disabled */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            text-align: center;
            font-family: Arial, sans-serif;
            margin: 20px;
        }
    </style>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <div id="no-js-message">
        Please enable JavaScript on your browser for the best experience on this site.
    </div>

    <!-- Main content -->
    <div id="content">
        <p>Welcome to our website! Enjoy browsing.</p>
    </div>

    <!-- JavaScript -->
    <script>
        // Hide the fallback message as JS is enabled
        document.getElementById('no-js-message').style.display = 'none';
    </script>

    <!-- If JavaScript is disabled, the fallback will be shown -->
    <noscript>
        <style>
            /* Overriding CSS to display the fallback when JS is disabled */
            #no-js-message {
                display: block;
            }
            #content {
                display: none; /* Optionally hide main content */
            }
        </style>
    </noscript>
</body>
</html>
```
