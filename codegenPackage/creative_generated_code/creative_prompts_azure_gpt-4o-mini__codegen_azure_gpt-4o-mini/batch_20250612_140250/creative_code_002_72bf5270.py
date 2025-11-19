"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alist.025680.xyz
Prompt: Can you provide a code snippet to check if JavaScript is enabled for AList functionality?
Generated: DETERMINISTIC_72bf5270b1bcfb52
Batch ID: 20250612_140250
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styles for the message */
        #no-js-message {
            display: none; /* Hide by default */
            color: red; 
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for full functionality.
    </div>

    <script>
        // Function to display a message if JavaScript is disabled
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'block';
        }

        // Function to indicate that JavaScript is enabled
        function jsEnabled() {
            console.log('JavaScript is enabled.');
            // Hide the no-JS message if it exists
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none';
        }

        // Setup an event listener to run the jsEnabled function
        document.addEventListener('DOMContentLoaded', jsEnabled);
    </script>

    <!-- Fallback content for users without JavaScript -->
    <noscript>
        <style>
            #no-js-message {
                display: block; /* Show message if JS is disabled */
            }
        </style>
        <div id="no-js-message">
            JavaScript is disabled in your browser. Please enable it for full functionality.
        </div>
    </noscript>

</body>
</html>
```
