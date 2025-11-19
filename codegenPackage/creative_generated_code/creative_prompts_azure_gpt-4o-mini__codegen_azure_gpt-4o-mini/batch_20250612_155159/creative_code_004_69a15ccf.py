"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arcium.de
Prompt: How do I create a fallback for users who have JavaScript disabled when accessing web content?
Generated: DETERMINISTIC_69a15ccf04a23528
Batch ID: 20250612_155159
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Basic styles for the fallback content */
        .fallback {
            display: none; /* Hide by default */
            background-color: #f8d7da; 
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
        }
    </style>
    <script>
        // Function to show a message if JavaScript is enabled
        function jsEnabled() {
            const fallbackDiv = document.getElementById('fallback');
            fallbackDiv.style.display = 'none'; // Hide fallback content
        }

        // Execute the jsEnabled function on page load
        window.onload = jsEnabled;
    </script>
</head>
<body>

    <!-- Fallback content for users with JavaScript disabled -->
    <noscript>
        <div class="fallback" id="fallback">
            <strong>Warning:</strong> JavaScript is disabled in your browser. Some features may not work as intended.
        </div>
    </noscript>

    <h1>Welcome to Our Website</h1>
    <p>This is a sample content that requires JavaScript for full functionality.</p>

    <!-- Main content that relies on JavaScript -->
    <div id="main-content">
        <p>JavaScript is enabled, and you can see interactive features here!</p>
        <button onclick="alert('Hello, JavaScript is working!')">Click Me!</button>
    </div>

</body>
</html>
```
