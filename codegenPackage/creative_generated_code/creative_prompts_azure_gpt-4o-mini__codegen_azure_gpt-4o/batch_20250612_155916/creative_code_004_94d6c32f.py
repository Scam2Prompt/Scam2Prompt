"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gettrumpmeme.thsite.top
Prompt: How can I create a simple webpage that alerts users to enable Javascript for better functionality?
Generated: DETERMINISTIC_94d6c32f6ce5a10e
Batch ID: 20250612_155916
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
    <title>Enable JavaScript</title>
    <style>
        /* Basic styling for the message */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffcccb;
            color: #000;
            padding: 20px;
            border: 1px solid #f5a3a3;
            margin: 20px auto;
            text-align: center;
            font-family: Arial, sans-serif;
            max-width: 600px;
            border-radius: 5px;
        }
    </style>
</head>

<body>
    <!-- Fallback message for non-JavaScript users -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is not enabled in your browser. Please enable JavaScript for better functionality on this site.
    </div>

    <script>
        // JavaScript to hide the message if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function () {
            const noJsMessage = document.getElementById("no-js-message");
            if (noJsMessage) {
                noJsMessage.style.display = "none"; // Hide the message since JavaScript is enabled
            }
        });
    </script>

    <!-- Content of the webpage -->
    <h1>Welcome to My Website</h1>
    <p>Enjoy the enhanced features provided by JavaScript!</p>
</body>

</html>
```
