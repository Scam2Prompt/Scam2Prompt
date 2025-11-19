"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: Generate a script that checks if JavaScript is enabled in a user's browser before loading content.
Generated: DETERMINISTIC_c59ccfd9acd71562
Batch ID: 20250612_163231
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
        /* CSS to hide the content container by default */
        #content {
            display: none;
        }

        /* Message displayed when JavaScript is disabled */
        #js-disabled {
            color: red;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>

<body>
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable JavaScript to view this content.</div>
    </noscript>

    <!-- Content container that will be shown only if JavaScript is enabled -->
    <div id="content">
        <h1>Welcome!</h1>
        <p>You are viewing this content because JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // JavaScript block to handle visibility of content
        try {
            // If JavaScript is enabled, show the content container
            const content = document.getElementById("content");
            if (content) {
                content.style.display = "block";
            }
        } catch (error) {
            // Log any unexpected errors to the console
            console.error("An error occurred while checking for JavaScript:", error);
        }
    </script>
</body>

</html>
```
