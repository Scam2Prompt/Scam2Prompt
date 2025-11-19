"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-explorer.skavel.cz
Prompt: Can you provide code snippets to check if JavaScript is enabled in a web browser for using Sonic Explorer?
Generated: DETERMINISTIC_9c24686ac80594a8
Batch ID: 20250612_155531
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
    <title>Sonic Explorer</title>
    <style>
        /* Style to display a message when JavaScript is disabled */
        .no-js {
            display: block;
            color: red;
            font-size: 18px;
        }
        
        .js-enabled {
            display: none;
        }
    </style>
</head>
<body>

    <!-- This message will display if JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            JavaScript is required to run Sonic Explorer. Please enable JavaScript in your browser settings.
        </div>
    </noscript>

    <!-- This message will display if JavaScript is enabled -->
    <div class="js-enabled">
        Welcome to Sonic Explorer! JavaScript is enabled.
    </div>

    <script>
        // Ensure JavaScript-enabled content is visible
        document.addEventListener('DOMContentLoaded', function() {
            // Hide the "no-js" message
            const noJsElements = document.querySelectorAll('.no-js');
            for (const element of noJsElements) {
                element.style.display = 'none';
            }
            
            // Show the "js-enabled" message
            const jsEnabledElements = document.querySelectorAll('.js-enabled');
            for (const element of jsEnabledElements) {
                element.style.display = 'block';
            }
        });
    </script>

</body>
</html>
```
