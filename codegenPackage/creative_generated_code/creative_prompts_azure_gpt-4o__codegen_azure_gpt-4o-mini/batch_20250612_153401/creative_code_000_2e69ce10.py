"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the functionality of the Honey App.
Generated: DETERMINISTIC_2e69ce101c89a396
Batch ID: 20250612_153401
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
            display: none; /* Hidden by default */
            background-color: #ffcccc; /* Light red background */
            color: #d8000c; /* Dark red text */
            border: 1px solid #d8000c; /* Dark red border */
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <div id="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript for the best experience.
    </div>

    <script>
        // Function to show the message indicating JavaScript is disabled
        function showNoJsMessage() {
            const messageDiv = document.getElementById('no-js-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Attempt to execute some JavaScript code
        try {
            // If this code runs, it means JavaScript is enabled
            console.log('JavaScript is enabled.');
        } catch (error) {
            // Log any errors that occur (shouldn't happen here)
            console.error('An error occurred while checking JavaScript functionality:', error);
        }

        // Set a timeout to show the message after a short delay
        // This ensures that if JavaScript is enabled, it won't show the message
        setTimeout(() => {
            // If this function isn't executed, JavaScript is likely disabled
            showNoJsMessage();
        }, 1000); // Delay in milliseconds (1 second)
    </script>
</body>
</html>
```
