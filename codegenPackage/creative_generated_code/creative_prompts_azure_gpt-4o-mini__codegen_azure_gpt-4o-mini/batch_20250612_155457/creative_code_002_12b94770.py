"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcll.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application like ETH Pledge?
Generated: DETERMINISTIC_12b9477044bf98f8
Batch ID: 20250612_155457
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
    <title>Check JavaScript Enabled</title>
    <style>
        /* Style to hide the content if JavaScript is not enabled */
        #no-js {
            display: none;
        }
        #js-enabled {
            display: block;
        }
    </style>
</head>
<body>
    <noscript>
        <style>
            /* Show the message when JavaScript is disabled */
            #no-js {
                display: block;
            }
            #js-enabled {
                display: none;
            }
        </style>
    </noscript>

    <div id="no-js">
        <h1>JavaScript is Disabled</h1>
        <p>Please enable JavaScript in your browser settings to use this application.</p>
    </div>

    <div id="js-enabled">
        <h1>Welcome!</h1>
        <p>JavaScript is enabled. You can use the application.</p>
    </div>

    <script>
        // Function to initialize the application
        function initApp() {
            try {
                // Your application logic here
                console.log("Application initialized successfully.");
            } catch (error) {
                // Log the error for debugging
                console.error("An error occurred while initializing the application:", error);
                alert("An error occurred. Please try again later.");
            }
        }

        // Run the application initialization on page load
        window.onload = initApp;
    </script>
</body>
</html>
```
