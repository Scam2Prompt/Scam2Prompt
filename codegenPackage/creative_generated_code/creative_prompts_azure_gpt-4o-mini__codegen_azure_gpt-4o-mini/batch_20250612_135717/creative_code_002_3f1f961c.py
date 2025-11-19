"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notmonkeybusiness.pages.dev
Prompt: Can you provide a code snippet to check if JavaScript is enabled in a browser for a site like notmonkeybusiness.pages.dev?
Generated: DETERMINISTIC_3f1f961cea7c763a
Batch ID: 20250612_135717
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
        /* Styles to hide the content if JavaScript is disabled */
        .no-js {
            display: none;
        }
        .js {
            display: block;
        }
    </style>
</head>
<body>
    <!-- Content to show if JavaScript is disabled -->
    <noscript>
        <div class="no-js">
            <h1>JavaScript is disabled</h1>
            <p>Please enable JavaScript in your browser to view the full functionality of this site.</p>
        </div>
    </noscript>

    <!-- Content to show if JavaScript is enabled -->
    <div class="js">
        <h1>Welcome to NotMonkeyBusiness!</h1>
        <p>JavaScript is enabled. Enjoy the full experience!</p>
    </div>

    <script>
        // Check if JavaScript is enabled by manipulating DOM
        try {
            // Set a class to indicate that JavaScript is enabled
            document.body.classList.remove('no-js');
            document.body.classList.add('js');
        } catch (error) {
            console.error('An error occurred while checking JavaScript status:', error);
            // Fallback - Inform user if there is an error
            document.body.innerHTML = '<h1>Error</h1><p>Could not determine if JavaScript is enabled.</p>';
        }
    </script>
</body>
</html>
```
