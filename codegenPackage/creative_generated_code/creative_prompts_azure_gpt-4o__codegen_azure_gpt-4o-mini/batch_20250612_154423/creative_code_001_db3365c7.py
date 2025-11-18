"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-web-utils-prod.app.greate.eu
Prompt: Create a script that mimics the functionality of the Metamask Web Utils domain details page by detecting JavaScript support and prompting users to enable it for proper app functionality.
Generated: DETERMINISTIC_db3365c7d8bda81a
Batch ID: 20250612_154423
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
    <title>MetaMask Web Utils - Enable JavaScript</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        .hidden {
            display: none;
        }
        .prompt {
            border: 1px solid #f00;
            padding: 20px;
            background-color: #ffe6e6;
            color: #d00;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <noscript>
        <div class="prompt">
            <h1>JavaScript Disabled</h1>
            <p>It seems that JavaScript is disabled in your browser.</p>
            <p>For the best experience, please enable JavaScript and refresh the page.</p>
        </div>
    </noscript>

    <div id="content" class="hidden">
        <h1>Welcome to MetaMask Web Utils</h1>
        <p>JavaScript is enabled. You can use all features of the application.</p>
    </div>

    <script>
        // Function to check if JavaScript is enabled
        function init() {
            try {
                // Show main content if JavaScript is enabled
                document.getElementById('content').classList.remove('hidden');
            } catch (error) {
                console.error("An error occurred while initializing the app: ", error);
                alert("An unexpected error occurred. Please refresh the page.");
            }
        }

        // Initialize the application
        init();
    </script>

</body>
</html>
```
