"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange.zweirad-hanselle.de
Prompt: Generate HTML and JavaScript code to detect if browser scripts are disabled and show instructions for enabling them.
Generated: DETERMINISTIC_3021d4699ac0d300
Batch ID: 20250612_145526
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
        /* Style for the no-script message */
        .no-script-message {
            display: none; /* Hidden by default, shown if JavaScript is disabled */
            font-family: Arial, sans-serif;
            color: #ff0000;
            background-color: #fff3f3;
            border: 1px solid #ffcccc;
            padding: 15px;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <!-- Message to display when JavaScript is disabled -->
    <noscript>
        <div class="no-script-message">
            JavaScript is disabled in your browser. Please enable JavaScript to use this website. 
            <br>
            <strong>Instructions to enable JavaScript:</strong>
            <ul>
                <li>Open your browser settings.</li>
                <li>Look for the "JavaScript" section under "Privacy" or "Content Settings".</li>
                <li>Toggle JavaScript to "On".</li>
                <li>Refresh this page.</li>
            </ul>
        </div>
    </noscript>

    <!-- Content when JavaScript is enabled -->
    <div id="main-content" style="display: none;">
        <h1>Welcome</h1>
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // JavaScript to handle the "JavaScript enabled" scenario
        try {
            // Ensure the main content is visible when JavaScript is enabled
            document.getElementById('main-content').style.display = 'block';
        } catch (error) {
            // Log an error if something unexpected happens
            console.error("Error handling JavaScript detection:", error);
        }
    </script>
</body>
</html>
```
