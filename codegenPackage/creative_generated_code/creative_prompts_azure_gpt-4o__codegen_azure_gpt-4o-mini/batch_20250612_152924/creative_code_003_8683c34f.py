"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synfutures.eu
Prompt: Generate JavaScript code to dynamically display a warning message when JavaScript is disabled on a webpage.
Generated: DETERMINISTIC_8683c34faef8fcd6
Batch ID: 20250612_152924
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
    <title>JavaScript Warning</title>
    <style>
        /* Styles for the warning message */
        #js-warning {
            display: none; /* Hidden by default */
            background-color: #ffcc00; /* Warning color */
            color: #000; /* Text color */
            padding: 15px; /* Spacing around the text */
            border: 1px solid #ff9900; /* Border color */
            text-align: center; /* Center the text */
            position: fixed; /* Fixed position */
            top: 10px; /* Top offset */
            left: 50%; /* Center horizontally */
            transform: translateX(-50%); /* Adjust for centering */
            z-index: 1000; /* Ensure it's on top */
            width: 90%; /* Responsive width */
            max-width: 600px; /* Maximum width */
        }
    </style>
</head>
<body>

<div id="js-warning">
    <strong>Warning:</strong> JavaScript is disabled in your browser. Please enable JavaScript for the best experience.
</div>

<noscript>
    <style>
        /* Display the warning message if JavaScript is disabled */
        #js-warning {
            display: block; /* Show the warning message */
        }
    </style>
</noscript>

<script>
    // This script is used to ensure that any necessary JavaScript code can run
    // If JavaScript is enabled, the warning message will remain hidden

    // Function to initialize the page
    function init() {
        // If JavaScript is enabled, we can do further initialization if needed
        console.log("JavaScript is enabled.");
        // Additional JavaScript functionality can be added here
    }

    // Call the init function
    try {
        init();
    } catch (error) {
        console.error("An error occurred during initialization:", error);
    }
</script>

</body>
</html>
```
