"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7473441704.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_155842
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
        /* Styles for the message when JavaScript is disabled */
        .no-js {
            display: none;
        }
        .js-enabled {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <style>
            .no-js {
                display: block;
            }
            .js-enabled {
                display: none;
            }
        </style>
        <div class="no-js">
            <h1>JavaScript is Disabled</h1>
            <p>Please enable JavaScript to enhance your browsing experience.</p>
        </div>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js-enabled">
        <h1>JavaScript is Enabled</h1>
        <p>Thank you for enabling JavaScript!</p>
    </div>

    <script>
        // This script runs if JavaScript is enabled
        try {
            console.log("JavaScript is enabled.");

            // Optional: Additional functionality can go here
        } catch (error) {
            console.error("An error occurred while checking JavaScript status:", error);
        }
    </script>
</body>
</html>
```
heck when the document is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
    </script>
</body>
</html>
```
