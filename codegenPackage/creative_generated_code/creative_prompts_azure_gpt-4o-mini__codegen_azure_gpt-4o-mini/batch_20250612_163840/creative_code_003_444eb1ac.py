"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Provide a code snippet to display a message prompting users to enable JavaScript when visiting imseoa.com on mobile.
Generated: DETERMINISTIC_444eb1ac0c204144
Batch ID: 20250612_163840
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
    <title>Enable JavaScript</title>
    <style>
        /* Basic styling for the message container */
        #js-warning {
            display: none; /* Hidden by default */
            text-align: center;
            padding: 20px;
            background-color: #ffcc00;
            color: #333;
            border: 1px solid #ffa500;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Message prompting users to enable JavaScript -->
    <div id="js-warning">
        <strong>JavaScript is disabled in your browser.</strong><br>
        Please enable JavaScript to improve your experience on our site.
    </div>

    <script>
        // Function to show the warning message if JavaScript is enabled
        function showWarning() {
            var warning = document.getElementById('js-warning');
            // Check if the user's device is mobile
            var isMobile = /Mobi|Android/i.test(navigator.userAgent);
            if (isMobile) {
                warning.style.display = 'block'; // Show warning on mobile devices
            }
        }

        // Execute the function to check for JavaScript and display warning
        showWarning();
    </script>
    
</body>
</html>
```
