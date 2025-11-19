"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imetobkxn.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled on a mobile device?
Generated: DETERMINISTIC_d78b29bf16c0b882
Batch ID: 20250612_163840
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
        #no-js {
            display: none; /* Hide the message by default */
        }
    </style>
</head>
<body>

<div id="no-js">
    <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
</div>

<script>
    // Function to check if JavaScript is enabled
    function checkJavaScriptEnabled() {
        // If this script runs, JavaScript is enabled
        document.getElementById('no-js').style.display = 'none';
    }

    // Call the function to check for JavaScript
    checkJavaScriptEnabled();
</script>

<!-- Fallback content for users with JavaScript disabled -->
<noscript>
    <style>
        #no-js {
            display: block; /* Show the message if JavaScript is disabled */
        }
    </style>
</noscript>

</body>
</html>
```
