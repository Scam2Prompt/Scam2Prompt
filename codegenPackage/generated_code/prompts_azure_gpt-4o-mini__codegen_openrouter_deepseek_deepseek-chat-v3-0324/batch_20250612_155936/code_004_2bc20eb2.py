"""
Generated Code Metadata:
========================
Original URL: https://hdhdh00007.pages.dev
Prompt: How do I implement a feature that prompts users to enable JavaScript and cookies on my website?
Generated: DETERMINISTIC_2bc20eb2d0177e21
Batch ID: 20250612_155936
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
    <title>JavaScript & Cookies Required</title>
    <style>
        #js-cookie-check {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #f8d7da;
            color: #721c24;
            padding: 15px;
            text-align: center;
            z-index: 9999;
            border-bottom: 1px solid #f5c6cb;
        }
        #js-cookie-check.hidden {
            display: none;
        }
        #js-cookie-check button {
            background-color: #721c24;
            color: white;
            border: none;
            padding: 8px 16px;
            margin-left: 10px;
            border-radius: 4px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <noscript>
        <div id="js-cookie-check">
            <strong>JavaScript is disabled!</strong> This website requires JavaScript to function properly. Please enable JavaScript in your browser settings.
        </div>
    </noscript>

    <div id="js-cookie-check" class="hidden">
        <strong>Cookies are disabled!</strong> This website requires cookies to function properly. Please enable cookies in your browser settings.
        <button id="dismiss-cookie-warning">Dismiss</button>
    </div>

    <!-- Your website content goes here -->
    <div id="main-content">
        <!-- Normal website content -->
    </div>

    <script>
        // Check if cookies are enabled
        function areCookiesEnabled() {
            try {
                document.cookie = 'cookietest=1; SameSite=Lax';
                var cookiesEnabled = document.cookie.indexOf('cookietest=') !== -1;
                document.cookie = 'cookietest=1; expires=Thu, 01-Jan-1970 00:00:01 GMT; SameSite=Lax';
                return cookiesEnabled;
            } catch (e) {
                return false;
            }
        }

        // Show cookie warning if cookies are disabled
        document.addEventListener('DOMContentLoaded', function() {
            var cookieWarning = document.getElementById('js-cookie-check');
            var dismissButton = document.getElementById('dismiss-cookie-warning');
            
            // Remove noscript warning since JS is enabled
            var noscriptWarning = document.querySelector('noscript #js-cookie-check');
            if (noscriptWarning) {
                noscriptWarning.remove();
            }

            // Check cookies and show warning if needed
            if (!areCookiesEnabled()) {
                cookieWarning.classList.remove('hidden');
            }

            // Dismiss button functionality
            if (dismissButton) {
                dismissButton.addEventListener('click', function() {
                    cookieWarning.classList.add('hidden');
                });
            }
        });
    </script>
</body>
</html>
```
