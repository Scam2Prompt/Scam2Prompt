"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://account.coinbasenft.de
Prompt: Create a script that checks for JavaScript support and redirects users to a help page if JavaScript is disabled, inspired by the Coinbase NFT domain page functionality.
Generated: DETERMINISTIC_d30805f05de5eb20
Batch ID: 20250612_153755
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
    <title>JavaScript Check</title>
    <noscript>
        <!-- Redirect users to a help page if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0;url=/help/javascript-disabled.html">
    </noscript>
    <script>
        // Ensure graceful handling in case JavaScript execution fails
        try {
            // JavaScript is enabled, no further action needed
            console.log('JavaScript is enabled.');
        } catch (error) {
            // Log the error for debugging purposes (if necessary)
            console.error('An error occurred while checking JavaScript:', error);
        }
    </script>
</head>
<body>
    <h1>Welcome to the Website</h1>
    <p>If you are seeing this message, JavaScript is enabled in your browser.</p>
</body>
</html>
```
