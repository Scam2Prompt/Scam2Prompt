"""
Generated Code Metadata:
========================
Original URL: https://debridge.global-connect.eu
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a custom message if it is disabled, similar to the functionality described on the "debridge.global-connect.eu" domain details page.
Generated: DETERMINISTIC_2329373b831d3884
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <style>
        .no-js-message {
            display: none;
            padding: 20px;
            background-color: #ffebee;
            color: #c62828;
            border: 1px solid #ef9a9a;
            border-radius: 4px;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="no-js-message">
            <h2>JavaScript is Disabled</h2>
            <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
        </div>
    </noscript>

    <script>
        // Immediately remove the noscript element if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            const noscriptElements = document.getElementsByTagName('noscript');
            while (noscriptElements.length > 0) {
                noscriptElements[0].parentNode.removeChild(noscriptElements[0]);
            }
        });

        // Fallback check (though not strictly necessary with noscript)
        function checkJavaScript() {
            try {
                // Attempt to create and manipulate DOM elements
                const testElement = document.createElement('div');
                testElement.style.display = 'none';
                document.body.appendChild(testElement);
                document.body.removeChild(testElement);
                return true;
            } catch (e) {
                return false;
            }
        }

        // Display message if JavaScript is disabled (fallback)
        if (!checkJavaScript()) {
            const messageDiv = document.createElement('div');
            messageDiv.className = 'no-js-message';
            messageDiv.innerHTML = `
                <h2>JavaScript is Disabled</h2>
                <p>This website requires JavaScript to function properly. Please enable JavaScript in your browser settings and refresh the page.</p>
            `;
            document.body.insertBefore(messageDiv, document.body.firstChild);
            messageDiv.style.display = 'block';
        }
    </script>
</body>
</html>
```
