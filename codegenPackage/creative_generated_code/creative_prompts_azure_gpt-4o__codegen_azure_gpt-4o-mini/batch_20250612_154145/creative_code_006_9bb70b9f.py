"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mokent.com
Prompt: Create a script to check if JavaScript is enabled and redirect users to enable it for a platform like MOKENT Trading.
Generated: DETERMINISTIC_9bb70b9fcc48db1e
Batch ID: 20250612_154145
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
    <title>MOKENT Trading - JavaScript Check</title>
    <style>
        /* Style for the message displayed if JavaScript is disabled */
        #no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }
    </style>
    <noscript>
        <style>
            /* Show the message if JavaScript is disabled */
            #no-js-message {
                display: block; /* Show the message */
            }
        </style>
    </noscript>
</head>
<body>

<div id="no-js-message">
    <h1>JavaScript is Disabled</h1>
    <p>To use the MOKENT Trading platform, please enable JavaScript in your browser settings.</p>
    <p>Here are instructions for enabling JavaScript:</p>
    <ul>
        <li><strong>Chrome:</strong> Go to Settings > Privacy and security > Site settings > JavaScript.</li>
        <li><strong>Firefox:</strong> Go to Options > Privacy & Security > Permissions > Enable JavaScript.</li>
        <li><strong>Edge:</strong> Go to Settings > Cookies and site permissions > JavaScript.</li>
        <li><strong>Safari:</strong> Go to Preferences > Security > Enable JavaScript.</li>
    </ul>
</div>

<script>
    // Check if JavaScript is enabled
    if (typeof document !== 'undefined') {
        // JavaScript is enabled; we can safely proceed
        console.log("JavaScript is enabled."); // Log to console for debugging
        
        // You can place additional JavaScript functionality here
        // For example, initializing the trading platform features
        
    } else {
        // If this block is executed, it means JavaScript is not enabled
        console.error("JavaScript is not enabled."); // Log an error to the console
    }
</script>

</body>
</html>
```
