"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqep.com
Prompt: How do I create a fallback for users who have JavaScript disabled when accessing DCQEP?
Generated: DETERMINISTIC_6a91189c1ead4f95
Batch ID: 20250612_155739
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
    <title>DCQEP - JavaScript Fallback</title>
    <style>
        /* Style for the JavaScript disabled message */
        .noscript-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 15px;
            border: 1px solid #f5c6cb; /* Border to match the theme */
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <noscript>
        <div class="noscript-message">
            <strong>JavaScript is disabled in your browser.</strong>
            <p>Please enable JavaScript to enjoy the full features of DCQEP.</p>
        </div>
    </noscript>

    <div id="content">
        <!-- Main content of the page goes here -->
        <h1>Welcome to DCQEP</h1>
        <p>Your interactive content will load here if JavaScript is enabled.</p>
    </div>

    <script>
        // JavaScript enabled: hide the noscript message
        document.addEventListener('DOMContentLoaded', (event) => {
            const noscriptMessage = document.querySelector('.noscript-message');
            if (noscriptMessage) {
                noscriptMessage.style.display = 'none'; // Hide the message if JS is enabled
            }
        });
    </script>
</body>
</html>
```
