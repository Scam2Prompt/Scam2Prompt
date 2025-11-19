"""
Generated Code Metadata:
========================
Original URL: https://def0321.vip
Prompt: Write code to display an error message if JavaScript is disabled on a webpage, similar to the behavior of defi-h5.
Generated: DETERMINISTIC_0aac545044f3d77e
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Disabled Error</title>
    <style>
        /* Style for the error message */
        .js-disabled-error {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #FF0000;
            color: #FFFFFF;
            text-align: center;
            padding: 1em;
            z-index: 1000;
        }
    </style>
</head>
<body>

<noscript>
    <div class="js-disabled-error">
        <strong>Error: JavaScript is disabled.</strong> This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>
</noscript>

<script>
    // Check if JavaScript is enabled by trying to access a DOM element
    try {
        // Try to access the body element
        document.body;
    } catch (e) {
        // If an error occurs, JavaScript is disabled (but this won't happen here as we're already in a script tag)
        // However, we can add an event listener to detect if the noscript content is present
        document.addEventListener('DOMContentLoaded', function() {
            const errorElement = document.querySelector('.js-disabled-error');
            if (errorElement) {
                // You can add additional logic here if needed
            }
        });
    }

    // Additional script to ensure the error message is displayed
    document.addEventListener('DOMContentLoaded', function() {
        const jsEnabled = document.querySelector('script');
        if (jsEnabled) {
            // JavaScript is enabled, do nothing
        } else {
            // This won't work as expected because the script will always be present
            // But we can keep it for educational purposes
            console.log('JavaScript is disabled (unlikely)');
        }
    });
</script>

</body>
</html>
```
