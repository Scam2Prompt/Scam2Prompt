"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giveawaysol.vercel.app
Prompt: How do I create a fallback for users who have JavaScript disabled, based on the experience at giveawaysol.vercel.app?
Generated: DETERMINISTIC_5014644421396243
Batch ID: 20250612_162504
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
    <title>Fallback for JavaScript Disabled Users</title>
    <style>
        /* Basic styling for the fallback message */
        .fallback-message {
            display: none; /* Hidden by default */
            text-align: center;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            margin: 20px;
        }
    </style>
</head>
<body>

    <!-- Main content of the page -->
    <div id="main-content">
        <h1>Welcome to Our Website</h1>
        <p>This site is enhanced with JavaScript. Please enable it for the best experience.</p>
        <!-- Content that requires JavaScript -->
        <button id="action-button">Click me!</button>
    </div>

    <!-- Fallback message for users with JavaScript disabled -->
    <div id="fallback-message" class="fallback-message">
        <p>JavaScript is disabled in your browser. Please enable it for a better experience!</p>
    </div>

    <script>
        // Check if JavaScript is enabled
        document.getElementById('main-content').style.display = 'block';
        
        // Function to handle button click
        function handleButtonClick() {
            alert('Button clicked! JavaScript is working.');
        }

        // Attach click event to button if JavaScript is enabled
        const actionButton = document.getElementById('action-button');
        if (actionButton) {
            actionButton.addEventListener('click', handleButtonClick);
        }
    </script>

    <!-- If JavaScript is disabled, the following will not execute -->
    <noscript>
        <style>
            /* Display the fallback message if JavaScript is disabled */
            #fallback-message {
                display: block; /* Show fallback message */
            }
            #main-content {
                display: none; /* Hide main content */
            }
        </style>
    </noscript>
</body>
</html>
```
