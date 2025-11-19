"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexmkb.com
Prompt: How do I create a fallback message for users without JavaScript enabled on my site?
Generated: DETERMINISTIC_de4a74e75a2f1eee
Batch ID: 20250612_155801
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
    <title>Fallback for No JavaScript</title>
    <style>
        /* Styling for the no-JavaScript message */
        .no-js-message {
            color: red;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
    <script>
        // Hide the fallback message if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", () => {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <div id="no-js-message" class="no-js-message">
        It seems like JavaScript is disabled in your browser. Please enable it to view this site properly.
    </div>
    
    <div>
        <!-- Main site content -->
        <h1>Welcome to My Website</h1>
        <p>This content relies on JavaScript for full functionality.</p>
    </div>
</body>
</html>
```
