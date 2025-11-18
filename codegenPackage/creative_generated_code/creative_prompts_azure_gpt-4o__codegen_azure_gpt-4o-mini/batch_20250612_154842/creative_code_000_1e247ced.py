"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pns.paladin.coinbaseindexfund.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message instructing the user to enable it, similar to the functionality described on `pns.paladin.coinbaseindexfund.com`.
Generated: DETERMINISTIC_1e247ced8ab9566c
Batch ID: 20250612_154842
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
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px;
            border: 1px solid #f5c6cb; /* Red border */
            margin: 20px;
            border-radius: 5px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>

    <noscript>
        <div id="no-js-message">
            <strong>JavaScript is disabled in your browser!</strong><br>
            Please enable JavaScript to use this site properly.
        </div>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            console.log("JavaScript is enabled."); // Log for debugging purposes
            // You can add additional JavaScript code here to enhance functionality
        }

        // Call the function to indicate that JavaScript is enabled
        checkJavaScript();
    </script>

</body>
</html>
```
