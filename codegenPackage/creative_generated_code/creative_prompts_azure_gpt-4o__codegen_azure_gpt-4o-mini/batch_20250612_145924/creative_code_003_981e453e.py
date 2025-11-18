"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origina-predictor.vercel.app
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the browser and displays a message like "You need to enable JavaScript to run this app," similar to the "Predictor" app.
Generated: DETERMINISTIC_981e453ee8deaf79
Batch ID: 20250612_145924
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Style for error message */
        #js-error-message {
            display: none; /* Hide by default */
            color: red; 
            font-weight: bold;
            padding: 10px;
            border: 1px solid red;
            background-color: #ffe6e6;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>

<div id="js-error-message">
    You need to enable JavaScript to run this app.
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
        try {
            // If this function runs, JavaScript is enabled
            document.getElementById('js-error-message').style.display = 'none';
        } catch (error) {
            // If an error occurs, display the error message
            console.error("Error checking JavaScript status:", error);
            displayErrorMessage();
        }
    }

    // Function to display error message
    function displayErrorMessage() {
        const errorMessageDiv = document.getElementById('js-error-message');
        errorMessageDiv.style.display = 'block'; // Show the error message
    }

    // Execute the check when the script is loaded
    checkJavaScriptEnabled();
</script>

<noscript>
    <!-- This message will only show if JavaScript is disabled -->
    <style>
        #js-error-message {
            display: block; /* Show if JavaScript is disabled */
        }
    </style>
</noscript>

</body>
</html>
```
