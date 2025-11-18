"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as.magiceden.eu
Prompt: Provide code to dynamically display a warning message when JavaScript is disabled, ensuring compatibility across major browsers.
Generated: DETERMINISTIC_037ed4fd43cb8fd1
Batch ID: 20250612_154829
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
    <title>JavaScript Warning</title>
    <style>
        /* Style for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #ffeeba; /* Light yellow background */
            color: #856404; /* Dark yellow text */
            border: 1px solid #ffeeba; /* Border to match background */
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <div id="js-warning">
        <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <script>
        // Function to show the warning message if JavaScript is enabled
        function showWarning() {
            const warningElement = document.getElementById('js-warning');
            if (warningElement) {
                warningElement.style.display = 'none'; // Hide warning if JS is enabled
            }
        }

        // Execute the function to hide the warning message
        showWarning();
    </script>

    <!-- No script tag to display warning when JavaScript is disabled -->
    <noscript>
        <style>
            /* Display warning message when JavaScript is disabled */
            #js-warning {
                display: block; /* Show warning */
            }
        </style>
    </noscript>

</body>
</html>
```
