"""
Generated Code Metadata:
========================
Original URL: https://dueleth.com
Prompt: Generate a code example for detecting whether JavaScript is enabled on a webpage, as seen in the Duel ETH website.
Generated: DETERMINISTIC_de649fec67e757c9
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection Example</title>
    <style>
        /* Basic styles for the message display */
        .no-js {
            display: none; /* Hide by default */
        }
        .js {
            display: block; /* Show when JS is enabled */
        }
    </style>
</head>
<body>
    <!-- Message for users with JavaScript disabled -->
    <noscript>
        <style>
            .no-js {
                display: block; /* Show when JS is disabled */
            }
        </style>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for the best experience.</p>
        </div>
    </noscript>

    <!-- Message for users with JavaScript enabled -->
    <div class="js">
        <p>JavaScript is enabled. Welcome to our website!</p>
    </div>

    <script>
        // Function to detect if JavaScript is enabled
        function detectJavaScript() {
            try {
                // If this script runs, JavaScript is enabled
                document.querySelector('.js').style.display = 'block';
            } catch (error) {
                // Log any errors to the console for debugging
                console.error('Error detecting JavaScript:', error);
            }
        }

        // Call the function to detect JavaScript
        detectJavaScript();
    </script>
</body>
</html>
```
