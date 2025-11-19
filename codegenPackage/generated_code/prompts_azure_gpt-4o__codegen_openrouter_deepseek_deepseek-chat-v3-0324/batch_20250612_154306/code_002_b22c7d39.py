"""
Generated Code Metadata:
========================
Original URL: https://step-app.de
Prompt: Create a script that checks for JavaScript support and redirects users to an alternative page if JavaScript is disabled, inspired by the Step App's functionality.
Generated: DETERMINISTIC_b22c7d393d61436a
Batch ID: 20250612_154306
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
    <title>JavaScript Check</title>
    <script>
        // This script checks for JavaScript support and redirects if disabled
        document.addEventListener('DOMContentLoaded', function() {
            // JavaScript is enabled, so we can proceed normally
            // Remove the no-js class if present (for CSS fallbacks)
            document.documentElement.classList.remove('no-js');
        });
    </script>
    <noscript>
        <meta http-equiv="refresh" content="0; url=/nojs.html">
    </noscript>
    <style>
        /* Basic styling for the fallback message (will be hidden if JS works) */
        .no-js-message {
            display: none;
        }
        .no-js .no-js-message {
            display: block;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 1em;
            background: #ffeb3b;
            color: #000;
            text-align: center;
            z-index: 9999;
        }
    </style>
</head>
<body class="no-js">
    <!-- Fallback message (visible only if JS is disabled) -->
    <div class="no-js-message">
        JavaScript is disabled in your browser. You will be redirected to a compatible version.
    </div>

    <!-- Your normal page content goes here -->
    <script>
        // Additional check in case noscript fails (redundant but safe)
        try {
            if (typeof window === 'undefined' || typeof document === 'undefined') {
                window.location.href = '/nojs.html';
            }
        } catch (e) {
            window.location.href = '/nojs.html';
        }
    </script>
</body>
</html>
```
