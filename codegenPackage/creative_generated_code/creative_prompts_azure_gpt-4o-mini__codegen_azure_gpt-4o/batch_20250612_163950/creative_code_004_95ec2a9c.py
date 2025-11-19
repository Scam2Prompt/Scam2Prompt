"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crystal.free.nf
Prompt: How do I create a fallback message for users with JavaScript disabled?
Generated: DETERMINISTIC_95ec2a9cfe2ab05e
Batch ID: 20250612_163950
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
        /* Style for the fallback message */
        .no-js-message {
            display: none; /* Hidden by default */
            color: red;
            font-weight: bold;
            margin-top: 20px;
        }

        /* Display the fallback message if JavaScript is disabled */
        .no-js-active .no-js-message {
            display: block;
        }
    </style>
    <script>
        // JavaScript to remove the "no-js-active" class when JavaScript is enabled
        document.documentElement.classList.remove('no-js-active');
    </script>
</head>
<body class="no-js-active">
    <!-- Content visible only if JavaScript is enabled -->
    <div id="content">
        <h1>Welcome to our website!</h1>
        <p>Enjoy our interactive features powered by JavaScript.</p>
    </div>

    <!-- Fallback message for users with JavaScript disabled -->
    <div class="no-js-message">
        JavaScript is disabled in your browser. Please enable it to access all features of this website.
    </div>
</body>
</html>
```
