"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ddgghb.pages.dev
Prompt: Can you provide code snippets to check if JavaScript is enabled in a user's browser?
Generated: DETERMINISTIC_d85a41af4e1af397
Batch ID: 20250612_163541
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
        /* Style for the message container */
        #js-message {
            display: none; /* Hide the message by default */
            padding: 15px;
            background-color: #e7f3fe;
            border: 1px solid #b3d7ff;
            color: #31708f;
        }
    </style>
</head>
<body>

<div id="js-message">
    JavaScript is enabled in your browser!
</div>

<noscript>
    <style>
        /* Style for when JavaScript is disabled */
        #js-message {
            display: block; /* Show the message if JavaScript is disabled */
            background-color: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
        }
    </style>
    <div>
        JavaScript is disabled in your browser! Please enable it for optimal experience.
    </div>
</noscript>

<script>
    // Function to display a message indicating JavaScript is enabled
    function checkJavaScriptEnabled() {
        const message = document.getElementById('js-message');
        try {
            message.style.display = 'block'; // Show the message
        } catch (error) {
            console.error('Error displaying the JavaScript enabled message:', error);
        }
    }

    // Call the function to check if JavaScript is enabled
    checkJavaScriptEnabled();
</script>

</body>
</html>
```
