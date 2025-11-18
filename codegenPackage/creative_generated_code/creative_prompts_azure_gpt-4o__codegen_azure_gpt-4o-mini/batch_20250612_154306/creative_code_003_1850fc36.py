"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://step-app.de
Prompt: Generate code for a landing page that displays a "JavaScript required" message when JavaScript is disabled, as seen on the Step App domain page.
Generated: DETERMINISTIC_1850fc366c57a499
Batch ID: 20250612_154306
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
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Landing Page</title>
    <style>
        /* Basic reset and style for the body */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }

        /* Style for the JavaScript required message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            width: 80%;
            max-width: 600px;
            margin: 0 auto;
        }
        
        /* Style for the content */
        .content {
            display: none; /* Hide content initially */
        }

        /* Show content only when JavaScript is enabled */
        .js-enabled .content {
            display: block; /* Show content */
        }

        /* Show message only when JavaScript is disabled */
        .js-enabled .no-js-message {
            display: none; /* Hide message */
        }
    </style>
</head>
<body class="no-js">

    <!-- Message displayed when JavaScript is disabled -->
    <div class="no-js-message">
        <strong>JavaScript required!</strong> Please enable JavaScript in your browser settings.
    </div>

    <!-- Content displayed when JavaScript is enabled -->
    <div class="content">
        <h1>Welcome to Our Landing Page</h1>
        <p>This content is only visible when JavaScript is enabled.</p>
    </div>

    <script>
        // Function to enable JS detection
        (function() {
            // Change the body class to indicate JS is enabled
            document.body.classList.remove('no-js');
            document.body.classList.add('js-enabled');
        })();
    </script>
</body>
</html>
```
