"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soneium.app
Prompt: How do I implement a fallback message for users without JavaScript on the Soneium domain details page?
Generated: DETERMINISTIC_3e63e27e00d78837
Batch ID: 20250612_155131
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
    <title>Soneium Domain Details</title>
    <style>
        /* Styles for the fallback message */
        .no-js-message {
            display: none; /* Hidden by default, shown only if JavaScript is disabled */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px 0;
        }
    </style>
    <script>
        // JavaScript to hide the fallback message
        document.addEventListener("DOMContentLoaded", function () {
            document.querySelector(".no-js-message").style.display = "none";
        });
    </script>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <div class="no-js-message">
        It seems JavaScript is disabled in your browser. Please enable JavaScript to use the Soneium domain details page.
    </div>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to the Soneium Domain Details Page</h1>
        <p>Loading domain details...</p>
        <!-- JavaScript-enabled content will dynamically load here -->
    </div>
</body>
</html>
```
