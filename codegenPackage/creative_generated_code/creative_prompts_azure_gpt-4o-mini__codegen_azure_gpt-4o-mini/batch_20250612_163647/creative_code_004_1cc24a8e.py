"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: How do I create a fallback message for users who have JavaScript disabled on my website?
Generated: DETERMINISTIC_1cc24a8ec498806d
Batch ID: 20250612_163647
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
    <title>Fallback Message Example</title>
    <style>
        /* Style for the fallback message */
        .fallback-message {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px 0;
        }
        /* Style for the active message when JavaScript is disabled */
        .no-js .fallback-message {
            display: block; /* Show when JS is disabled */
        }
    </style>
</head>
<body class="no-js">

    <!-- Fallback message for users with JavaScript disabled -->
    <div class="fallback-message">
        It seems that JavaScript is disabled in your browser. For the best experience, please enable JavaScript or upgrade to a modern browser.
    </div>

    <!-- Main content of the page -->
    <h1>Welcome to My Website</h1>
    <p>This is an example of how to handle users with JavaScript disabled.</p>

    <script>
        // Check if JavaScript is enabled
        document.body.classList.remove('no-js'); // Remove the no-js class if JS is enabled

        // Additional JavaScript functionality can go here
        console.log("JavaScript is enabled!");
    </script>
</body>
</html>
```
