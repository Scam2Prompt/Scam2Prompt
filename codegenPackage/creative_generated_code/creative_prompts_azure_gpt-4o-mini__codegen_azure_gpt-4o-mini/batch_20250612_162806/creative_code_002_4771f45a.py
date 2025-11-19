"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mawsoninc-integrates.com
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a web application similar to Mawson Inc. Workbench?
Generated: DETERMINISTIC_4771f45abd9a314f
Batch ID: 20250612_162806
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
        /* Style to hide the no-js message */
        .no-js {
            display: none;
        }
        /* Style to show the js-enabled message */
        .js {
            display: block;
        }
    </style>
</head>
<body class="no-js">

    <div id="js-enabled-message" class="js">
        <h1>JavaScript is enabled!</h1>
        <p>Welcome to the Mawson Inc. Workbench.</p>
    </div>

    <div id="no-js-message">
        <h1>JavaScript is disabled!</h1>
        <p>Please enable JavaScript to use the full functionality of the site.</p>
    </div>

    <script>
        // Function to set the body class based on JavaScript availability
        function enableJavaScript() {
            // Set the body class to 'js' to indicate that JavaScript is enabled
            document.body.classList.remove('no-js');
            document.body.classList.add('js');

            // Optionally hide the "no-js" message if JavaScript is enabled
            const noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        }

        // Execute the function to enable JavaScript
        enableJavaScript();
    </script>
</body>
</html>
```
