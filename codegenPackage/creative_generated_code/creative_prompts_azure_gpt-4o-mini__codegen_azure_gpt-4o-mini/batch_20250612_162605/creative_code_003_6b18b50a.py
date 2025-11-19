"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.fi
Prompt: Create a code example that detects JavaScript support in browsers for a site like Polkadot.fi.
Generated: DETERMINISTIC_6b18b50aa3d40419
Batch ID: 20250612_162605
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
    <title>JavaScript Support Detection</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .no-js { display: block; }
        .js { display: none; }
    </style>
</head>
<body>

    <!-- Message displayed when JavaScript is not supported -->
    <noscript>
        <div class="no-js">
            <h1>JavaScript is disabled or not supported</h1>
            <p>Some features of this site may not work correctly. Please enable JavaScript for the best experience.</p>
        </div>
    </noscript>

    <!-- Content displayed when JavaScript is supported -->
    <div class="js">
        <h1>Welcome to Polkadot.fi</h1>
        <p>Your browser supports JavaScript!</p>
    </div>

    <script>
        // Check if JavaScript is supported
        (function() {
            // Use a try-catch block for error handling
            try {
                // Show the JS section and hide the no-js section
                document.querySelector('.js').style.display = 'block';
                document.querySelector('.no-js').style.display = 'none';
            } catch (error) {
                console.error('An error occurred while detecting JavaScript support:', error);
                // Optionally, you can notify the user here
            }
        })();
    </script>

</body>
</html>
```
