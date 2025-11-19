"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sdddd.pages.dev
Prompt: Create a code snippet that displays a message for users who visit the chimpers-dojo website without JavaScript enabled.
Generated: DETERMINISTIC_bc2a01cc8b83b5d2
Batch ID: 20250612_163742
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
    <title>Chimpers Dojo</title>
    <style>
        /* Styles for the no-JavaScript message */
        .no-js-message {
            font-family: Arial, sans-serif;
            font-size: 1.2em;
            color: #ff0000;
            background-color: #fff3f3;
            border: 1px solid #ffcccc;
            padding: 15px;
            margin: 20px;
            text-align: center;
        }

        /* Hide the no-JavaScript message if JavaScript is enabled */
        .no-js-message {
            display: none;
        }
    </style>
    <script>
        // JavaScript to hide the no-JavaScript message
        document.addEventListener("DOMContentLoaded", function () {
            const noJsMessageElement = document.querySelector(".no-js-message");
            if (noJsMessageElement) {
                noJsMessageElement.style.display = "none";
            }
        });
    </script>
</head>
<body>
    <!-- Message for users who have JavaScript disabled -->
    <div class="no-js-message">
        <p>It seems JavaScript is disabled in your browser. To enjoy the full experience of the Chimpers Dojo website, please enable JavaScript.</p>
    </div>

    <!-- Main Content -->
    <div id="main-content">
        <h1>Welcome to Chimpers Dojo</h1>
        <p>Train your skills and become the best dojo master!</p>
    </div>
</body>
</html>
```
