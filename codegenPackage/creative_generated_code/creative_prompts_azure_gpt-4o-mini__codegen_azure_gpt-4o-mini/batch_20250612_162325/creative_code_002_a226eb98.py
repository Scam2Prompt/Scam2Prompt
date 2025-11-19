"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rarityconnect.rf.gd
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_162325
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
    <div class="no-js">
        <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
    </div>
    
    <!-- Message displayed when JavaScript is enabled -->
    <div class="js">
        <p>JavaScript is enabled in your browser!</p>
    </div>

    <script>
        // Function to hide the no-JS message and show the JS-enabled message
        function checkJavaScript() {
            // Select the elements
            const noJsMessage = document.querySelector('.no-js');
            const jsMessage = document.querySelector('.js');

            // Check if elements exist before manipulating
            if (noJsMessage && jsMessage) {
                // Hide the no-JS message and show the JS-enabled message
                noJsMessage.style.display = 'none';
                jsMessage.style.display = 'block';
            } else {
                console.error('Message elements are missing in the DOM.');
            }
        }

        // Run the checkJavaScript function when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', checkJavaScript);
    </script>
</body>
</html>
```
