"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseindexfund.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_162106
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
        /* Style to hide the message for users with JavaScript enabled */
        .no-js {
            display: none;
        }
    </style>
    <noscript>
        <!-- Message for users with JavaScript disabled -->
        <style>
            .js {
                display: none;
            }
        </style>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience on this website.</p>
        </div>
    </noscript>
</head>
<body>
    <div class="js">
        <h1>Welcome to Our Web Application</h1>
        <p>JavaScript is enabled in your browser!</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        try {
            // This code runs only if JavaScript is enabled
            console.log("JavaScript is enabled.");
        } catch (error) {
            console.error("An error occurred while checking JavaScript status:", error);
        }
    </script>
</body>
</html>
```
