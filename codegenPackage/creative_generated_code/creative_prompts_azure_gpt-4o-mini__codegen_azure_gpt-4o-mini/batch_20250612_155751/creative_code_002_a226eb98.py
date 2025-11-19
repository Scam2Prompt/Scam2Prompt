"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedefiant.de
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_155751
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
        // Function to check if JavaScript is enabled
        (function() {
            // Add a class to the body indicating JavaScript is enabled
            document.body.className += " js";
        })();
    </script>
</body>
</html>
```
