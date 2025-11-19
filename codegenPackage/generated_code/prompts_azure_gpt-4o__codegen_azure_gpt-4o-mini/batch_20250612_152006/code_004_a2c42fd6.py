"""
Generated Code Metadata:
========================
Original URL: https://lrt-sym.biotic.fi
Prompt: Create a script that redirects users to an error page if JavaScript is disabled, inspired by the behavior of the "lrt-sym.biotic.fi" domain details page.
Generated: DETERMINISTIC_a2c42fd61c391db6
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Redirect Example</title>
    <style>
        /* Basic styling for the error message */
        .error-message {
            display: none; /* Hide by default */
            color: red;
            font-size: 20px;
            text-align: center;
            margin-top: 20%;
        }
    </style>
    <script>
        // Function to redirect to the error page
        function redirectToErrorPage() {
            window.location.href = 'error.html'; // Change to your error page URL
        }

        // Execute the redirect function on page load
        window.onload = function() {
            // If JavaScript is enabled, do nothing
            // If JavaScript is disabled, the error message will be shown
        };
    </script>
</head>
<body>
    <div class="error-message" id="error-message">
        <p>JavaScript is disabled in your browser. Please enable it to access this site.</p>
    </div>

    <noscript>
        <style>
            /* Show the error message if JavaScript is disabled */
            #error-message {
                display: block; /* Show the error message */
            }
        </style>
    </noscript>

    <script>
        // If JavaScript is enabled, we can hide the error message
        document.getElementById('error-message').style.display = 'none';
    </script>
</body>
</html>
```
