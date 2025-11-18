"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.co.za
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the behavior described on coinbase.co.za.
Generated: DETERMINISTIC_e73f000cf34e9737
Batch ID: 20250612_154809
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
        /* Styles for the message when JS is disabled */
        #no-js-message {
            display: none; /* Initially hide the message */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to display if JavaScript is disabled -->
    <div id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript to use all features of this site.</p>
    </div>

    <script>
        // Function to hide the "no JS" message
        function hideNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            noJsMessage.style.display = 'none'; // Hide the message
        }

        // Function to handle potential errors
        function handleError(error) {
            console.error('An error occurred:', error);
            // Additional error handling logic can be added here
        }

        // Immediately invoked function to execute when JS is enabled
        (function() {
            try {
                // Hide the no-JS message if JS is enabled
                hideNoJsMessage();
            } catch (error) {
                // Handle any errors that may occur
                handleError(error);
            }
        })();
    </script>
</body>
</html>
```
