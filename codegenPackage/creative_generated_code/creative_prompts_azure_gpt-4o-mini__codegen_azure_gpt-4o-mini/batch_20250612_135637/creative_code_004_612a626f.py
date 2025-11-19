"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.si
Prompt: How do I create a fallback message for users who have JavaScript disabled when accessing the Blur.si domain details page?
Generated: DETERMINISTIC_612a626f924580db
Batch ID: 20250612_135637
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
    <title>Blur.si Domain Details</title>
    <style>
        /* Styles for the fallback message */
        .no-js-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            margin: 20px;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
        }
    </style>
    <script>
        // Function to show the fallback message if JavaScript is disabled
        function showFallbackMessage() {
            const fallbackMessage = document.getElementById('no-js-message');
            if (fallbackMessage) {
                fallbackMessage.style.display = 'block';
            }
        }

        // Execute on page load
        document.addEventListener('DOMContentLoaded', () => {
            // Ensure the fallback message is hidden when JS is enabled
            const fallbackMessage = document.getElementById('no-js-message');
            if (fallbackMessage) {
                fallbackMessage.style.display = 'none';
            }
        });
    </script>
</head>
<body>

    <!-- Fallback message for users with JavaScript disabled -->
    <div id="no-js-message" class="no-js-message">
        JavaScript is disabled in your browser. Please enable JavaScript to view the full content of the Blur.si domain details page.
    </div>

    <!-- Main content of the page -->
    <div id="content">
        <h1>Blur.si Domain Details</h1>
        <p>Welcome to the Blur.si domain details page. Here, you can find all the necessary information regarding your domain.</p>
        <!-- More interactive content would be loaded here with JavaScript -->
    </div>

    <noscript>
        <!-- The noscript tag is for browsers that have JavaScript disabled -->
        <style>
            .no-js-message {
                display: block; /* Display fallback message */
            }
        </style>
    </noscript>

</body>
</html>
```
