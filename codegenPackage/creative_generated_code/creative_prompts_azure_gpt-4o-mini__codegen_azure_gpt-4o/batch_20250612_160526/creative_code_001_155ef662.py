"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogebox.link
Prompt: Write a code snippet that demonstrates how to enable JavaScript for a web application that requires it for operation, similar to Dogebox.
Generated: DETERMINISTIC_155ef66217ac70c5
Batch ID: 20250612_160526
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
    <title>JavaScript Check</title>
    <style>
        /* Styles to hide JavaScript-dependent content initially */
        .js-enabled-content {
            display: none;
        }

        /* If JavaScript is enabled, show the content */
        .js-enabled .js-enabled-content {
            display: block;
        }

        /* Fallback message styles */
        .no-js-message {
            color: red;
            font-weight: bold;
        }
    </style>
    <script>
        // Add a "js-enabled" class to the <html> element if JavaScript is enabled
        document.documentElement.className += ' js-enabled';
    </script>
</head>

<body>
    <!-- Fallback message for users without JavaScript -->
    <noscript>
        <p class="no-js-message">
            JavaScript is required to use this application. Please enable it in your browser settings.
        </p>
    </noscript>

    <!-- Content that requires JavaScript to function -->
    <div class="js-enabled-content">
        <h1>Welcome to the Application!</h1>
        <p>JavaScript is enabled, and everything is working correctly.</p>
        <button onclick="alert('JavaScript is working!')">Click Me</button>
    </div>
</body>

</html>
```
