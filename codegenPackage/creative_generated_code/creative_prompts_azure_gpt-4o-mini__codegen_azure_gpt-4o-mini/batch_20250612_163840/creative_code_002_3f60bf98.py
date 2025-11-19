"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imptp.com
Prompt: Can you provide a code snippet that checks if JavaScript is enabled on a mobile browser?
Generated: DETERMINISTIC_3f60bf985f7c9875
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
        /* Style for the message shown when JavaScript is disabled */
        .no-js {
            display: block;
            color: red;
            font-weight: bold;
        }
        /* Hide the message when JavaScript is enabled */
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- Message for when JavaScript is disabled -->
    <div id="no-js-message" class="no-js">JavaScript is disabled in your browser. Please enable it for better functionality.</div>

    <!-- This script will run if JavaScript is enabled -->
    <script>
        // Ensure the document is fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Hide the message indicating JavaScript is disabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.classList.remove('no-js'); // Hide the disabled message
                noJsMessage.classList.add('js'); // Add the class to manage visibility
            }
        });
    </script>
</body>
</html>
```
