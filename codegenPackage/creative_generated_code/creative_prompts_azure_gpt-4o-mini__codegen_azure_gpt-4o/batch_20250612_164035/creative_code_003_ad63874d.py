"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbtrum.net
Prompt: Generate a script that checks if JavaScript is enabled in a user's browser before allowing access to a web application.
Generated: DETERMINISTIC_ad63874db4d0a20c
Batch ID: 20250612_164035
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
        /* Basic styling for the no-Javascript message */
        .no-js {
            display: none;
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }

        .js-enabled-content {
            display: none;
        }
    </style>
    <script>
        // If JavaScript is enabled, hide the no-JS message and show JS-enabled content
        document.addEventListener('DOMContentLoaded', function () {
            const noJsMessage = document.getElementById('no-js-message');
            const jsContent = document.getElementById('js-enabled-content');

            if (noJsMessage && jsContent) {
                // Hide no-JS message and show JS-enabled content
                noJsMessage.style.display = 'none';
                jsContent.style.display = 'block';
            }
        });
    </script>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <div id="no-js-message" class="no-js">
        JavaScript is disabled in your browser. Please enable JavaScript to access this application.
    </div>

    <!-- Content displayed if JavaScript is enabled -->
    <div id="js-enabled-content" class="js-enabled-content">
        <h1>Welcome to the Web Application</h1>
        <p>JavaScript is enabled in your browser. You may proceed.</p>
    </div>
</body>
</html>
```
