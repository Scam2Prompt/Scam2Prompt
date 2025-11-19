"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbo.com
Prompt: Can you provide a code snippet that checks if JavaScript is enabled on a mobile browser and prompts the user accordingly?
Generated: DETERMINISTIC_a5fe1ccaee5413af
Batch ID: 20250612_155742
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
        #js-warning {
            display: none; /* Hide warning by default */
            background-color: #ffcc00;
            color: #000;
            padding: 15px;
            border: 1px solid #ff9900;
            margin: 20px 0;
        }
    </style>
</head>
<body>

<div id="js-warning">
    <strong>JavaScript is disabled!</strong> Please enable JavaScript in your browser settings for the best experience.
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScript() {
        // Check if the script is running (meaning JS is enabled)
        document.getElementById('js-warning').style.display = 'none'; // Hide warning if JS is enabled
    }

    // Error handling for potential issues
    try {
        checkJavaScript();
    } catch (error) {
        console.error("An error occurred while checking JavaScript status: ", error);
    }
</script>

<noscript>
    <!-- This message will be displayed if JavaScript is disabled in the browser -->
    <style>
        #js-warning {
            display: block; /* Show warning message */
        }
    </style>
</noscript>

</body>
</html>
```
