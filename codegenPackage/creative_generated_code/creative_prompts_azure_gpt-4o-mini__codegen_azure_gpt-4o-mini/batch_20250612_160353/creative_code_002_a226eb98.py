"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibot15.cc
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_a226eb98342535c1
Batch ID: 20250612_160353
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
        /* Styles for the message */
        #js-enabled {
            display: none; /* Initially hidden */
            color: green;
            font-weight: bold;
        }
        #js-disabled {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <!-- Message displayed if JavaScript is enabled -->
    <div id="js-enabled">JavaScript is enabled in your browser.</div>
    
    <!-- Message displayed if JavaScript is disabled -->
    <noscript>
        <div id="js-disabled">JavaScript is disabled in your browser. Please enable it for the best experience.</div>
    </noscript>

    <script>
        // Function to display a message confirming JavaScript is enabled
        function checkJavaScriptEnabled() {
            try {
                // Display the message if JavaScript is enabled
                document.getElementById('js-enabled').style.display = 'block';
            } catch (error) {
                console.error('An error occurred while checking JavaScript status:', error);
            }
        }

        // Call the function to check if JavaScript is enabled
        checkJavaScriptEnabled();
    </script>
    
</body>
</html>
```
