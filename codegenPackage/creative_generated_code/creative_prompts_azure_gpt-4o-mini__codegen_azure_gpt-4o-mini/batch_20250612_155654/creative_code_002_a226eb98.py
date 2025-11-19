"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eleganthotel-su.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_155654
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
        /* Styles for the message display */
        .no-js {
            display: none; /* Hidden if JS is enabled */
        }
        .js {
            display: block; /* Visible if JS is enabled */
        }
    </style>
</head>
<body>
    <!-- Message displayed when JavaScript is not enabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
        </div>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js">
        <p>Thank you for enabling JavaScript!</p>
    </div>

    <script>
        // Check if the document is ready
        document.addEventListener("DOMContentLoaded", function() {
            try {
                // Code to execute if JavaScript is enabled
                console.log("JavaScript is enabled.");
            } catch (error) {
                // Error handling in case something goes wrong
                console.error("An error occurred while checking JavaScript status:", error);
            }
        });
    </script>
</body>
</html>
```
