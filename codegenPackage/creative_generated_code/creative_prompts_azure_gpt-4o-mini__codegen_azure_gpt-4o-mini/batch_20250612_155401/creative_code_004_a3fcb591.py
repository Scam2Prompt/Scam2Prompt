"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmm.us
Prompt: How do I create a fallback message for users who have JavaScript disabled, similar to the one on coinmm.us?
Generated: DETERMINISTIC_a3fcb591c33badcb
Batch ID: 20250612_155401
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
    <title>Fallback Message Example</title>
    <style>
        /* Basic styles for the fallback message */
        .fallback-message {
            display: none; /* Hidden by default, will be shown if JS is disabled */
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
            padding: 15px;
            margin: 20px;
            border-radius: 4px;
        }

        /* Hide the fallback message when JavaScript is enabled */
        .js-enabled .fallback-message {
            display: none;
        }

        /* Show the fallback message when JavaScript is disabled */
        .js-disabled .fallback-message {
            display: block;
        }
    </style>
</head>
<body class="js-enabled"> <!-- Default class assumes JS is enabled -->

    <noscript>
        <style>
            /* Add a class to the body when JavaScript is disabled */
            .js-enabled { display: none; }
            .js-disabled { display: block; }
        </style>
        <div class="fallback-message">
            <strong>JavaScript is disabled in your browser.</strong> 
            Please enable JavaScript to access the full functionality of this website.
        </div>
    </noscript>

    <script>
        // JavaScript to ensure correct class is set based on JS availability
        document.body.classList.remove('js-enabled');
        document.body.classList.add('js-disabled');
    </script>

    <h1>Welcome to Our Website</h1>
    <p>This content is only accessible with JavaScript enabled.</p>

</body>
</html>
```
