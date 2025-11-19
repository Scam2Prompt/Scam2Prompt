"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdzv.com
Prompt: How do I create a fallback for users who have JavaScript disabled on their mobile devices?
Generated: DETERMINISTIC_ef3764e1354d3871
Batch ID: 20250612_155457
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
    <title>JavaScript Fallback Example</title>
    <style>
        /* Basic styling for fallback content */
        .fallback {
            display: none; /* Hide by default */
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 4px;
        }

        .js-active {
            display: none; /* Hide the JS content if JS is active */
        }
    </style>
</head>
<body>

    <div class="fallback" id="fallbackContent">
        <p>Your browser does not support JavaScript or it is disabled. Please enable JavaScript or use a browser that supports it for the best experience.</p>
    </div>

    <div class="js-active" id="jsContent">
        <h1>Welcome to our Website!</h1>
        <p>This content requires JavaScript to be enabled.</p>
        <button id="actionButton">Click me!</button>
    </div>

    <script>
        // This script will be executed if JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Show the JavaScript content and hide the fallback
            document.getElementById('jsContent').style.display = 'block';
            document.getElementById('fallbackContent').style.display = 'none';

            // Example action for demonstration purposes
            const button = document.getElementById('actionButton');
            button.addEventListener('click', function() {
                alert("JavaScript is working!");
            });
        });
    </script>

    <!-- Fallback for users without JavaScript -->
    <noscript>
        <style>
            /* Show fallback content if JavaScript is disabled */
            .fallback {
                display: block; /* Show fallback content */
            }
            .js-active {
                display: none; /* Hide JS content */
            }
        </style>
        <div class="fallback">
            <p>Your browser does not support JavaScript or it is disabled. Please enable JavaScript or use a browser that supports it for the best experience.</p>
        </div>
    </noscript>

</body>
</html>
```
