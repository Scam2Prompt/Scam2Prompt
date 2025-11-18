"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d952.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message like "mining-h5 doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_acede2a23bea3833
Batch ID: 20250612_154954
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
        /* Hide the warning message by default */
        .js-warning {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="js-warning" id="js-warning">
        mining-h5 doesn't work properly without JavaScript enabled.
    </div>

    <script>
        // This function displays the warning message if JavaScript is disabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            warningElement.style.display = 'block';
        }

        // Add an event listener that runs when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', () => {
            // If JavaScript is enabled, we can display the content normally
            console.log('JavaScript is enabled.');
        });
    </script>

    <noscript>
        <!-- This message will be displayed if JavaScript is disabled -->
        <style>
            #js-warning {
                display: block; /* Show the warning in case JavaScript is disabled */
            }
        </style>
    </noscript>

</body>
</html>
```
