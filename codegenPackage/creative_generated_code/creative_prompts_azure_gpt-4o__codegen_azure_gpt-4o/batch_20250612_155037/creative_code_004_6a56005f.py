"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-pay.starpay.top
Prompt: Write a script to redirect users to a troubleshooting page if JavaScript is disabled, ensuring proper functionality for payment systems like Starpay.
Generated: DETERMINISTIC_6a56005f43a6d790
Batch ID: 20250612_155037
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
    <title>Payment System</title>
    <noscript>
        <!-- Redirect users to a troubleshooting page if JavaScript is disabled -->
        <meta http-equiv="refresh" content="0;url=/troubleshooting.html">
    </noscript>
</head>
<body>
    <h1>Welcome to Starpay Payment System</h1>
    
    <!-- Payment system initialization -->
    <script>
        // Ensure the script runs only if JavaScript is enabled
        (function() {
            try {
                // Initialize Starpay payment system
                const starpayInit = () => {
                    console.log('Starting Starpay payment system...');
                    // Add payment system initialization code here
                    // Example: Starpay.initialize({ apiKey: 'your-api-key' });
                };

                // Execute Starpay initialization
                starpayInit();
            } catch (error) {
                // Log errors and redirect users if initialization fails
                console.error('Error initializing Starpay:', error);
                window.location.href = '/troubleshooting.html';
            }
        })();
    </script>
</body>
</html>
```
