"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton.run
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web browser for ton.run?
Generated: DETERMINISTIC_ac78213e8f1f06ce
Batch ID: 20250612_162843
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Basic styles for the message display */
        .no-js {
            display: none;
            color: red;
            font-weight: bold;
        }
        .js {
            display: none;
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is not enabled -->
    <div class="no-js" id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience.
    </div>

    <!-- Message displayed when JavaScript is enabled -->
    <div class="js" id="js-message">
        JavaScript is enabled! You can proceed.
    </div>

    <script>
        // Function to show messages based on JavaScript availability
        function checkJavaScript() {
            try {
                // Display the message indicating that JavaScript is enabled
                document.getElementById('js-message').style.display = 'block';
            } catch (error) {
                // Log the error if any unexpected issue arises
                console.error('Error displaying JavaScript enabled message:', error);
            }
        }

        // Function to hide the no-JavaScript message if JavaScript is enabled
        function hideNoJSMessage() {
            try {
                document.getElementById('no-js-message').style.display = 'none';
            } catch (error) {
                console.error('Error hiding no-JavaScript message:', error);
            }
        }

        // Call the functions to check JavaScript status
        hideNoJSMessage();
        checkJavaScript();
    </script>

</body>
</html>
```
