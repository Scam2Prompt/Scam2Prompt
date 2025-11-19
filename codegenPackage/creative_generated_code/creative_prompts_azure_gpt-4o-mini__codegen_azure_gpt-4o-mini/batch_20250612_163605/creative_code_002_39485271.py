"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runonflux.xyz
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_163605
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
        /* Styles to hide the message for users with JavaScript disabled */
        .no-js {
            display: none;
        }
    </style>
    <script>
        // Function to indicate that JavaScript is enabled
        function enableJavaScript() {
            document.body.classList.remove('no-js');
        }

        // Call the function to enable JavaScript on page load
        window.onload = enableJavaScript;
    </script>
</head>
<body class="no-js">
    <noscript>
        <!-- Message for users with JavaScript disabled -->
        <div>
            <strong>JavaScript is disabled in your browser.</strong>
            Please enable JavaScript to improve your experience.
        </div>
    </noscript>
    
    <!-- Main content of the page -->
    <div>
        <h1>Welcome to Our Web Application!</h1>
        <p>If you see this message, JavaScript is enabled.</p>
    </div>
</body>
</html>
```
