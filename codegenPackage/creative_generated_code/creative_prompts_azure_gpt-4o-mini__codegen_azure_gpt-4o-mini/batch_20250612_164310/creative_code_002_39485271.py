"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesla.bz
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application?
Generated: DETERMINISTIC_39485271d7840f12
Batch ID: 20250612_164310
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
        /* Styles to hide the message if JavaScript is enabled */
        .no-js {
            display: block;
        }
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
        </div>
    </noscript>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js-enabled">
        <p>JavaScript is enabled in your browser. Enjoy your experience!</p>
    </div>

    <script>
        // Function to handle JavaScript enabled case
        function checkJavaScript() {
            // Remove 'no-js' class and add 'js-enabled' class
            document.querySelector('.no-js').style.display = 'none';
            document.querySelector('.js-enabled').style.display = 'block';
        }

        // Check if the DOM is fully loaded before running the function
        document.addEventListener('DOMContentLoaded', checkJavaScript);
    </script>

</body>
</html>
```
