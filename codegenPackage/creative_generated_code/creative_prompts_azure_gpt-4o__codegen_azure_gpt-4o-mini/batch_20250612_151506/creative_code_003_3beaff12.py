"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominionxshow.com
Prompt: Write code to implement a feature that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, inspired by dominion-x-client requirements.
Generated: DETERMINISTIC_3beaff1269a1e12d
Batch ID: 20250612_151506
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
    <title>JavaScript Support Check</title>
    <script>
        // This function will execute when the page loads
        // It indicates that JavaScript is enabled
        document.addEventListener("DOMContentLoaded", function() {
            // Remove the noscript tag if JavaScript is enabled
            const noscriptMessage = document.getElementById('noscript-message');
            if (noscriptMessage) {
                noscriptMessage.style.display = 'none'; // Hide the noscript message
            }
        });

        // Function to redirect to an alternate page
        function redirectToAlternativePage() {
            // Redirect to the specified alternative URL
            window.location.href = 'alternative.html'; // Change to the desired URL
        }

        // Check if JavaScript is enabled
        if (!window.navigator.javaEnabled()) {
            redirectToAlternativePage(); // Redirect if JavaScript is disabled
        }
    </script>
</head>
<body>
    <noscript>
        <div id="noscript-message" style="color: red; font-weight: bold;">
            JavaScript is disabled in your browser. You will be redirected to an alternative page.
        </div>
    </noscript>
    
    <h1>Welcome to Our Website</h1>
    <p>This content is only accessible if JavaScript is enabled.</p>
</body>
</html>
```
