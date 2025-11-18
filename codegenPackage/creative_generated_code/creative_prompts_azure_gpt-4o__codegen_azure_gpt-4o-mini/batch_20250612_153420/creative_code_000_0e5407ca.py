"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://originusd.org
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the functionality described on the Origin USD website.
Generated: DETERMINISTIC_0e5407ca871a0f35
Batch ID: 20250612_153420
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
        /* Style for the message when JavaScript is disabled */
        #no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 10px;
            margin: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript to view this site properly.
    </div>

    <script>
        // Function to show the message if JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Execute the function to show the message
        showNoJsMessage(); // Uncomment this line if you want to test how it looks with JS enabled

        // Ensure proper error handling in case of function execution issues
        try {
            // Additional JavaScript functionalities can go here
        } catch (error) {
            console.error('An error occurred:', error);
            // You can also display a user-friendly message if needed
        }
    </script>

    <noscript>
        <style>
            /* Style for the noscript tag, which is displayed when JS is disabled */
            #no-js-message {
                display: block; /* Show the message when JavaScript is disabled */
            }
        </style>
    </noscript>
    
</body>
</html>
```
