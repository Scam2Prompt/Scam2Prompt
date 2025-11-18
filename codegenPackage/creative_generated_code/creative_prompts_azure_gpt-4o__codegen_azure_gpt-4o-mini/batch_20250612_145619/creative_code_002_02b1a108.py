"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtlioken.com
Prompt: Create a JavaScript function that checks if JavaScript is enabled in the user's browser and displays a warning message if it's disabled, tailored for a site requiring ETH pledges.
Generated: DETERMINISTIC_02b1a108c94c3ac0
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
    <title>ETH Pledge Site</title>
    <style>
        #warning {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <div id="warning">
        <strong>Warning!</strong> JavaScript is required for this site to function properly. Please enable JavaScript to proceed with your ETH pledge.
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScriptEnabled() {
            // Selecting the warning message element
            const warningElement = document.getElementById('warning');

            // Check if JavaScript is enabled by displaying the warning message
            if (warningElement) {
                warningElement.style.display = 'block'; // Show the warning
            } else {
                console.error('Warning element not found in the DOM.');
            }
        }

        // Immediately invoke checkJavaScriptEnabled to show warning if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>

    <noscript>
        <style>
            #warning {
                display: block; /* Show the warning if JavaScript is disabled */
            }
        </style>
        <div>
            <strong>Warning!</strong> JavaScript is disabled in your browser. Please enable JavaScript for optimal performance and to pledge ETH.
        </div>
    </noscript>

</body>
</html>
```
