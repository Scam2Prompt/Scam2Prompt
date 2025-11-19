"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.online
Prompt: How can I enable JavaScript for the Celestia domain details page to ensure proper functionality?
Generated: DETERMINISTIC_534ac6b7603c2e5b
Batch ID: 20250612_155639
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
    <title>Celestia Domain Details</title>
    <script>
        // Function to check if JavaScript is enabled
        function checkJavaScript() {
            const jsEnabledDiv = document.getElementById('js-enabled');
            jsEnabledDiv.style.display = 'block'; // Show message if JavaScript is enabled
        }

        // Function to handle potential errors
        function handleError(error) {
            console.error('An error occurred:', error);
            alert('There was an issue loading the page. Please try again later.');
        }

        // Adding an event listener to execute when the document is fully loaded
        document.addEventListener('DOMContentLoaded', () => {
            try {
                checkJavaScript();
                // Additional JavaScript functionality can be initialized here
            } catch (error) {
                handleError(error);
            }
        });
    </script>
    <noscript>
        <style>
            /* Styles to show a message when JavaScript is disabled */
            .no-js-message {
                display: block;
                color: red;
                font-weight: bold;
            }
        </style>
    </noscript>
</head>
<body>
    <h1>Welcome to the Celestia Domain Details Page</h1>
    
    <div id="js-enabled" style="display: none;">
        <p>JavaScript is enabled! Enjoy the enhanced functionality.</p>
    </div>
    
    <div class="no-js-message">
        <p>JavaScript is disabled in your browser. Please enable JavaScript for the best experience.</p>
    </div>
    
    <!-- Additional content for the domain details can be added here -->
</body>
</html>
```
