"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-five.vercel.app
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like Linea?
Generated: DETERMINISTIC_240c6526a807c2d2
Batch ID: 20250612_161441
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
        /* Style to hide the content if JavaScript is disabled */
        .no-js {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Message shown when JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript to use this web application.</p>
        </div>
    </noscript>

    <!-- Content that requires JavaScript -->
    <div id="js-enabled" style="display: none;">
        <h1>Welcome to the Application!</h1>
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            try {
                // Show content if JavaScript is enabled
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                console.error('Error displaying content:', error);
                // Handle error (alternative actions can be taken here)
            }
        }

        // Run the function to check for JavaScript
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
