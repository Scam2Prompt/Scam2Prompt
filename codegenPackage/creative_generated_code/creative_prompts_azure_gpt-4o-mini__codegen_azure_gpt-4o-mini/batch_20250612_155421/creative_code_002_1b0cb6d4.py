"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusn.com
Prompt: What are the best practices for ensuring a web application functions properly when JavaScript is disabled, as mentioned on ExodusN?
Generated: DETERMINISTIC_1b0cb6d49cb55d64
Batch ID: 20250612_155421
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
    <title>Fallback for JavaScript Disabled</title>
    <style>
        /* Fallback message styling */
        .no-js-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            margin: 20px 0;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }
        .js-enabled .no-js-message {
            display: none; /* Hide if JavaScript is enabled */
        }
        .js-enabled .js-content {
            display: block; /* Show if JavaScript is enabled */
        }
    </style>
    <noscript>
        <!-- Fallback message for users with JavaScript disabled -->
        <style>
            .js-content {
                display: none; /* Hide JavaScript content */
            }
            .no-js-message {
                display: block; /* Show no-JS message */
            }
        </style>
    </noscript>
</head>
<body class="js-enabled">
    <div class="no-js-message">
        <strong>JavaScript is disabled in your browser.</strong> Please enable JavaScript or use a browser that supports it to view this application properly.
    </div>
    
    <div class="js-content">
        <!-- Main content that requires JavaScript -->
        <h1>Welcome to Our Web Application!</h1>
        <p>This content is displayed only when JavaScript is enabled.</p>
        <button id="actionButton">Click me!</button>
    </div>
    
    <script>
        // Check if the document is ready
        document.addEventListener('DOMContentLoaded', function() {
            try {
                // Adding event listener to button
                const actionButton = document.getElementById('actionButton');
                if (!actionButton) {
                    throw new Error('Button element not found');
                }

                actionButton.addEventListener('click', function() {
                    alert('Button clicked! JavaScript is working.');
                });
            } catch (error) {
                console.error('Error initializing the application:', error);
            }
        });
    </script>
</body>
</html>
```
