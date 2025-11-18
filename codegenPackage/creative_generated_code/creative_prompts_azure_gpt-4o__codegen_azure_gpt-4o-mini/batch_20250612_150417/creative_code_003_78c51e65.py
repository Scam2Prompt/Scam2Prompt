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
    <title>JavaScript Disabled Warning</title>
    <style>
        /* Styling for the warning message */
        #js-warning {
            display: none; /* Hide by default */
            background-color: #ffcc00;
            color: #000;
            border: 2px solid #ff9900;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translateX(-50%);
            z-index: 1000;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>שגיאה:</strong> כדי להשתמש באתר זה, אנא הפעל את JavaScript בדפדפן שלך.
    </div>

    <script>
        // Function to show the warning message
        function showWarning() {
            const warningDiv = document.getElementById('js-warning');
            if (warningDiv) {
                warningDiv.style.display = 'block'; // Display the warning message
            } else {
                console.error("Warning element not found."); // Error handling
            }
        }

        // Check if JavaScript is disabled by setting a flag
        document.addEventListener('DOMContentLoaded', function() {
            // Normally, if JS is enabled, we would not want to show the warning
            // If JS is enabled, we do nothing
        });
    </script>

    <noscript>
        <style>
            /* This style ensures the warning message is visible if JS is disabled */
            #js-warning {
                display: block; /* Show the warning message */
            }
        </style>
    </noscript>

</body>
</html>
```
