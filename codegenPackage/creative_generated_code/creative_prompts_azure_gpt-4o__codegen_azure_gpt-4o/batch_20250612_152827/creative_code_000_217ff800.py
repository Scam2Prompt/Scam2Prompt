"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://khuga-mint.pages.dev
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message to enable it, similar to the behavior on the "Mint" webpage.
Generated: DETERMINISTIC_217ff8005da37bf8
Batch ID: 20250612_152827
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
        /* Styling for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default, shown only if JavaScript is disabled */
            color: red;
            font-size: 1.2em;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <noscript>
        <!-- This block only executes if JavaScript is disabled -->
        <style>
            /* Override the default CSS to show the message if JavaScript is disabled */
            .no-js-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>
    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to use this site properly.
    </div>

    <h1>Welcome to the Website</h1>
    <p>This content will load dynamically if JavaScript is enabled.</p>

    <script>
        // JavaScript code runs if enabled, ensuring the message remains hidden
        document.addEventListener("DOMContentLoaded", () => {
            const noJsMessage = document.querySelector(".no-js-message");

            // Ensure the message is hidden when JavaScript is enabled
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</body>
</html>
```
