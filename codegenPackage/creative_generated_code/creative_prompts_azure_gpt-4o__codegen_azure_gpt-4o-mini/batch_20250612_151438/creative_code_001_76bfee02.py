"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equinix.online
Prompt: Create a script that redirects users to a custom error page if JavaScript is disabled on their browser.
Generated: DETERMINISTIC_76bfee027ac9eca1
Batch ID: 20250612_151438
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
    <title>Error Page Redirect</title>
    <style>
        /* Style for the fallback content */
        .noscript-message {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Fallback message for users with JavaScript disabled -->
    <div class="noscript-message">
        <h1>JavaScript Disabled</h1>
        <p>Your browser does not support JavaScript or it is disabled. You will be redirected to a custom error page.</p>
    </div>

    <script>
        // JavaScript code to redirect users to a custom error page
        window.onload = function() {
            // Redirect to the custom error page
            window.location.href = 'error.html'; // Change 'error.html' to your custom error page URL
        };
    </script>

    <!-- Show the fallback message if JavaScript is disabled -->
    <noscript>
        <style>
            .noscript-message {
                display: block; /* Show the message if JavaScript is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
