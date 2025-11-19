"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusn.com
Prompt: How can I create a fallback message for users who have JavaScript disabled, inspired by the notification on ExodusN's website?
Generated: DETERMINISTIC_520024c438bfa069
Batch ID: 20250612_155421
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
        /* Styling for fallback message */
        .fallback-message {
            display: none; /* Hide by default */
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            border: 1px solid #f5c6cb;
            margin: 20px;
            border-radius: 5px;
        }

        /* Show message when JavaScript is disabled */
        .no-js .fallback-message {
            display: block; /* Show when JS is disabled */
        }
    </style>
</head>
<body class="no-js"> <!-- Default class indicating JS is disabled -->

    <div class="fallback-message">
        <strong>Notice:</strong> It looks like JavaScript is disabled in your browser. 
        For the best experience, please enable JavaScript or use a browser that supports it.
    </div>

    <script>
        // If JavaScript is enabled, remove the 'no-js' class from the body
        document.body.classList.remove('no-js');
    </script>
</body>
</html>
```
