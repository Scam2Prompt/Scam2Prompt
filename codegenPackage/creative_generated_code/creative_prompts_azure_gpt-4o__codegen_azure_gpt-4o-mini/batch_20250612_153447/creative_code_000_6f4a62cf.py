"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the Webmail login page of https://webmail.everclear.pk.
Generated: DETERMINISTIC_6f4a62cffe5f1077
Batch ID: 20250612_153447
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
        /* Style for the warning message */
        .js-warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div class="js-warning" id="js-warning">
    <strong>Warning!</strong> It seems that JavaScript is disabled in your browser. 
    Please enable JavaScript to use this website properly.
</div>

<!-- JavaScript code to display the warning message if JavaScript is disabled -->
<script>
    // Function to show the warning message
    function showWarning() {
        const warningElement = document.getElementById('js-warning');
        if (warningElement) {
            warningElement.style.display = 'block'; // Show the warning message
        } else {
            console.error('Warning element not found'); // Log error if element is not found
        }
    }
</script>

<script>
    // Execute the function to show the warning if JavaScript is disabled
    document.addEventListener('DOMContentLoaded', function() {
        // If JavaScript is running, we can safely remove the warning message
        const warningElement = document.getElementById('js-warning');
        if (warningElement) {
            warningElement.style.display = 'none'; // Hide the message
        }
    });
</script>

<!-- Here we leave this block intentionally unevaluated, which will only run if JS is disabled -->
<noscript>
    <style>
        #js-warning {
            display: block; /* Show the warning message if JavaScript is disabled */
        }
    </style>
</noscript>

</body>
</html>
```
