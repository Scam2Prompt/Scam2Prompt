"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.world
Prompt: Write code to detect whether JavaScript is enabled in a browser and display a message prompting users to enable it for accessing the "Polkadot Go - POAP Hunt" app.
Generated: DETERMINISTIC_dfdfbe42827d9921
Batch ID: 20250612_142620
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
    <title>Polkadot Go - POAP Hunt</title>
    <style>
        /* Style to hide the message by default */
        #no-js-message {
            display: none;
            color: red;
            font-size: 18px;
            text-align: center;
            margin-top: 50px;
        }
    </style>
    <noscript>
        <style>
            /* Style to show the message if JavaScript is disabled */
            #no-js-message {
                display: block;
            }
        </style>
    </noscript>
</head>
<body>

    <div id="no-js-message">
        <p>JavaScript is disabled in your browser. Please enable JavaScript to access the "Polkadot Go - POAP Hunt" app.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            // Log message for debugging
            console.log("JavaScript is enabled.");

            // Optionally, you could perform further initialization for the app here
        }

        // Execute the function to check JavaScript availability
        try {
            checkJavaScript();
        } catch (error) {
            console.error("An error occurred while checking JavaScript:", error);
        }
    </script>
</body>
</html>
```
