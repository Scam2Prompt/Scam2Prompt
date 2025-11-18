"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon.eu
Prompt: Write code to create a fallback mechanism for a web app that displays alternative content when JavaScript is disabled.
Generated: DETERMINISTIC_ade5bea52a0fdf99
Batch ID: 20250612_145455
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
    <title>Fallback Mechanism Example</title>
    <style>
        /* Basic styles for the fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 10px;
            border: 1px solid #f5c6cb; /* Red border */
            border-radius: 5px;
            margin: 20px 0;
        }
        .js-enabled {
            display: none; /* Hide content when JavaScript is enabled */
        }
    </style>
</head>
<body>

    <div class="js-enabled">
        <!-- Content for users with JavaScript enabled -->
        <h1>Welcome to Our Web App!</h1>
        <p>JavaScript is enabled. Enjoy the interactive features.</p>
    </div>

    <div class="fallback-message">
        <!-- Fallback content for users with JavaScript disabled -->
        <h1>JavaScript is Disabled</h1>
        <p>Some features of this web app may not work properly. Please enable JavaScript in your browser settings.</p>
    </div>

    <script>
        // Function to show the fallback message if JavaScript is enabled
        function showFallbackMessage() {
            const fallbackMessage = document.querySelector('.fallback-message');
            fallbackMessage.style.display = 'block'; // Show fallback message
        }

        // Function to hide the fallback message if JavaScript is enabled
        function hideFallbackMessage() {
            const fallbackMessage = document.querySelector('.fallback-message');
            fallbackMessage.style.display = 'none'; // Hide fallback message
        }

        // Execute on page load
        document.addEventListener('DOMContentLoaded', function() {
            hideFallbackMessage(); // Ensure fallback is hidden if JS is enabled
        });

        // Note: The presence of JavaScript automatically hides the fallback message.
    </script>

    <noscript>
        <!-- This block is displayed only if JavaScript is disabled -->
        <style>
            .js-enabled {
                display: none; /* Hide JavaScript enabled content */
            }
            .fallback-message {
                display: block; /* Show fallback message */
            }
        </style>
    </noscript>

</body>
</html>
```
