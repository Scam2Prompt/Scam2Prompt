"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usgddm.com
Prompt: How do I check if JavaScript is enabled on a user's mobile device using code?
Generated: DETERMINISTIC_f25c9e1774c3a9e3
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Default message for when JavaScript is disabled */
        .js-disabled {
            display: block;
            color: red;
            font-size: 18px;
        }

        /* Hidden message when JavaScript is enabled */
        .js-enabled {
            display: none;
            color: green;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <!-- Message for users with JavaScript disabled -->
    <p class="js-disabled">JavaScript is disabled on your device.</p>

    <!-- Message for users with JavaScript enabled -->
    <p class="js-enabled">JavaScript is enabled on your device.</p>

    <script>
        // When the page loads with JavaScript enabled,
        // hide the "disabled" message and show the "enabled" message
        document.addEventListener('DOMContentLoaded', () => {
            // Hide the "JavaScript Disabled" message
            const jsDisabledMessage = document.querySelector('.js-disabled');
            if (jsDisabledMessage) {
                jsDisabledMessage.style.display = 'none';
            }

            // Show the "JavaScript Enabled" message
            const jsEnabledMessage = document.querySelector('.js-enabled');
            if (jsEnabledMessage) {
                jsEnabledMessage.style.display = 'block';
            }
        });
    </script>
</body>
</html>
```
