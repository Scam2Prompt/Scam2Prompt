"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dueleth.com
Prompt: Generate a code example for detecting whether JavaScript is enabled on a webpage, as seen in the Duel ETH website.
Generated: DETERMINISTIC_de649fec67e757c9
Batch ID: 20250612_151659
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
        /* Default style when JavaScript is disabled */
        .js-disabled {
            display: block;
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 20px;
        }

        /* Hide this message when JavaScript is enabled */
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message displayed if JavaScript is disabled -->
    <div class="js-disabled">
        JavaScript is disabled. Please enable it for the best experience.
    </div>

    <!-- Content loaded when JavaScript is enabled -->
    <div class="js-enabled">
        Welcome! JavaScript is enabled on your browser.
    </div>

    <script>
        // JavaScript block to detect if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            try {
                // Hide the "JavaScript Disabled" message
                const jsDisabledElement = document.querySelector(".js-disabled");
                if (jsDisabledElement) {
                    jsDisabledElement.style.display = "none";
                }

                // Show the "JavaScript Enabled" content
                const jsEnabledElement = document.querySelector(".js-enabled");
                if (jsEnabledElement) {
                    jsEnabledElement.style.display = "block";
                }
            } catch (error) {
                // Log any potential errors in the console
                console.error("Error detecting JavaScript state:", error);
            }
        });
    </script>
</body>
</html>
```
