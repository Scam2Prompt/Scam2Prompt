"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethphbi.com
Prompt: Can you provide code snippets for checking if JavaScript is enabled in a mobile browser?
Generated: DETERMINISTIC_39c6350887aae600
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
    <title>JavaScript Check</title>
    <style>
        /* Message for users with JavaScript disabled */
        .no-js-message {
            display: none;
            color: red;
            text-align: center;
            font-size: 1.2em;
        }
    </style>
</head>

<body>
    <noscript>
        <!-- This message will only be shown if JavaScript is disabled -->
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to view this page correctly.
        </div>
    </noscript>

    <!-- Content displayed only if JavaScript is enabled -->
    <div id="js-enabled-content" style="display: none; text-align: center;">
        JavaScript is enabled in your browser! Enjoy the website.
    </div>

    <script>
        // Ensure this script runs only if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            try {
                // Show content for users with JavaScript enabled
                const jsEnabledContent = document.getElementById("js-enabled-content");
                if (jsEnabledContent) {
                    jsEnabledContent.style.display = "block";
                }
            } catch (error) {
                // Log any unexpected errors
                console.error("An error occurred while checking JavaScript status:", error);
            }
        });
    </script>
</body>

</html>
```
