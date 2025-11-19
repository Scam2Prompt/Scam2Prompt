"""
Generated Code Metadata:
========================
Original URL: https://beejustice.com
Prompt: Can you provide a code snippet that demonstrates how to check if JavaScript is enabled in a user's browser, as seen on Bee Justice?
Generated: DETERMINISTIC_44990ac8d4300a48
Batch ID: 20250612_162504
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
    <title>JavaScript Detection</title>
    <style>
        .js-enabled { display: none; }
        .js-disabled { display: block; }
    </style>
    <noscript>
        <style>
            .js-enabled { display: block; }
            .js-disabled { display: none; }
        </style>
    </noscript>
</head>
<body>
    <!-- Content for when JavaScript is disabled -->
    <div class="js-disabled">
        <p>JavaScript is disabled in your browser. Please enable JavaScript for full functionality.</p>
    </div>

    <!-- Content for when JavaScript is enabled -->
    <div class="js-enabled">
        <p>JavaScript is enabled in your browser.</p>
    </div>

    <script>
        // This will execute only if JavaScript is enabled
        document.addEventListener('DOMContentLoaded', function() {
            // Remove the noscript styles by adding a class
            document.documentElement.className += ' js-active';
            
            // Show JavaScript-enabled content
            var enabledElements = document.querySelectorAll('.js-enabled');
            var disabledElements = document.querySelectorAll('.js-disabled');
            
            enabledElements.forEach(function(el) {
                el.style.display = 'block';
            });
            
            disabledElements.forEach(function(el) {
                el.style.display = 'none';
            });
            
            // Optional: Store the JavaScript status in localStorage
            try {
                localStorage.setItem('javascriptEnabled', 'true');
            } catch (e) {
                console.error('Could not access localStorage:', e);
            }
        });
    </script>
</body>
</html>
```
