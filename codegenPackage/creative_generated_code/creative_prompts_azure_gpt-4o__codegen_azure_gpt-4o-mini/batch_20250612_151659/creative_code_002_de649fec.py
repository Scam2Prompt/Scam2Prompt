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
    <title>JavaScript Detection Example</title>
    <style>
        /* Styles for the message display */
        .no-js {
            display: none; /* Hidden by default */
        }
        .js {
            display: block; /* Shown when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <!-- Message for users with JavaScript disabled -->
    <noscript>
        <style>
            .no-js {
                display: block; /* Show this message if JavaScript is disabled */
            }
        </style>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience on this website.</p>
        </div>
    </noscript>

    <!-- Message for users with JavaScript enabled -->
    <div class="js">
        <p>Welcome! JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // This script runs when the page is loaded
        document.addEventListener("DOMContentLoaded", function () {
            try {
                // Log a message to the console for debugging purposes
                console.log("JavaScript is enabled and running.");

                // Additional JavaScript functionality can be added here

            } catch (error) {
                // Log any errors to the console for debugging
                console.error("An error occurred:", error);
            }
        });
    </script>

</body>
</html>
```
