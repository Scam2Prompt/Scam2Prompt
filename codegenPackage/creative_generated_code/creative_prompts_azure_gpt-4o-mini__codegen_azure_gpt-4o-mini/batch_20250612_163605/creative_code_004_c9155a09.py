"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runonflux.xyz
Prompt: How do I create a fallback message for users without JavaScript enabled on my website?
Generated: DETERMINISTIC_c9155a0964f37808
Batch ID: 20250612_163605
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Hide the fallback message by default */
        .fallback {
            display: none;
            color: red;
            font-weight: bold;
        }
        .js-enabled {
            display: none; /* Hide this message when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <!-- Fallback message for users without JavaScript -->
    <div class="fallback" id="fallbackMessage">
        It seems that JavaScript is disabled in your browser. Please enable it for the best experience on this website.
    </div>

    <!-- Message for users with JavaScript enabled -->
    <div class="js-enabled" id="jsMessage">
        JavaScript is enabled. Thank you for enabling it!
    </div>

    <script>
        // This script is executed if JavaScript is enabled
        document.getElementById('fallbackMessage').style.display = 'none'; // Hide the fallback message
        document.getElementById('jsMessage').style.display = 'block'; // Show the JavaScript enabled message
    </script>

</body>
</html>
```
