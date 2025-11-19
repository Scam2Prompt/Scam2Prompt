"""
Generated Code Metadata:
========================
Original URL: https://digitalconsultinggroup.my
Prompt: How can I implement a JavaScript-enabled check on my website, similar to https://digitalconsultinggroup.my, and what are the benefits of doing so?
Generated: DETERMINISTIC_67261be9507182ab
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check Example</title>
    <style>
        /* Basic styling for the message */
        #js-check-message {
            display: none; /* Hidden by default */
            padding: 10px;
            margin: 20px;
            border: 1px solid #ccc;
            background-color: #f9f9f9;
            color: #333;
        }
    </style>
</head>
<body>

    <div id="js-check-message">
        JavaScript is enabled on your browser!
    </div>

    <noscript>
        <style>
            /* Style for the message when JavaScript is disabled */
            #js-check-message {
                display: none; /* Hide the message */
            }
        </style>
        <div style="color: red; padding: 10px;">
            JavaScript is disabled in your browser. Please enable it for the best experience.
        </div>
    </noscript>

    <script>
        // Function to display a message if JavaScript is enabled
        function displayJsEnabledMessage() {
            const messageDiv = document.getElementById('js-check-message');
            if (messageDiv) {
                messageDiv.style.display = 'block'; // Show the message
            } else {
                console.error('Message div not found'); // Error handling
            }
        }

        // Execute the function to show the message
        displayJsEnabledMessage();
    </script>

</body>
</html>
```
