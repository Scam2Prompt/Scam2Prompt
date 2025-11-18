"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapfinderbs.github.io
Prompt: Create a script to detect if JavaScript is disabled on a webpage and display a custom message for AveSwap users.
Generated: DETERMINISTIC_307746bf8a97cb07
Batch ID: 20250612_151141
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
    <title>AveSwap Detection</title>
    <style>
        /* Style for the message container */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #f5c6cb; /* Border color */
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to be displayed if JavaScript is disabled -->
    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable it for the best experience on AveSwap.
    </div>

    <script>
        // Function to show the message if JavaScript gets executed
        function showMessage() {
            const messageContainer = document.getElementById('no-js-message');
            messageContainer.style.display = 'none'; // Hide the message if JS is enabled
        }

        // Execute the function to show message
        showMessage();
    </script>

    <noscript>
        <!-- Fallback content for users with JavaScript disabled -->
        <style>
            #no-js-message {
                display: block; /* Show the message if JS is disabled */
            }
        </style>
    </noscript>
</body>
</html>
```
