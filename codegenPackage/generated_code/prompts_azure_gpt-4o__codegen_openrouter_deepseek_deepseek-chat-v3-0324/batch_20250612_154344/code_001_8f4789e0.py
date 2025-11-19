"""
Generated Code Metadata:
========================
Original URL: https://jrny.world
Prompt: Create a script to detect if JavaScript is disabled in a browser and display a message prompting users to enable JavaScript for the "JRNY" app.
Generated: DETERMINISTIC_8f4789e0fd6d5ba4
Batch ID: 20250612_154344
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
    <title>JRNY App</title>
    <style>
        /* Style for the noscript message */
        .noscript-message {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            z-index: 9999;
            padding: 20px;
            box-sizing: border-box;
        }
        
        .noscript-content {
            max-width: 600px;
            padding: 30px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .noscript-content h1 {
            color: #dc3545;
            margin-bottom: 20px;
        }
        
        .noscript-content p {
            margin-bottom: 20px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <!-- Main app content (hidden when JavaScript is disabled) -->
    <div id="app-content">
        <!-- Your JRNY app content goes here -->
    </div>

    <!-- Noscript message (shown when JavaScript is disabled) -->
    <noscript>
        <div class="noscript-message">
            <div class="noscript-content">
                <h1>JavaScript is Disabled</h1>
                <p>The JRNY app requires JavaScript to function properly. Please enable JavaScript in your browser settings to continue.</p>
                <p>Here's how to enable JavaScript:</p>
                <ul style="text-align: left; margin-left: 20px;">
                    <li><strong>Chrome:</strong> Settings > Privacy and security > Site Settings > JavaScript</li>
                    <li><strong>Firefox:</strong> Options > Privacy & Security > Permissions > Enable JavaScript</li>
                    <li><strong>Safari:</strong> Preferences > Security > Enable JavaScript</li>
                    <li><strong>Edge:</strong> Settings > Cookies and site permissions > JavaScript</li>
                </ul>
                <p>After enabling JavaScript, please refresh this page.</p>
            </div>
        </div>
    </noscript>

    <!-- Optional: Hide main content when JavaScript is disabled -->
    <script>
        // Hide the noscript message if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // This will only run if JavaScript is enabled
            document.getElementById('app-content').style.display = 'block';
        });
    </script>
</body>
</html>
```
