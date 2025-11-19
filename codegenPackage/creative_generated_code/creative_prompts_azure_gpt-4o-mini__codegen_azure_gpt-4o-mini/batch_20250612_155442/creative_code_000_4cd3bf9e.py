"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: How can I enable JavaScript for better functionality on the Sophon.eu website?
Generated: DETERMINISTIC_4cd3bf9e590fc292
Batch ID: 20250612_155442
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
    <title>Sophon.eu - Enable JavaScript</title>
    <style>
        /* Style to hide the content if JavaScript is disabled */
        .no-js #content {
            display: none;
        }
        .no-js #js-message {
            display: block;
        }
    </style>
</head>
<body class="no-js">
    <noscript>
        <!-- Alert users that JavaScript is required for full functionality -->
        <div id="js-message" style="color: red;">
            JavaScript is disabled in your browser. Please enable it for better functionality on this site.
        </div>
    </noscript>
    
    <div id="content">
        <!-- Main content of the website that requires JavaScript -->
        <h1>Welcome to Sophon.eu</h1>
        <p>This site works best with JavaScript enabled.</p>
    </div>

    <script>
        // Check if JavaScript is enabled and update the body class accordingly
        document.body.classList.remove('no-js');

        // Example function to demonstrate JavaScript functionality
        function showWelcomeMessage() {
            const welcomeMessage = document.createElement('p');
            welcomeMessage.textContent = "Thank you for enabling JavaScript!";
            document.getElementById('content').appendChild(welcomeMessage);
        }

        // Execute the function to show the message
        showWelcomeMessage();

        // Error handling for potential issues
        window.addEventListener('error', function(event) {
            console.error('An error occurred: ', event.message);
            alert('An unexpected error occurred. Please try refreshing the page.');
        });
    </script>
</body>
</html>
```
