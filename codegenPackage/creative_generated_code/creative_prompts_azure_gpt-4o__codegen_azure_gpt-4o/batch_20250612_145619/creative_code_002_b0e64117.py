"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Generate a sample HTML and JavaScript code snippet to create a notification banner for users when JavaScript is disabled, referencing the ETH Pledge website's requirement.
Generated: DETERMINISTIC_b0e64117cef84220
Batch ID: 20250612_145619
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
    <title>Notification Banner</title>
    <style>
        /* Style for the notification banner */
        .no-js-banner {
            display: none; /* Hidden by default */
            background-color: #f44336; /* Red background */
            color: white;
            padding: 15px;
            text-align: center;
            font-size: 16px;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .has-js .no-js-banner {
            display: none; /* Ensure it's hidden when JavaScript is enabled */
        }

        .no-js .no-js-banner {
            display: block; /* Show the banner when JavaScript is disabled */
        }
    </style>
</head>
<body class="no-js">
    <!-- Notification Banner -->
    <div class="no-js-banner">
        JavaScript is disabled in your browser. Please enable it to access all features of the ETH Pledge website.
    </div>

    <!-- Main content goes here -->
    <main>
        <h1>Welcome to the ETH Pledge Website</h1>
        <p>Explore our platform and take the pledge to make a difference.</p>
    </main>

    <script>
        // Adding a JS-enabled class to the <body> tag
        document.body.classList.remove('no-js'); // Remove no-js class
        document.body.classList.add('has-js');   // Add has-js class
    </script>
</body>
</html>
```
