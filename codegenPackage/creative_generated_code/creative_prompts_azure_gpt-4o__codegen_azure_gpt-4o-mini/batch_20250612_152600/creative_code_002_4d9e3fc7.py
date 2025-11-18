"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlast.com
Prompt: Create a script that checks for JavaScript support on a mobile device and redirects users to an alternative page if JavaScript is disabled, inspired by the ETH Pledge website functionality.
Generated: DETERMINISTIC_4d9e3fc7db80489a
Batch ID: 20250612_152600
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
    <title>JavaScript Support Check</title>
    <style>
        /* Style for the warning message */
        .warning {
            display: none;
            background-color: #ffcc00;
            color: #333;
            padding: 15px;
            text-align: center;
            font-family: Arial, sans-serif;
            margin: 10px 0;
        }
    </style>
</head>
<body>

<div class="warning" id="js-warning">
    JavaScript is disabled in your browser. Please enable JavaScript or use a different browser to view this content.
</div>

<script>
    // Function to redirect to an alternative page if JavaScript is disabled
    function checkJavaScriptSupport() {
        // Create a script element
        const script = document.createElement('script');
        
        // Set a fallback to execute if JavaScript is disabled
        script.innerHTML = `
            // This code runs if JavaScript is enabled
            document.getElementById('js-warning').style.display = 'none';
        `;
        
        // Append the script to the body for execution
        document.body.appendChild(script);
        
        // Set a timeout to check if the script has executed
        setTimeout(() => {
            // Check if the warning message is still visible
            if (document.getElementById('js-warning').style.display === '') {
                // If the warning is still showing, redirect to an alternative page
                window.location.href = 'alternative-page.html'; // Adjust the URL as needed
            }
        }, 100);
    }

    // Execute the check on page load
    window.onload = checkJavaScriptSupport;
</script>

</body>
</html>
```
