"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethbo.com
Prompt: How do I create a fallback message for users who have JavaScript disabled on their mobile devices?
Generated: DETERMINISTIC_5ef3a301d638dfb0
Batch ID: 20250612_155742
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
    <title>Fallback Message Example</title>
    <style>
        /* Basic styles for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
            text-align: center;
        }
    </style>
</head>
<body>

    <!-- Fallback message for users with JavaScript disabled -->
    <noscript>
        <div class="fallback-message">
            <strong>Important:</strong> It seems that JavaScript is disabled on your device. 
            Please enable JavaScript to view the full functionality of this website.
        </div>
    </noscript>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to Our Website</h1>
        <p>This content is only visible if JavaScript is enabled.</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Display main content or handle any functionalities
            const mainContent = document.getElementById('main-content');
            if (mainContent) {
                // JavaScript is enabled, you can perform any additional functionalities here
                console.log('JavaScript is enabled.');
            } else {
                console.error('Main content could not be found.');
            }
        });
    </script>
    
</body>
</html>
```
