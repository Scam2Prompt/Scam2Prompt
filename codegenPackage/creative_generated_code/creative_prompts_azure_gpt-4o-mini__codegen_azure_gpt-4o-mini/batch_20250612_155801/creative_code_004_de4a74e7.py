"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexmkb.com
Prompt: How do I create a fallback message for users without JavaScript enabled on my site?
Generated: DETERMINISTIC_de4a74e75a2f1eee
Batch ID: 20250612_155801
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
    <title>Fallback Message Example</title>
    <style>
        /* Style for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
    <script>
        // Function to show the main content when JavaScript is enabled
        function showMainContent() {
            document.getElementById('main-content').style.display = 'block';
        }

        // Function to hide the fallback message when JavaScript is enabled
        function hideFallbackMessage() {
            document.getElementById('fallback').style.display = 'none';
        }

        // Run functions on page load
        window.onload = function() {
            showMainContent();
            hideFallbackMessage();
        };
    </script>
</head>
<body>
    <div id="fallback" class="fallback-message">
        <strong>Note:</strong> It seems you have JavaScript disabled in your browser. 
        Please enable JavaScript to fully experience this site.
    </div>

    <div id="main-content" style="display: none;">
        <h1>Welcome to My Site</h1>
        <p>This content is only visible when JavaScript is enabled.</p>
    </div>
</body>
</html>
```
