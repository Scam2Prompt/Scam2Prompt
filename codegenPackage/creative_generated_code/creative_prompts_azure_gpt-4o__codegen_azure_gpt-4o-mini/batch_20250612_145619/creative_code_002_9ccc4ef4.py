"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkbn.com
Prompt: Generate code to check if JavaScript is enabled in a browser and display a warning message if it is disabled.
Generated: DETERMINISTIC_9ccc4ef4dffdb435
Batch ID: 20250612_145619
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
        /* Style for the warning message */
        .warning {
            display: none; /* Hidden by default */
            background-color: #ffcc00; /* Warning color */
            color: #000; /* Text color */
            padding: 15px; /* Padding around the message */
            margin: 20px auto; /* Center the message */
            border: 1px solid #ffa500; /* Border color */
            width: 80%; /* Width of the warning box */
            text-align: center; /* Center text */
        }
    </style>
</head>
<body>

<div id="warning" class="warning">
    Warning: JavaScript is disabled in your browser. Please enable it for the best experience.
</div>

<script>
    // Function to show the warning message if JavaScript is disabled
    function checkJavaScriptEnabled() {
        var warningElement = document.getElementById('warning');
        if (!warningElement) {
            console.error('Warning element not found in the DOM.');
            return; // Exit the function if the warning element is not found
        }
        
        warningElement.style.display = 'none'; // Hide the warning by default
    }

    // Call the function to check for JavaScript
    checkJavaScriptEnabled();
</script>

<noscript>
    <!-- This block will only render if JavaScript is disabled -->
    <style>
        #warning {
            display: block; /* Show the warning message */
        }
    </style>
</noscript>

</body>
</html>
```
