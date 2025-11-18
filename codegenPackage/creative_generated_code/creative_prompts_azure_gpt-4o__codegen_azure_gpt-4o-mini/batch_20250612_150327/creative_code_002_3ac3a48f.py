"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdop.tech
Prompt: Create a basic HTML and JavaScript setup for an app that checks for JavaScript availability and redirects users to an error page if JavaScript is disabled.
Generated: DETERMINISTIC_3ac3a48fda31400a
Batch ID: 20250612_150327
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
    <title>JavaScript Availability Check</title>
    <style>
        /* Basic styles for the error page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        h1 {
            color: red;
        }
    </style>
    <noscript>
        <!-- Fallback content for users with JavaScript disabled -->
        <style>
            /* Display error message when JavaScript is disabled */
            .no-js-error {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-error" style="display:none;">
        <h1>Error: JavaScript is Disabled</h1>
        <p>Please enable JavaScript in your browser to use this application.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // If JavaScript is enabled, hide the error message
            const errorDiv = document.querySelector('.no-js-error');
            if (errorDiv) {
                errorDiv.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```
