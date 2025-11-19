"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.consesys.io
Prompt: Can you provide a code snippet to detect if JavaScript is enabled in a user's browser for a web application?
Generated: DETERMINISTIC_5d4f64f799f26345
Batch ID: 20250612_155122
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
    <title>JavaScript Detection</title>
    <style>
        /* Styles to show/hide elements based on JavaScript availability */
        .no-js {
            display: block; /* Show this message if JavaScript is disabled */
        }
        .js {
            display: none; /* Hide this message if JavaScript is enabled */
        }
    </style>
</head>
<body>

    <!-- Message for users without JavaScript -->
    <noscript>
        <div class="no-js">
            <p>JavaScript is disabled in your browser. Please enable it for a better experience.</p>
        </div>
    </noscript>

    <!-- Message for users with JavaScript -->
    <div class="js">
        <p>JavaScript is enabled in your browser!</p>
    </div>

    <script>
        // This script will run if JavaScript is enabled
        document.querySelector('.js').style.display = 'block'; // Show the JS enabled message
        document.querySelector('.no-js').style.display = 'none'; // Hide the no-JS message
    } catch (error) {
        console.error("An error occurred while detecting JavaScript: ", error);
        // Handle the error gracefully
    }
    </script>

</body>
</html>
```
