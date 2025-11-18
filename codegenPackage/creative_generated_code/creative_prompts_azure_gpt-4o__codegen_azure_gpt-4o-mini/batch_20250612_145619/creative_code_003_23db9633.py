"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Write code to display a fallback message for users accessing a webpage without JavaScript enabled, specifically targeting mobile browsers.
Generated: DETERMINISTIC_23db963321805bfe
Batch ID: 20250612_145619
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
    <title>Fallback Message</title>
    <style>
        /* Basic styling for the fallback message */
        .fallback-message {
            display: none; /* Hidden by default */
            background-color: #ffcc00;
            color: #333;
            padding: 20px;
            text-align: center;
            font-size: 1.2em;
        }

        /* Only display the fallback message on mobile devices without JavaScript */
        @media (max-width: 767px) {
            .fallback-message {
                display: block; /* Show on mobile */
            }
        }
    </style>
</head>
<body>
    <!-- Fallback message for users without JavaScript -->
    <div class="fallback-message">
        This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
    </div>

    <script>
        // Check if JavaScript is enabled and hide the fallback message if it is
        document.addEventListener('DOMContentLoaded', function() {
            const fallbackMessage = document.querySelector('.fallback-message');
            if (fallbackMessage) {
                fallbackMessage.style.display = 'none'; // Hide if JS is enabled
            }
        });
    </script>
</body>
</html>
```
