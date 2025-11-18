"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monada.online
Prompt: Create a script that checks for JavaScript support and redirects users to a fallback page if JavaScript is not enabled.
Generated: DETERMINISTIC_c7730c5780e0be06
Batch ID: 20250612_154115
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
    <title>JavaScript Support Check</title>

    <style>
        /* Message to display when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hide by default */
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">
            <h1>JavaScript is Disabled</h1>
            <p>This website requires JavaScript to function properly. Please enable JavaScript or use a browser that supports it.</p>
            <a href="fallback.html">Go to fallback page</a>
        </div>
    </noscript>

    <script>
        // Check if JavaScript is enabled
        try {
            // If JavaScript is enabled, redirect to the main page or perform other actions
            console.log("JavaScript is enabled."); // For debugging purposes
            // Uncomment the next line to redirect if necessary
            // window.location.href = "main.html";
        } catch (error) {
            // Handle any unexpected errors
            console.error("An error occurred while checking JavaScript support:", error);
            // Optionally redirect to a fallback page
            window.location.href = "fallback.html";
        }
    </script>
</body>
</html>
```
