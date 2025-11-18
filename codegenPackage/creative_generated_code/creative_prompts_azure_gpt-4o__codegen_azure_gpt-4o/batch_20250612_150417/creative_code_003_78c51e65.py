"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getin.co.il
Prompt: Generate HTML and JavaScript code to display a warning message when JavaScript is disabled, ensuring the message is styled and localized for Hebrew users like on https://getin.co.il.
Generated: DETERMINISTIC_78c51e65e73c5886
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>אזהרת JavaScript</title>
    <style>
        /* Style for the warning message */
        .no-js-warning {
            display: none; /* Hidden by default, shown only if JavaScript is disabled */
            background-color: #ffcccb; /* Light red background for warning */
            color: #000; /* Black text color */
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            border: 2px solid #ff0000; /* Red border for emphasis */
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Warning message for users with JavaScript disabled -->
    <div class="no-js-warning">
        <p><strong>אזהרה:</strong> האתר דורש שפת JavaScript כדי לפעול כראוי. אנא אפשר את JavaScript בדפדפן שלך.</p>
    </div>

    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <style>
            .no-js-warning {
                display: block; /* Display warning if JavaScript is disabled */
            }
        </style>
    </noscript>

    <script>
        /* Ensure the warning remains hidden if JavaScript is enabled */
        document.addEventListener('DOMContentLoaded', function () {
            const warningElement = document.querySelector('.no-js-warning');
            if (warningElement) {
                warningElement.style.display = 'none'; // Hide the warning
            }
        });
    </script>
</body>
</html>
```
