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
        /* Style for the message when JavaScript is disabled */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            padding: 15px; /* Padding for better visibility */
            border: 1px solid #d8000c; /* Dark red border */
            margin: 20px; /* Margin for spacing */
            border-radius: 5px; /* Rounded corners */
            text-align: center; /* Center align text */
        }
    </style>
</head>
<body>
    <div class="no-js-message" id="no-js-message">
        <strong>JavaScript is disabled!</strong> Please enable JavaScript to view the full functionality of the Chimpers Dojo website.
    </div>

    <script>
        // Function to hide the no-JS message if JavaScript is enabled
        function enableJs() {
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none'; // Hide the message
            }
        }

        // Call the function to enable JavaScript
        enableJs();
    </script>
    
    <!-- Content of the website goes here -->
    <h1>Welcome to Chimpers Dojo!</h1>
    <p>Your adventure in coding begins here.</p>
    
    <noscript>
        <!-- Fallback message for users without JavaScript -->
        <style>
            .no-js-message {
                display: block; /* Display the message if JS is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
