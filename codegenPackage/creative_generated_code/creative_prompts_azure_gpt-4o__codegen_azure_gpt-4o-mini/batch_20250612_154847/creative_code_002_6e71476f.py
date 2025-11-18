"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wt.bridgeinvestmarket.com
Prompt: Develop a JavaScript function to check if JavaScript is enabled in the user's browser and display a message like "You need to enable JavaScript to run this app," as seen on the Web Trader site.
Generated: DETERMINISTIC_6e71476f28728847
Batch ID: 20250612_154847
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
        /* Styles for the message container */
        #js-warning {
            display: none; /* Hide the warning by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JavaScript disabled -->
    <div id="js-warning">
        You need to enable JavaScript to run this app.
    </div>

    <script>
        // Function to display a warning message if JavaScript is disabled
        function checkJavaScriptEnabled() {
            try {
                // Display the warning message container
                document.getElementById('js-warning').style.display = 'block';
            } catch (error) {
                console.error('Error displaying JavaScript warning:', error);
                // Fallback action in case of an error
                alert('An error occurred while checking JavaScript status.');
            }
        }

        // Call the function to check for JavaScript
        checkJavaScriptEnabled();
    </script>
</body>
</html>
```
