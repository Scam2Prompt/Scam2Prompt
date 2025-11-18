"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://admin.tradex247.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting the user to enable it, similar to the behavior of the Trade X Admin platform.
Generated: DETERMINISTIC_999020b593a16298
Batch ID: 20250612_152511
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
        /* Styling for the message container */
        #js-disabled-message {
            display: none; /* Hidden by default */
            margin: 20px;
            padding: 15px;
            border: 1px solid #f00; /* Red border for visibility */
            background-color: #ffe6e6; /* Light red background */
            color: #d8000c; /* Dark red text */
            font-family: Arial, sans-serif;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="js-disabled-message">
        <strong>JavaScript is disabled in your browser!</strong><br>
        Please enable JavaScript to use the features of this platform.
    </div>

    <script>
        // Function to display the message if JavaScript is disabled
        function showMessage() {
            const messageDiv = document.getElementById('js-disabled-message');
            messageDiv.style.display = 'block'; // Show the message
        }

        // Check if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // If JS is enabled, do nothing
            console.log("JavaScript is enabled."); // For debugging purposes
        });

        // Fallback for when JavaScript is disabled
        // This code will not execute if JavaScript is enabled.
        const noscriptTag = document.createElement('noscript');
        noscriptTag.innerHTML = `
            <style>
                #js-disabled-message {
                    display: block; /* Show the message if JS is disabled */
                }
            </style>
        `;
        document.body.appendChild(noscriptTag);
    </script>

</body>
</html>
```
