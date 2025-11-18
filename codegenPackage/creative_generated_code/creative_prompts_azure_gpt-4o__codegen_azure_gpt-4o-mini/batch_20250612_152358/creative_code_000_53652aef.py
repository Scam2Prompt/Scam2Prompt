"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgifts.web.app
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting users to enable it, similar to the functionality described on the Shibonk Gang Whitelist webpage.
Generated: DETERMINISTIC_53652aef557e0038
Batch ID: 20250612_152358
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
    <title>JavaScript Check</title>
    <style>
        /* Styles to display the message prominently */
        #js-message {
            display: none; /* Hide the message initially */
            background-color: #f44336; /* Red background for warning */
            color: white; /* White text for contrast */
            padding: 20px; /* Padding for better appearance */
            text-align: center; /* Center the text */
            position: fixed; /* Fixed position to stay in view */
            top: 0; /* Position at the top */
            left: 0; /* Position on the left */
            right: 0; /* Stretch to the right */
            z-index: 1000; /* Ensure it appears above other content */
        }
    </style>
</head>
<body>

<div id="js-message">
    JavaScript is disabled in your browser. Please enable it for the best experience.
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
        // Display the message if JavaScript is disabled
        document.getElementById('js-message').style.display = 'block';
    }

    // Run the function to check if JavaScript is enabled
    checkJavaScriptEnabled();

    // If JavaScript is enabled, hide the message
    document.getElementById('js-message').style.display = 'none';
</script>

</body>
</html>
```
