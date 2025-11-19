"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.heheepro.com
Prompt: Can you provide a code snippet to detect if JavaScript is enabled in a web application like HEHEE Pro?
Generated: DETERMINISTIC_d03ef8ea188bd2b7
Batch ID: 20250612_162511
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
        /* Styles to show/hide elements based on JavaScript status */
        .no-js {
            display: block;
        }
        .js {
            display: none;
        }
    </style>
</head>
<body>
    <!-- This message is displayed if JavaScript is disabled -->
    <div class="no-js">
        <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
    </div>

    <!-- This message is displayed if JavaScript is enabled -->
    <div class="js">
        <p>JavaScript is enabled. Welcome to HEHEE Pro!</p>
    </div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            try {
                // If this script runs, then JavaScript is enabled
                document.querySelector('.no-js').style.display = 'none';
                document.querySelector('.js').style.display = 'block';
            } catch (error) {
                // Handle any errors that may arise
                console.error('An error occurred while detecting JavaScript:', error);
            }
        }

        // Execute the detection function
        detectJavaScript();
    </script>
</body>
</html>
```
