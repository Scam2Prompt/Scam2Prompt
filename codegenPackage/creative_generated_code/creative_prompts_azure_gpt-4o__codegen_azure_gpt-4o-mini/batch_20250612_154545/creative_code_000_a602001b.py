"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ravitechworld.com
Prompt: Write JavaScript code to detect if JavaScript is enabled in a user's browser and display a custom message if it is disabled, referencing techniques commonly used in interactive web applications.
Generated: DETERMINISTIC_a602001b4e900796
Batch ID: 20250612_154545
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
        /* Style for the message displayed when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            padding: 20px;
            border: 1px solid #f00;
            background-color: #ffe6e6;
            color: #d8000c;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <!-- Message to display when JavaScript is disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable it for a better experience on this website.
    </div>

    <script>
        // Function to display the no-JS message
        function showNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'block'; // Show the message
            }
        }

        // Function to hide the no-JS message
        function hideNoJsMessage() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Execute when the DOM is fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            hideNoJsMessage(); // Hide the no-JS message as JavaScript is running
        });

        // In case of error during DOM manipulation, handle gracefully
        try {
            // Additional JavaScript functionality can be added here
        } catch (error) {
            console.error('An error occurred while executing JavaScript:', error);
            showNoJsMessage(); // Show the message if there's an error
        }
    </script>

    <noscript>
        <!-- This block will only be rendered if JavaScript is disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message when no JavaScript */
            }
        </style>
    </noscript>

</body>
</html>
```
