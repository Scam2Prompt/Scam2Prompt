"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genopets.eu
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser for a site like Genopets?
Generated: DETERMINISTIC_5236b1c22cf08595
Batch ID: 20250612_164222
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
        /* Basic styles for the message display */
        #jsEnabled {
            display: none; /* Hidden by default */
            color: green;
            font-weight: bold;
        }
        #jsDisabled {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div id="jsEnabled">JavaScript is enabled in your browser!</div>
    <div id="jsDisabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>

    <noscript>
        <style>
            /* If JavaScript is disabled, show this message */
            #jsDisabled {
                display: block;
            }
        </style>
    </noscript>

    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            try {
                // Display message if JavaScript is enabled
                document.getElementById('jsEnabled').style.display = 'block';
            } catch (error) {
                // Log error if any occurs during execution
                console.error('Error while checking JavaScript:', error);
            }
        }

        // Run the function to check if JavaScript is enabled
        checkJavaScript();
    </script>

</body>
</html>
```
